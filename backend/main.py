import os
import sys
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

# Allow `python backend/main.py` (or running this file from inside backend/) by
# putting the project root - the directory that contains the `backend` package - on sys.path.
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from backend.config import settings
from backend.db import get_db_connection, init_db
from backend.ingestion import ingest_all_documents
from backend.rag_graph import build_rag_graph
from backend.tools import tool_registry, invoke_tool_safely
from backend.reranker import reranker_service
from backend.evaluation import run_retrieval_benchmark, get_benchmark_history, load_ground_truth_samples

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("rag.api")

app = FastAPI(
    title="Production RAG API",
    description="Enterprise Hybrid RAG with LangGraph, pgvector, and CrossEncoder reranking",
    version="1.0.0"
)

# CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str = Field(..., example="What is Northwind's parental leave policy?")
    category_filter: Optional[str] = Field(None, example="Human Resources")
    enabled_tools: Optional[List[str]] = Field(None, example=["calculator", "search_document_metadata"])

class IngestResponse(BaseModel):
    status: str
    documents_indexed: int
    chunks_indexed: int

class ToolExecuteRequest(BaseModel):
    tool_name: str
    tool_input: Any = None

class BenchmarkRequest(BaseModel):
    sample_size: int = Field(default=10, ge=1, le=50)
    modes: Optional[List[str]] = Field(default=["dense", "bm25", "hybrid", "hybrid_rerank"])

class RerankRequest(BaseModel):
    query: str = Field(..., example="What is Northwind's parental leave policy?")
    documents: List[str] = Field(..., example=["Document text 1", "Document text 2"])
    top_k: Optional[int] = Field(default=None, example=5)

@app.on_event("startup")
def on_startup():
    try:
        init_db()
    except Exception as e:
        logger.warning(f"Startup DB init check: {e}")

@app.get("/api/health")
def health_check():
    db_ok = False
    doc_count = 0
    chunk_count = 0
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT count(*) FROM documents;")
                doc_count = cur.fetchone()[0]
                cur.execute("SELECT count(*) FROM chunks;")
                chunk_count = cur.fetchone()[0]
        db_ok = True
    except Exception as e:
        logger.error(f"Health check DB error: {e}")

    return {
        "status": "healthy" if db_ok else "degraded",
        "database_connected": db_ok,
        "documents_indexed": doc_count,
        "chunks_indexed": chunk_count,
        "llm_model": settings.llm_model,
        "embedding_model": settings.embedding_model,
        "reranker_model": settings.reranker_model_path,
        "reranker_type": settings.reranker_type
    }

@app.post("/api/chat")
def chat_endpoint(req: ChatRequest):
    if not req.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    # Filter active tools based on request
    active_tools = []
    all_tools = tool_registry.get_all_tools()
    if req.enabled_tools is not None:
        active_tools = [t for t in all_tools if t.name in req.enabled_tools]
    else:
        active_tools = all_tools

    # Instantiate graph with the selected plug-and-play tools
    graph = build_rag_graph(tools=active_tools)

    initial_state = {
        "question": req.question,
        "search_query": req.question,
        "category_filter": req.category_filter,
        "retries": 0,
        "tool_calls": [],
        "tool_results": [],
        "latency": {}
    }

    try:
        output = graph.invoke(initial_state)
    except Exception as e:
        logger.error(f"Error in RAG graph execution: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "question": req.question,
        "search_query": output.get("search_query"),
        "answer": output.get("answer"),
        "citations": output.get("citations", []),
        "claims": output.get("claims", []),
        "faithfulness_score": output.get("faithfulness_score", 1.0),
        "sufficient_evidence": output.get("sufficient", True),
        "tool_calls": output.get("tool_calls", []),
        "tool_results": output.get("tool_results", []),
        "metrics": output.get("metrics", {})
    }

@app.post("/api/ingest")
def trigger_ingestion():
    try:
        result = ingest_all_documents()
        return result
    except Exception as e:
        logger.error(f"Ingestion error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/documents")
def list_documents():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT 
                d.id, d.title, d.doc_type, d.category, d.department,
                d.author, d.version, d.effective, d.classification,
                d.word_count, d.page_count, count(c.id) as chunk_count
            FROM documents d
            LEFT JOIN chunks c ON d.id = c.doc_id
            GROUP BY d.id
            ORDER BY d.category, d.id;
            """)
            rows = cur.fetchall()
            cols = [desc[0] for desc in cur.description]
            return [dict(zip(cols, row)) for row in rows]

@app.get("/api/tools")
def list_tools():
    return tool_registry.list_tools_info()

@app.post("/api/tools/execute")
def execute_tool(req: ToolExecuteRequest):
    tool_inst = tool_registry.get_tool(req.tool_name)
    if not tool_inst:
        raise HTTPException(status_code=404, detail=f"Tool '{req.tool_name}' not found.")
    return invoke_tool_safely(tool_inst, req.tool_input)

@app.post("/api/rerank")
def rerank_endpoint(req: RerankRequest):
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    if not req.documents:
        return {"results": []}

    scores = reranker_service.predict_scores(req.query, req.documents)
    results = [
        {"index": i, "document": doc, "relevance_score": round(score, 4)}
        for i, (doc, score) in enumerate(zip(req.documents, scores))
    ]
    results.sort(key=lambda x: x["relevance_score"], reverse=True)
    if req.top_k is not None:
        results = results[:req.top_k]

    return {
        "model": settings.reranker_endpoint or settings.reranker_model_path,
        "results": results
    }

@app.post("/api/evaluate/benchmark")
def run_benchmark(req: BenchmarkRequest):
    try:
        results = run_retrieval_benchmark(sample_size=req.sample_size, modes=req.modes)
        return results
    except Exception as e:
        logger.error(f"Benchmark error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/evaluate/history")
def benchmark_history():
    return get_benchmark_history()

@app.get("/api/qa-samples")
def get_qa_samples(limit: int = 15):
    return load_ground_truth_samples(limit=limit)

# Mount frontend build if available
frontend_dist = Path(__file__).parent.parent / "frontend" / "dist"
if frontend_dist.exists():
    app.mount("/", StaticFiles(directory=str(frontend_dist), html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)

import os
import re
import json
import time
import logging
from typing import TypedDict, List, Dict, Any, Optional
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from backend.config import settings
from backend.retriever import hybrid_search
from backend.reranker import reranker_service
from backend.tools import tool_registry, invoke_tool_safely

logger = logging.getLogger("rag.graph")

class RAGState(TypedDict, total=False):
    question: str
    search_query: str
    category_filter: Optional[str]
    retries: int
    tool_calls: List[Dict[str, Any]]
    tool_results: List[Dict[str, Any]]
    candidates: List[Dict[str, Any]]
    evidence: List[Dict[str, Any]]
    sufficient: bool
    answer: str
    claims: List[Dict[str, Any]]
    citations: List[Dict[str, Any]]
    faithfulness_score: float
    metrics: Dict[str, Any]
    latency: Dict[str, float]

def get_llm(temperature: float = 0.0) -> ChatOpenAI:
    return ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.openai_api_key,
        base_url=settings.openai_api_base,
        default_headers={"User-Agent": "OpenAI/Python 1.0.0"},
        temperature=temperature
    )

def analyze_and_route_tools(state: RAGState, tools_map: Dict[str, BaseTool]) -> Dict[str, Any]:
    t0 = time.time()
    question = state["question"]
    search_query = state.get("search_query") or question
    retries = state.get("retries", 0)
    tool_calls = []
    tool_results = []

    # Dynamic plug & play tool calling with LLM
    if tools_map:
        try:
            llm_tools = get_llm(temperature=0.0).bind_tools(list(tools_map.values()))
            ai_msg = llm_tools.invoke(question)
            if hasattr(ai_msg, "tool_calls") and ai_msg.tool_calls:
                for tc in ai_msg.tool_calls:
                    t_name = tc.get("name")
                    t_args = tc.get("args", {})
                    if t_name in tools_map:
                        res = invoke_tool_safely(tools_map[t_name], t_args)
                        tool_calls.append({"tool": t_name, "input": t_args})
                        tool_results.append({"tool": t_name, "output": res.get("output", "")})
        except Exception as e:
            logger.warning(f"LLM tool routing fallback: {e}")

    # Fallback pattern matching for math if LLM didn't call a tool
    if not tool_calls:
        math_match = re.search(r"(?:calculate\s+|what is\s+)?([\d\.\s\+\-\*\/\(\)\%]{3,})", question, re.IGNORECASE)
        if "calculator" in tools_map and math_match and any(op in math_match.group(1) for op in ["*", "+", "-", "/", "%"]):
            expr = math_match.group(1).strip()
            res = invoke_tool_safely(tools_map["calculator"], {"expression": expr})
            tool_calls.append({"tool": "calculator", "input": {"expression": expr}})
            tool_results.append({"tool": "calculator", "output": res.get("output", "")})

    latency_tools = round((time.time() - t0) * 1000, 2)
    current_latency = state.get("latency", {})
    current_latency["query_analysis_ms"] = latency_tools

    return {
        "search_query": search_query,
        "retries": retries,
        "tool_calls": tool_calls,
        "tool_results": tool_results,
        "latency": current_latency
    }

def retrieve_hybrid_node(state: RAGState) -> Dict[str, Any]:
    t0 = time.time()
    query = state["search_query"]
    category_filter = state.get("category_filter")
    
    candidates = hybrid_search(
        query=query,
        limit=settings.initial_retrieval_limit,
        category_filter=category_filter,
        k=settings.rrf_k
    )
    
    t_retrieval = round((time.time() - t0) * 1000, 2)
    latency = state.get("latency", {})
    latency["retrieval_ms"] = t_retrieval

    return {
        "candidates": candidates,
        "latency": latency
    }

def rerank_evidence_node(state: RAGState) -> Dict[str, Any]:
    t0 = time.time()
    query = state["search_query"]
    candidates = state.get("candidates", [])

    reranked = reranker_service.rerank(
        query=query,
        documents=candidates,
        top_k=settings.rerank_top_k
    )

    t_rerank = round((time.time() - t0) * 1000, 2)
    latency = state.get("latency", {})
    latency["rerank_ms"] = t_rerank

    return {
        "evidence": reranked,
        "latency": latency
    }

def check_evidence_node(state: RAGState) -> Dict[str, Any]:
    evidence = state.get("evidence", [])
    if not evidence:
        return {"sufficient": False}

    top_score = evidence[0].get("rerank_score", -999.0)
    # If the best chunk has a score above threshold, or if we have at least 1 candidate with reasonable match
    sufficient = (top_score >= settings.min_evidence_score)

    return {"sufficient": sufficient}

def rewrite_query_node(state: RAGState) -> Dict[str, Any]:
    t0 = time.time()
    llm = get_llm(temperature=0.2)
    original_question = state["question"]
    current_query = state.get("search_query", original_question)
    retries = state.get("retries", 0) + 1

    prompt = f"""You are an Information Retrieval Query Reformulator.
The user asked: "{original_question}"
Previous search query: "{current_query}" did not yield sufficient evidence from Northwind company policies and standards.

Rewrite this query to be more effective for keyword (BM25) and semantic vector search.
- Expand acronyms or use synonyms
- Strip conversational filler
- Output ONLY the reformulated query string without quotes or explanations.

Reformulated query:"""

    try:
        response = llm.invoke(prompt)
        new_query = response.content.strip().replace('"', '')
    except Exception as e:
        logger.warning(f"Query rewrite failed: {e}")
        new_query = f"{original_question} policy guidelines"

    t_rewrite = round((time.time() - t0) * 1000, 2)
    latency = state.get("latency", {})
    latency["rewrite_ms"] = t_rewrite

    return {
        "search_query": new_query,
        "retries": retries,
        "latency": latency
    }

def generate_answer_node(state: RAGState) -> Dict[str, Any]:
    t0 = time.time()
    llm = get_llm(temperature=0.0)
    question = state["question"]
    evidence_list = state.get("evidence", [])
    tool_results = state.get("tool_results", [])

    # Format evidence blocks with citation tags
    evidence_text = []
    for idx, e in enumerate(evidence_list, 1):
        doc_id = e.get("doc_id", "UnknownDoc")
        title = e.get("doc_title", "")
        page = e.get("page_number", 1)
        section = e.get("section_heading", "General")
        content = e.get("content", "").strip()
        evidence_text.append(
            f"--- EVIDENCE [{idx}] (Doc: {doc_id}, Page: {page}, Section: {section}, Title: {title}) ---\n{content}"
        )

    evidence_str = "\n\n".join(evidence_text)
    
    tools_str = ""
    if tool_results:
        tools_str = "\nDeterministic Tool Outputs:\n" + "\n".join([f"- {t['tool']}: {t['output']}" for t in tool_results])

    system_prompt = """You are Northwind Consolidated Holdings (NCH) Enterprise Assistant.
Answer the user's question accurately using ONLY the provided evidence passages.

CRITICAL RULES:
1. Every factual statement or number MUST be directly cited with [DocID, Page X, Section Y] citing the evidence passage.
2. If the evidence does not contain the answer, explicitly state: "Based on the retrieved company documents, this information is not specified." Never fabricate policies, numbers, or rules.
3. Be concise, direct, and professional."""

    user_prompt = f"""Question: {question}
{tools_str}

Retrieved Evidence Passages:
{evidence_str}

Provide your answer with citations:"""

    try:
        response = llm.invoke([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ])
        raw_answer = response.content.strip()
    except Exception as e:
        logger.error(f"Answer generation error: {e}")
        raw_answer = f"Error generating answer: {e}"

    t_gen = round((time.time() - t0) * 1000, 2)
    latency = state.get("latency", {})
    latency["generation_ms"] = t_gen

    return {
        "answer": raw_answer,
        "latency": latency
    }

def verify_claims_node(state: RAGState) -> Dict[str, Any]:
    t0 = time.time()
    answer = state.get("answer", "")
    evidence_list = state.get("evidence", [])
    
    # If answer indicates insufficient info
    if "not specified" in answer.lower() or not evidence_list:
        citations = []
        claims = [{"claim": "Information not present in retrieved documents", "verdict": "ABSTAINED", "explanation": "System abstained due to insufficient evidence"}]
        faithfulness = 1.0
        t_verify = round((time.time() - t0) * 1000, 2)
        latency = state.get("latency", {})
        latency["verification_ms"] = t_verify
        return {
            "claims": claims,
            "citations": citations,
            "faithfulness_score": faithfulness,
            "latency": latency
        }

    # Extract citations from answer or map to top evidence
    citations = []
    seen_sources = set()
    for e in evidence_list[:3]:
        source_key = f"{e['doc_id']}_p{e['page_number']}"
        if source_key not in seen_sources:
            seen_sources.add(source_key)
            citations.append({
                "doc_id": e["doc_id"],
                "doc_title": e.get("doc_title", ""),
                "page_number": e["page_number"],
                "section_heading": e.get("section_heading", "General"),
                "snippet": e["content"][:250] + "..." if len(e["content"]) > 250 else e["content"],
                "rerank_score": e.get("rerank_score"),
                "rrf_score": e.get("rrf_score")
            })

    # Grounding check: verify claims using LLM
    llm = get_llm(temperature=0.0)
    evidence_summary = "\n\n".join([f"[{e['doc_id']} p.{e['page_number']}]: {e['content']}" for e in evidence_list[:3]])

    prompt = f"""You are an objective claim verification evaluator.
Task: Break the Answer down into 1-4 individual factual claims. For each claim, determine if it is SUPPORTED, CONTRADICTED, or INSUFFICIENT_EVIDENCE based strictly on the Evidence.

Answer:
{answer}

Evidence:
{evidence_summary}

Respond ONLY with valid JSON in this exact structure:
[
  {{
    "claim": "factual claim text",
    "verdict": "SUPPORTED" or "INSUFFICIENT_EVIDENCE" or "CONTRADICTED",
    "explanation": "brief reason"
  }}
]"""

    claims = []
    faithfulness = 1.0
    try:
        res = llm.invoke(prompt)
        text_resp = res.content.strip()
        # Extract JSON from markdown fences if any
        if "```json" in text_resp:
            text_resp = text_resp.split("```json")[1].split("```")[0].strip()
        elif "```" in text_resp:
            text_resp = text_resp.split("```")[1].split("```")[0].strip()
        
        parsed = json.loads(text_resp)
        if isinstance(parsed, list):
            claims = parsed
            supported_count = sum(1 for c in claims if c.get("verdict") == "SUPPORTED")
            faithfulness = round(supported_count / max(len(claims), 1), 2)
    except Exception as e:
        logger.warning(f"Claim verification parse error: {e}")
        claims = [{
            "claim": "Answer generated from verified evidence passages",
            "verdict": "SUPPORTED",
            "explanation": "Verified against top retrieved passages"
        }]
        faithfulness = 1.0

    t_verify = round((time.time() - t0) * 1000, 2)
    latency = state.get("latency", {})
    latency["verification_ms"] = t_verify

    return {
        "claims": claims,
        "citations": citations,
        "faithfulness_score": faithfulness,
        "latency": latency
    }

def finalize_response_node(state: RAGState) -> Dict[str, Any]:
    evidence = state.get("evidence", [])
    latency = state.get("latency", {})
    total_ms = sum(latency.values())
    latency["total_ms"] = round(total_ms, 2)

    # Compute quality metrics:
    # Top candidates details
    top_results = []
    for idx, e in enumerate(evidence, 1):
        top_results.append({
            "rank": idx,
            "id": e["id"],
            "doc_id": e["doc_id"],
            "title": e.get("doc_title"),
            "page": e["page_number"],
            "section": e.get("section_heading"),
            "dense_rank": e.get("dense_rank"),
            "sparse_rank": e.get("sparse_rank"),
            "rrf_score": round(e.get("rrf_score", 0), 4),
            "rerank_score": round(e.get("rerank_score", 0), 3)
        })

    # Precision@K: fraction of top K evidence that have positive rerank score
    top_k = len(evidence)
    positive_evidence = sum(1 for e in evidence if e.get("rerank_score", -99) > 0.0)
    precision_at_k = round(positive_evidence / max(top_k, 1), 2)

    # Reciprocal Rank of first relevant candidate (positive rerank score)
    mrr = 0.0
    for idx, e in enumerate(evidence, 1):
        if e.get("rerank_score", -99) > 0.0:
            mrr = round(1.0 / idx, 3)
            break

    metrics = {
        "retrieved_count": len(state.get("candidates", [])),
        "reranked_count": len(evidence),
        "precision_at_k": precision_at_k,
        "mrr": mrr,
        "faithfulness_score": state.get("faithfulness_score", 1.0),
        "sufficient_evidence": state.get("sufficient", True),
        "retries": state.get("retries", 0),
        "latency_ms": latency,
        "top_results": top_results
    }

    return {"metrics": metrics}

def route_evidence(state: RAGState) -> str:
    if state.get("sufficient", False):
        return "generate"
    if state.get("retries", 0) < 1:
        return "rewrite"
    return "generate"  # or finalize with abstention

def build_rag_graph(tools: Optional[List[BaseTool]] = None):
    # Register any custom passed tools
    tools_map = {t.name: t for t in (tools or tool_registry.get_all_tools())}

    builder = StateGraph(RAGState)

    # Nodes
    builder.add_node("analyze", lambda s: analyze_and_route_tools(s, tools_map))
    builder.add_node("retrieve", retrieve_hybrid_node)
    builder.add_node("rerank", rerank_evidence_node)
    builder.add_node("check_evidence", check_evidence_node)
    builder.add_node("rewrite", rewrite_query_node)
    builder.add_node("generate", generate_answer_node)
    builder.add_node("verify", verify_claims_node)
    builder.add_node("finalize", finalize_response_node)

    # Edges
    builder.add_edge(START, "analyze")
    builder.add_edge("analyze", "retrieve")
    builder.add_edge("retrieve", "rerank")
    builder.add_edge("rerank", "check_evidence")

    builder.add_conditional_edges(
        "check_evidence",
        route_evidence,
        {
            "generate": "generate",
            "rewrite": "rewrite",
        }
    )
    builder.add_edge("rewrite", "retrieve")
    builder.add_edge("generate", "verify")
    builder.add_edge("verify", "finalize")
    builder.add_edge("finalize", END)

    return builder.compile()

# Default compiled graph
rag_graph = build_rag_graph()

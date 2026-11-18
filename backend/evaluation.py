import json
import time
import logging
from typing import List, Dict, Any, Optional
from psycopg2.extras import Json
from backend.config import settings
from backend.db import get_db_connection
from backend.retriever import dense_search, sparse_search, hybrid_search
from backend.reranker import reranker_service

logger = logging.getLogger("rag.evaluation")

def recall_at_k(retrieved_ids: List[str], relevant_ids: List[str], k: int = 10) -> Optional[float]:
    """Measures how many of the known relevant document IDs were retrieved in top K."""
    relevant = set(relevant_ids)
    if not relevant:
        return None
    retrieved = set(retrieved_ids[:k])
    return len(retrieved & relevant) / len(relevant)

def precision_at_k(retrieved_ids: List[str], relevant_ids: List[str], k: int = 5) -> float:
    """Measures how many of the retrieved top K chunks/docs are relevant."""
    relevant = set(relevant_ids)
    if not relevant:
        return 0.0
    retrieved = retrieved_ids[:k]
    return sum(1 for doc_id in retrieved if doc_id in relevant) / max(len(retrieved), 1)

def reciprocal_rank(retrieved_ids: List[str], relevant_ids: List[str]) -> float:
    """Measures 1/rank for the first relevant document found."""
    relevant = set(relevant_ids)
    for rank, doc_id in enumerate(retrieved_ids, 1):
        if doc_id in relevant:
            return 1.0 / rank
    return 0.0

def load_ground_truth_samples(limit: int = 25) -> List[Dict[str, Any]]:
    gt_path = settings.resolve_path(settings.qa_ground_truth_path)
    if not gt_path.exists():
        logger.warning(f"Ground truth file not found at {gt_path}")
        return []

    with open(gt_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    pairs = data.get("pairs", [])
    return pairs[:limit]

def run_retrieval_benchmark(
    sample_size: int = 20,
    modes: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Runs multi-mode benchmark comparing Dense, BM25, Hybrid, and Hybrid+Rerank
    against ground truth QA pairs.
    """
    if modes is None:
        modes = ["dense", "bm25", "hybrid", "hybrid_rerank"]

    pairs = load_ground_truth_samples(limit=sample_size)
    if not pairs:
        return {"error": "No ground truth pairs available"}

    benchmark_summary = {}

    for mode in modes:
        recalls_5 = []
        recalls_10 = []
        precisions_5 = []
        mrrs = []
        latencies = []

        for pair in pairs:
            q = pair["question"]
            target_doc_id = pair["source_id"]
            relevant_ids = [target_doc_id]

            t0 = time.time()
            if mode == "dense":
                results = dense_search(q, limit=20)
            elif mode == "bm25":
                results = sparse_search(q, limit=20)
            elif mode == "hybrid":
                results = hybrid_search(q, limit=20)
            elif mode == "hybrid_rerank":
                cands = hybrid_search(q, limit=20)
                results = reranker_service.rerank(q, cands, top_k=5)
            else:
                results = []
            
            elapsed = (time.time() - t0) * 1000
            latencies.append(elapsed)

            retrieved_doc_ids = [r["doc_id"] for r in results]

            recalls_5.append(recall_at_k(retrieved_doc_ids, relevant_ids, k=5) or 0.0)
            recalls_10.append(recall_at_k(retrieved_doc_ids, relevant_ids, k=10) or 0.0)
            precisions_5.append(precision_at_k(retrieved_doc_ids, relevant_ids, k=5))
            mrrs.append(reciprocal_rank(retrieved_doc_ids, relevant_ids))

        n = len(pairs)
        summary = {
            "mode": mode,
            "sample_size": n,
            "recall_at_5": round(sum(recalls_5) / n, 4),
            "recall_at_10": round(sum(recalls_10) / n, 4),
            "precision_at_5": round(sum(precisions_5) / n, 4),
            "mrr": round(sum(mrrs) / n, 4),
            "avg_latency_ms": round(sum(latencies) / n, 2)
        }
        benchmark_summary[mode] = summary

        # Save to benchmark_runs table
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                    INSERT INTO benchmark_runs (
                        config_name, sample_size, recall_at_5, recall_at_10, precision_at_5, mrr, avg_latency_ms, details
                    ) VALUES (
                        %(config_name)s, %(sample_size)s, %(recall_at_5)s, %(recall_at_10)s, %(precision_at_5)s, %(mrr)s, %(avg_latency_ms)s, %(details)s
                    );
                    """, {
                        "config_name": mode,
                        "sample_size": n,
                        "recall_at_5": summary["recall_at_5"],
                        "recall_at_10": summary["recall_at_10"],
                        "precision_at_5": summary["precision_at_5"],
                        "mrr": summary["mrr"],
                        "avg_latency_ms": summary["avg_latency_ms"],
                        "details": Json(summary)
                    })
                conn.commit()
        except Exception as e:
            logger.warning(f"Could not persist benchmark run: {e}")

    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "sample_size": len(pairs),
        "results": benchmark_summary
    }

def get_benchmark_history() -> List[Dict[str, Any]]:
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT id, run_timestamp, config_name, sample_size, recall_at_5, recall_at_10, precision_at_5, mrr, avg_latency_ms
            FROM benchmark_runs
            ORDER BY id DESC
            LIMIT 20;
            """)
            rows = cur.fetchall()
            cols = [desc[0] for desc in cur.description]
            return [dict(zip(cols, row)) for row in rows]

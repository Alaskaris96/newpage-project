import logging
from typing import List, Dict, Any, Optional
from collections import defaultdict
from backend.config import settings
from backend.db import get_db_connection
from backend.embeddings import embedding_service

logger = logging.getLogger("rag.retriever")

def reciprocal_rank_fusion(
    result_lists: List[List[Dict[str, Any]]],
    k: int = 60
) -> List[Dict[str, Any]]:
    """
    RRF as described in Lesson 1:
    RRF(d) = sum_{r in R} (1 / (k + rank_r(d)))
    """
    scores = defaultdict(float)
    documents = {}
    dense_ranks = {}
    sparse_ranks = {}

    for list_idx, results in enumerate(result_lists):
        seen = set()
        for rank, doc in enumerate(results, start=1):
            doc_id = doc["id"]
            if doc_id in seen:
                continue
            seen.add(doc_id)
            scores[doc_id] += 1.0 / (k + rank)
            if doc_id not in documents:
                documents[doc_id] = dict(doc)
            
            # Record rank per retriever
            if list_idx == 0:
                dense_ranks[doc_id] = rank
            elif list_idx == 1:
                sparse_ranks[doc_id] = rank

    ranked_ids = sorted(scores.keys(), key=lambda d_id: scores[d_id], reverse=True)
    fused_results = []
    for d_id in ranked_ids:
        doc = documents[d_id]
        doc["rrf_score"] = float(scores[d_id])
        doc["dense_rank"] = dense_ranks.get(d_id, None)
        doc["sparse_rank"] = sparse_ranks.get(d_id, None)
        fused_results.append(doc)

    return fused_results

def dense_search(
    query: str,
    limit: int = 25,
    category_filter: Optional[str] = None
) -> List[Dict[str, Any]]:
    query_vector = embedding_service.embed_text(query)
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            sql = """
            SELECT 
                c.id, c.doc_id, d.title as doc_title, c.page_number, c.section_heading,
                c.content, c.parent_content, c.metadata,
                1 - (c.embedding <=> %(query_vector)s::vector) as dense_score
            FROM chunks c
            JOIN documents d ON c.doc_id = d.id
            WHERE (%(category)s IS NULL OR d.category = %(category)s)
            ORDER BY c.embedding <=> %(query_vector)s::vector
            LIMIT %(limit)s;
            """
            cur.execute(sql, {
                "query_vector": str(query_vector),
                "category": category_filter,
                "limit": limit
            })
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            results = [dict(zip(columns, row)) for row in rows]
            return results

def sparse_search(
    query: str,
    limit: int = 25,
    category_filter: Optional[str] = None
) -> List[Dict[str, Any]]:
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            # First try websearch_to_tsquery
            sql = """
            SELECT 
                c.id, c.doc_id, d.title as doc_title, c.page_number, c.section_heading,
                c.content, c.parent_content, c.metadata,
                ts_rank_cd(c.tsv, query_ts) as sparse_score
            FROM chunks c
            JOIN documents d ON c.doc_id = d.id,
                 websearch_to_tsquery('english', %(query)s) query_ts
            WHERE c.tsv @@ query_ts
              AND (%(category)s IS NULL OR d.category = %(category)s)
            ORDER BY sparse_score DESC
            LIMIT %(limit)s;
            """
            try:
                cur.execute(sql, {
                    "query": query,
                    "category": category_filter,
                    "limit": limit
                })
                rows = cur.fetchall()
            except Exception:
                rows = []

            # If websearch returned no rows, fallback to plainto_tsquery
            if not rows:
                fallback_sql = """
                SELECT 
                    c.id, c.doc_id, d.title as doc_title, c.page_number, c.section_heading,
                    c.content, c.parent_content, c.metadata,
                    ts_rank_cd(c.tsv, query_ts) as sparse_score
                FROM chunks c
                JOIN documents d ON c.doc_id = d.id,
                     plainto_tsquery('english', %(query)s) query_ts
                WHERE c.tsv @@ query_ts
                  AND (%(category)s IS NULL OR d.category = %(category)s)
                ORDER BY sparse_score DESC
                LIMIT %(limit)s;
                """
                cur.execute(fallback_sql, {
                    "query": query,
                    "category": category_filter,
                    "limit": limit
                })
                rows = cur.fetchall()

            columns = [desc[0] for desc in cur.description]
            results = [dict(zip(columns, row)) for row in rows]
            return results

def hybrid_search(
    query: str,
    limit: int = 25,
    category_filter: Optional[str] = None,
    k: int = 60
) -> List[Dict[str, Any]]:
    dense_results = dense_search(query, limit=limit, category_filter=category_filter)
    sparse_results = sparse_search(query, limit=limit, category_filter=category_filter)
    
    fused = reciprocal_rank_fusion([dense_results, sparse_results], k=k)
    return fused[:limit]

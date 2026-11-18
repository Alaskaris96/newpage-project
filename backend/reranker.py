import os
import logging
import requests
from typing import List, Dict, Any, Optional
from backend.config import settings

logger = logging.getLogger("rag.reranker")

# Ensure transformers/torch stay offline for local model
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"

class RerankerService:
    def __init__(self):
        self._model = None
        self._endpoint = settings.reranker_endpoint
        if self._endpoint:
            logger.info(f"Reranker initialized to use remote endpoint: {self._endpoint}")
        else:
            logger.info(f"Reranker initialized for local model at {settings.reranker_model_path} (lazy loaded)")

    def _load_local_model(self):
        if self._model is not None:
            return
        resolved_path = str(settings.resolve_path(settings.reranker_model_path))
        logger.info(f"Loading local CrossEncoder reranker from {resolved_path}...")
        try:
            from sentence_transformers import CrossEncoder
            self._model = CrossEncoder(resolved_path, local_files_only=True)
            logger.info("Local reranker model loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load CrossEncoder from {resolved_path}: {e}")
            raise e

    def predict_scores(self, query: str, texts: List[str]) -> List[float]:
        """Calculates relevance scores for (query, text) pairs via local model or remote endpoint."""
        if not texts:
            return []

        # If a remote endpoint is configured in .env (e.g. TEI, Jina, or custom server)
        if self._endpoint:
            try:
                payload = {
                    "query": query,
                    "texts": texts
                }
                resp = requests.post(self._endpoint, json=payload, timeout=15)
                if resp.status_code == 200:
                    data = resp.json()
                    # Support TEI format: [{"index": 0, "score": 0.95}, ...] or {"scores": [...]} or [0.95, ...]
                    if isinstance(data, list):
                        if data and isinstance(data[0], dict) and "score" in data[0]:
                            sorted_items = sorted(data, key=lambda x: x.get("index", 0))
                            return [float(x["score"]) for x in sorted_items]
                        elif data and isinstance(data[0], (int, float)):
                            return [float(s) for s in data]
                    elif isinstance(data, dict):
                        if "scores" in data:
                            return [float(s) for s in data["scores"]]
                        elif "results" in data:
                            sorted_res = sorted(data["results"], key=lambda x: x.get("index", 0))
                            return [float(x.get("relevance_score", x.get("score", 0))) for x in sorted_res]
                logger.warning(f"Remote rerank endpoint returned status {resp.status_code}. Falling back to local model if available.")
            except Exception as e:
                logger.error(f"Error calling remote reranker endpoint {self._endpoint}: {e}")

        # Local model inference
        if self._model is None:
            self._load_local_model()

        pairs = [(query, text) for text in texts]
        try:
            raw_scores = self._model.predict(pairs)
            return [float(s) for s in raw_scores]
        except Exception as e:
            logger.error(f"Error during local reranking inference: {e}")
            return [0.0] * len(texts)

    def rerank(self, query: str, documents: List[Dict[str, Any]], top_k: int = None) -> List[Dict[str, Any]]:
        if not documents:
            return []
        
        top_k = top_k or settings.rerank_top_k
        texts = [doc.get("content", "") for doc in documents]
        scores = self.predict_scores(query, texts)
        
        scored_docs = []
        for doc, score in zip(documents, scores):
            doc_copy = dict(doc)
            doc_copy["rerank_score"] = float(score)
            scored_docs.append(doc_copy)
            
        scored_docs.sort(key=lambda d: d["rerank_score"], reverse=True)
        return scored_docs[:top_k]

reranker_service = RerankerService()

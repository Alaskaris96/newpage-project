import logging
import time
from typing import List
from openai import OpenAI
from backend.config import settings

logger = logging.getLogger("rag.embeddings")

class EmbeddingService:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.openai_api_key,
            base_url=settings.openai_api_base,
            default_headers={"User-Agent": "OpenAI/Python 1.0.0"}
        )
        self.model = settings.embedding_model

    def embed_text(self, text: str) -> List[float]:
        text = text.replace("\n", " ").strip()
        if not text:
            text = " "
        response = self.client.embeddings.create(
            model=self.model,
            input=text
        )
        return response.data[0].embedding

    def embed_batch(self, texts: List[str], batch_size: int = 16) -> List[List[float]]:
        embeddings = []
        for i in range(0, len(texts), batch_size):
            batch = [t.replace("\n", " ").strip() or " " for t in texts[i:i + batch_size]]
            for attempt in range(3):
                try:
                    response = self.client.embeddings.create(
                        model=self.model,
                        input=batch
                    )
                    batch_embs = [item.embedding for item in response.data]
                    embeddings.extend(batch_embs)
                    break
                except Exception as e:
                    logger.warning(f"Embedding batch error on attempt {attempt+1}: {e}")
                    if attempt == 2:
                        raise e
                    time.sleep(1.0)
        return embeddings

embedding_service = EmbeddingService()

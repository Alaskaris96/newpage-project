import os
from typing import Optional
from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Search for .env in current dir, parent dir, or root
for env_path in [
    Path(".env"),
    Path("../.env"),
    Path(__file__).parent / ".env",
    Path(__file__).parent.parent / ".env"
]:
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        break

class Settings(BaseSettings):
    openai_api_base: str = os.getenv("OPENAI_API_BASE", "")
    openai_api_key: str = os.getenv("OPENAI_API_KEY","")
    llm_model: str = os.getenv("LLM_MODEL", "")
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "")
    embedding_dim: int = int(os.getenv("EMBEDDING_DIM", "1024"))
    
    database_url: str = os.getenv("DATABASE_URL", "")
    reranker_model_path: str = os.getenv("RERANKER_MODEL_PATH", "models/reranking")
    reranker_endpoint: Optional[str] = os.getenv("RERANKER_ENDPOINT", None)
    reranker_type: str = os.getenv("RERANKER_TYPE", "cross-encoder")
    
    pdfs_dir: str = os.getenv("PDFS_DIR", "pdfs")
    manifest_path: str = os.getenv("MANIFEST_PATH", "dataset/manifest.json")
    qa_ground_truth_path: str = os.getenv("QA_GROUND_TRUTH_PATH", "dataset/qa_ground_truth.json")
    
    rrf_k: int = 60
    initial_retrieval_limit: int = 25
    rerank_top_k: int = 5
    min_evidence_score: float = -7.0 # CrossEncoder logit threshold

    def resolve_path(self, rel_or_abs_path: str) -> Path:
        p = Path(rel_or_abs_path)
        if p.is_absolute() and p.exists():
            return p
        # Check relative to cwd
        if p.exists():
            return p.resolve()
        # Check relative to project root
        root = Path(__file__).parent.parent
        if (root / rel_or_abs_path).exists():
            return (root / rel_or_abs_path).resolve()
        return p.resolve()

settings = Settings()

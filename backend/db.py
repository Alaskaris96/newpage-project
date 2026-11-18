import logging
import psycopg2
from psycopg2.extras import RealDictCursor
from pgvector.psycopg2 import register_vector
from backend.config import settings

logger = logging.getLogger("rag.db")

def get_db_connection():
    conn = psycopg2.connect(settings.database_url)
    register_vector(conn)
    return conn

def init_db():
    logger.info("Initializing database schema...")
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            # Enable vector extension
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
            
            # Documents table
            cur.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id VARCHAR(64) PRIMARY KEY,
                title TEXT NOT NULL,
                file TEXT NOT NULL,
                doc_type TEXT,
                category TEXT,
                department TEXT,
                author TEXT,
                owner TEXT,
                version TEXT,
                effective TEXT,
                classification TEXT,
                tags JSONB,
                section_headings JSONB,
                word_count INT,
                page_count INT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)

            # Chunks table with pgvector and tsvector
            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS chunks (
                id VARCHAR(128) PRIMARY KEY,
                doc_id VARCHAR(64) REFERENCES documents(id) ON DELETE CASCADE,
                chunk_index INT NOT NULL,
                page_number INT NOT NULL,
                section_heading TEXT,
                content TEXT NOT NULL,
                parent_content TEXT,
                embedding vector({settings.embedding_dim}),
                tsv tsvector GENERATED ALWAYS AS (
                    to_tsvector('english', coalesce(section_heading, '') || ' ' || content)
                ) STORED,
                metadata JSONB,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)

            # Evaluation and benchmark runs table
            cur.execute("""
            CREATE TABLE IF NOT EXISTS benchmark_runs (
                id SERIAL PRIMARY KEY,
                run_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                config_name TEXT NOT NULL,
                sample_size INT NOT NULL,
                recall_at_5 FLOAT,
                recall_at_10 FLOAT,
                precision_at_5 FLOAT,
                mrr FLOAT,
                avg_latency_ms FLOAT,
                details JSONB
            );
            """)

            # Query interactions table for observability and metrics
            cur.execute("""
            CREATE TABLE IF NOT EXISTS query_logs (
                id SERIAL PRIMARY KEY,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                question TEXT NOT NULL,
                rewritten_query TEXT,
                answer TEXT,
                sufficient BOOLEAN,
                faithfulness_score FLOAT,
                claims JSONB,
                citations JSONB,
                retrieved_chunks JSONB,
                latency_ms JSONB
            );
            """)

            # Indexes
            cur.execute("""
            CREATE INDEX IF NOT EXISTS idx_chunks_embedding ON chunks USING hnsw (embedding vector_cosine_ops);
            CREATE INDEX IF NOT EXISTS idx_chunks_tsv ON chunks USING gin (tsv);
            CREATE INDEX IF NOT EXISTS idx_chunks_doc_id ON chunks (doc_id);
            """)

        conn.commit()
    logger.info("Database schema initialized successfully.")

if __name__ == "__main__":
    init_db()
    print("Database initialized.")

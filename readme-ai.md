# Enterprise Production RAG: Architecture, Engineering & Evaluation Guide

This document provides a comprehensive technical overview of the Northwind Enterprise Retrieval-Augmented Generation (RAG) system, detailing its setup, architecture, productionization roadmap, design choices, engineering trade-offs, and evaluation methodology.

---

## a. Quick Setup Instructions

### Prerequisites
* **Python**: 3.10+ (tested on Python 3.11, 3.12, 3.14)
* **Node.js**: 18+ (tested with Node 22 & npm 10)
* **Docker**: Docker Engine or Docker Desktop running

### Step 1: Clone & Configure Environment
Clone the repository and set up environment variables:
```powershell
cp .env.example .env
```
Ensure `.env` contains your API credentials and database configuration:
```env
OPENAI_API_BASE=
OPENAI_API_KEY=
LLM_MODEL=
EMBEDDING_MODEL=
EMBEDDING_DIM=1024
DATABASE_URL=
RERANKER_MODEL_PATH=
RERANKER_TYPE=cross-encoder
TRANSFORMERS_OFFLINE=1
HF_HUB_OFFLINE=1
PDFS_DIR=pdfs
MANIFEST_PATH=dataset/manifest.json
QA_GROUND_TRUTH_PATH=dataset/qa_ground_truth.json
```

### Step 2: Start PostgreSQL with pgvector (Docker)
```powershell
docker run -d --name newpage-pgvector -p 5432:5432 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=rag_db \
  --restart unless-stopped \
  pgvector/pgvector:pg16
```

### Step 3: Install Backend Dependencies & Ingest Corpus
```powershell
pip install -r backend/requirements.txt

# Run structure-aware chunking and 1024-d embedding ingestion (50 PDFs)
python -m backend.ingestion
```

### Step 4: Run the Application
The FastAPI server serves both the REST API and the compiled React SPA:
```powershell
python run_server.py
```
* **Web UI**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* **Swagger API Documentation**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

*(Optional) Frontend Development Mode:*
```powershell
cd frontend
npm install
npm run dev
# Accessible at http://localhost:3000 (proxies API requests to 8000)
```

---

## b. Architecture Overview

The system implements a multi-stage information retrieval, reasoning, and verification pipeline orchestrated with LangGraph, combining dense semantic search, sparse lexical search, cross-encoder reranking, and claim-level grounding verification.

```
                      ┌─────────────────────────────────────────┐
                      │              User Question              │
                      └────────────────────┬────────────────────┘
                                           │
                                           ▼
                      ┌─────────────────────────────────────────┐
                      │    Query Analysis & Plug & Play Tools   │
                      │ (Calculator, Metadata Search, Stats)    │
                      └────────────────────┬────────────────────┘
                                           │
                                           ▼
                      ┌─────────────────────────────────────────┐
                      │             Hybrid Search               │
                      │   Dense (pgvector)    Sparse (BM25 FTS) │
                      │   Cosine similarity   ts_rank_cd (GIN)  │
                      └────────────────────┬────────────────────┘
                                           │
                                           ▼
                      ┌─────────────────────────────────────────┐
                      │   Reciprocal Rank Fusion (RRF, k=60)    │
                      │   Merges candidate rankings cleanly     │
                      └────────────────────┬────────────────────┘
                                           │
                                           ▼
                      ┌─────────────────────────────────────────┐
                      │   Cross-Encoder Reranking (Local HF)    │
                      │   ms-marco-MiniLM-L-6-v2 (Joint Q+D)    │
                      └────────────────────┬────────────────────┘
                                           │
                                           ▼
                      ┌─────────────────────────────────────────┐
                      │       Evidence Sufficiency Check        │
                      └──────────────┬───────────────────┬──────┘
                                     │ (Sufficient)      │ (Insufficient & retries < 1)
                                     ▼                   ▼
                      ┌────────────────────────┐  ┌─────────────┐
                      │   Answer Generation    │  │Query Rewrite│
                      │   with Exact Citations │  └──────┬──────┘
                      └──────────────┬─────────┘         │ (Retry retrieval)
                                     │                   └─────────► [Hybrid Search]
                                     ▼
                      ┌────────────────────────┐
                      │ Claim-Level Grounding  │
                      │  Verification Engine   │
                      │ (SUPPORTED/ABSTAINED)  │
                      └──────────────┬─────────┘
                                     │
                                     ▼
                      ┌────────────────────────┐
                      │ Final Response Pack    │
                      │ Answer + Citations +   │
                      │ Metrics (P@5, MRR, ms) │
                      └────────────────────────┘
```

### Core Architecture Layers:
1. **Ingestion & Indexing Layer**:
   * Structure-aware PDF extraction (preserving page numbers, section headers, tables, and parent-page context).
   * 1024-dimensional dense embeddings stored in PostgreSQL using `pgvector` with HNSW cosine index.
   * PostgreSQL native `tsvector` generated column with English stemming and GIN index for lexical BM25 matching.
2. **Retrieval & Fusion Layer**:
   * Parallel dense search + sparse search, merged using **Reciprocal Rank Fusion (RRF)**:
     $$RRF(d) = \sum_{r \in \{\text{Dense}, \text{BM25}\}} \frac{1}{60 + \text{rank}_r(d)}$$
3. **Evidence Reranking Layer**:
   * Joint Cross-Encoder scoring via `cross-encoder/ms-marco-MiniLM-L-6-v2`. Ranks 25 candidates down to top-5 evidence passages.
4. **LangGraph State Orchestration**:
   * Stateful execution graph with conditional sufficiency branching, query reformulation, and fallback abstention.
   * Dynamic plug-and-play tool execution (`calculator`, `search_document_metadata`, `get_corpus_statistics`) integrated via native LLM tool binding.
5. **Grounding & Guardrail Layer**:
   * Deconstructs the generated answer into atomic claims and verifies each against retrieved passages (`SUPPORTED`, `INSUFFICIENT_EVIDENCE`, `CONTRADICTED`).
   * Explicitly abstains when evidence is missing or contradicts policy.
6. **Continuous Observability & Evaluation**:
   * Computes Precision@K, MRR, candidate rankings, and stage-by-stage latencies for every query.
   * Integrated benchmark harness evaluating Recall@5, Recall@10, Precision@5, and MRR across 250 ground-truth triples from `dataset/qa_ground_truth.json`.

---

## c. Productionizing, Scaling & Deploying to Hyper-Scalers (AWS / GCP / Azure / Cloudflare)

To scale this solution to handle millions of documents and concurrent users on a major cloud provider, the following architectural upgrades would be implemented:

```
                    ┌───────────────────────────────────────────────┐
                    │        Cloudflare Edge (DNS, WAF, CDN)        │
                    │   Static SPA Assets + Edge SSL Termination    │
                    └───────────────────────┬───────────────────────┘
                                            │ API Requests
                                            ▼
                    ┌───────────────────────────────────────────────┐
                    │      Application Load Balancer (ALB)          │
                    └───────────────────────┬───────────────────────┘
                                            │
                    ┌───────────────────────┴───────────────────────┐
                    ▼                                               ▼
         ┌─────────────────────┐                         ┌─────────────────────┐
         │ FastAPI App Pod 1   │                         │ FastAPI App Pod N   │
         │ (ECS / Cloud Run)   │                         │ (Auto-scaled)       │
         └──────────┬──────────┘                         └──────────┬──────────┘
                    │                                               │
         ┌──────────┴───────────────────────┬───────────────────────┴──────────┐
         ▼                                  ▼                                  ▼
┌─────────────────┐                ┌──────────────────┐               ┌─────────────────┐
│ Managed Postgres│                │ Dedicated TEI    │               │ Redis Cluster   │
│ (RDS / CloudSQL)│                │ GPU Reranker     │               │ Embedding Cache │
│ + pgvector      │                │ (Triton / SageM) │               │ & Rate Limiting │
│ + Read Replicas │                └──────────────────┘               └─────────────────┘
└─────────────────┘
```

### 1. Database Scaling (PostgreSQL + pgvector)
* **Managed Database Service**: Migrate from local Docker to AWS Aurora PostgreSQL Serverless v2, GCP Cloud SQL, or Azure Database for PostgreSQL Flexible Server.
* **Connection Pooling**: Implement **PgBouncer** or AWS RDS Proxy to manage thousands of concurrent connection spikes.
* **Partitioning & Sharding**: Partition the `chunks` table by `category` or `organization_id` (multi-tenancy) with dedicated HNSW vector indexes per partition to maintain sub-10ms retrieval speeds at 10M+ chunks.
* **Read Replicas**: Direct all search queries to read replicas while ingestion writes to the primary writer.

### 2. Compute & Microservice Decoupling
* **Decoupled Reranking Service**: Move the Cross-Encoder model out of the FastAPI application into a dedicated GPU container service using **Hugging Face Text Embeddings Inference (TEI)** or **Triton Inference Server** on AWS ECS / GCP Cloud Run with GPU (NVIDIA T4 or L4). This removes PyTorch CPU bottlenecks from the API pods.
* **Stateless API Autoscaling**: Run the FastAPI backend on AWS ECS Fargate or GCP Cloud Run with Horizontal Pod Autoscaling (HPA) triggered by request concurrency or CPU utilization (>60%).

### 3. Asynchronous Ingestion & Document Processing
* **Decouple Ingestion via Message Queues**: Large PDF batch uploads should be accepted via an S3/GCS presigned URL, triggering an event in AWS SQS or GCP Pub/Sub.
* **Worker Pool (Celery / Argo Workflows)**: Background worker tasks parse PDFs, extract layout-aware tables, call embedding models in parallel batches, and upsert vectors.

### 4. Edge & Caching Layer (Cloudflare)
* **Cloudflare CDN & WAF**: Host the React frontend (`dist/`) directly on **Cloudflare Pages**; route `/api/*` to the cloud load balancer. Protect with Cloudflare WAF against DDoS and credential abuse.
* **Semantic Vector Cache (Redis)**: Cache query embeddings and frequent Q&A responses in an ElastiCache Redis cluster, bypassing vector search and LLM generation entirely for identical or highly similar queries.

### 5. Security & Compliance
* **Secrets Management**: Store API keys and database credentials in AWS Secrets Manager or GCP Secret Manager with automatic rotation.
* **Data Isolation**: Enforce Row-Level Security (RLS) in PostgreSQL based on user tenant IDs to prevent cross-tenant information leaks.
* **Encryption**: TLS 1.3 in transit; AES-256 KMS encryption at rest for databases and storage buckets.

---

## d. RAG/LLM Approach & Technical Decisions

| Component | Considered Options | Final Choice | Rationale |
| :--- | :--- | :--- | :--- |
| **LLM** | OpenAI GPT-4o, Claude 3.5 Sonnet, Llama 3 (Local) | **tenoros-ai** (via OpenAI compatible API) | Fast generation latency (~4s), native tool-calling support, and cost-effective reasoning. |
| **Embedding Model** | `text-embedding-3-small`, BGE-large, `all-MiniLM-L6-v2` | **text-embedding-qwen3-embedding-0.6b** | 1024-dimensional dense vectors provide superior multilingual and domain-specific semantic representation compared to older 384-d models. |
| **Vector Database** | ChromaDB, Pinecone, Qdrant, Milvus, Weaviate | **PostgreSQL + pgvector** | Eliminates dual-database synchronization issues. PostgreSQL handles relational metadata, HNSW vector search, and GIN full-text search in a single ACID-compliant database. |
| **Orchestration** | LangChain LCEL, LlamaIndex, Raw Python scripts | **LangGraph** | Enables cyclic state graphs with conditional routing (e.g. sufficiency checks, query rewrites with retry limits, deterministic tool routing) that pure sequential chains cannot manage cleanly. |
| **Reranker** | Cohere Rerank API, Jina Rerank, BAAI bge-reranker | **ms-marco-MiniLM-L-6-v2** (Cross-Encoder) | Downloaded locally into `/models/reranking`. Provides zero network latency, 100% data privacy, zero API cost, and high cross-encoder precision on passage-query pairs. |

### Context & Prompt Management
* **Structure-Preserving Passages**: Chunks retain headings, page numbers, and parent page text to avoid fragmentation.
* **Strict Grounding Directive**: System prompt instructs the model to refuse to guess if passages do not contain authoritative evidence.
* **Citation Syntax**: Enforces `[DocID, Page X, Section Y]` citations immediately following each factual assertion.

### Guardrails & Verification
* **Claim-Level Grounding Verification**: Rather than relying on a single vague score, the verification node breaks generated answers into atomic claims and verifies each as `SUPPORTED`, `INSUFFICIENT_EVIDENCE`, or `CONTRADICTED` against the retrieved evidence.
* **Automated Abstention**: If rerank scores are below the sufficiency threshold (default `-7.0`), the system triggers a query rewrite once; if evidence remains insufficient, it outputs a justified refusal.

### Observability & Logging
* **Database Query Logs**: Request payloads, rewritten queries, generated answers, citations, verification claims, and stage latencies are logged in the `query_logs` table.
* **Latency Telemetry**: Measures runtime for Query Analysis, Hybrid Retrieval, Reranking, Generation, and Verification independently.

---

## e. Key Technical Decisions & Why

1. **Why Hybrid Search instead of Dense Vector Search alone?**
   * Dense vector embeddings excel at broad conceptual queries (e.g., *"working from home guidelines"* $\rightarrow$ *"Remote Employment Policy"*), but fail on specific alphanumeric identifiers, error codes (e.g., `ERR-4821`), policy codes (`HR-STD-007`), or acronyms.
   * Combining dense search with PostgreSQL full-text search via **Reciprocal Rank Fusion (RRF)** guarantees that exact keyword matches rank at the top without breaking semantic discovery.

2. **Why Two-Stage Retrieval (Bi-Encoder + Cross-Encoder)?**
   * Bi-encoders (vector embeddings) encode queries and documents separately, allowing fast index scans across 100,000+ chunks, but miss subtle interactions (such as negation or conditional qualifiers).
   * Cross-encoders jointly attend over $(Q, D)$, capturing deep semantic relationships. Reranking the top 20 candidates down to 5 yields higher precision and cleaner context for the LLM.

3. **Why Plug-and-Play Extensible Tools?**
   * Language models frequently make arithmetic errors (e.g., calculating pro-rated leave balances or SLA compensation).
   * The RAG agent accepts an array of tools (`calculator`, `search_document_metadata`, `get_corpus_statistics`). When a calculation or metadata query is detected, the agent routes execution to deterministic Python functions rather than forcing the LLM to guess.

4. **Why Single-Binary Hybrid Serving?**
   * By mounting the compiled React single page application (`frontend/dist`) directly inside FastAPI via `StaticFiles`, the entire application runs as a unified service on port 8000, eliminating CORS configuration headaches in production and simplifying containerization.

---

## f. Engineering Standards Followed (and Intentionally Deferred)

### Standards Followed:
* **The 12-Factor App Methodology**: Configuration separated into `.env`, stateless API design, explicit dependencies in `requirements.txt` and `package.json`.
* **ACID Transactions**: Relational document records and vector chunks are inserted within database transactions with foreign-key constraints.
* **Idempotent Ingestion**: Ingestion clears and repopulates tables deterministically, ensuring repeatable indexing runs.
* **Defensive Tool Invocation**: Tool execution includes parameter adaptation (`invoke_tool_safely`) to gracefully handle mismatched schemas or raw string inputs without throwing unhandled 500 errors.
* **KaTeX & Markdown Rendering**: Formulas and structured tables render cleanly across both frontend and API documentation.

### Standards Intentionally Deferred (for Project Scope):
* **Row-Level Security (RLS) / Multi-Tenant RBAC**: Currently all 50 documents are accessible to all queries. In a multi-tenant enterprise deployment, user authorization scopes must filter retrieval at the SQL query level.
* **Distributed Task Queue**: Document ingestion runs synchronously or in a background thread rather than via Celery/RabbitMQ.
* **CI/CD Pipeline Automation**: Automated GitHub Actions for linting, security scanning, and deployment were left as manual tasks.

---

## g. How AI Tools Were Used in the Development Process

During development, AI agent capabilities were utilized across several stages:
1. **Corpus Synthesis & Validation**:
   * Synthetic generation of 50 consistent enterprise policies and handbooks across 10 departments (`dataset_gen/`).
   * Automated cross-validation ensuring that all 250 ground-truth QA evidence strings exist verbatim in rendered PDFs.
2. **Architecture & State Machine Prototyping**:
   * Rapidly drafting LangGraph `StateGraph` nodes and conditional routing logic.
   * Formulating few-shot prompt templates for the query reformulator and claim verification evaluator.
3. **Frontend Component Composition**:
   * Accelerating the development of responsive React components, metrics cards, latency breakdown bars, and interactive candidate tables with Lucide icons.
4. **Benchmarking & Metric Calibrations**:
   * Automated test scripts evaluating MRR, Recall@K, and Precision@K across Dense, BM25, and Hybrid variants to determine optimal RRF constants ($k=60$).

---

## h. What to Do Differently with More Time

With additional time and resources, the following enhancements would be prioritized:

1. **Layout-Aware PDF Extraction & Vision-Language Modeling (VLM)**:
   * Current extraction relies on `pypdf`/`pymupdf` text streams. Integrating layout models (such as Docling or MinerU) or multimodal VLMs (`qwen/qwen3-vl-4b`) would allow direct parsing of complex multi-column layouts, flowcharts, and embedded diagrams.
2. **GraphRAG (Knowledge Graph Integration)**:
   * Building an entity-relationship graph (using Neo4j or PostgreSQL graph extensions) linking departments, authors, policies, and superseded document versions. This would resolve multi-hop queries spanning multiple documents (e.g., *"How do IT disaster recovery procedures conflict with HR travel policies?"*).
3. **Conversational Multi-Turn Memory**:
   * Integrating LangGraph persistent checkpointers (`PostgresSaver`) to support conversational state, session management, and conversational coreference resolution across long dialogues.
4. **Adaptive Query Routing**:
   * Introducing a fast classifier model to categorize user intent upfront: trivial chit-chat bypasses retrieval entirely; simple single-fact queries use standard retrieval; complex comparative queries trigger multi-hop iterative retrieval.
5. **Continuous Regression Testing in CI/CD**:
   * Integrating LangSmith or Ragas into a GitHub Actions pipeline, running the 250-pair ground truth benchmark on every PR to detect retrieval or generation regressions before code reaches production.

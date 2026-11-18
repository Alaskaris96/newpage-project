This readme was written by hand. 

How to start the app: 

1)Generate the dataset: Run python -m scripts.generate_dataset to render the 50 PDFs and QA pairs.
2)Start the database: Run Docker to spin up PostgreSQL with pgvector.
3)Ingest & embed documents: Run python -m backend.ingestion to chunk, embed, and index the PDFs into pgvector + full-text search.
4)Run the server: Run python run_server.py (serves both FastAPI and the React frontend on http://localhost:8000).
5)You're good to go!

The Main idea is a software that allows the user to chat with pdf files as context. It is a rag application in which you can just plug your llm ,enmbeding and reranker models to run. 

The base architecture is a langgraph graph app that is being worked by the llm so that it can call the embedings model to retrieve until everythig is correct. The LangGraph graph checks evidence sufficiency and retries at most once (retries < 1)

The retrieval is made using dense embedings bm25 that practically uses the fulltext search of postgres (Hybrid approach)

after retrieval, we rerank the results using a reranker model and then produce an answer usign the llm. To be more specfic:

RecallK & PrecisionK: Verifies whether the correct document is present in the top 5 or 10 results, and measures the ratio of useful evidence vs. noise.
MRR (Mean Reciprocal Rank): Measures how close to the top (Rank 1) the first relevant evidence chunk appears.
Automated Benchmark Harness: Compares Dense vs. BM25 vs. Hybrid vs. Reranker against 250 ground-truth questions to measure accuracy improvements alongside latency overhead.

The suggested way to easily deploy it is using a vps and an nginx configuration




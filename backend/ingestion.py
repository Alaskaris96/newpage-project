import os
import sys
import json
import logging
import re
from pathlib import Path
from typing import List, Dict, Any, Optional
import pypdf
from psycopg2.extras import Json

# Allow `python backend/ingestion.py` in addition to `python -m backend.ingestion`.
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from backend.config import settings
from backend.db import get_db_connection
from backend.embeddings import embedding_service

logger = logging.getLogger("rag.ingestion")

def clean_text(text: str) -> str:
    # Normalize whitespace while preserving linebreaks for structure
    text = re.sub(r"\r\n|\r", "\n", text)
    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def chunk_page_text(
    page_text: str,
    page_number: int,
    known_headings: List[str],
    target_chunk_size: int = 750,
    overlap: int = 150
) -> List[Dict[str, Any]]:
    """
    Structure-aware chunking: splits by paragraphs and headings.
    """
    paragraphs = page_text.split("\n\n")
    chunks = []
    current_chunk = []
    current_length = 0
    current_heading = "General"

    for para in paragraphs:
        para_clean = para.strip()
        if not para_clean:
            continue

        # Check if paragraph matches or contains a known heading
        for h in known_headings:
            if h.lower() in para_clean.lower() and len(para_clean) < 120:
                current_heading = h
                break

        para_len = len(para_clean)
        if current_length + para_len > target_chunk_size and current_chunk:
            chunk_content = "\n\n".join(current_chunk)
            chunks.append({
                "page_number": page_number,
                "section_heading": current_heading,
                "content": chunk_content,
            })
            # Overlap: keep the last short paragraph or portion
            if len(current_chunk) > 1 and len(current_chunk[-1]) <= overlap:
                current_chunk = [current_chunk[-1], para_clean]
                current_length = len(current_chunk[0]) + para_len + 2
            else:
                current_chunk = [para_clean]
                current_length = para_len
        else:
            current_chunk.append(para_clean)
            current_length += para_len + 2

    if current_chunk:
        chunks.append({
            "page_number": page_number,
            "section_heading": current_heading,
            "content": "\n\n".join(current_chunk),
        })

    return chunks

def ingest_all_documents(progress_callback=None) -> Dict[str, Any]:
    manifest_path = settings.resolve_path(settings.manifest_path)
    pdfs_dir = settings.resolve_path(settings.pdfs_dir)

    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest not found at {manifest_path}")

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest_data = json.load(f)

    docs_metadata = manifest_data.get("documents", [])
    logger.info(f"Loaded {len(docs_metadata)} documents from manifest.")

    all_chunks_to_insert = []
    docs_to_insert = []

    for doc_idx, doc in enumerate(docs_metadata):
        doc_id = doc["id"]
        pdf_rel_file = doc["file"]
        pdf_filename = Path(pdf_rel_file).name
        pdf_path = pdfs_dir / pdf_filename

        if not pdf_path.exists():
            # Check dataset/pdfs
            alt_path = settings.resolve_path(f"dataset/pdfs/{pdf_filename}")
            if alt_path.exists():
                pdf_path = alt_path
            else:
                logger.warning(f"PDF file not found: {pdf_path}")
                continue

        # Extract pages
        reader = pypdf.PdfReader(str(pdf_path))
        doc_headings = doc.get("section_headings", [])

        docs_to_insert.append({
            "id": doc_id,
            "title": doc["title"],
            "file": str(pdf_path),
            "doc_type": doc.get("doc_type"),
            "category": doc.get("category"),
            "department": doc.get("department"),
            "author": doc.get("author"),
            "owner": doc.get("owner"),
            "version": doc.get("version"),
            "effective": doc.get("effective"),
            "classification": doc.get("classification"),
            "tags": doc.get("tags", []),
            "section_headings": doc_headings,
            "word_count": doc.get("word_count", 0),
            "page_count": len(reader.pages)
        })

        chunk_counter = 0
        for p_idx, page in enumerate(reader.pages):
            page_num = p_idx + 1
            page_text = clean_text(page.extract_text() or "")
            if not page_text:
                continue

            page_chunks = chunk_page_text(
                page_text=page_text,
                page_number=page_num,
                known_headings=doc_headings
            )

            for c in page_chunks:
                chunk_id = f"{doc_id}_p{page_num}_c{chunk_counter}"
                all_chunks_to_insert.append({
                    "id": chunk_id,
                    "doc_id": doc_id,
                    "chunk_index": chunk_counter,
                    "page_number": page_num,
                    "section_heading": c["section_heading"],
                    "content": c["content"],
                    "parent_content": page_text, # Parent context expansion
                    "metadata": {
                        "doc_title": doc["title"],
                        "category": doc.get("category"),
                        "department": doc.get("department"),
                        "version": doc.get("version"),
                        "author": doc.get("author"),
                        "classification": doc.get("classification"),
                        "tags": doc.get("tags", [])
                    }
                })
                chunk_counter += 1

        if progress_callback:
            progress_callback(doc_idx + 1, len(docs_metadata))

    logger.info(f"Extracted {len(all_chunks_to_insert)} chunks across {len(docs_to_insert)} documents.")

    # Compute embeddings in batches
    logger.info("Computing dense embeddings...")
    contents = [c["content"] for c in all_chunks_to_insert]
    embeddings = embedding_service.embed_batch(contents, batch_size=20)
    for c, emb in zip(all_chunks_to_insert, embeddings):
        c["embedding"] = emb

    # Insert into PostgreSQL
    logger.info("Writing documents and chunks to database...")
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            # Clear existing data for fresh ingestion
            cur.execute("DELETE FROM chunks;")
            cur.execute("DELETE FROM documents;")

            # Insert documents
            for d in docs_to_insert:
                cur.execute("""
                INSERT INTO documents (
                    id, title, file, doc_type, category, department, author, owner,
                    version, effective, classification, tags, section_headings, word_count, page_count
                ) VALUES (
                    %(id)s, %(title)s, %(file)s, %(doc_type)s, %(category)s, %(department)s, %(author)s, %(owner)s,
                    %(version)s, %(effective)s, %(classification)s, %(tags)s, %(section_headings)s, %(word_count)s, %(page_count)s
                );
                """, {
                    **d,
                    "tags": Json(d["tags"]),
                    "section_headings": Json(d["section_headings"])
                })

            # Insert chunks
            for c in all_chunks_to_insert:
                cur.execute("""
                INSERT INTO chunks (
                    id, doc_id, chunk_index, page_number, section_heading,
                    content, parent_content, embedding, metadata
                ) VALUES (
                    %(id)s, %(doc_id)s, %(chunk_index)s, %(page_number)s, %(section_heading)s,
                    %(content)s, %(parent_content)s, %(embedding)s, %(metadata)s
                );
                """, {
                    **c,
                    "metadata": Json(c["metadata"])
                })

        conn.commit()

    logger.info(f"Ingestion complete: {len(docs_to_insert)} documents, {len(all_chunks_to_insert)} chunks.")
    return {
        "status": "success",
        "documents_indexed": len(docs_to_insert),
        "chunks_indexed": len(all_chunks_to_insert)
    }

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    res = ingest_all_documents()
    print("Ingestion result:", res)
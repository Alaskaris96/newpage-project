"""Generate the 50-document Northwind RAG corpus.

Outputs:
  dataset/pdfs/*.pdf          the corpus
  dataset/manifest.json       per-document metadata for ingestion
  dataset/qa_ground_truth.json  retrieval QA pairs with evidence strings
  dataset/corpus_text/*.txt   extracted text, useful for chunking experiments

Usage:  python -m scripts.generate_dataset
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dataset_gen import all_documents  # noqa: E402
from dataset_gen.render import render_pdf  # noqa: E402

DATASET = ROOT / "dataset"
PDF_DIR = DATASET / "pdfs"
TEXT_DIR = DATASET / "corpus_text"


def slugify(text: str) -> str:
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text[:60]


def validate(docs) -> list[str]:
    """Structural checks that would otherwise produce a broken corpus."""
    problems = []
    seen_ids = set()
    for doc in docs:
        for key in ("id", "title", "doc_type", "category", "summary", "sections", "tags"):
            if key not in doc:
                problems.append(f"{doc.get('id', '?')}: missing key '{key}'")
        if doc["id"] in seen_ids:
            problems.append(f"{doc['id']}: duplicate document id")
        seen_ids.add(doc["id"])
        if not doc.get("sections"):
            problems.append(f"{doc['id']}: no sections")
        for sec in doc.get("sections", []):
            if "heading" not in sec:
                problems.append(f"{doc['id']}: section without heading")
            has_body = any(
                sec.get(k) for k in ("paragraphs", "bullets", "steps", "table", "qa", "notes")
            )
            if not has_body:
                problems.append(f"{doc['id']}: section '{sec.get('heading')}' is empty")
            if sec.get("table"):
                widths = {len(r) for r in sec["table"]}
                if len(widths) != 1:
                    problems.append(
                        f"{doc['id']}: ragged table in '{sec.get('heading')}' ({sorted(widths)})"
                    )
                elif widths and list(widths)[0] < 2:
                    problems.append(f"{doc['id']}: table in '{sec.get('heading')}' too narrow")
        for qa in doc.get("qa", []):
            for key in ("question", "answer", "evidence"):
                if not qa.get(key):
                    problems.append(f"{doc['id']}: QA item missing '{key}'")
    return problems


def main() -> int:
    docs = all_documents()
    problems = validate(docs)
    if problems:
        print("Validation failed:")
        for p in problems:
            print("  -", p)
        return 1

    PDF_DIR.mkdir(parents=True, exist_ok=True)
    TEXT_DIR.mkdir(parents=True, exist_ok=True)

    manifest = []
    qa_rows = []
    total_words = 0

    for doc in docs:
        filename = f"{doc['id']}-{slugify(doc['title'])}.pdf"
        out_path = PDF_DIR / filename
        words = render_pdf(doc, out_path)
        total_words += words

        text_parts = [doc["title"], doc["summary"]]
        for sec in doc["sections"]:
            text_parts.append(sec["heading"])
            text_parts.extend(sec.get("paragraphs", []))
            text_parts.extend(sec.get("bullets", []))
            text_parts.extend(sec.get("steps", []))
            text_parts.extend(sec.get("notes", []))
            for qa in sec.get("qa", []):
                text_parts.extend([qa["question"], qa["answer"]])
            if sec.get("table"):
                for row in sec["table"]:
                    text_parts.append(" | ".join(str(c) for c in row))
        (TEXT_DIR / f"{doc['id']}.txt").write_text("\n\n".join(text_parts), encoding="utf-8")

        manifest.append(
            {
                "id": doc["id"],
                "title": doc["title"],
                "file": f"pdfs/{filename}",
                "doc_type": doc["doc_type"],
                "category": doc["category"],
                "department": doc.get("department"),
                "author": doc.get("author"),
                "owner": doc.get("owner"),
                "version": doc.get("version"),
                "effective": doc.get("effective"),
                "classification": doc.get("classification"),
                "tags": doc["tags"],
                "section_headings": [s["heading"] for s in doc["sections"]],
                "word_count": words,
                "page_count": None,
                "qa_count": len(doc.get("qa", [])),
            }
        )

        for i, qa in enumerate(doc.get("qa", []), start=1):
            qa_rows.append(
                {
                    "id": f"{doc['id']}-QA{i:02d}",
                    "question": qa["question"],
                    "answer": qa["answer"],
                    "evidence": qa["evidence"],
                    "source_id": doc["id"],
                    "source_file": f"pdfs/{filename}",
                    "source_title": doc["title"],
                    "category": doc["category"],
                }
            )

    pages = 0
    try:
        from pypdf import PdfReader

        for row in manifest:
            reader = PdfReader(DATASET / row["file"])
            row["page_count"] = len(reader.pages)
            pages += len(reader.pages)
    except Exception as exc:  # pragma: no cover
        print(f"warning: page counting skipped ({exc})")

    (DATASET / "manifest.json").write_text(
        json.dumps(
            {
                "corpus": "Northwind Consolidated Holdings synthetic corpus",
                "document_count": len(manifest),
                "total_words": total_words,
                "total_pages": pages,
                "categories": sorted({r["category"] for r in manifest}),
                "documents": manifest,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    (DATASET / "qa_ground_truth.json").write_text(
        json.dumps(
            {
                "corpus": "Northwind Consolidated Holdings synthetic corpus",
                "pair_count": len(qa_rows),
                "pairs": qa_rows,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(f"documents : {len(manifest)}")
    print(f"categories: {len({r['category'] for r in manifest})}")
    print(f"pages     : {pages}")
    print(f"words     : {total_words}")
    print(f"qa pairs  : {len(qa_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

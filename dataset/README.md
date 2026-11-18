# Northwind RAG Dataset

50 synthetic, text-based PDFs for testing a retrieval-augmented generation
application, plus a 250-pair ground-truth QA set for retrieval evaluation.

All documents are set inside one fictional company, **Northwind Consolidated
Holdings (NCH)**, a SaaS content-platform vendor. Because the corpus shares a
single consistent world, cross-document questions have stable answers and
contradictions between documents are detectable.

## Contents

| Path | Description |
| --- | --- |
| `pdfs/` | 50 PDFs, 107 pages, ~40,600 extractable words |
| `corpus_text/` | One `.txt` per document, pre-extracted for chunking experiments |
| `manifest.json` | Per-document metadata: id, title, category, doc type, author, version, classification, tags, section headings, word/page counts |
| `qa_ground_truth.json` | 250 question / answer / evidence triples with source document references |

## Categories

Ten categories, five documents each: Human Resources, Information Security, IT
Operations, Finance, Legal and Compliance, Product Management, Data and
Analytics, Customer Support, Software Engineering, Marketing.

## Document types

The corpus deliberately mixes structures so a chunker is exercised by more than
prose: policies, standards, handbooks, runbooks with numbered steps,
specifications, RFCs, release notes, research reports, calendars, playbooks,
and go-to-market plans. Many documents contain tables, Q&A blocks, and
highlighted notes.

## Using the QA set

Each pair carries an `evidence` string quoted from the source document, which
supports three kinds of evaluation:

```json
{
  "id": "HR-STD-007-QA02",
  "question": "How many weeks of fully paid parental leave does Northwind offer?",
  "answer": "20 fully paid weeks, gender-neutral, after 12 months of service.",
  "evidence": "20 weeks of fully paid parental leave",
  "source_id": "HR-STD-007",
  "source_file": "pdfs/HR-STD-007-leave-of-absence-and-time-off-standard.pdf",
  "category": "Human Resources"
}
```

- **Retrieval accuracy** — does the correct `source_id` appear in the top-k
  retrieved chunks?
- **Evidence coverage** — does the retrieved chunk contain the `evidence` string?
- **Answer faithfulness** — does the generated answer match `answer` without
  contradicting the source?

Every `evidence` string is verbatim text from its PDF and is verified by
`scripts/validate_dataset.py`.

## Regenerating

```powershell
python -m pip install reportlab pypdf
python -m scripts.generate_dataset      # writes dataset/
python -m scripts.validate_dataset      # extractability + evidence checks
python -m scripts.retrieval_smoketest   # BM25 sanity check
```

Content lives in `dataset_gen/corpus_*.py`, one module per category. Edit a
module and re-run `generate_dataset` to regenerate; the validator fails the
build if a table is ragged, a section is empty, an id is duplicated, or an
evidence string no longer matches the rendered PDF.

## Known characteristics

- Text is real selectable text (reportlab Platypus), not scanned images, so any
  PDF text extractor works without OCR.
- Questions are answerable from a single document. Multi-hop questions are not
  included; if you need them, add pairs whose `evidence` spans two `source_id`
  values.
- Four questions are deliberately answerable from more than one document
  (for example log-retention periods appear in three policies). A retrieval
  system scoring 100% on this set is likely overfitting to document titles.
- Numbers are invented. Do not use this corpus for anything factual.

"""Validate the generated corpus for RAG use.

Checks, for every PDF:
  1. the file parses and has pages
  2. text is extractable (not image-only) and meets a minimum word count
  3. every QA evidence string for that document is found in the extracted text
  4. the document title and id appear in the extracted text
  5. no QA answer is trivially short
Also checks corpus-level uniqueness so questions are not duplicated.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATASET = ROOT / "dataset"
MIN_WORDS = 350


def norm(text: str) -> str:
    """Normalise for substring matching across PDF line-wrapping."""
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2013", "-").replace("\u2014", "-")
    text = re.sub(r"\s+", " ", text)
    return text.lower().strip()


def fragments(evidence: str) -> list[str]:
    """Split an evidence citation into locatable fragments.

    Evidence is authored with ' | ' to separate table cells and '...' to skip
    intervening text. PDF extraction emits table cells on separate lines, so
    both markers are treated as boundaries and each fragment is matched
    independently.
    """
    parts = re.split(r"\s*\.\.\.\s*|\s*\|\s*", evidence)
    return [norm(p) for p in parts if len(norm(p)) >= 3]


def main() -> int:
    from pypdf import PdfReader

    manifest = json.loads((DATASET / "manifest.json").read_text(encoding="utf-8"))
    qa = json.loads((DATASET / "qa_ground_truth.json").read_text(encoding="utf-8"))

    extracted: dict[str, str] = {}
    failures: list[str] = []
    thin: list[str] = []

    for row in manifest["documents"]:
        path = DATASET / row["file"]
        if not path.exists():
            failures.append(f"{row['id']}: file missing {row['file']}")
            continue
        try:
            reader = PdfReader(str(path))
            raw = "\n".join(page.extract_text() or "" for page in reader.pages)
        except Exception as exc:
            failures.append(f"{row['id']}: parse error {exc}")
            continue

        text = norm(raw)
        extracted[row["id"]] = text
        words = len(re.findall(r"\w+", text))

        if row["page_count"] != len(reader.pages):
            failures.append(
                f"{row['id']}: page_count mismatch manifest={row['page_count']} actual={len(reader.pages)}"
            )
        if words < MIN_WORDS:
            thin.append(f"{row['id']}: only {words} extractable words")
        if words == 0:
            failures.append(f"{row['id']}: no extractable text (image-only PDF?)")
        if norm(row["title"]) not in text:
            failures.append(f"{row['id']}: title not found in extracted text")
        if row["id"].lower() not in text:
            failures.append(f"{row['id']}: document id not found in extracted text")

    # Evidence must be locatable in the source PDF text.
    missing = 0
    for pair in qa["pairs"]:
        text = extracted.get(pair["source_id"], "")
        frags = fragments(pair["evidence"])
        if not frags:
            failures.append(f"{pair['id']}: evidence has no locatable fragment")
            continue
        absent = [f for f in frags if f not in text]
        if absent:
            missing += 1
            failures.append(
                f"{pair['id']}: {len(absent)}/{len(frags)} evidence fragments missing "
                f"in {pair['source_id']} -> {absent[0][:70]}"
            )
        if not pair["answer"].strip():
            failures.append(f"{pair['id']}: empty answer")
        if norm(pair["answer"]) == norm(pair["question"]):
            failures.append(f"{pair['id']}: answer duplicates the question")

    # Corpus-level checks.
    questions = [norm(p["question"]) for p in qa["pairs"]]
    dupes = {q for q in questions if questions.count(q) > 1}
    for q in sorted(dupes):
        failures.append(f"duplicate question: {q[:70]}")

    ids = [p["id"] for p in qa["pairs"]]
    if len(set(ids)) != len(ids):
        failures.append("duplicate QA ids present")

    counts = [
        len(re.findall(r"\w+", extracted[r["id"]]))
        for r in manifest["documents"]
        if r["id"] in extracted
    ]
    counts.sort()

    print("=== corpus validation ===")
    print(f"documents checked      : {len(manifest['documents'])}")
    print(f"extractable            : {len(extracted)}")
    print(f"qa pairs checked       : {len(qa['pairs'])}")
    print(f"evidence matched       : {len(qa['pairs']) - missing}/{len(qa['pairs'])}")
    if counts:
        print(f"words per doc min/med/max: {counts[0]} / {counts[len(counts)//2]} / {counts[-1]}")
        print(f"total extractable words: {sum(counts)}")
    if thin:
        print("\nTHIN DOCUMENTS:")
        for t in thin:
            print("  -", t)
    if failures:
        print(f"\nFAILURES ({len(failures)}):")
        for f in failures[:40]:
            print("  -", f)
        return 1

    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

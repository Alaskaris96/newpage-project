"""Retrieval smoke test for the generated corpus.

Chunks every extracted PDF text, scores chunks against each ground-truth
question with BM25, and reports top-1 / top-3 document accuracy plus evidence
coverage. This is a sanity check that the corpus is actually retrievable, not a
replacement for evaluating a real embedding model.

Usage:  python -m scripts.retrieval_smoketest
"""

from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATASET = ROOT / "dataset"
TOP_K = 5
CHUNK_WORDS = 180
OVERLAP = 30

STOP = set(
    """a an the and or but if then than that this these those of to in on for with
    without at by from as is are was were be been being do does did not no so such
    it its they them their we our you your he she his her which who whom what when
    where how why all any each other more most some than into over under between
    within per may must can should would could will shall have has had also""".split()
)


def tokens(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9]+", text.lower()) if t not in STOP and len(t) > 2]


def chunk(text: str) -> list[str]:
    words = text.split()
    if not words:
        return []
    out, i = [], 0
    while i < len(words):
        out.append(" ".join(words[i : i + CHUNK_WORDS]))
        if i + CHUNK_WORDS >= len(words):
            break
        i += CHUNK_WORDS - OVERLAP
    return out


class BM25:
    def __init__(self, docs: list[list[str]], k1: float = 1.5, b: float = 0.75):
        self.docs = docs
        self.k1, self.b = k1, b
        self.n = len(docs)
        self.avg = sum(len(d) for d in docs) / max(self.n, 1)
        self.df: Counter = Counter()
        for d in docs:
            self.df.update(set(d))

    def score(self, query: list[str]) -> list[float]:
        scores = []
        for d in self.docs:
            tf = Counter(d)
            s = 0.0
            for t in query:
                f = tf.get(t, 0)
                if not f:
                    continue
                idf = math.log(1 + (self.n - self.df[t] + 0.5) / (self.df[t] + 0.5))
                s += idf * (f * (self.k1 + 1)) / (f + self.k1 * (1 - self.b + self.b * len(d) / self.avg))
            scores.append(s)
        return scores


def main() -> int:
    manifest = json.loads((DATASET / "manifest.json").read_text(encoding="utf-8"))
    qa = json.loads((DATASET / "qa_ground_truth.json").read_text(encoding="utf-8"))

    chunks: list[str] = []
    owner: list[str] = []
    for row in manifest["documents"]:
        txt = (DATASET / "corpus_text" / f"{row['id']}.txt").read_text(encoding="utf-8")
        for c in chunk(re.sub(r"\s+", " ", txt)):
            chunks.append(c)
            owner.append(row["id"])

    index = BM25([tokens(c) for c in chunks])
    print(f"indexed {len(chunks)} chunks from {len(manifest['documents'])} documents")

    top1 = top3 = ev = 0
    misses: list[str] = []
    for pair in qa["pairs"]:
        ranked = sorted(range(len(chunks)), key=lambda i: -index.score(tokens(pair["question"]))[i])
        doc_rank: list[str] = []
        for i in ranked:
            if owner[i] not in doc_rank:
                doc_rank.append(owner[i])
            if len(doc_rank) >= TOP_K:
                break
        if doc_rank and doc_rank[0] == pair["source_id"]:
            top1 += 1
        if pair["source_id"] in doc_rank[:3]:
            top3 += 1
        else:
            misses.append(f"{pair['id']}: expected {pair['source_id']}, got {doc_rank[:3]}")

        best = ranked[0]
        if all(f in chunks[best].lower() for f in re.findall(r"[a-z0-9]+", pair["evidence"].lower()) if len(f) > 4):
            ev += 1

    total = len(qa["pairs"])
    print(f"top-1 document accuracy : {top1}/{total} ({100*top1/total:.1f}%)")
    print(f"top-3 document accuracy : {top3}/{total} ({100*top3/total:.1f}%)")
    print(f"best-chunk evidence hit : {ev}/{total} ({100*ev/total:.1f}%)")
    if misses:
        print("\nMISSES:")
        for m in misses[:15]:
            print("  -", m)
    ok = top3 / total >= 0.95
    print("\nRetrieval smoke test:", "PASSED" if ok else "BELOW 95% top-3")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

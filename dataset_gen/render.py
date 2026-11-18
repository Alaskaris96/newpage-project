"""PDF rendering for the synthetic RAG corpus.

Uses reportlab Platypus so every document is real, selectable, extractable text
(no images, no scanned pages). Layout varies by document type so a chunker sees
different structures: prose sections, bullet lists, numbered runbook steps,
tables, Q&A pairs and highlighted notes.
"""

from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

MARGIN = 20 * mm
BOTTOM_MARGIN = 22 * mm
ACCENT = colors.HexColor("#1F3A5F")
MUTED = colors.HexColor("#5A6472")
RULE = colors.HexColor("#C9D2DC")
BAND = colors.HexColor("#EEF2F7")

PAGE_W, PAGE_H = A4
USABLE_W = PAGE_W - 2 * MARGIN


def _build_styles() -> dict:
    base = getSampleStyleSheet()
    s = {}
    s["category"] = ParagraphStyle(
        "category", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8,
        leading=10, textColor=ACCENT, spaceAfter=2,
    )
    s["title"] = ParagraphStyle(
        "title", parent=base["Title"], fontName="Helvetica-Bold", fontSize=20,
        leading=24, alignment=TA_LEFT, textColor=colors.HexColor("#12233A"),
        spaceBefore=0, spaceAfter=3,
    )
    s["doctype"] = ParagraphStyle(
        "doctype", parent=base["Normal"], fontName="Helvetica-Oblique", fontSize=10,
        leading=13, textColor=MUTED, spaceAfter=8,
    )
    s["meta"] = ParagraphStyle(
        "meta", parent=base["Normal"], fontSize=8.5, leading=11.5, textColor=MUTED
    )
    s["h1"] = ParagraphStyle(
        "h1", parent=base["Heading1"], fontName="Helvetica-Bold", fontSize=12.5,
        leading=15.5, textColor=ACCENT, spaceBefore=12, spaceAfter=5, keepWithNext=1,
    )
    s["body"] = ParagraphStyle(
        "body", parent=base["Normal"], fontName="Helvetica", fontSize=9.6,
        leading=13.6, alignment=TA_JUSTIFY, spaceAfter=6,
    )
    s["bullet"] = ParagraphStyle(
        "bullet", parent=s["body"], leftIndent=11, bulletIndent=2, spaceAfter=3,
        alignment=TA_LEFT,
    )
    s["step"] = ParagraphStyle(
        "step", parent=s["body"], leftIndent=18, bulletIndent=2, spaceAfter=4,
        alignment=TA_LEFT,
    )
    s["note"] = ParagraphStyle(
        "note", parent=s["body"], fontName="Helvetica-Oblique", fontSize=9.2,
        leading=12.5, leftIndent=8, borderPadding=5, backColor=BAND,
        spaceBefore=3, spaceAfter=8,
    )
    s["qa_q"] = ParagraphStyle(
        "qa_q", parent=s["body"], fontName="Helvetica-Bold", spaceAfter=2,
        alignment=TA_LEFT,
    )
    s["qa_a"] = ParagraphStyle("qa_a", parent=s["body"], leftIndent=10, spaceAfter=8)
    s["table_head"] = ParagraphStyle(
        "table_head", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8.6,
        leading=11, textColor=colors.white,
    )
    s["table_cell"] = ParagraphStyle(
        "table_cell", parent=base["Normal"], fontSize=8.6, leading=11
    )
    s["toc"] = ParagraphStyle(
        "toc", parent=base["Normal"], fontSize=9, leading=13, textColor=MUTED,
        spaceAfter=4,
    )
    return s


ST = _build_styles()

_TAG = re.compile(r"<(?!/?[biu]\b|br\s*/?>)", re.I)


def _escape(text: str) -> str:
    """Escape stray markup, then re-enable **bold** / *italic* inline markers."""
    text = _TAG.sub("&lt;", str(text))
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<i>\1</i>", text)
    return text


def _table(rows) -> Table:
    data = [
        [Paragraph(_escape(c), ST["table_head"]) for c in rows[0]],
        *[[Paragraph(_escape(c), ST["table_cell"]) for c in row] for row in rows[1:]],
    ]
    t = Table(data, hAlign="LEFT", repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, BAND]),
                ("GRID", (0, 0), (-1, -1), 0.4, RULE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return t


def _footer(doc_id: str, title: str):
    def draw(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.5)
        canvas.line(MARGIN, 15 * mm, PAGE_W - MARGIN, 15 * mm)
        canvas.setFont("Helvetica", 7.2)
        canvas.setFillColor(MUTED)
        canvas.drawString(MARGIN, 11 * mm, f"{doc_id}  |  {title}")
        canvas.drawRightString(PAGE_W - MARGIN, 11 * mm, f"Page {doc.page}")
        canvas.restoreState()

    return draw


def render_pdf(doc: dict, out_path: Path) -> int:
    """Render one document dict to `out_path`; return the rendered word count."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    story = []

    story.append(Paragraph(_escape(doc["category"].upper()), ST["category"]))
    story.append(Paragraph(_escape(doc["title"]), ST["title"]))
    story.append(Paragraph(_escape(doc["doc_type"]), ST["doctype"]))
    story.append(HRFlowable(width="100%", thickness=1.1, color=ACCENT, spaceAfter=6))

    meta_rows = [[Paragraph(_escape(
        f"Document ID: <b>{doc['id']}</b> &nbsp;|&nbsp; Version: "
        f"{doc.get('version', '1.0')} &nbsp;|&nbsp; Effective: "
        f"{doc.get('effective', 'n/a')} &nbsp;|&nbsp; Owner: "
        f"{doc.get('owner', 'n/a')}"), ST["meta"])],
        [Paragraph(_escape(
            f"Author: {doc.get('author', 'n/a')} &nbsp;|&nbsp; Department: "
            f"{doc.get('department', doc['category'])} &nbsp;|&nbsp; Classification: "
            f"{doc.get('classification', 'Internal')} &nbsp;|&nbsp; Review cycle: "
            f"{doc.get('review', 'Annual')}"), ST["meta"])]]
    meta = Table(meta_rows, colWidths=[USABLE_W])
    meta.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BAND),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.append(meta)
    story.append(Spacer(1, 9))

    if doc.get("summary"):
        story.append(Paragraph("Summary", ST["h1"]))
        story.append(Paragraph(_escape(doc["summary"]), ST["body"]))

    headings = [s["heading"] for s in doc["sections"]]
    if len(headings) >= 5:
        story.append(Paragraph("Contents", ST["h1"]))
        story.append(Paragraph(" &nbsp;|&nbsp; ".join(map(_escape, headings)), ST["toc"]))

    for sec in doc["sections"]:
        story.append(Paragraph(_escape(sec["heading"]), ST["h1"]))
        for p in sec.get("paragraphs", []):
            story.append(Paragraph(_escape(p), ST["body"]))
        if sec.get("table"):
            story.append(_table(sec["table"]))
            story.append(Spacer(1, 6))
        for b in sec.get("bullets", []):
            story.append(Paragraph(_escape(b), ST["bullet"], bulletText="\u2022"))
        for i, step in enumerate(sec.get("steps", []), start=1):
            story.append(Paragraph(_escape(step), ST["step"], bulletText=f"{i}."))
        for qa in sec.get("qa", []):
            story.append(Paragraph(_escape("Q: " + qa["question"]), ST["qa_q"]))
            story.append(Paragraph(_escape("A: " + qa["answer"]), ST["qa_a"]))
        for n in sec.get("notes", []):
            story.append(Paragraph(_escape(n), ST["note"]))

    if doc.get("tags"):
        story.append(Spacer(1, 5))
        story.append(Paragraph(_escape("Keywords: " + ", ".join(doc["tags"])), ST["meta"]))

    pdf = BaseDocTemplate(
        str(out_path), pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN,
        bottomMargin=BOTTOM_MARGIN,
        title=doc["title"], author=doc.get("author", "Northwind Consolidated Holdings"),
        subject=(doc.get("summary") or doc["title"])[:200],
        creator="dataset_gen",
    )
    pdf.addPageTemplates([PageTemplate(
        id="body",
        frames=[Frame(MARGIN, BOTTOM_MARGIN, USABLE_W,
                      PAGE_H - MARGIN - BOTTOM_MARGIN, id="main",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)],
        onPage=_footer(doc["id"], doc["title"]),
    )])
    pdf.build(story)

    words = 0
    for sec in doc["sections"]:
        for p in sec.get("paragraphs", []):
            words += len(re.findall(r"\w+", p))
        for b in sec.get("bullets", []) + sec.get("steps", []) + sec.get("notes", []):
            words += len(re.findall(r"\w+", b))
        for qa in sec.get("qa", []):
            words += len(re.findall(r"\w+", qa["question"] + " " + qa["answer"]))
    return words

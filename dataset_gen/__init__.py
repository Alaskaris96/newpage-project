"""Synthetic RAG corpus generator for Northwind Consolidated Holdings."""

from .corpus_hr import DOCS as HR
from .corpus_sec import DOCS as SEC
from .corpus_it import DOCS as IT
from .corpus_fin import DOCS as FIN
from .corpus_legal import DOCS as LEGAL
from .corpus_product import DOCS as PRODUCT
from .corpus_data import DOCS as DATA
from .corpus_support import DOCS as SUPPORT
from .corpus_eng import DOCS as ENG
from .corpus_mkt import DOCS as MKT

MODULES = [HR, SEC, IT, FIN, LEGAL, PRODUCT, DATA, SUPPORT, ENG, MKT]


def all_documents():
    docs = []
    for module in MODULES:
        docs.extend(module)
    return docs


__all__ = ["all_documents", "MODULES"]

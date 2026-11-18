import logging
import math
from typing import List, Dict, Any, Optional, Callable
from langchain_core.tools import BaseTool, tool
from pydantic import BaseModel, Field
from backend.db import get_db_connection

logger = logging.getLogger("rag.tools")

class CalculatorInput(BaseModel):
    expression: str = Field(description="Mathematical expression to evaluate, e.g. '20 * 5' or '100 - (25 * 0.2)'")

@tool("calculator", args_schema=CalculatorInput)
def calculate_expression(expression: str) -> str:
    """Useful for evaluating mathematical and numeric calculations accurately (e.g. leave days, salary pro-rata, SLA percentages)."""
    allowed_names = {
        k: v for k, v in math.__dict__.items() if not k.startswith("__")
    }
    allowed_names.update({"abs": abs, "round": round, "min": min, "max": max})
    try:
        # Strip dangerous characters
        cleaned = expression.strip()
        result = eval(cleaned, {"__builtins__": None}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Calculation error: {e}"

class MetadataSearchInput(BaseModel):
    query: str = Field(description="Search term for document metadata (e.g. author name, department, doc_id, or classification)")

@tool("search_document_metadata", args_schema=MetadataSearchInput)
def search_document_metadata(query: str) -> str:
    """Useful to look up document metadata such as author, version, effective date, department, or classification."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT id, title, doc_type, category, department, author, version, effective, classification
            FROM documents
            WHERE id ILIKE %(q)s 
               OR title ILIKE %(q)s 
               OR author ILIKE %(q)s 
               OR department ILIKE %(q)s
               OR classification ILIKE %(q)s
            LIMIT 5;
            """, {"q": f"%{query.strip()}%"})
            rows = cur.fetchall()
            if not rows:
                return f"No document metadata found matching '{query}'."
            
            output = []
            for r in rows:
                output.append(
                    f"ID: {r[0]} | Title: {r[1]} | Type: {r[2]} | Cat: {r[3]} | Dept: {r[4]} | Author: {r[5]} | Ver: {r[6]} | Date: {r[7]} | Class: {r[8]}"
                )
            return "\n".join(output)

class CorpusStatsInput(BaseModel):
    category: Optional[str] = Field(default=None, description="Optional category to filter statistics, e.g. 'Human Resources'")

@tool("get_corpus_statistics", args_schema=CorpusStatsInput)
def get_corpus_statistics(category: Optional[str] = None) -> str:
    """Returns overview statistics of the Northwind policy corpus, including document counts by category, total pages, and word counts."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            if category:
                cur.execute("""
                SELECT count(*), sum(page_count), sum(word_count)
                FROM documents WHERE category ILIKE %(cat)s;
                """, {"cat": f"%{category.strip()}%"})
                doc_cnt, page_cnt, word_cnt = cur.fetchone()
                return f"Category '{category}': {doc_cnt} documents, {page_cnt or 0} pages, {word_cnt or 0} words."
            else:
                cur.execute("""
                SELECT category, count(*), sum(page_count)
                FROM documents
                GROUP BY category
                ORDER BY category;
                """)
                rows = cur.fetchall()
                lines = ["Northwind Corpus Breakdown:"]
                for cat, d_cnt, p_cnt in rows:
                    lines.append(f"- {cat}: {d_cnt} documents ({p_cnt} pages)")
                return "\n".join(lines)

class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, BaseTool] = {}
        # Register defaults
        self.register_tool(calculate_expression)
        self.register_tool(search_document_metadata)
        self.register_tool(get_corpus_statistics)

    def register_tool(self, tool_instance: BaseTool):
        self._tools[tool_instance.name] = tool_instance
        logger.info(f"Registered tool: {tool_instance.name}")

    def get_tool(self, name: str) -> Optional[BaseTool]:
        return self._tools.get(name)

    def get_all_tools(self) -> List[BaseTool]:
        return list(self._tools.values())

    def list_tools_info(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": t.name,
                "description": t.description,
                "args_schema": str(t.args_schema.schema()) if t.args_schema else None
            }
            for t in self._tools.values()
        ]

tool_registry = ToolRegistry()

def invoke_tool_safely(tool_inst: BaseTool, input_data: Any) -> Dict[str, Any]:
    """Safely invokes a tool, adapting mismatched argument keys and plain strings."""
    try:
        if isinstance(input_data, dict):
            # If the tool has a single required field and it wasn't matched
            schema = tool_inst.args_schema.schema() if tool_inst.args_schema else None
            if schema and "properties" in schema:
                props = list(schema["properties"].keys())
                if len(props) == 1 and props[0] not in input_data and input_data:
                    first_val = next(iter(input_data.values()), "")
                    input_data = {props[0]: first_val}
            res = tool_inst.invoke(input_data)
        elif isinstance(input_data, str):
            input_str = input_data.strip()
            if tool_inst.name == "calculator":
                res = tool_inst.invoke({"expression": input_str})
            elif tool_inst.name == "search_document_metadata":
                res = tool_inst.invoke({"query": input_str})
            elif tool_inst.name == "get_corpus_statistics":
                res = tool_inst.invoke({"category": input_str if input_str else None})
            else:
                res = tool_inst.invoke(input_str)
        else:
            res = tool_inst.invoke(input_data or {})

        return {
            "status": "success",
            "tool": tool_inst.name,
            "output": str(res)
        }
    except Exception as e:
        logger.error(f"Safe tool invocation failed for {tool_inst.name}: {e}")
        return {
            "status": "error",
            "tool": tool_inst.name,
            "error": str(e),
            "output": f"Error executing tool: {e}"
        }

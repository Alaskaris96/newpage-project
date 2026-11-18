import sys
from pathlib import Path

# Ensure the project root (containing the `backend` package) is importable.
_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import uvicorn

if __name__ == "__main__":
    print("=" * 60)
    print("Starting Northwind Enterprise RAG Production Server")
    print("API & UI: http://127.0.0.1:8000")
    print("API Docs: http://127.0.0.1:8000/docs")
    print("=" * 60)
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=False)

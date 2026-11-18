export async function fetchDocumentsApi() {
  const res = await fetch('/api/documents');
  if (!res.ok) {
    throw new Error(`Failed to load documents: status ${res.status}`);
  }
  return res.json();
}

export async function triggerIngestApi() {
  const res = await fetch('/api/ingest', { method: 'POST' });
  if (!res.ok) {
    throw new Error(`Ingestion trigger failed: status ${res.status}`);
  }
  return res.json();
}

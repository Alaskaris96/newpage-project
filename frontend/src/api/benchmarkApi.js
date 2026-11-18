export async function runBenchmarkApi({ sampleSize, modes }) {
  const res = await fetch('/api/evaluate/benchmark', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      sample_size: parseInt(sampleSize, 10),
      modes: modes || ['dense', 'bm25', 'hybrid', 'hybrid_rerank']
    })
  });

  if (!res.ok) {
    throw new Error(`Benchmark run failed: status ${res.status}`);
  }

  return res.json();
}

export async function fetchBenchmarkHistoryApi() {
  const res = await fetch('/api/evaluate/history');
  if (!res.ok) {
    throw new Error(`Failed to load benchmark history: status ${res.status}`);
  }
  return res.json();
}

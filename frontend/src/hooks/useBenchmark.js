import { useState, useEffect, useCallback } from 'react';
import { runBenchmarkApi, fetchBenchmarkHistoryApi } from '../api/benchmarkApi';

export function useBenchmark() {
  const [sampleSize, setSampleSize] = useState(5);
  const [benchmarkResult, setBenchmarkResult] = useState(null);
  const [benchmarkLoading, setBenchmarkLoading] = useState(false);
  const [benchmarkHistory, setBenchmarkHistory] = useState([]);

  const reloadBenchmarkHistory = useCallback(async () => {
    try {
      const data = await fetchBenchmarkHistoryApi();
      setBenchmarkHistory(data);
    } catch (err) {
      console.error('Benchmark history error:', err);
    }
  }, []);

  useEffect(() => {
    reloadBenchmarkHistory();
  }, [reloadBenchmarkHistory]);

  const handleRunBenchmark = useCallback(async () => {
    setBenchmarkLoading(true);
    try {
      const data = await runBenchmarkApi({
        sampleSize: parseInt(sampleSize, 10),
        modes: ['dense', 'bm25', 'hybrid', 'hybrid_rerank']
      });
      setBenchmarkResult(data);
      await reloadBenchmarkHistory();
    } catch (err) {
      alert(`Benchmark error: ${err.message}`);
    } finally {
      setBenchmarkLoading(false);
    }
  }, [sampleSize, reloadBenchmarkHistory]);

  return {
    sampleSize,
    setSampleSize,
    benchmarkResult,
    benchmarkLoading,
    benchmarkHistory,
    handleRunBenchmark,
    reloadBenchmarkHistory
  };
}

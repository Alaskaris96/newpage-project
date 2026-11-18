import React from 'react';
import { BarChart3, RefreshCw, Database } from 'lucide-react';
import { formatPercentage, formatDate } from '../../utils/formatters';
import { SAMPLE_SIZE_OPTIONS } from '../../utils/constants';

export function BenchmarkTab({
  sampleSize,
  onSelectSampleSize,
  benchmarkLoading,
  benchmarkResult,
  benchmarkHistory,
  onRunBenchmark
}) {
  return (
    <div className="tab-page-container">
      <div className="panel-card">
        <div className="panel-card-header">
          <div>
            <h3 className="panel-title">
              <BarChart3 size={20} />
              Automated Retrieval Benchmark
            </h3>
            <p className="panel-subtitle">
              Compares Dense Vector (pgvector) vs Sparse (BM25 full-text) vs Hybrid (RRF) vs Cross-Encoder Rerank on ground truth QA pairs.
            </p>
          </div>
          <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'center' }}>
            <select
              className="bw-select"
              value={sampleSize}
              onChange={e => onSelectSampleSize(Number(e.target.value))}
            >
              {SAMPLE_SIZE_OPTIONS.map(opt => (
                <option key={opt.value} value={opt.value}>{opt.label}</option>
              ))}
            </select>
            <button
              className="bw-btn-primary"
              onClick={onRunBenchmark}
              disabled={benchmarkLoading}
            >
              {benchmarkLoading ? (
                <>
                  <span className="mini-spinner" style={{ borderTopColor: '#000000' }}></span>
                  Running Benchmark...
                </>
              ) : (
                <>
                  <RefreshCw size={15} />
                  Run Benchmark
                </>
              )}
            </button>
          </div>
        </div>

        {benchmarkResult && (
          <div style={{ marginTop: '1.25rem' }}>
            <div style={{ fontSize: '0.88rem', fontWeight: 600, color: '#ffffff', marginBottom: '0.75rem' }}>
              Results on {benchmarkResult.sample_size} Test Questions ({benchmarkResult.timestamp}):
            </div>
            <div className="table-wrapper">
              <table className="clean-table">
                <thead>
                  <tr>
                    <th>Retrieval Strategy</th>
                    <th>Recall@5</th>
                    <th>Recall@10</th>
                    <th>Precision@5</th>
                    <th>MRR</th>
                    <th>Avg Latency</th>
                  </tr>
                </thead>
                <tbody>
                  {Object.entries(benchmarkResult.results).map(([key, item]) => (
                    <tr key={key}>
                      <td style={{ fontWeight: 600, color: '#ffffff', textTransform: 'capitalize' }}>
                        {key === 'hybrid_rerank' ? 'Hybrid + Cross-Encoder' : key}
                      </td>
                      <td>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                          <span>{formatPercentage(item.recall_at_5)}</span>
                          <div style={{ width: 60, height: 6, background: '#2b2b2b', borderRadius: 3 }}>
                            <div style={{ width: `${item.recall_at_5 * 100}%`, height: '100%', background: '#ffffff', borderRadius: 3 }}></div>
                          </div>
                        </div>
                      </td>
                      <td>{formatPercentage(item.recall_at_10)}</td>
                      <td>{formatPercentage(item.precision_at_5)}</td>
                      <td style={{ fontWeight: 600, color: '#ffffff' }}>{Number(item.mrr).toFixed(3)}</td>
                      <td>{Number(item.avg_latency_ms).toFixed(1)} ms</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </div>

      {/* Benchmark History */}
      <div className="panel-card">
        <div className="panel-card-header">
          <h3 className="panel-title">
            <Database size={18} />
            Historical Benchmark Runs (PostgreSQL)
          </h3>
        </div>
        <div className="table-wrapper">
          <table className="clean-table">
            <thead>
              <tr>
                <th>Run ID</th>
                <th>Timestamp</th>
                <th>Configuration</th>
                <th>Samples</th>
                <th>Recall@5</th>
                <th>Precision@5</th>
                <th>MRR</th>
                <th>Avg Latency</th>
              </tr>
            </thead>
            <tbody>
              {benchmarkHistory.map((run, i) => (
                <tr key={i}>
                  <td>#{run.id}</td>
                  <td>{formatDate(run.run_timestamp)}</td>
                  <td style={{ fontWeight: 600, color: '#ffffff' }}>{run.config_name}</td>
                  <td>{run.sample_size}</td>
                  <td>{formatPercentage(run.recall_at_5)}</td>
                  <td>{formatPercentage(run.precision_at_5)}</td>
                  <td style={{ color: '#ffffff', fontWeight: 600 }}>{run.mrr?.toFixed(3)}</td>
                  <td>{run.avg_latency_ms ? `${Number(run.avg_latency_ms).toFixed(1)} ms` : '—'}</td>
                </tr>
              ))}
              {benchmarkHistory.length === 0 && (
                <tr>
                  <td colSpan="8" style={{ textAlign: 'center', color: '#8e8e8e', padding: '1.5rem' }}>
                    No past benchmark runs logged yet. Click "Run Benchmark" above.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

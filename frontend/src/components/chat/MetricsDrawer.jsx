import React from 'react';
import { BarChart3, Clock, X } from 'lucide-react';
import { truncateText, formatPercentage } from '../../utils/formatters';

export function MetricsDrawer({
  metricsOpen,
  onClose,
  assistantMessages,
  activeMsg,
  displayMetrics,
  onSelectTurn
}) {
  if (!metricsOpen) return null;

  return (
    <aside className="metrics-drawer">
      <div className="drawer-header">
        <div className="drawer-title">
          <BarChart3 size={18} />
          RAG Quality & Evidence
        </div>
        <button className="icon-btn" onClick={onClose}>
          <X size={16} />
        </button>
      </div>

      {assistantMessages.length > 1 && (
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', justifyContent: 'space-between' }}>
          <span style={{ fontSize: '0.75rem', color: '#8e8e8e' }}>Select Turn:</span>
          <select
            value={activeMsg?.origIndex ?? ''}
            onChange={e => onSelectTurn(Number(e.target.value))}
            className="bw-select"
            style={{ fontSize: '0.75rem', padding: '0.25rem 0.5rem' }}
          >
            {assistantMessages.map((m, ai) => (
              <option key={m.origIndex} value={m.origIndex}>
                Turn #{ai + 1}: {truncateText(m.question, 22) || `Response #${ai + 1}`}
              </option>
            ))}
          </select>
        </div>
      )}

      {displayMetrics ? (
        <>
          {activeMsg?.question && (
            <div style={{ fontSize: '0.78rem', color: '#ffffff', background: '#212121', padding: '0.5rem 0.75rem', borderRadius: '6px', border: '1px solid #383838' }}>
              Turn: <em>"{activeMsg.question}"</em>
            </div>
          )}

          <div className="metrics-kpi-grid">
            <div className="kpi-card">
              <div className="kpi-label">Precision@5</div>
              <div className="kpi-value">{displayMetrics.precision_at_k}</div>
            </div>
            <div className="kpi-card">
              <div className="kpi-label">MRR</div>
              <div className="kpi-value">{displayMetrics.mrr}</div>
            </div>
            <div className="kpi-card">
              <div className="kpi-label">Faithfulness</div>
              <div className="kpi-value">
                {formatPercentage(displayMetrics.faithfulness_score !== undefined ? displayMetrics.faithfulness_score : 1, 0)}
              </div>
            </div>
            <div className="kpi-card">
              <div className="kpi-label">Total Latency</div>
              <div className="kpi-value">{displayMetrics.latency_ms?.total_ms}ms</div>
            </div>
          </div>

          {/* Latency breakdown */}
          <div className="latency-card">
            <div className="latency-title">
              <Clock size={14} />
              Stage Latency Breakdown
            </div>
            <div className="latency-row">
              <span style={{ color: '#8e8e8e' }}>1. Hybrid Retrieval (Dense+BM25):</span>
              <span style={{ fontWeight: 600 }}>{displayMetrics.latency_ms?.retrieval_ms ?? 0} ms</span>
            </div>
            <div className="latency-row">
              <span style={{ color: '#8e8e8e' }}>2. Cross-Encoder Reranking:</span>
              <span style={{ fontWeight: 600 }}>{displayMetrics.latency_ms?.rerank_ms ?? 0} ms</span>
            </div>
            <div className="latency-row">
              <span style={{ color: '#8e8e8e' }}>3. LLM Generation:</span>
              <span style={{ fontWeight: 600 }}>{displayMetrics.latency_ms?.generation_ms ?? 0} ms</span>
            </div>
            <div className="latency-row">
              <span style={{ color: '#8e8e8e' }}>4. Claim Verification:</span>
              <span style={{ fontWeight: 600 }}>{displayMetrics.latency_ms?.verification_ms ?? 0} ms</span>
            </div>
          </div>

          {/* Top candidates table */}
          <div>
            <div style={{ fontSize: '0.78rem', fontWeight: 600, color: '#8e8e8e', marginBottom: '0.45rem', textTransform: 'uppercase' }}>
              Top Retrieved & Reranked Evidence
            </div>
            <div className="table-wrapper">
              <table className="clean-table">
                <thead>
                  <tr>
                    <th>#</th>
                    <th>Doc</th>
                    <th>P.</th>
                    <th>Dense</th>
                    <th>BM25</th>
                    <th>RRF</th>
                    <th>Rerank</th>
                  </tr>
                </thead>
                <tbody>
                  {displayMetrics.top_results?.map((res, i) => (
                    <tr key={i}>
                      <td style={{ fontWeight: 600 }}>{res.rank}</td>
                      <td title={res.title} style={{ color: '#ffffff' }}>{res.doc_id}</td>
                      <td>{res.page}</td>
                      <td>{res.dense_rank ? `#${res.dense_rank}` : '—'}</td>
                      <td>{res.sparse_rank ? `#${res.sparse_rank}` : '—'}</td>
                      <td>{res.rrf_score}</td>
                      <td style={{ fontWeight: 600, color: '#ffffff' }}>{res.rerank_score}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </>
      ) : (
        <div style={{ color: '#8e8e8e', fontSize: '0.85rem', textAlign: 'center', padding: '2rem 1rem' }}>
          Send a query to view stage-by-stage latency, Precision@K, MRR, and candidate reranking scores.
        </div>
      )}
    </aside>
  );
}

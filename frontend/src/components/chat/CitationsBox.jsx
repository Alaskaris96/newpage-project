import React from 'react';

export function CitationsBox({ citations }) {
  if (!citations || citations.length === 0) return null;

  return (
    <div className="citations-box">
      <div className="citations-header">
        <span>Grounded Sources & Citations</span>
        <span>{citations.length} documents</span>
      </div>
      <div className="citations-grid">
        {citations.map((c, ci) => (
          <div key={ci} className="citation-item">
            <div className="citation-meta">
              <span>[{c.doc_id}] {c.doc_title} (Page {c.page_number})</span>
              <span style={{ fontSize: '0.72rem', color: '#8e8e8e' }}>
                Rerank: {c.rerank_score !== undefined ? Number(c.rerank_score).toFixed(2) : ''}
              </span>
            </div>
            <div className="citation-body">"{c.snippet}"</div>
          </div>
        ))}
      </div>
    </div>
  );
}

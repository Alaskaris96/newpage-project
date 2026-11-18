import React from 'react';
import { CheckCircle2 } from 'lucide-react';
import { formatPercentage } from '../../utils/formatters';

export function ClaimsBox({ claims, faithfulnessScore }) {
  if (!claims || claims.length === 0) return null;

  return (
    <div className="claims-box">
      <div className="claims-header">
        <span style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
          <CheckCircle2 size={15} />
          Claim-Level Grounding Verification
        </span>
        <span>
          Faithfulness: {formatPercentage(faithfulnessScore !== undefined ? faithfulnessScore : 1, 0)}
        </span>
      </div>
      {claims.map((cl, ci) => (
        <div key={ci} className="claim-row">
          <span
            className={`monochrome-tag ${
              cl.verdict === 'SUPPORTED'
                ? 'tag-supported'
                : cl.verdict === 'INSUFFICIENT_EVIDENCE'
                ? 'tag-insufficient'
                : 'tag-contradicted'
            }`}
          >
            {cl.verdict}
          </span>
          <div style={{ flex: 1 }}>
            <div style={{ color: '#ffffff' }}>{cl.claim}</div>
            {cl.explanation && (
              <div style={{ fontSize: '0.74rem', color: '#8e8e8e', marginTop: '0.15rem' }}>
                {cl.explanation}
              </div>
            )}
          </div>
        </div>
      ))}
    </div>
  );
}

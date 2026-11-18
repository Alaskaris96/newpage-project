import React from 'react';
import { Sparkles } from 'lucide-react';

export function EmptyChatHero({ qaSamples, onSendPrompt }) {
  return (
    <div className="empty-chat-hero">
      <div className="hero-avatar">
        <Sparkles size={26} />
      </div>
      <h2 className="hero-title">What would you like to know?</h2>
      <p className="hero-subtitle">
        Query Northwind Consolidated Holdings’ 50 enterprise PDFs with hybrid retrieval, cross-encoder reranking, and claim-level verification.
      </p>

      <div className="prompt-suggestions-grid">
        {qaSamples.slice(0, 4).map((sample, i) => (
          <div
            key={i}
            className="prompt-card"
            onClick={() => onSendPrompt(sample.question)}
          >
            <div>{sample.question}</div>
            <div className="prompt-card-category">{sample.category || 'Ground Truth QA'}</div>
          </div>
        ))}
        <div
          className="prompt-card"
          onClick={() => onSendPrompt("Calculate 25 * 0.8 for prorated leave calculation")}
        >
          <div>Calculate 25 * 0.8 for prorated leave calculation</div>
          <div className="prompt-card-category">Deterministic Tool Call</div>
        </div>
        <div
          className="prompt-card"
          onClick={() => onSendPrompt("Who wrote HR-POL-001 and what is its classification?")}
        >
          <div>Who wrote HR-POL-001 and what is its classification?</div>
          <div className="prompt-card-category">Document Metadata Lookup</div>
        </div>
      </div>
    </div>
  );
}

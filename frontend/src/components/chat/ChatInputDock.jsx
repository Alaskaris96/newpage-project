import React from 'react';
import { ArrowUp } from 'lucide-react';

export function ChatInputDock({
  question,
  onChangeQuestion,
  onSendQuestion,
  isLoading,
  selectedCategory,
  onClearCategory
}) {
  return (
    <div className="bottom-dock">
      <div className="dock-inner">
        {selectedCategory && (
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.45rem' }}>
            <span style={{ fontSize: '0.74rem', background: '#212121', border: '1px solid #383838', padding: '0.2rem 0.6rem', borderRadius: '12px', color: '#ffffff', display: 'inline-flex', alignItems: 'center', gap: '0.4rem' }}>
              Active Filter: <strong>{selectedCategory}</strong>
              <button
                onClick={onClearCategory}
                style={{ background: 'none', border: 'none', color: '#8e8e8e', cursor: 'pointer', fontSize: '0.9rem', lineHeight: 1 }}
                title="Clear category filter"
              >
                ×
              </button>
            </span>
          </div>
        )}
        <div className="input-pill-wrapper">
          <input
            type="text"
            className="chat-input-field"
            placeholder="Ask anything about Northwind policies, SLAs, or calculate metrics..."
            value={question}
            onChange={e => onChangeQuestion(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && !e.shiftKey && onSendQuestion()}
            disabled={isLoading}
          />
          <button
            className="chat-send-circle"
            onClick={() => onSendQuestion()}
            disabled={isLoading || !question.trim()}
            title="Send question"
          >
            {isLoading ? (
              <span className="mini-spinner" style={{ borderTopColor: '#000000' }}></span>
            ) : (
              <ArrowUp size={18} />
            )}
          </button>
        </div>
        <div className="dock-disclaimer">
          Northwind RAG answers are strictly grounded in 50 enterprise PDFs with Cross-Encoder reranking and claim-level verification.
        </div>
      </div>
    </div>
  );
}

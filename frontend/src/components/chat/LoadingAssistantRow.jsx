import React from 'react';
import { Sparkles } from 'lucide-react';

export function LoadingAssistantRow() {
  return (
    <div className="message-row assistant">
      <div className="loading-assistant-row">
        <div className="assistant-avatar-circle">
          <Sparkles size={16} />
        </div>
        <div className="typing-indicator-box">
          <div className="typing-dots">
            <span className="typing-dot"></span>
            <span className="typing-dot"></span>
            <span className="typing-dot"></span>
          </div>
          <div className="loading-status-text">
            <span className="mini-spinner"></span>
            <span>Searching documents & reranking evidence...</span>
          </div>
        </div>
      </div>
    </div>
  );
}

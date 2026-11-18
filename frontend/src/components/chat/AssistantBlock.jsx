import React from 'react';
import { Sparkles } from 'lucide-react';
import { ToolCallBox } from './ToolCallBox';
import { ClaimsBox } from './ClaimsBox';
import { CitationsBox } from './CitationsBox';

export function AssistantBlock({ msg, index, isSelected, onInspectTurn }) {
  return (
    <div className="message-row assistant">
      <div className="assistant-block">
        <div className="assistant-avatar-circle">
          <Sparkles size={16} />
        </div>
        <div className="assistant-content-area">
          <div className="assistant-text">{msg.content}</div>

          {/* Tool executions */}
          <ToolCallBox toolResults={msg.tool_results} />

          {/* Grounding & Claims Verification */}
          <ClaimsBox claims={msg.claims} faithfulnessScore={msg.faithfulness_score} />

          {/* Evidence Citations */}
          <CitationsBox citations={msg.citations} />

          {/* Action Bar */}
          {msg.metrics && (
            <div className="assistant-action-bar">
              <span style={{ fontSize: '0.74rem', color: '#8e8e8e' }}>
                {msg.metrics.retrieved_count ? `${msg.metrics.retrieved_count} chunks retrieved · Total ${msg.metrics.latency_ms?.total_ms}ms` : ''}
              </span>
              <button
                className={`inspect-turn-btn ${isSelected ? 'active' : ''}`}
                onClick={() => onInspectTurn(index)}
              >
                Inspect Metrics & Candidates
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

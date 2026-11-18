import React from 'react';
import { Wrench } from 'lucide-react';

export function ToolCallBox({ toolResults }) {
  if (!toolResults || toolResults.length === 0) return null;

  return (
    <div className="tool-call-box">
      <div style={{ fontWeight: 600, color: '#ffffff', marginBottom: '0.35rem', display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
        <Wrench size={13} />
        Deterministic Tool Executions:
      </div>
      {toolResults.map((tr, ti) => (
        <div key={ti} style={{ color: '#d1d1d1' }}>
          • <strong>{tr.tool}</strong>: {tr.output}
        </div>
      ))}
    </div>
  );
}

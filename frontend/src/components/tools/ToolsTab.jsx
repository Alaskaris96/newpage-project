import React from 'react';
import { Wrench, Calculator } from 'lucide-react';

export function ToolsTab({
  tools,
  enabledTools,
  onToggleTool,
  toolTestName,
  toolTestInput,
  toolTestResult,
  onChangeToolTestInput,
  onSelectToolTestName,
  onExecuteTool
}) {
  return (
    <div className="tab-page-container">
      <div className="panel-card">
        <div className="panel-card-header">
          <div>
            <h3 className="panel-title">
              <Wrench size={20} />
              Plug & Play Tools Registry
            </h3>
            <p className="panel-subtitle">
              The LangGraph agent dynamically accepts an array of tools and routes requests when deterministic answers are required.
            </p>
          </div>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1rem', marginBottom: '1.5rem' }}>
          {tools.map((t, idx) => {
            const isChecked = enabledTools.includes(t.name);
            return (
              <div
                key={idx}
                style={{
                  background: '#212121',
                  border: `1px solid ${isChecked ? '#ffffff' : '#383838'}`,
                  borderRadius: '8px',
                  padding: '1rem'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                  <span style={{ fontWeight: 600, color: '#ffffff', display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
                    <Calculator size={15} />
                    {t.name}
                  </span>
                  <label style={{ display: 'flex', alignItems: 'center', gap: '0.35rem', fontSize: '0.75rem', cursor: 'pointer', color: '#d1d1d1' }}>
                    <input
                      type="checkbox"
                      checked={isChecked}
                      onChange={() => onToggleTool(t.name)}
                    />
                    Active for RAG
                  </label>
                </div>
                <p style={{ fontSize: '0.8rem', color: '#8e8e8e' }}>{t.description}</p>
              </div>
            );
          })}
        </div>

        {/* Tool Execution Playground */}
        <div style={{ background: '#212121', padding: '1.25rem', borderRadius: '8px', border: '1px solid #383838' }}>
          <span style={{ fontSize: '0.92rem', fontWeight: 600, color: '#ffffff', display: 'block', marginBottom: '0.75rem' }}>
            Test Tool Execution Directly
          </span>
          <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap', marginBottom: '0.75rem' }}>
            <select
              className="bw-select"
              value={toolTestName}
              onChange={e => onSelectToolTestName(e.target.value)}
            >
              {tools.map(t => (
                <option key={t.name} value={t.name}>{t.name}</option>
              ))}
            </select>
            <input
              type="text"
              className="bw-input"
              value={toolTestInput}
              onChange={e => onChangeToolTestInput(e.target.value)}
              style={{ flex: 1, minWidth: '240px', fontFamily: 'monospace' }}
              placeholder='JSON input, e.g. {"expression": "25 * 0.8"}'
            />
            <button className="bw-btn-secondary" onClick={onExecuteTool}>
              Execute Tool
            </button>
          </div>

          {toolTestResult && (
            <pre style={{ background: '#171717', padding: '0.75rem', borderRadius: '6px', fontSize: '0.8rem', overflowX: 'auto', color: '#ffffff', border: '1px solid #383838' }}>
              {JSON.stringify(toolTestResult, null, 2)}
            </pre>
          )}
        </div>
      </div>
    </div>
  );
}

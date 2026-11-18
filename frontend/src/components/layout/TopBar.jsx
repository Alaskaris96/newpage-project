import React from 'react';
import { PanelLeft, BarChart3 } from 'lucide-react';

export function TopBar({
  sidebarOpen,
  onToggleSidebar,
  activeTab,
  metricsOpen,
  onToggleMetrics,
  totalLatencyMs
}) {
  return (
    <header className="top-bar">
      <div className="top-bar-left">
        <button
          className="icon-btn"
          onClick={onToggleSidebar}
          title={sidebarOpen ? "Close sidebar" : "Open sidebar"}
        >
          <PanelLeft size={18} />
        </button>
        <div className="model-title">
          Northwind Enterprise RAG
          <span className="model-badge">Hybrid + Reranker</span>
        </div>
      </div>

      <div className="top-bar-right">
        {activeTab === 'chat' && (
          <button
            className={`toggle-metrics-btn ${metricsOpen ? 'active' : ''}`}
            onClick={onToggleMetrics}
          >
            <BarChart3 size={15} />
            <span>{metricsOpen ? 'Hide Metrics' : 'Inspect RAG Metrics'}</span>
            {totalLatencyMs && (
              <span style={{ opacity: 0.7, fontSize: '0.72rem' }}>
                ({totalLatencyMs}ms)
              </span>
            )}
          </button>
        )}
      </div>
    </header>
  );
}

import React from 'react';
import {
  Plus,
  Sparkles,
  MessageSquare,
  BarChart3,
  BookOpen,
  Wrench
} from 'lucide-react';

export function Sidebar({
  sidebarOpen,
  activeTab,
  onSelectTab,
  onNewChat,
  uniqueCategories,
  selectedCategory,
  onSelectCategory,
  health,
  documentsCount,
  chunksCount
}) {
  return (
    <aside className={`sidebar ${sidebarOpen ? '' : 'collapsed'}`}>
      <div className="sidebar-header">
        <button className="new-chat-btn" onClick={onNewChat}>
          <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Plus size={16} />
            New chat
          </span>
          <Sparkles size={14} style={{ opacity: 0.6 }} />
        </button>
      </div>

      <nav className="sidebar-nav">
        <div className="sidebar-section-title">Navigation</div>
        <button
          className={`sidebar-nav-item ${activeTab === 'chat' ? 'active' : ''}`}
          onClick={() => onSelectTab('chat')}
        >
          <MessageSquare size={16} />
          Northwind Chat
        </button>
        <button
          className={`sidebar-nav-item ${activeTab === 'benchmark' ? 'active' : ''}`}
          onClick={() => onSelectTab('benchmark')}
        >
          <BarChart3 size={16} />
          Evaluation & Benchmark
        </button>
        <button
          className={`sidebar-nav-item ${activeTab === 'corpus' ? 'active' : ''}`}
          onClick={() => onSelectTab('corpus')}
        >
          <BookOpen size={16} />
          Corpus ({documentsCount || 50} PDFs)
        </button>
        <button
          className={`sidebar-nav-item ${activeTab === 'tools' ? 'active' : ''}`}
          onClick={() => onSelectTab('tools')}
        >
          <Wrench size={16} />
          Plug & Play Tools
        </button>

        <div className="sidebar-section-title" style={{ marginTop: '0.75rem' }}>Category Filter</div>
        <select
          className="sidebar-filter-select"
          value={selectedCategory}
          onChange={e => onSelectCategory(e.target.value)}
        >
          <option value="">All Categories ({documentsCount || 50} docs)</option>
          {uniqueCategories.map(cat => (
            <option key={cat} value={cat}>{cat}</option>
          ))}
        </select>
      </nav>

      <div className="sidebar-footer">
        <div className="status-badge">
          <span>PostgreSQL + pgvector</span>
          <span className="status-dot"></span>
        </div>
        <div className="status-badge">
          <span>Index: {health ? `${health.documents_indexed} Docs / ${health.chunks_indexed} Chunks` : (documentsCount ? `${documentsCount} Docs / ${chunksCount} Chunks` : 'Loading...')}</span>
        </div>
        <div className="status-badge">
          <span>LLM: {health?.llm_model}</span>
        </div>
        <div className="status-badge">
          <span>Rerank: ms-marco-MiniLM</span>
        </div>
      </div>
    </aside>
  );
}

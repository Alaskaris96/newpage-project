import React from 'react';
import { FileText, RefreshCw } from 'lucide-react';

export function CorpusTab({
  documents,
  isIngesting,
  ingestStatus,
  onIngestAll
}) {
  return (
    <div className="tab-page-container">
      <div className="panel-card">
        <div className="panel-card-header">
          <div>
            <h3 className="panel-title">
              <FileText size={20} />
              Northwind Consolidated Holdings Corpus ({documents.length} PDFs)
            </h3>
            <p className="panel-subtitle">
              Ingested from <code>/dataset/pdfs</code> with structure-aware chunking, dense vectors, and fulltext tsvectors.
            </p>
          </div>
          <div>
            <button
              className="bw-btn-primary"
              onClick={onIngestAll}
              disabled={isIngesting}
            >
              {isIngesting ? (
                <>
                  <span className="mini-spinner" style={{ borderTopColor: '#000000' }}></span>
                  Ingesting...
                </>
              ) : (
                <>
                  <RefreshCw size={15} />
                  Re-Ingest All PDFs
                </>
              )}
            </button>
          </div>
        </div>

        {ingestStatus && (
          <div style={{ background: '#212121', padding: '0.75rem', borderRadius: '6px', marginBottom: '1rem', border: '1px solid #383838', fontSize: '0.85rem' }}>
            {ingestStatus}
          </div>
        )}

        <div className="table-wrapper">
          <table className="clean-table">
            <thead>
              <tr>
                <th>Doc ID</th>
                <th>Title</th>
                <th>Category</th>
                <th>Type</th>
                <th>Author</th>
                <th>Version</th>
                <th>Pages</th>
                <th>Chunks</th>
              </tr>
            </thead>
            <tbody>
              {documents.map((doc, idx) => (
                <tr key={idx}>
                  <td style={{ fontWeight: 600, color: '#ffffff' }}>{doc.id}</td>
                  <td>{doc.title}</td>
                  <td>{doc.category}</td>
                  <td>{doc.doc_type}</td>
                  <td>{doc.author}</td>
                  <td>v{doc.version}</td>
                  <td>{doc.page_count}</td>
                  <td style={{ fontWeight: 600, color: '#ffffff' }}>{doc.chunk_count}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

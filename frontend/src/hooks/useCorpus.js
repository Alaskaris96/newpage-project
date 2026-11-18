import { useState, useEffect, useCallback, useMemo } from 'react';
import { fetchDocumentsApi, triggerIngestApi } from '../api/corpusApi';

export function useCorpus(onIngestSuccess) {
  const [documents, setDocuments] = useState([]);
  const [isIngesting, setIsIngesting] = useState(false);
  const [ingestStatus, setIngestStatus] = useState(null);

  const reloadDocuments = useCallback(async () => {
    try {
      const data = await fetchDocumentsApi();
      setDocuments(data);
    } catch (err) {
      console.error('Fetch documents error:', err);
    }
  }, []);

  useEffect(() => {
    reloadDocuments();
  }, [reloadDocuments]);

  const uniqueCategories = useMemo(() => {
    return Array.from(new Set(documents.map(d => d.category).filter(Boolean))).sort();
  }, [documents]);

  const handleIngestAll = useCallback(async () => {
    setIsIngesting(true);
    setIngestStatus('Ingesting and embedding 50 PDF files...');
    try {
      const data = await triggerIngestApi();
      setIngestStatus(`Success: ${data.documents_indexed} documents, ${data.chunks_indexed} chunks indexed.`);
      await reloadDocuments();
      if (onIngestSuccess) {
        onIngestSuccess();
      }
    } catch (err) {
      setIngestStatus(`Error: ${err.message}`);
    } finally {
      setIsIngesting(false);
    }
  }, [reloadDocuments, onIngestSuccess]);

  return {
    documents,
    isIngesting,
    ingestStatus,
    uniqueCategories,
    handleIngestAll,
    reloadDocuments
  };
}

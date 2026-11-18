export const DEFAULT_TOOL_INPUTS = {
  calculator: '{"expression": "25 * 0.8"}',
  search_document_metadata: '{"query": "HR-POL-001"}',
  get_corpus_statistics: '{"category": "Human Resources"}'
};

export const BENCHMARK_MODES = ['dense', 'bm25', 'hybrid', 'hybrid_rerank'];

export const SAMPLE_SIZE_OPTIONS = [
  { value: 5, label: '5 Questions (Fast)' },
  { value: 10, label: '10 Questions' },
  { value: 20, label: '20 Questions' }
];

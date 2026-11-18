import { useState, useEffect, useCallback } from 'react';
import { fetchToolsApi, executeToolApi } from '../api/toolsApi';
import { DEFAULT_TOOL_INPUTS } from '../utils/constants';

export function useTools() {
  const [tools, setTools] = useState([]);
  const [enabledTools, setEnabledTools] = useState(['calculator', 'search_document_metadata', 'get_corpus_statistics']);
  const [toolTestName, setToolTestName] = useState('calculator');
  const [toolTestInput, setToolTestInput] = useState(DEFAULT_TOOL_INPUTS.calculator || '');
  const [toolTestResult, setToolTestResult] = useState(null);

  const reloadTools = useCallback(async () => {
    try {
      const data = await fetchToolsApi();
      setTools(data);
      setEnabledTools(data.map(t => t.name));
    } catch (err) {
      console.error('Fetch tools error:', err);
    }
  }, []);

  useEffect(() => {
    reloadTools();
  }, [reloadTools]);

  const toggleTool = useCallback((toolName) => {
    setEnabledTools(prev => {
      if (prev.includes(toolName)) {
        return prev.filter(t => t !== toolName);
      } else {
        return [...prev, toolName];
      }
    });
  }, []);

  const handleToolSelectChange = useCallback((newToolName) => {
    setToolTestName(newToolName);
    if (DEFAULT_TOOL_INPUTS[newToolName]) {
      setToolTestInput(DEFAULT_TOOL_INPUTS[newToolName]);
    }
  }, []);

  const handleExecuteTool = useCallback(async () => {
    try {
      const result = await executeToolApi({
        toolName: toolTestName,
        toolInput: toolTestInput
      });
      setToolTestResult(result);
    } catch (err) {
      setToolTestResult({ error: err.message });
    }
  }, [toolTestName, toolTestInput]);

  return {
    tools,
    enabledTools,
    toggleTool,
    toolTestName,
    toolTestInput,
    setToolTestInput,
    toolTestResult,
    handleToolSelectChange,
    handleExecuteTool,
    reloadTools
  };
}

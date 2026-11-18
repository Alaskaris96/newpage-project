import { useState, useEffect, useCallback, useMemo } from 'react';
import { sendChatMessageApi, fetchQaSamplesApi } from '../api/chatApi';

export function useChat() {
  const [question, setQuestion] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState([]);
  const [currentMetrics, setCurrentMetrics] = useState(null);
  const [selectedMessageIndex, setSelectedMessageIndex] = useState(null);
  const [qaSamples, setQaSamples] = useState([]);

  useEffect(() => {
    let isMounted = true;
    fetchQaSamplesApi(6)
      .then(samples => {
        if (isMounted) setQaSamples(samples);
      })
      .catch(err => console.error('Fetch QA samples error:', err));
    return () => { isMounted = false; };
  }, []);

  const handleSendQuestion = useCallback(async (qToSend, categoryFilter, enabledTools) => {
    const q = (qToSend || question || '').trim();
    if (!q || isLoading) return;

    const userMsg = { role: 'user', content: q };
    setMessages(prev => [...prev, userMsg]);
    setQuestion('');
    setIsLoading(true);

    try {
      const data = await sendChatMessageApi({
        question: q,
        categoryFilter: categoryFilter || null,
        enabledTools
      });

      const assistantMsg = {
        role: 'assistant',
        question: q,
        content: data.answer,
        citations: data.citations,
        claims: data.claims,
        faithfulness_score: data.faithfulness_score,
        metrics: data.metrics,
        tool_calls: data.tool_calls,
        tool_results: data.tool_results,
        sufficient: data.sufficient_evidence
      };

      setMessages(prev => {
        const next = [...prev, assistantMsg];
        setSelectedMessageIndex(next.length - 1);
        return next;
      });
      setCurrentMetrics(data.metrics);
    } catch (err) {
      setMessages(prev => [
        ...prev,
        { role: 'assistant', content: `Error processing query: ${err.message}`, isError: true }
      ]);
    } finally {
      setIsLoading(false);
    }
  }, [question, isLoading]);

  const handleNewChat = useCallback(() => {
    setMessages([]);
    setCurrentMetrics(null);
    setSelectedMessageIndex(null);
  }, []);

  const assistantMessages = useMemo(() => {
    return messages.map((m, i) => ({ ...m, origIndex: i })).filter(m => m.role === 'assistant');
  }, [messages]);

  const activeMsg = useMemo(() => {
    if (selectedMessageIndex !== null && messages[selectedMessageIndex]?.role === 'assistant') {
      return messages[selectedMessageIndex];
    }
    return assistantMessages[assistantMessages.length - 1] || null;
  }, [messages, selectedMessageIndex, assistantMessages]);

  const displayMetrics = useMemo(() => {
    return activeMsg?.metrics || currentMetrics;
  }, [activeMsg, currentMetrics]);

  return {
    question,
    setQuestion,
    isLoading,
    messages,
    qaSamples,
    selectedMessageIndex,
    setSelectedMessageIndex,
    assistantMessages,
    activeMsg,
    displayMetrics,
    handleSendQuestion,
    handleNewChat
  };
}

import React from 'react';
import {
  useSystemHealth,
  useCorpus,
  useTools,
  useBenchmark,
  useNavigation,
  useChat
} from './hooks';
import {
  Sidebar,
  TopBar,
  ChatView,
  BenchmarkTab,
  CorpusTab,
  ToolsTab
} from './components';

export default function App() {
  // Navigation & View layout state
  const {
    activeTab,
    setActiveTab,
    sidebarOpen,
    setSidebarOpen,
    metricsOpen,
    setMetricsOpen,
    selectedCategory,
    setSelectedCategory
  } = useNavigation('chat');

  // System & Health hook
  const { health, reloadHealth } = useSystemHealth();

  // Corpus & Ingestion hook
  const {
    documents,
    isIngesting,
    ingestStatus,
    uniqueCategories,
    handleIngestAll
  } = useCorpus(reloadHealth);

  // Tools Registry hook
  const {
    tools,
    enabledTools,
    toggleTool,
    toolTestName,
    toolTestInput,
    setToolTestInput,
    toolTestResult,
    handleToolSelectChange,
    handleExecuteTool
  } = useTools();

  // Benchmark hook
  const {
    sampleSize,
    setSampleSize,
    benchmarkResult,
    benchmarkLoading,
    benchmarkHistory,
    handleRunBenchmark
  } = useBenchmark();

  // Chat & Verification hook
  const {
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
  } = useChat();

  return (
    <div className="chatgpt-app">
      {/* Left Sidebar */}
      <Sidebar
        sidebarOpen={sidebarOpen}
        activeTab={activeTab}
        onSelectTab={setActiveTab}
        onNewChat={handleNewChat}
        uniqueCategories={uniqueCategories}
        selectedCategory={selectedCategory}
        onSelectCategory={setSelectedCategory}
        health={health}
        documentsCount={documents.length}
        chunksCount={health?.chunks_indexed}
      />

      {/* Main Viewport */}
      <div className="main-viewport">
        {/* Top App Header */}
        <TopBar
          sidebarOpen={sidebarOpen}
          onToggleSidebar={() => setSidebarOpen(!sidebarOpen)}
          activeTab={activeTab}
          metricsOpen={metricsOpen}
          onToggleMetrics={() => setMetricsOpen(!metricsOpen)}
          totalLatencyMs={displayMetrics?.latency_ms?.total_ms}
        />

        {/* TAB 1: Chat & Verification */}
        {activeTab === 'chat' && (
          <ChatView
            messages={messages}
            isLoading={isLoading}
            question={question}
            onChangeQuestion={setQuestion}
            onSendQuestion={q => handleSendQuestion(q, selectedCategory, enabledTools)}
            qaSamples={qaSamples}
            selectedCategory={selectedCategory}
            onClearCategory={() => setSelectedCategory('')}
            selectedMessageIndex={selectedMessageIndex}
            onInspectTurn={idx => {
              setSelectedMessageIndex(idx);
              setMetricsOpen(true);
            }}
            metricsOpen={metricsOpen}
            onCloseMetrics={() => setMetricsOpen(false)}
            assistantMessages={assistantMessages}
            activeMsg={activeMsg}
            displayMetrics={displayMetrics}
          />
        )}

        {/* TAB 2: Evaluation & Benchmark */}
        {activeTab === 'benchmark' && (
          <BenchmarkTab
            sampleSize={sampleSize}
            onSelectSampleSize={setSampleSize}
            benchmarkLoading={benchmarkLoading}
            benchmarkResult={benchmarkResult}
            benchmarkHistory={benchmarkHistory}
            onRunBenchmark={handleRunBenchmark}
          />
        )}

        {/* TAB 3: Corpus & Ingestion */}
        {activeTab === 'corpus' && (
          <CorpusTab
            documents={documents}
            isIngesting={isIngesting}
            ingestStatus={ingestStatus}
            onIngestAll={handleIngestAll}
          />
        )}

        {/* TAB 4: Plug & Play Tools */}
        {activeTab === 'tools' && (
          <ToolsTab
            tools={tools}
            enabledTools={enabledTools}
            onToggleTool={toggleTool}
            toolTestName={toolTestName}
            toolTestInput={toolTestInput}
            toolTestResult={toolTestResult}
            onChangeToolTestInput={setToolTestInput}
            onSelectToolTestName={handleToolSelectChange}
            onExecuteTool={handleExecuteTool}
          />
        )}
      </div>
    </div>
  );
}

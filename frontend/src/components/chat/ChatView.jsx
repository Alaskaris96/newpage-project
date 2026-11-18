import React, { useRef, useEffect } from 'react';
import { EmptyChatHero } from './EmptyChatHero';
import { UserBubble } from './UserBubble';
import { AssistantBlock } from './AssistantBlock';
import { LoadingAssistantRow } from './LoadingAssistantRow';
import { ChatInputDock } from './ChatInputDock';
import { MetricsDrawer } from './MetricsDrawer';

export function ChatView({
  messages,
  isLoading,
  question,
  onChangeQuestion,
  onSendQuestion,
  qaSamples,
  selectedCategory,
  onClearCategory,
  selectedMessageIndex,
  onInspectTurn,
  metricsOpen,
  onCloseMetrics,
  assistantMessages,
  activeMsg,
  displayMetrics
}) {
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isLoading]);

  return (
    <div className="chat-body-wrapper">
      <div className="chat-center-pane">
        <div className="messages-container">
          {messages.length === 0 ? (
            <EmptyChatHero
              qaSamples={qaSamples}
              onSendPrompt={q => onSendQuestion(q)}
            />
          ) : (
            <div className="messages-inner">
              {messages.map((msg, idx) =>
                msg.role === 'user' ? (
                  <UserBubble key={idx} content={msg.content} />
                ) : (
                  <AssistantBlock
                    key={idx}
                    msg={msg}
                    index={idx}
                    isSelected={selectedMessageIndex === idx}
                    onInspectTurn={onInspectTurn}
                  />
                )
              )}

              {isLoading && <LoadingAssistantRow />}

              <div ref={messagesEndRef} />
            </div>
          )}
        </div>

        <ChatInputDock
          question={question}
          onChangeQuestion={onChangeQuestion}
          onSendQuestion={onSendQuestion}
          isLoading={isLoading}
          selectedCategory={selectedCategory}
          onClearCategory={onClearCategory}
        />
      </div>

      <MetricsDrawer
        metricsOpen={metricsOpen}
        onClose={onCloseMetrics}
        assistantMessages={assistantMessages}
        activeMsg={activeMsg}
        displayMetrics={displayMetrics}
        onSelectTurn={onInspectTurn}
      />
    </div>
  );
}

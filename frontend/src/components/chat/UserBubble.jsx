import React from 'react';

export function UserBubble({ content }) {
  return (
    <div className="message-row user">
      <div className="user-bubble">{content}</div>
    </div>
  );
}

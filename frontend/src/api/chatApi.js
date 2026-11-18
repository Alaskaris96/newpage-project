export async function sendChatMessageApi({ question, categoryFilter, enabledTools }) {
  const res = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      question,
      category_filter: categoryFilter || null,
      enabled_tools: enabledTools
    })
  });

  if (!res.ok) {
    throw new Error(`Chat API error: status ${res.status}`);
  }

  return res.json();
}

export async function fetchQaSamplesApi(limit = 6) {
  const res = await fetch(`/api/qa-samples?limit=${limit}`);
  if (!res.ok) {
    throw new Error(`Failed to fetch QA samples: status ${res.status}`);
  }
  return res.json();
}

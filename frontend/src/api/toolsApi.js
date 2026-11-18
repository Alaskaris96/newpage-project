export async function fetchToolsApi() {
  const res = await fetch('/api/tools');
  if (!res.ok) {
    throw new Error(`Failed to load tools: status ${res.status}`);
  }
  return res.json();
}

export async function executeToolApi({ toolName, toolInput }) {
  let payload;
  try {
    payload = typeof toolInput === 'string' ? JSON.parse(toolInput) : toolInput;
  } catch {
    payload = toolInput;
  }

  const res = await fetch('/api/tools/execute', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      tool_name: toolName,
      tool_input: payload
    })
  });

  if (!res.ok) {
    throw new Error(`Tool execution failed: status ${res.status}`);
  }

  return res.json();
}

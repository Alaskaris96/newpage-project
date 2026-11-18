export function formatPercentage(ratio, decimals = 1) {
  if (ratio === null || ratio === undefined || isNaN(ratio)) return '—';
  return `${(Number(ratio) * 100).toFixed(decimals)}%`;
}

export function formatMs(ms) {
  if (ms === null || ms === undefined || isNaN(ms)) return '0 ms';
  return `${Number(ms).toFixed(1)} ms`;
}

export function formatDate(timestamp) {
  if (!timestamp) return '—';
  try {
    return new Date(timestamp).toLocaleString();
  } catch {
    return String(timestamp);
  }
}

export function truncateText(text, max = 22) {
  if (!text) return '';
  return text.length > max ? text.slice(0, max) + '...' : text;
}

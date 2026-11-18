import { useState, useEffect, useCallback } from 'react';
import { fetchHealthApi } from '../api/systemApi';

export function useSystemHealth() {
  const [health, setHealth] = useState(null);
  const [error, setError] = useState(null);

  const reloadHealth = useCallback(async () => {
    try {
      const data = await fetchHealthApi();
      setHealth(data);
      setError(null);
    } catch (err) {
      console.error('System health error:', err);
      setError(err.message);
    }
  }, []);

  useEffect(() => {
    reloadHealth();
  }, [reloadHealth]);

  return { health, error, reloadHealth };
}

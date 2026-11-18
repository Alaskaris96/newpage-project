import { useState } from 'react';

export function useNavigation(defaultTab = 'chat') {
  const [activeTab, setActiveTab] = useState(defaultTab);
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [metricsOpen, setMetricsOpen] = useState(false);
  const [selectedCategory, setSelectedCategory] = useState('');

  return {
    activeTab,
    setActiveTab,
    sidebarOpen,
    setSidebarOpen,
    metricsOpen,
    setMetricsOpen,
    selectedCategory,
    setSelectedCategory
  };
}

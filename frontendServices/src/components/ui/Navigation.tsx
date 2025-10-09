import React from 'react';
import { useApp } from '@/context/AppContext';
import { NAVIGATION_TABS } from '@/utils/constants';

const Navigation: React.FC = () => {
  const { activeTab, setActiveTab } = useApp();

  return (
    <nav className="flex items-center space-x-1">
      {NAVIGATION_TABS.map((tab) => {
        const Icon = tab.icon;
        const isActive = activeTab === tab.id;
        
        return (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            title={tab.description}
            className={`
              flex items-center space-x-2 px-4 py-2 rounded-lg font-medium 
              transition-all duration-200 transform hover:scale-105
              ${isActive
                ? 'bg-blue-600 text-white shadow-sm scale-105'
                : 'text-gray-600 hover:text-gray-800 hover:bg-gray-100'
              }
            `}
          >
            <Icon size={18} />
            <span>{tab.label}</span>
          </button>
        );
      })}
    </nav>
  );
};

export default Navigation;
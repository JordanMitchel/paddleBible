import { TabType } from '@/utils/constants';
import React, { createContext, useContext, useState, ReactNode } from 'react';

interface AppContextType {
  activeTab: TabType;
  setActiveTab: (tab: TabType) => void;
  isLoginModalOpen: boolean;
  setIsLoginModalOpen: (open: boolean) => void;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

export const useApp = () => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useApp must be used within an AppProvider');
  }
  return context;
};

interface AppProviderProps {
  children: ReactNode;
}

export const AppProvider: React.FC<AppProviderProps> = ({ children }) => {
  const [activeTab, setActiveTab] = useState<TabType>('home');
  const [isLoginModalOpen, setIsLoginModalOpen] = useState(false);

  return (
    <AppContext.Provider
      value={{
        activeTab,
        setActiveTab,
        isLoginModalOpen,
        setIsLoginModalOpen,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};
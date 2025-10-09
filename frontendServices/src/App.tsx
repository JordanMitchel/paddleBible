import React from 'react';
import { SWRConfig } from 'swr';
import Layout from '@/components/layout/Layout';
import { AuthProvider } from '@/components/auth/AuthProvider';
import { AppProvider } from '@/context/AppContext';
import LoginModal from '@/components/auth/LoginModal';
import { fetcher } from '@/services/api';

function App() {
  return (
    <SWRConfig
      value={{
        fetcher,
        revalidateOnFocus: false,
        revalidateOnReconnect: true,
        errorRetryCount: 3,
      }}
    >
      <AuthProvider>
        <AppProvider>
          <Layout />
          <LoginModal />
        </AppProvider>
      </AuthProvider>
    </SWRConfig>
  );
}

export default App;
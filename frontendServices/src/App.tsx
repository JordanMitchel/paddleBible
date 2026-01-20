import Layout from '@/components/layout/Layout';
import { AuthProvider } from '@/components/auth/AuthProvider';
import { AppProvider } from '@/context/AppContext';
import LoginModal from '@/components/auth/LoginModal';
import { ThemeModeProvider } from './context/theme-context';
import { BrowserRouter } from 'react-router-dom';

function App() {
  return (
      <AuthProvider>
        <ThemeModeProvider>
          <AppProvider>
            <Layout />
            <LoginModal />
          </AppProvider>
        </ThemeModeProvider>
      </AuthProvider>
  );
}

export default App;
import React from 'react';
import { Home } from 'lucide-react';
import Logo from './Logo';
import Navigation from './Navigation';
import Button from './Button';
import { useApp } from '@/context/AppContext';
import { useAuth } from '@/components/auth/AuthProvider';

const Header: React.FC = () => {
  const { activeTab, setActiveTab, setIsLoginModalOpen } = useApp();
  const { isAuthenticated, user, logout } = useAuth();

  return (
    <header className="w-full bg-white/95 backdrop-blur-sm shadow-sm sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-8">
            <Logo />
            
            <button
              onClick={() => setActiveTab('home')}
              className={`
                flex items-center space-x-2 px-3 py-2 rounded-lg transition-all duration-200
                ${activeTab === 'home' 
                  ? 'bg-blue-100 text-blue-700 shadow-sm' 
                  : 'text-gray-600 hover:text-gray-800 hover:bg-gray-100'
                }
              `}
            >
              <Home size={20} />
              <span className="font-medium">Home</span>
            </button>
          </div>

          <div className="flex items-center space-x-6">
            <Navigation />
            
            {isAuthenticated ? (
              <div className="flex items-center space-x-4">
                <div className="flex items-center space-x-2">
                  <div className="w-8 h-8 rounded-full bg-gradient-to-r from-blue-600 to-indigo-600 flex items-center justify-center">
                    <span className="text-white text-sm font-medium">
                      {user?.name?.charAt(0).toUpperCase()}
                    </span>
                  </div>
                  <span className="text-sm text-gray-600">{user?.name}</span>
                </div>
                <Button variant="outline" size="sm" onClick={logout}>
                  Logout
                </Button>
              </div>
            ) : (
              <Button variant="primary" size="sm" onClick={() => setIsLoginModalOpen(true)}>
                Log In
              </Button>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
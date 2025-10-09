import React from 'react';
import Header from '@/components/ui/Header';
import Hero from './Hero';

const Layout: React.FC = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <Header />
      <main className="flex-1">
        <Hero />
      </main>
    </div>
  );
};

export default Layout;
import React from 'react';
import { useApp } from '@/context/AppContext';
import Home from '@/pages/Home';
import Read from '@/pages/Read';
import Paddle from '@/pages/Paddle';
import Explore from '@/pages/Explore';
import About from '@/pages/About';

const Hero: React.FC = () => {
  const { activeTab } = useApp();

  const renderTabContent = () => {
    switch (activeTab) {
      case 'home':
        return <Home />;
      case 'read':
        return <Read />;
      case 'paddle':
        return <Paddle />;
      case 'explore':
        return <Explore />;
      case 'about':
        return <About />;
      default:
        return <Home />;
    }
  };

  return (
    <div className="w-full transition-all duration-300 ease-in-out">
      {renderTabContent()}
    </div>
  );
};

export default Hero;
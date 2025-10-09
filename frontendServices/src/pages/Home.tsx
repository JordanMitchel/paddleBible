import React from 'react';
import Button from '@/components/ui/Button';
import Card from '@/components/ui/Card';
import { useApp } from '@/context/AppContext';

const Home: React.FC = () => {
  const { setActiveTab } = useApp(); // Get setActiveTab from context

  return (
    <div className="max-w-7xl mx-auto px-6 py-16">
      <div className="text-center">
        <h1 className="text-5xl font-bold text-gray-900 mb-6">
          Welcome to Your
          <span className="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
            {" "}Adventure
          </span>
        </h1>
        <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto leading-relaxed">
          Discover amazing content, paddle through experiences, and explore new horizons. 
          Your journey starts here with our innovative platform.
        </p>
        
        <div className="flex items-center justify-center space-x-4 mb-16">
          <Button size="lg">Get Started</Button>
          <Button variant="outline"
            size="lg"
            onClick={() => setActiveTab('about')} // Add click handler
>Learn More</Button>
        </div>
        
        <div className="grid md:grid-cols-3 gap-8">
          <Card hover padding="md">
            <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4 mx-auto">
              <span className="text-blue-600 text-xl">📚</span>
            </div>
            <h3 className="text-lg font-semibold mb-2 text-gray-900">Rich Content</h3>
            <p className="text-gray-600 leading-relaxed">
              Access the bible in different languages with all of its context.
            </p>
          </Card>
          
          <Card hover padding="md">
            <div className="w-12 h-12 bg-indigo-100 rounded-lg flex items-center justify-center mb-4 mx-auto">
              <span className="text-indigo-600 text-xl">🚣</span>
            </div>
            <h3 className="text-lg font-semibold mb-2 text-gray-900">Interactive Experiences</h3>
            <p className="text-gray-600 leading-relaxed">
              Paddle through immersive text that maps to earth at your pace.
            </p>
          </Card>
          
          <Card hover padding="md">
            <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mb-4 mx-auto">
              <span className="text-purple-600 text-xl">🧭</span>
            </div>
            <h3 className="text-lg font-semibold mb-2 text-gray-900">Discover & Explore</h3>
            <p className="text-gray-600 leading-relaxed">
              Take a different perspective on the bible through maps and then stories.
            </p>
          </Card>
        </div>
      </div>
    </div>
  );
};

export default Home;
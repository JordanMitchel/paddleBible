import React from 'react';
import { Compass, TrendingUp, Star, MapPin } from 'lucide-react';
import Card from '@/components/ui/Card';

const Explore: React.FC = () => {
  const categories = ['Technology', 'Science', 'Arts', 'Culture', 'Innovation'];
  const trending = [1, 2, 3];

  return (
    <div className="w-full max-w-6xl mx-auto px-4 sm:px-6 py-8 sm:py-16">
      <div className="text-center mb-8 sm:mb-12">
        <Compass size={64} className="mx-auto text-blue-600 mb-6" />
        <h1 className="text-4xl font-bold text-gray-900 mb-4">Explore</h1>
        <p className="text-lg text-gray-600 leading-relaxed">
          Discover new territories, uncover hidden gems, and venture into uncharted possibilities.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8">
        <div className="lg:col-span-2">
          <h2 className="text-2xl font-semibold text-gray-900 mb-6 flex items-center">
            <TrendingUp className="mr-2 text-blue-600" size={24} />
            Trending Now
          </h2>
          <div className="space-y-4">
            {trending.map((item) => (
              <Card key={item} hover padding="md">
                <div className="flex items-center space-x-4">
                  <div className="w-16 h-16 bg-gradient-to-br from-purple-500 to-pink-500 rounded-xl flex items-center justify-center flex-shrink-0">
                    <MapPin className="text-white" size={24} />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-lg font-semibold text-gray-900 mb-1">
                      Amazing Discovery {item}
                    </h3>
                    <p className="text-gray-600 mb-2 leading-relaxed">
                      Uncover the secrets behind this fascinating topic...
                    </p>
                    <div className="flex items-center space-x-2">
                      <Star className="text-yellow-500" size={16} />
                      <span className="text-sm text-gray-500">4.8 rating</span>
                    </div>
                  </div>
                </div>
              </Card>
            ))}
          </div>
        </div>

        <div>
          <h2 className="text-xl font-semibold text-gray-900 mb-6">Categories</h2>
          <div className="space-y-3">
            {categories.map((category) => (
              <button
                key={category}
                className="w-full text-left px-4 py-3 bg-white rounded-lg shadow-sm hover:shadow-md transition-all hover:bg-blue-50 hover:border-blue-200 border border-gray-200 font-medium text-gray-900"
              >
                {category}
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Explore;
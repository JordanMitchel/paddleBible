import React from 'react';
import { Waves, Play } from 'lucide-react';
import Button from '@/components/ui/Button';
import Card from '@/components/ui/Card';

const Paddle: React.FC = () => {
  const experiences = [1, 2, 3, 4];

  return (
    <div className="max-w-4xl mx-auto px-6 py-16">
      <div className="text-center mb-12">
        <Waves size={64} className="mx-auto text-blue-600 mb-6" />
        <h1 className="text-4xl font-bold text-gray-900 mb-4">Paddle</h1>
        <p className="text-lg text-gray-600 leading-relaxed">
          Navigate through interactive experiences and immersive content that engages all your senses.
        </p>
      </div>

      <div className="grid md:grid-cols-2 gap-8">
        {experiences.map((item) => (
          <Card key={item} hover padding="md">
            <div className="aspect-video bg-gradient-to-br from-blue-400 to-indigo-500 rounded-lg mb-4 relative overflow-hidden group">
              <div className="absolute inset-0 flex items-center justify-center">
                <button className="bg-white/20 hover:bg-white/30 text-white p-4 rounded-full backdrop-blur-sm transition-all group-hover:scale-110">
                  <Play size={24} />
                </button>
              </div>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">
              Interactive Experience {item}
            </h3>
            <p className="text-gray-600 mb-4 leading-relaxed">
              An immersive journey through digital landscapes and interactive storytelling.
            </p>
            <div className="flex items-center justify-between">
              <span className="text-sm text-blue-600 font-medium">30 min experience</span>
              <Button size="sm">Start Journey</Button>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default Paddle;
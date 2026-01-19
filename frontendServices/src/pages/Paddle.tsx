import React from 'react';
import { Waves, Play, Globe, TreeDeciduous, Languages, Landmark } from 'lucide-react';
import Button from '@/components/ui/Button';
import Card from '@/components/ui/Card';

const experiences = [
  {
    title: 'Interactive Experience 1',
    description: 'An immersive journey through digital landscapes and interactive storytelling.',
    activity: 'The globe',
    icon: <Globe className="w-8 h-8 text-blue-500 mb-2" />,
  },
  {
    title: 'Interactive Experience 2',
    description: 'An immersive journey through geneology from Adam to Jesus.',
    activity: 'The family tree',
    icon: <TreeDeciduous className="w-8 h-8 text-green-500 mb-2" />,
  },
  {
    title: 'Interactive Experience 3',
    description: 'An immersive journey through the words of Jesus.',
    activity: 'Proclaiming the good news',
    icon: <Languages className="w-8 h-8 text-yellow-500 mb-2" />, // Chinese character/language icon
  },
  {
    title: 'Interactive Experience 4',
    description: 'An immersive journey through word usage and Etymology.',
    activity: 'The original languages',
    icon: <Languages className="w-8 h-8 text-purple-500 mb-2" />,
  },
  {
    title: 'Interactive Experience 5',
    description: 'An immersive journey through architecture and design.',
    activity: 'The designs in the bible',
    icon: <Landmark className="w-8 h-8 text-red-500 mb-2" />,
  },
];

const Paddle: React.FC = () => {
  return (
    <div className="w-full max-w-4xl mx-auto px-4 sm:px-6 py-8 sm:py-16">
      <div className="text-center mb-8 sm:mb-12">
        <Waves size={64} className="mx-auto text-blue-600 mb-6" />
        <h1 className="text-4xl font-bold text-gray-900 mb-4">Paddle</h1>
        <p className="text-lg text-gray-600 leading-relaxed">
          Navigate through interactive experiences and immersive content that engages all your senses.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8">
        {experiences.map((item) => (
          <Card key={item.title} hover padding="md">
            {item.icon}
            <div className="aspect-video bg-gradient-to-br from-blue-400 to-indigo-500 rounded-lg mb-4 relative overflow-hidden group">
              <div className="absolute inset-0 flex items-center justify-center">
                <button className="bg-white/20 hover:bg-white/30 text-white p-4 rounded-full backdrop-blur-sm transition-all group-hover:scale-110">
                  <Play size={24} />
                </button>
              </div>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">
              {item.title}
            </h3>
            <p className="text-gray-600 mb-4 leading-relaxed">
              {item.description}
            </p>
            <div className="flex items-center justify-between">
              <span className="text-sm text-blue-600 font-medium">{item.activity}</span>
              <Button size="sm">Start Journey</Button>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default Paddle;
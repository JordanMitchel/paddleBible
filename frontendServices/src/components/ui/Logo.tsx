import React from 'react';
import { BookOpenIcon } from '@heroicons/react/24/solid';

const Logo: React.FC = () => {
  return (
    <div className="flex items-center space-x-2">
      <div className="w-10 h-10 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-lg flex items-center justify-center">
        <BookOpenIcon className="h-6 w-6 text-white" />
      </div>
      <span className="text-xl font-semibold text-gray-800">Paddle</span>
    </div>
  );
};

export default Logo;
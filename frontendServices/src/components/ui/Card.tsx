import React, { ReactNode } from 'react';

interface CardProps {
  children: ReactNode;
  className?: string;
  hover?: boolean;
  padding?: 'none' | 'sm' | 'md' | 'lg';
}

const Card: React.FC<CardProps> = ({
  children,
  className = '',
  hover = false,
  padding = 'md',
}) => {
  const paddingClasses = {
    none: '',
    sm: 'p-4',
    md: 'p-6',
    lg: 'p-8',
  };

  const hoverClasses = hover 
    ? 'hover:shadow-md hover:border-gray-200 hover:-translate-y-1 cursor-pointer' 
    : '';

  return (
    <div
      className={`bg-white rounded-xl border border-gray-100 shadow-sm transition-all duration-300 ${paddingClasses[padding]} ${hoverClasses} ${className}`}
    >
      {children}
    </div>
  );
};

export default Card;
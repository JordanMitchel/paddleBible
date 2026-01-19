import { BookOpen, Waves, Compass, Church } from 'lucide-react';

export type TabType = 'home' | 'read' | 'paddle' | 'explore' | 'about';

export interface NavigationTab {
  id: TabType;
  label: string;
  icon: React.ComponentType<{ size?: number | string; className?: string }>;
  description?: string;
  path: string;
}

export const NAVIGATION_TABS: NavigationTab[] = [
  {
    id: 'home',
    label: 'Home',
    icon: Church,
    description: 'Welcome to PaddleBible',
    path: '/',
  },
  {
    id: 'read',
    label: 'Read',
    icon: BookOpen,
    description: 'Explore the bible and its chapters',
    path: '/read',
  },
  {
    id: 'paddle',
    label: 'Paddle',
    icon: Waves,
    description: 'Paddle through the scriptures',
    path: '/paddle',
  },
  {
    id: 'explore',
    label: 'Explore',
    icon: Compass,
    description: 'Navigate by map first then scripture',
    path: '/explore',
  },
  {
    id: 'about',
    label: 'About',
    icon: Church,
    description: 'Learn more about us',
    path: '/about',
  },
];

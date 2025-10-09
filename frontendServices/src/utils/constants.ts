import { BookOpen, Waves, Compass, Church } from 'lucide-react';
import { NavigationTab } from '@/types';

export const NAVIGATION_TABS: NavigationTab[] = [
  {
    id: 'read',
    label: 'Read',
    icon: BookOpen,
    description: 'Explore The bible and its chapters',
  },
  {
    id: 'paddle',
    label: 'Paddle',
    icon: Waves,
    description: 'Paddle through the scriptures',
  },
  {
    id: 'explore',
    label: 'Explore',
    icon: Compass,
    description: 'Nvaigate by map first then scripture',
  },
  {
    id: 'about',
    label: 'About',
    icon: Church,
    description: 'Learn more about us',
  }
];
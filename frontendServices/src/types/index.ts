export interface User {
  id: string;
  email: string;
  name: string;
  avatar?: string;
}

export interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
}

export type TabType = 'home' | 'read' | 'paddle' | 'explore' | 'about';

export interface NavigationTab {
  id: TabType;
  label: string;
  icon: React.ComponentType<{ size?: number; className?: string }>;
  description?: string;
}
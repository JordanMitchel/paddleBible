import { ReactNode } from "react";
import { FaApple, FaGoogle, FaGithub, FaDiscord } from "react-icons/fa";

export type FooterLink = {
  label: string;
  href: string;
  icon?: ReactNode;
};

export type FooterSection = {
  title: string;
  links: FooterLink[];
};

export const FOOTER_SECTIONS: FooterSection[] = [
  {
    title: 'Paddle',
    links: [
      { label: 'Features', href: '#' },
      { label: 'Versions', href: '#' },
      { label: 'Pricing', href: '#' },
    ],
  },
  {
    title: 'Resources',
    links: [
      { label: 'Docs', href: '#' },
      { label: 'Support', href: '#' },
      { label: 'Blog', href: '#' },
    ],
  },
  {
    title: 'Contact',
    links: [
      { label: 'Email', href: 'mailto:support@paddle.app' },
      { label: 'Twitter', href: '#' },
      { label: 'Discord', href: '#' },
    ],
  },
  {
    title: 'Login',
    links: [
      {
        label: 'Continue with GitHub',
        href: '/auth/github',
        icon: <div><FaGithub size={20}/></div>,
      },
      {
        label: 'Continue with Google',
        href: '/auth/google',
        icon: <FaGoogle size={20} />,
      },
      {
        label: 'Continue with Apple',
        href: '/auth/apple',
        icon: <FaApple size={24} />
      },
      {
        label: 'Continue with Discord',
        href: '/auth/discord',
        icon: <FaDiscord size={24} />
      },
      {
        label: 'Sign in',
        href: '/login',
      },
    ],
  },
];

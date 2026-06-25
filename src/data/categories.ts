export interface Category {
  slug: string;
  name: string;
  icon: string;
  description: string;
}

export const categories: Category[] = [
  {
    slug: 'getting-started',
    name: 'Getting Started',
    icon: '🚀',
    description: 'Install, configure and take your first steps with Home Assistant.',
  },
  {
    slug: 'automations',
    name: 'Automations',
    icon: '⚡',
    description: 'Build powerful automations to control your home automatically.',
  },
  {
    slug: 'integrations',
    name: 'Integrations',
    icon: '🔌',
    description: 'Connect devices and services — Zigbee, Z-Wave, Google, Alexa and more.',
  },
  {
    slug: 'dashboards',
    name: 'Dashboards',
    icon: '📊',
    description: 'Design beautiful Lovelace dashboards to monitor and control everything.',
  },
];

export function getCategoryBySlug(slug: string): Category | undefined {
  return categories.find(c => c.slug === slug);
}

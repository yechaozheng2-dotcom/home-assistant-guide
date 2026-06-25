## Task 2: Global Styles & Category Config

**Files:**
- Create: `src/styles/global.css`
- Create: `src/data/categories.ts`

**Interfaces:**
- Produces:
  - CSS custom properties: `--color-bg`, `--color-heading`, `--color-accent`, `--color-accent-warm`, `--color-muted`, `--color-border`, `--color-surface`
  - Callout CSS classes: `.callout-pros`, `.callout-cons`, `.callout-eco`
  - `categories` array export from `src/data/categories.ts` with shape `{ slug: string, name: string, icon: string, description: string }[]`

- [ ] **Step 1: Create `src/styles/global.css`**

```css
@import 'tailwindcss';
@plugin '@tailwindcss/typography';

:root {
  --color-bg: #FAFDF7;
  --color-heading: #1A2E1A;
  --color-accent: #3D7A45;
  --color-accent-warm: #C17C3A;
  --color-muted: #6B7F6B;
  --color-border: #D4E6D4;
  --color-surface: #FFFFFF;
}

body {
  background-color: var(--color-bg);
  color: var(--color-heading);
  font-family: 'Inter', system-ui, sans-serif;
}

@layer components {
  .callout-pros {
    background-color: #F0FAF0;
    border-left: 4px solid var(--color-accent);
    border-radius: 0.5rem;
    padding: 1rem 1.25rem;
    margin: 1.5rem 0;
  }

  .callout-pros li::before {
    content: '✓ ';
    color: var(--color-accent);
    font-weight: 700;
  }

  .callout-cons {
    background-color: #FDF6EE;
    border-left: 4px solid var(--color-accent-warm);
    border-radius: 0.5rem;
    padding: 1rem 1.25rem;
    margin: 1.5rem 0;
  }

  .callout-cons li::before {
    content: '✗ ';
    color: var(--color-accent-warm);
    font-weight: 700;
  }

  .callout-eco {
    background-color: #EEF5EE;
    border: 1px solid var(--color-border);
    border-radius: 0.5rem;
    padding: 1rem 1.25rem;
    margin: 1.5rem 0;
    display: flex;
    gap: 0.75rem;
    align-items: flex-start;
  }

  .callout-eco::before {
    content: '🌿';
    font-size: 1.25rem;
    flex-shrink: 0;
    margin-top: 0.1rem;
  }
}
```

- [ ] **Step 2: Create `src/data/categories.ts`**

```typescript
export interface Category {
  slug: string;
  name: string;
  icon: string;
  description: string;
}

export const categories: Category[] = [
  {
    slug: 'bamboo',
    name: 'Bamboo Products',
    icon: '🎋',
    description: 'Kitchenware, decor, and daily essentials made from fast-growing bamboo.',
  },
  {
    slug: 'kitchen',
    name: 'Kitchen',
    icon: '🍳',
    description: 'Eco-friendly cookware, utensils, and storage for a greener kitchen.',
  },
  {
    slug: 'home-decor',
    name: 'Home Decor',
    icon: '🏡',
    description: 'Sustainable decor that looks good and does good.',
  },
  {
    slug: 'daily',
    name: 'Daily Essentials',
    icon: '🌿',
    description: 'Swaps for everyday plastic items — toothbrushes, bottles, paper.',
  },
];

export function getCategoryBySlug(slug: string): Category | undefined {
  return categories.find(c => c.slug === slug);
}
```

- [ ] **Step 3: Commit**

```bash
git add src/styles/global.css src/data/categories.ts
git commit -m "feat: add global styles and category config"
```

---


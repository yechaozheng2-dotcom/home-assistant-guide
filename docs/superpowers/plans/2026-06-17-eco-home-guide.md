# Eco Home Guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a complete Astro 6 + Tailwind 4 affiliate content site for eco-friendly home products, cloned from diy-maker-station's architecture with all branding replaced and eco-specific features added.

**Architecture:** Static Astro site with Markdown content, category config-driven navigation, frontmatter-driven product cards, and a custom rehype plugin that transforms `[!pros]`/`[!cons]`/`[!eco]` blockquotes into styled callout blocks at build time.

**Tech Stack:** Astro 6, Tailwind 4, `@tailwindcss/typography`, `@astrojs/sitemap`, pagefind 1.x, sharp, Google Fonts (Lora + Inter)

## Global Constraints

- Site name everywhere: **Eco Home Guide** — zero occurrences of "DIY Maker Station" allowed
- Author default: **Eco Home Guide**
- OG `site_name`: **Eco Home Guide**
- JSON-LD publisher name: **Eco Home Guide**
- Astro: `^6.x`, Tailwind: `^4.x`, Node: `>=22.12.0`
- All color values use CSS custom properties from `:root` in `global.css` — no hardcoded hex in components
- Content schema `category` field is `z.string()` (not an enum) so pipeline can add categories without touching schema
- All affiliate links: `target="_blank" rel="noopener noreferrer nofollow"`

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `package.json` | Create | Dependencies, scripts (dev/build/postbuild/preview) |
| `tsconfig.json` | Create | Strict Astro TS config |
| `astro.config.mjs` | Create | Site URL, integrations (sitemap), Vite (Tailwind), rehype-callouts plugin |
| `public/favicon.svg` | Create | Green-leaf SVG favicon |
| `public/robots.txt` | Create | Allow all, sitemap pointer |
| `src/styles/global.css` | Create | CSS custom properties (green palette), Tailwind import, typography plugin, callout block styles |
| `src/data/categories.ts` | Create | Single source of truth: 4 category objects with slug/name/icon/description |
| `src/lib/rehype-callouts.ts` | Create | rehype plugin: `[!pros]`/`[!cons]`/`[!eco]` blockquote → styled div |
| `src/content.config.ts` | Create | Blog collection schema with products array |
| `src/components/Header.astro` | Create | Sticky header, brand name, category nav from `categories.ts`, search icon |
| `src/components/Footer.astro` | Create | Copyright, nav links (About/Privacy/Disclaimer/Terms) |
| `src/components/EcoBadge.astro` | Create | Pill label for eco certifications inside ProductCard |
| `src/components/ProductCard.astro` | Create | Frontmatter-driven product card: image, name, description, badge, stars, CTA |
| `src/components/PostCard.astro` | Create | Article card: image, category label, title, excerpt, date, reading time |
| `src/components/NewsletterForm.astro` | Create | Email capture form (static, no backend) |
| `src/components/TableOfContents.astro` | Create | Sidebar/mobile TOC from headings array |
| `src/layouts/BaseLayout.astro` | Create | HTML shell: SEO meta, OG, Twitter Card, JSON-LD, Google Fonts |
| `src/layouts/PostLayout.astro` | Create | 3-col article layout, products section, TOC sidebar |
| `src/pages/index.astro` | Create | Hero, category grid, latest 6 posts, newsletter |
| `src/pages/blog/index.astro` | Create | All posts sorted by date |
| `src/pages/blog/[slug].astro` | Create | Dynamic route → PostLayout |
| `src/pages/categories/[category].astro` | Create | Filtered posts by category slug |
| `src/pages/search.astro` | Create | pagefind UI widget |
| `src/pages/about.astro` | Create | Site mission, eco focus |
| `src/pages/privacy-policy.astro` | Create | Privacy policy with affiliate disclosure |
| `src/pages/disclaimer.astro` | Create | Amazon Associates + affiliate disclosure |
| `src/pages/terms.astro` | Create | Terms of service |

---

## Task 1: Project Scaffold

**Files:**
- Create: `package.json`
- Create: `tsconfig.json`
- Create: `astro.config.mjs`
- Create: `public/robots.txt`
- Create: `public/favicon.svg`

**Interfaces:**
- Produces: runnable `npm run dev` and `npm run build`

- [ ] **Step 1: Create `package.json`**

```json
{
  "name": "eco-home-guide",
  "type": "module",
  "version": "0.0.1",
  "engines": {
    "node": ">=22.12.0"
  },
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "postbuild": "npx pagefind --site dist",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "@tailwindcss/typography": "^0.5.20",
    "@tailwindcss/vite": "^4.3.1",
    "astro": "^6.4.7",
    "tailwindcss": "^4.3.1"
  },
  "devDependencies": {
    "@astrojs/sitemap": "^3.7.3",
    "pagefind": "^1.5.2",
    "sharp": "^0.35.1"
  }
}
```

- [ ] **Step 2: Create `tsconfig.json`**

```json
{
  "extends": "astro/tsconfigs/strict",
  "include": [".astro/types.d.ts", "**/*"],
  "exclude": ["dist"]
}
```

- [ ] **Step 3: Create `astro.config.mjs`** (rehype plugin import added in Task 4)

```js
// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://ecohomeguide.com',
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
  output: 'static',
});
```

- [ ] **Step 4: Create `public/robots.txt`**

```
User-agent: *
Allow: /

Sitemap: https://ecohomeguide.com/sitemap-index.xml
```

- [ ] **Step 5: Create `public/favicon.svg`** — a simple green leaf SVG

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none">
  <circle cx="16" cy="16" r="16" fill="#3D7A45"/>
  <path d="M16 6 C10 10 8 18 12 24 C14 20 18 16 24 14 C20 10 16 6 16 6Z" fill="#FAFDF7"/>
</svg>
```

- [ ] **Step 6: Install dependencies**

Run: `npm install`

Expected: `node_modules` created, no errors.

- [ ] **Step 7: Verify Astro CLI works**

Run: `npx astro info`

Expected: Astro version printed, no errors.

- [ ] **Step 8: Commit**

```bash
git init
git add package.json tsconfig.json astro.config.mjs public/robots.txt public/favicon.svg
git commit -m "feat: scaffold eco-home-guide project"
```

---

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

## Task 3: Content Schema

**Files:**
- Create: `src/content.config.ts`

**Interfaces:**
- Produces: `blog` collection with schema — `title`, `description`, `pubDate`, `updatedDate?`, `category`, `tags`, `image?`, `imageAlt?`, `draft`, `products?` array

- [ ] **Step 1: Create `src/content.config.ts`**

```typescript
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    category: z.string(),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
    imageAlt: z.string().optional(),
    draft: z.boolean().default(false),
    products: z.array(z.object({
      name: z.string(),
      description: z.string(),
      affiliateUrl: z.string(),
      image: z.string().optional(),
      badge: z.string().optional(),
      rating: z.number().min(1).max(5).optional(),
    })).optional(),
  }),
});

export const collections = { blog };
```

- [ ] **Step 2: Verify schema parses existing content**

Run: `npx astro check`

Expected: No type errors. (If the existing blog post has a `category` value not yet in `categories.ts`, that's fine — schema uses `z.string()`, not an enum.)

- [ ] **Step 3: Commit**

```bash
git add src/content.config.ts
git commit -m "feat: add content schema with products array"
```

---

## Task 4: rehype-callouts Plugin

**Files:**
- Create: `src/lib/rehype-callouts.ts`
- Modify: `astro.config.mjs`

**Interfaces:**
- Consumes: Astro markdown pipeline (blockquote AST nodes)
- Produces: `<div class="callout-pros">`, `<div class="callout-cons">`, `<div class="callout-eco">` HTML elements in rendered output; `.callout-*` CSS classes from Task 2 style them

- [ ] **Step 1: Create `src/lib/rehype-callouts.ts`**

```typescript
import type { Plugin } from 'unified';
import type { Root, Element, Text, Paragraph } from 'hast';
import { visit } from 'unist-util-visit';

const CALLOUT_TYPES = ['pros', 'cons', 'eco'] as const;
type CalloutType = typeof CALLOUT_TYPES[number];

function getCalloutType(node: Element): CalloutType | null {
  const firstChild = node.children[0];
  if (!firstChild || firstChild.type !== 'element') return null;

  const para = firstChild as Element;
  if (para.tagName !== 'p') return null;

  const textNode = para.children[0];
  if (!textNode || textNode.type !== 'text') return null;

  const text = (textNode as Text).value.trim();
  for (const type of CALLOUT_TYPES) {
    if (text === `[!${type}]`) return type;
  }
  return null;
}

export const rehypeCallouts: Plugin<[], Root> = () => {
  return (tree: Root) => {
    visit(tree, 'element', (node: Element, index, parent) => {
      if (node.tagName !== 'blockquote') return;
      if (index === undefined || !parent) return;

      const calloutType = getCalloutType(node);
      if (!calloutType) return;

      const remainingChildren = node.children.slice(1);

      const replacement: Element = {
        type: 'element',
        tagName: 'div',
        properties: { className: [`callout-${calloutType}`] },
        children: remainingChildren,
      };

      parent.children.splice(index, 1, replacement);
    });
  };
};
```

- [ ] **Step 2: Install `unist-util-visit` (required by the plugin)**

Run: `npm install unist-util-visit`

Expected: Package added to `node_modules`.

- [ ] **Step 3: Update `astro.config.mjs` to load the plugin**

Replace the entire file with:

```js
// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';
import { rehypeCallouts } from './src/lib/rehype-callouts.ts';

export default defineConfig({
  site: 'https://ecohomeguide.com',
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
  markdown: {
    rehypePlugins: [rehypeCallouts],
  },
  output: 'static',
});
```

- [ ] **Step 4: Verify no build error**

Run: `npx astro check`

Expected: No type errors.

- [ ] **Step 5: Commit**

```bash
git add src/lib/rehype-callouts.ts astro.config.mjs package.json package-lock.json
git commit -m "feat: add rehype-callouts plugin for pros/cons/eco blocks"
```

---

## Task 5: Base Components

**Files:**
- Create: `src/components/EcoBadge.astro`
- Create: `src/components/TableOfContents.astro`
- Create: `src/components/NewsletterForm.astro`
- Create: `src/components/Footer.astro`

**Interfaces:**
- `EcoBadge` consumes: `badge: string` prop
- `TableOfContents` consumes: `headings: { depth: number; slug: string; text: string }[]` prop
- `Footer` consumes: nothing (reads current year inline)

- [ ] **Step 1: Create `src/components/EcoBadge.astro`**

```astro
---
interface Props {
  badge: string;
}
const { badge } = Astro.props;
---

<span class="inline-block text-xs font-semibold px-2 py-0.5 rounded-full bg-green-100 text-green-800">
  {badge}
</span>
```

- [ ] **Step 2: Create `src/components/TableOfContents.astro`**

```astro
---
interface Heading {
  depth: number;
  slug: string;
  text: string;
}

interface Props {
  headings: Heading[];
}

const { headings } = Astro.props;
const filteredHeadings = headings.filter(h => h.depth <= 3);
---

<nav>
  <ul class="space-y-1 text-sm">
    {filteredHeadings.map(heading => (
      <li style={`padding-left: ${(heading.depth - 2) * 12}px`}>
        <a
          href={`#${heading.slug}`}
          class="block py-1 text-[var(--color-muted)] hover:text-[var(--color-accent)] transition-colors leading-snug"
        >
          {heading.text}
        </a>
      </li>
    ))}
  </ul>
</nav>
```

- [ ] **Step 3: Create `src/components/NewsletterForm.astro`**

```astro
---
---

<div class="bg-[var(--color-heading)] text-white rounded-2xl p-8 text-center">
  <h2 class="text-2xl font-bold mb-2">Live Greener, One Swap at a Time</h2>
  <p class="text-[var(--color-muted)] mb-6">Eco product picks, buying guides, and sustainable living tips — straight to your inbox.</p>
  <form class="flex gap-3 max-w-md mx-auto" onsubmit="return false;">
    <input
      type="email"
      placeholder="your@email.com"
      class="flex-1 px-4 py-3 rounded-lg bg-[#2A3B2A] border border-[var(--color-muted)] text-white placeholder-[var(--color-muted)] focus:outline-none focus:border-[var(--color-accent)]"
    />
    <button
      type="submit"
      class="px-6 py-3 bg-[var(--color-accent)] text-white font-semibold rounded-lg hover:opacity-90 transition-opacity"
    >
      Subscribe
    </button>
  </form>
  <p class="text-xs text-[var(--color-muted)] mt-3">Coming soon. Drop your email to be notified at launch.</p>
</div>
```

- [ ] **Step 4: Create `src/components/Footer.astro`**

```astro
---
const year = new Date().getFullYear();
---

<footer class="border-t border-[var(--color-border)] mt-20">
  <div class="max-w-7xl mx-auto px-4 py-10">
    <div class="flex flex-col md:flex-row justify-between items-center gap-4">
      <p class="text-sm text-[var(--color-muted)]">
        © {year} Eco Home Guide. All rights reserved.
      </p>
      <nav class="flex flex-wrap gap-6 text-sm text-[var(--color-muted)]">
        <a href="/about/" class="hover:text-[var(--color-accent)] transition-colors">About</a>
        <a href="/privacy-policy/" class="hover:text-[var(--color-accent)] transition-colors">Privacy Policy</a>
        <a href="/disclaimer/" class="hover:text-[var(--color-accent)] transition-colors">Disclaimer</a>
        <a href="/terms/" class="hover:text-[var(--color-accent)] transition-colors">Terms</a>
      </nav>
    </div>
  </div>
</footer>
```

- [ ] **Step 5: Commit**

```bash
git add src/components/EcoBadge.astro src/components/TableOfContents.astro src/components/NewsletterForm.astro src/components/Footer.astro
git commit -m "feat: add base components (EcoBadge, TOC, Newsletter, Footer)"
```

---

## Task 6: Header, ProductCard, PostCard

**Files:**
- Create: `src/components/Header.astro`
- Create: `src/components/ProductCard.astro`
- Create: `src/components/PostCard.astro`

**Interfaces:**
- `Header` consumes: `categories` from `src/data/categories.ts`
- `ProductCard` consumes props: `name: string`, `description: string`, `affiliateUrl: string`, `image?: string`, `badge?: string`, `rating?: number`
- `PostCard` consumes props: `title: string`, `description: string`, `slug: string`, `pubDate: Date`, `category: string`, `image?: string`, `imageAlt?: string`

- [ ] **Step 1: Create `src/components/Header.astro`**

```astro
---
import { categories } from '../data/categories';
---

<header class="border-b border-[var(--color-border)] bg-[var(--color-bg)] sticky top-0 z-50">
  <div class="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
    <a href="/" class="font-bold text-xl text-[var(--color-heading)] hover:text-[var(--color-accent)] transition-colors" style="font-family: 'Lora', serif;">
      Eco Home Guide
    </a>
    <nav class="hidden md:flex items-center gap-6">
      {categories.map(cat => (
        <a
          href={`/categories/${cat.slug}/`}
          class="text-sm font-medium text-[var(--color-muted)] hover:text-[var(--color-accent)] transition-colors"
        >
          {cat.name}
        </a>
      ))}
      <a
        href="/blog/"
        class="text-sm font-medium text-[var(--color-muted)] hover:text-[var(--color-accent)] transition-colors"
      >
        All Articles
      </a>
    </nav>
    <a
      href="/search/"
      class="text-[var(--color-muted)] hover:text-[var(--color-accent)] transition-colors"
      aria-label="Search"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35M17 11A6 6 0 1 1 5 11a6 6 0 0 1 12 0z" />
      </svg>
    </a>
  </div>
</header>
```

- [ ] **Step 2: Create `src/components/ProductCard.astro`**

```astro
---
import EcoBadge from './EcoBadge.astro';

interface Props {
  name: string;
  description: string;
  affiliateUrl: string;
  image?: string;
  badge?: string;
  rating?: number;
}

const { name, description, affiliateUrl, image, badge, rating } = Astro.props;
const stars = rating ? Array.from({ length: 5 }, (_, i) => i < rating) : null;
---

<div class="flex gap-4 border border-[var(--color-border)] rounded-xl p-4 bg-[var(--color-surface)] hover:shadow-sm transition-shadow border-l-4 border-l-[var(--color-accent)]">
  {image ? (
    <img src={image} alt={name} class="w-20 h-20 object-cover rounded-lg flex-shrink-0" loading="lazy" />
  ) : (
    <div class="w-20 h-20 bg-[var(--color-border)] rounded-lg flex-shrink-0 flex items-center justify-center text-[var(--color-muted)] text-xs">
      No image
    </div>
  )}
  <div class="flex-1 min-w-0">
    <div class="flex items-start justify-between gap-2 flex-wrap">
      <h3 class="font-semibold text-[var(--color-heading)]">{name}</h3>
      {badge && <EcoBadge badge={badge} />}
    </div>
    <p class="text-sm text-[var(--color-muted)] mt-1">{description}</p>
    <div class="flex items-center justify-between mt-3">
      {stars && (
        <div class="flex gap-0.5">
          {stars.map(filled => (
            <span class={filled ? 'text-[var(--color-accent-warm)]' : 'text-[var(--color-border)]'}>★</span>
          ))}
        </div>
      )}
      <a
        href={affiliateUrl}
        target="_blank"
        rel="noopener noreferrer nofollow"
        class="text-sm font-semibold text-white bg-[var(--color-accent)] px-4 py-1.5 rounded-lg hover:opacity-90 transition-opacity ml-auto"
      >
        View on Amazon →
      </a>
    </div>
  </div>
</div>
```

- [ ] **Step 3: Create `src/components/PostCard.astro`**

```astro
---
import { getCategoryBySlug } from '../data/categories';

interface Props {
  title: string;
  description: string;
  slug: string;
  pubDate: Date;
  category: string;
  image?: string;
  imageAlt?: string;
}

const { title, description, slug, pubDate, category, image, imageAlt } = Astro.props;
const categoryMeta = getCategoryBySlug(category);
const categoryLabel = categoryMeta?.name ?? category;
const readingTime = Math.ceil(description.split(' ').length / 200) + 5;
---

<article class="border border-[var(--color-border)] rounded-xl overflow-hidden hover:shadow-md transition-shadow bg-[var(--color-surface)]">
  {image && (
    <a href={`/blog/${slug}/`}>
      <img
        src={image}
        alt={imageAlt || title}
        class="w-full aspect-video object-cover"
        width="800"
        height="450"
        loading="lazy"
        decoding="async"
      />
    </a>
  )}
  <div class="p-6">
    <a
      href={`/categories/${category}/`}
      class="text-xs font-semibold text-[var(--color-accent)] uppercase tracking-wide hover:underline"
    >
      {categoryLabel}
    </a>
    <h2 class="mt-2 text-xl font-bold text-[var(--color-heading)] leading-snug" style="font-family: 'Lora', serif;">
      <a href={`/blog/${slug}/`} class="hover:text-[var(--color-accent)] transition-colors">
        {title}
      </a>
    </h2>
    <p class="mt-2 text-sm text-[var(--color-muted)] line-clamp-2">{description}</p>
    <div class="mt-4 flex items-center gap-3 text-xs text-[var(--color-muted)]">
      <time datetime={pubDate.toISOString()}>
        {pubDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}
      </time>
      <span>·</span>
      <span>{readingTime} min read</span>
    </div>
  </div>
</article>
```

- [ ] **Step 4: Commit**

```bash
git add src/components/Header.astro src/components/ProductCard.astro src/components/PostCard.astro
git commit -m "feat: add Header, ProductCard, PostCard components"
```

---

## Task 7: Layouts

**Files:**
- Create: `src/layouts/BaseLayout.astro`
- Create: `src/layouts/PostLayout.astro`

**Interfaces:**
- `BaseLayout` props: `title: string`, `description: string`, `image?: string`, `type?: 'website' | 'article'`, `pubDate?: Date`, `updatedDate?: Date`, `author?: string`
- `PostLayout` props: `post: CollectionEntry<'blog'>`, `headings: { depth: number; slug: string; text: string }[]`
- `PostLayout` consumes: `ProductCard` (Task 6), `TableOfContents` (Task 5), `BaseLayout`

- [ ] **Step 1: Create `src/layouts/BaseLayout.astro`**

```astro
---
import '../styles/global.css';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';

interface Props {
  title: string;
  description: string;
  image?: string;
  type?: 'website' | 'article';
  pubDate?: Date;
  updatedDate?: Date;
  author?: string;
}

const {
  title,
  description,
  image = '/og-default.png',
  type = 'website',
  pubDate,
  updatedDate,
  author = 'Eco Home Guide',
} = Astro.props;

const canonicalURL = new URL(Astro.url.pathname, Astro.site);
const imageURL = new URL(image, Astro.site);

const jsonLd = type === 'article' ? {
  '@context': 'https://schema.org',
  '@type': 'Article',
  headline: title,
  description: description,
  image: imageURL.href,
  author: { '@type': 'Person', name: author },
  publisher: {
    '@type': 'Organization',
    name: 'Eco Home Guide',
    logo: { '@type': 'ImageObject', url: new URL('/favicon.svg', Astro.site).href },
  },
  datePublished: pubDate?.toISOString(),
  dateModified: (updatedDate ?? pubDate)?.toISOString(),
  mainEntityOfPage: { '@type': 'WebPage', '@id': canonicalURL.href },
} : {
  '@context': 'https://schema.org',
  '@type': 'WebSite',
  name: 'Eco Home Guide',
  url: Astro.site?.href,
};
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <link rel="canonical" href={canonicalURL} />
    <meta name="generator" content={Astro.generator} />

    <title>{title}</title>
    <meta name="description" content={description} />
    <meta name="author" content={author} />

    <!-- Open Graph -->
    <meta property="og:type" content={type} />
    <meta property="og:url" content={canonicalURL} />
    <meta property="og:title" content={title} />
    <meta property="og:description" content={description} />
    <meta property="og:image" content={imageURL} />
    <meta property="og:site_name" content="Eco Home Guide" />
    {type === 'article' && pubDate && (
      <meta property="article:published_time" content={pubDate.toISOString()} />
    )}
    {type === 'article' && updatedDate && (
      <meta property="article:modified_time" content={updatedDate.toISOString()} />
    )}

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content={title} />
    <meta name="twitter:description" content={description} />
    <meta name="twitter:image" content={imageURL} />

    <!-- JSON-LD Structured Data -->
    <script type="application/ld+json" set:html={JSON.stringify(jsonLd)} />

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Lora:wght@400;600;700&display=swap" rel="stylesheet" />
  </head>
  <body class="min-h-screen flex flex-col">
    <Header />
    <main class="flex-1">
      <slot />
    </main>
    <Footer />
  </body>
</html>
```

- [ ] **Step 2: Create `src/layouts/PostLayout.astro`**

```astro
---
import BaseLayout from './BaseLayout.astro';
import TableOfContents from '../components/TableOfContents.astro';
import ProductCard from '../components/ProductCard.astro';
import { getCategoryBySlug } from '../data/categories';
import type { CollectionEntry } from 'astro:content';

interface Props {
  post: CollectionEntry<'blog'>;
  headings: { depth: number; slug: string; text: string }[];
}

const { post, headings } = Astro.props;
const { title, description, pubDate, updatedDate, category, image, imageAlt, products } = post.data;
const categoryMeta = getCategoryBySlug(category);
const categoryLabel = categoryMeta?.name ?? category;
---

<BaseLayout title={title} description={description} image={image} type="article" pubDate={pubDate} updatedDate={updatedDate}>
  <article class="max-w-7xl mx-auto px-4 py-12">
    <div class="lg:grid lg:grid-cols-[1fr_680px_1fr] lg:gap-8">

      <!-- Left spacer -->
      <div></div>

      <!-- Article body -->
      <div>
        <a
          href={`/categories/${category}/`}
          class="inline-block text-sm font-semibold text-[var(--color-accent)] uppercase tracking-wide mb-4 hover:underline"
        >
          {categoryLabel}
        </a>

        <h1 class="text-4xl font-bold text-[var(--color-heading)] leading-tight mb-4" style="font-family: 'Lora', serif;">{title}</h1>

        <div class="flex items-center gap-4 text-sm text-[var(--color-muted)] mb-8">
          <time datetime={pubDate.toISOString()}>
            {pubDate.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}
          </time>
          {updatedDate && (
            <span>· Updated {updatedDate.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}</span>
          )}
        </div>

        {image && (
          <img
            src={image}
            alt={imageAlt || title}
            class="w-full rounded-xl mb-10 aspect-video object-cover"
            width="1200"
            height="675"
            loading="eager"
            fetchpriority="high"
          />
        )}

        {headings.length > 0 && (
          <details class="lg:hidden border border-[var(--color-border)] rounded-lg p-4 mb-8">
            <summary class="font-semibold cursor-pointer">Table of Contents</summary>
            <TableOfContents headings={headings} />
          </details>
        )}

        <div class="prose prose-lg max-w-none
          prose-headings:text-[var(--color-heading)] prose-headings:font-bold
          prose-a:text-[var(--color-accent)] prose-a:no-underline hover:prose-a:underline
          prose-blockquote:not-italic">
          <slot />
        </div>

        {products && products.length > 0 && (
          <div class="mt-16 border-t border-[var(--color-border)] pt-10">
            <h2 class="text-xl font-bold mb-6" style="font-family: 'Lora', serif;">Recommended Products</h2>
            <div class="grid gap-4">
              {products.map(product => (
                <ProductCard
                  name={product.name}
                  description={product.description}
                  affiliateUrl={product.affiliateUrl}
                  image={product.image}
                  badge={product.badge}
                  rating={product.rating}
                />
              ))}
            </div>
          </div>
        )}
      </div>

      <!-- Right sidebar -->
      <div class="hidden lg:block">
        <div class="sticky top-8 space-y-8">
          {headings.length > 0 && (
            <div class="border border-[var(--color-border)] rounded-xl p-6">
              <h3 class="font-semibold text-sm uppercase tracking-wide text-[var(--color-muted)] mb-4">Table of Contents</h3>
              <TableOfContents headings={headings} />
            </div>
          )}
          <div class="border-2 border-dashed border-[var(--color-border)] rounded-xl p-6 text-center text-[var(--color-muted)] text-sm">
            Ad Placement
          </div>
        </div>
      </div>

    </div>
  </article>
</BaseLayout>
```

- [ ] **Step 3: Commit**

```bash
git add src/layouts/BaseLayout.astro src/layouts/PostLayout.astro
git commit -m "feat: add BaseLayout and PostLayout"
```

---

## Task 8: Pages — Core

**Files:**
- Create: `src/pages/index.astro`
- Create: `src/pages/blog/index.astro`
- Create: `src/pages/blog/[slug].astro`
- Create: `src/pages/categories/[category].astro`

**Interfaces:**
- All pages consume: `BaseLayout` (Task 7), `PostCard` (Task 6)
- `[slug].astro` consumes: `PostLayout` (Task 7)
- `[category].astro` consumes: `categories` from `src/data/categories.ts` (Task 2) for `getStaticPaths`

- [ ] **Step 1: Create `src/pages/index.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import PostCard from '../components/PostCard.astro';
import NewsletterForm from '../components/NewsletterForm.astro';
import { categories } from '../data/categories';
import { getCollection } from 'astro:content';

const allPosts = await getCollection('blog', ({ data }) => !data.draft);
const recentPosts = allPosts
  .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf())
  .slice(0, 6);
---

<BaseLayout
  title="Eco Home Guide — Sustainable Living, Bamboo Products & Green Home Essentials"
  description="Guides, reviews, and product picks for eco-conscious homeowners. Bamboo products, green kitchen essentials, sustainable decor, and everyday eco swaps."
>
  <section class="max-w-7xl mx-auto px-4 pt-20 pb-16 text-center">
    <h1 class="text-5xl md:text-6xl font-bold text-[var(--color-heading)] leading-tight mb-6" style="font-family: 'Lora', serif;">
      Live Greener.<br />
      <span class="text-[var(--color-accent)]">Shop Smarter.</span>
    </h1>
    <p class="text-xl text-[var(--color-muted)] max-w-2xl mx-auto mb-8">
      Honest guides and product picks for sustainable living — bamboo kitchenware, eco home decor, and everyday plastic-free swaps.
    </p>
    <a href="/blog/" class="inline-block px-8 py-4 bg-[var(--color-accent)] text-white font-bold rounded-xl hover:opacity-90 transition-opacity text-lg">
      Browse All Guides →
    </a>
  </section>

  <section class="max-w-7xl mx-auto px-4 py-12">
    <h2 class="text-2xl font-bold text-[var(--color-heading)] mb-8" style="font-family: 'Lora', serif;">Shop by Category</h2>
    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
      {categories.map(cat => (
        <a href={`/categories/${cat.slug}/`} class="border border-[var(--color-border)] rounded-xl p-6 hover:border-[var(--color-accent)] hover:shadow-md transition-all bg-[var(--color-surface)]">
          <div class="text-3xl mb-3">{cat.icon}</div>
          <h3 class="font-bold text-lg text-[var(--color-heading)]">{cat.name}</h3>
          <p class="text-sm text-[var(--color-muted)] mt-1">{cat.description}</p>
        </a>
      ))}
    </div>
  </section>

  <section class="max-w-7xl mx-auto px-4 py-12">
    <h2 class="text-2xl font-bold text-[var(--color-heading)] mb-8" style="font-family: 'Lora', serif;">Latest Guides</h2>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
      {recentPosts.map(post => (
        <PostCard
          title={post.data.title}
          description={post.data.description}
          slug={post.id}
          pubDate={post.data.pubDate}
          category={post.data.category}
          image={post.data.image}
          imageAlt={post.data.imageAlt}
        />
      ))}
    </div>
  </section>

  <section class="max-w-3xl mx-auto px-4 py-16">
    <NewsletterForm />
  </section>
</BaseLayout>
```

- [ ] **Step 2: Create `src/pages/blog/index.astro`**

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import PostCard from '../../components/PostCard.astro';
import { getCollection } from 'astro:content';

const allPosts = await getCollection('blog', ({ data }) => !data.draft);
const posts = allPosts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
---

<BaseLayout
  title="All Guides — Eco Home Guide"
  description="Browse all sustainable living guides, product reviews, and eco buying guides from Eco Home Guide."
>
  <div class="max-w-7xl mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold text-[var(--color-heading)] mb-4" style="font-family: 'Lora', serif;">All Guides</h1>
    <p class="text-[var(--color-muted)] mb-10">{posts.length} guides published</p>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
      {posts.map(post => (
        <PostCard
          title={post.data.title}
          description={post.data.description}
          slug={post.id}
          pubDate={post.data.pubDate}
          category={post.data.category}
          image={post.data.image}
          imageAlt={post.data.imageAlt}
        />
      ))}
    </div>
  </div>
</BaseLayout>
```

- [ ] **Step 3: Create `src/pages/blog/[slug].astro`**

```astro
---
import { getCollection, render } from 'astro:content';
import PostLayout from '../../layouts/PostLayout.astro';

export async function getStaticPaths() {
  const posts = await getCollection('blog', ({ data }) => !data.draft);
  return posts.map(post => ({
    params: { slug: post.id },
    props: { post },
  }));
}

const { post } = Astro.props;
const { Content, headings } = await render(post);
---

<PostLayout post={post} headings={headings}>
  <Content />
</PostLayout>
```

- [ ] **Step 4: Create `src/pages/categories/[category].astro`**

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import PostCard from '../../components/PostCard.astro';
import { categories, getCategoryBySlug } from '../../data/categories';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  return categories.map(cat => ({ params: { category: cat.slug } }));
}

const { category } = Astro.params;
const meta = getCategoryBySlug(category!);

const allPosts = await getCollection('blog', ({ data }) => !data.draft && data.category === category);
const posts = allPosts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
---

<BaseLayout
  title={`${meta?.name ?? category} — Eco Home Guide`}
  description={meta?.description ?? `Browse ${category} guides on Eco Home Guide.`}
>
  <div class="max-w-7xl mx-auto px-4 py-12">
    <div class="flex items-center gap-3 mb-3">
      {meta?.icon && <span class="text-4xl">{meta.icon}</span>}
      <h1 class="text-4xl font-bold text-[var(--color-heading)]" style="font-family: 'Lora', serif;">{meta?.name ?? category}</h1>
    </div>
    <p class="text-[var(--color-muted)] max-w-2xl mb-10">{meta?.description}</p>
    {posts.length === 0 ? (
      <p class="text-[var(--color-muted)]">No guides yet. Check back soon!</p>
    ) : (
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        {posts.map(post => (
          <PostCard
            title={post.data.title}
            description={post.data.description}
            slug={post.id}
            pubDate={post.data.pubDate}
            category={post.data.category}
            image={post.data.image}
            imageAlt={post.data.imageAlt}
          />
        ))}
      </div>
    )}
  </div>
</BaseLayout>
```

- [ ] **Step 5: Verify dev server renders the existing blog post**

Run: `npm run dev`

Open `http://localhost:4321/blog/best-bamboo-products-2026-kitchen-home-decor-and-daily-essentials-affiliate-buyi/`

Expected: Article renders with Eco Home Guide header, green palette, Lora font headings.

- [ ] **Step 6: Commit**

```bash
git add src/pages/index.astro src/pages/blog/index.astro "src/pages/blog/[slug].astro" "src/pages/categories/[category].astro"
git commit -m "feat: add core pages (index, blog, slug, categories)"
```

---

## Task 9: Search & Legal Pages

**Files:**
- Create: `src/pages/search.astro`
- Create: `src/pages/about.astro`
- Create: `src/pages/privacy-policy.astro`
- Create: `src/pages/disclaimer.astro`
- Create: `src/pages/terms.astro`

**Interfaces:**
- All consume: `BaseLayout` (Task 7)

- [ ] **Step 1: Create `src/pages/search.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout
  title="Search — Eco Home Guide"
  description="Search all eco product guides, sustainable living articles, and buying guides on Eco Home Guide."
>
  <div class="max-w-3xl mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold text-[var(--color-heading)] mb-8" style="font-family: 'Lora', serif;">Search</h1>
    <div id="search"></div>
  </div>
</BaseLayout>

<link rel="stylesheet" href="/pagefind/pagefind-ui.css" />
<script src="/pagefind/pagefind-ui.js" is:inline></script>
<script is:inline>
  window.addEventListener('DOMContentLoaded', () => {
    new PagefindUI({
      element: '#search',
      showSubResults: true,
      highlightParam: 'highlight',
    });
  });
</script>
```

- [ ] **Step 2: Create `src/pages/about.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout
  title="About — Eco Home Guide"
  description="Eco Home Guide helps conscious consumers find the best sustainable home products — bamboo kitchenware, eco decor, and plastic-free daily essentials."
>
  <div class="max-w-2xl mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold text-[var(--color-heading)] mb-6" style="font-family: 'Lora', serif;">About Eco Home Guide</h1>
    <div class="prose prose-lg max-w-none prose-a:text-[var(--color-accent)]">
      <p>
        Eco Home Guide exists for one reason: making sustainable shopping easier. There are thousands of "eco-friendly" products out there — and most of them aren't worth the premium.
      </p>
      <p>
        We dig into the materials, certifications, and real-world usability so you can make confident choices for your home without spending hours on research.
      </p>
      <h2>What We Cover</h2>
      <ul>
        <li><strong>Bamboo Products</strong> — kitchenware, decor, and daily essentials from a genuinely renewable resource</li>
        <li><strong>Eco Kitchen</strong> — cookware, storage, and utensils that reduce waste without sacrificing quality</li>
        <li><strong>Home Decor</strong> — sustainable pieces that look good and last</li>
        <li><strong>Daily Essentials</strong> — plastic-free swaps for toothbrushes, bottles, packaging, and more</li>
      </ul>
      <h2>Our Approach</h2>
      <p>
        Every recommendation on this site comes with a clear explanation of why we think it's worth your money — materials, certifications, durability, and honest trade-offs included.
      </p>
      <p>
        We participate in affiliate programs including Amazon Associates. See our <a href="/disclaimer/">Disclaimer</a> for full disclosure.
      </p>
    </div>
  </div>
</BaseLayout>
```

- [ ] **Step 3: Create `src/pages/privacy-policy.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
const domain = 'ecohomeguide.com';
const email = 'hello@ecohomeguide.com';
---

<BaseLayout title="Privacy Policy — Eco Home Guide" description="Privacy policy for Eco Home Guide.">
  <div class="max-w-2xl mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold text-[var(--color-heading)] mb-8" style="font-family: 'Lora', serif;">Privacy Policy</h1>
    <div class="prose prose-lg max-w-none">
      <p><em>Last updated: June 17, 2026</em></p>
      <p>This Privacy Policy describes how Eco Home Guide ("{domain}") collects, uses, and shares information when you visit our website.</p>
      <h2>Information We Collect</h2>
      <p>We collect information you voluntarily provide (such as your email address if you subscribe to our newsletter) and information automatically collected when you visit our site, including IP address, browser type, pages viewed, and time spent on pages via analytics tools.</p>
      <h2>Cookies</h2>
      <p>We use cookies for analytics and advertising purposes. You can control cookie settings through your browser. By using this site, you consent to our use of cookies.</p>
      <h2>Google AdSense</h2>
      <p>We use Google AdSense to display ads. Google may use cookies to serve ads based on your prior visits to this or other websites. You can opt out at <a href="https://www.google.com/settings/ads">google.com/settings/ads</a>.</p>
      <h2>Affiliate Links</h2>
      <p>This site contains affiliate links. See our <a href="/disclaimer/">Disclaimer</a> for details.</p>
      <h2>Third-Party Services</h2>
      <p>We may use third-party services including Google Analytics, Google AdSense, and email marketing platforms. These services have their own privacy policies.</p>
      <h2>Your Rights (GDPR / CCPA)</h2>
      <p>You have the right to access, correct, or delete your personal data. To exercise these rights, contact us at {email}.</p>
      <h2>Contact</h2>
      <p>Questions? Email us at <a href={`mailto:${email}`}>{email}</a>.</p>
    </div>
  </div>
</BaseLayout>
```

- [ ] **Step 4: Create `src/pages/disclaimer.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="Disclaimer — Eco Home Guide" description="Affiliate and earnings disclaimer for Eco Home Guide.">
  <div class="max-w-2xl mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold text-[var(--color-heading)] mb-8" style="font-family: 'Lora', serif;">Disclaimer</h1>
    <div class="prose prose-lg max-w-none">
      <p><em>Last updated: June 17, 2026</em></p>
      <h2>Affiliate Disclosure</h2>
      <p>Eco Home Guide participates in affiliate marketing programs, including the Amazon Associates Program. This means we may earn a commission when you click on links to products and make a purchase — at no additional cost to you.</p>
      <p>We only recommend products we have researched thoroughly. Our editorial opinions are not influenced by affiliate relationships.</p>
      <h2>Amazon Associates Disclosure</h2>
      <p>As an Amazon Associate, I earn from qualifying purchases. Product prices and availability are accurate as of the date/time indicated and are subject to change.</p>
      <h2>Accuracy</h2>
      <p>We strive for accuracy in all product information, certifications, and environmental claims. Always verify certifications directly with the manufacturer before purchasing.</p>
    </div>
  </div>
</BaseLayout>
```

- [ ] **Step 5: Create `src/pages/terms.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
const email = 'hello@ecohomeguide.com';
---

<BaseLayout title="Terms of Service — Eco Home Guide" description="Terms of service for Eco Home Guide.">
  <div class="max-w-2xl mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold text-[var(--color-heading)] mb-8" style="font-family: 'Lora', serif;">Terms of Service</h1>
    <div class="prose prose-lg max-w-none">
      <p><em>Last updated: June 17, 2026</em></p>
      <h2>Use of This Site</h2>
      <p>By accessing Eco Home Guide, you agree to these terms. You may use this site for personal, non-commercial purposes only.</p>
      <h2>Intellectual Property</h2>
      <p>All content on this site — including text, images, and guides — is owned by Eco Home Guide unless otherwise noted. You may not reproduce or republish content without written permission.</p>
      <h2>User Conduct</h2>
      <p>You agree not to use this site to distribute spam, malware, or illegal content.</p>
      <h2>Limitation of Liability</h2>
      <p>Eco Home Guide is provided "as is." We are not liable for any damages arising from your use of this site.</p>
      <h2>Changes</h2>
      <p>We reserve the right to modify these terms at any time. Continued use of the site constitutes acceptance of the updated terms.</p>
      <h2>Contact</h2>
      <p>Questions? Email <a href={`mailto:${email}`}>{email}</a>.</p>
    </div>
  </div>
</BaseLayout>
```

- [ ] **Step 6: Commit**

```bash
git add src/pages/search.astro src/pages/about.astro src/pages/privacy-policy.astro src/pages/disclaimer.astro src/pages/terms.astro
git commit -m "feat: add search and legal pages"
```

---

## Task 10: Build Verification

**Files:**
- No new files — verification only

**Interfaces:**
- Consumes: all prior tasks

- [ ] **Step 1: Run full build**

Run: `npm run build`

Expected: Build completes with no errors. `dist/` created. pagefind index generated in `dist/pagefind/`.

- [ ] **Step 2: Check for "DIY Maker Station" strings**

Run: `grep -r "DIY Maker Station" src/ --include="*.astro" --include="*.ts" --include="*.css"`

Expected: No output (zero matches).

- [ ] **Step 3: Check type safety**

Run: `npx astro check`

Expected: No type errors.

- [ ] **Step 4: Preview build**

Run: `npm run preview`

Open `http://localhost:4321/` and verify:
- Homepage loads with green palette
- Category grid shows all 4 categories
- "Latest Guides" section shows the bamboo article
- Header shows "Eco Home Guide" brand name
- `/blog/best-bamboo-products-2026.../` renders with Lora headings and green accent links
- `/search/` loads pagefind UI

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "feat: complete eco-home-guide initial build"
```

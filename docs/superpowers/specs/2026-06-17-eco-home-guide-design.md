# Eco Home Guide — Site Design Spec

**Date:** 2026-06-17  
**Status:** Approved

---

## 1. Overview

Eco Home Guide is an affiliate content site targeting sustainable-living consumers. It covers bamboo products, eco-friendly kitchenware, home decor, and daily essentials. Monetization is via Amazon affiliate commissions and eco-brand advertising.

Built with Astro 6 + Tailwind 4, modeled on the diy-maker-station codebase with all branding, naming, and domain-specific details replaced.

---

## 2. Architecture

```
src/
  components/
    Header.astro            # reads categories from data/categories.ts
    Footer.astro
    PostCard.astro          # article card for index/list pages
    ProductCard.astro       # product recommendation card (frontmatter-driven)
    EcoBadge.astro          # eco certification pill label used inside ProductCard
    NewsletterForm.astro
    TableOfContents.astro
  data/
    categories.ts           # single source of truth for all category config
  lib/
    rehype-callouts.ts      # rehype plugin: [!pros]/[!cons]/[!eco] → HTML blocks
  content/
    blog/                   # pipeline writes .md files here
  content.config.ts
  layouts/
    BaseLayout.astro        # SEO, OG, JSON-LD, fonts
    PostLayout.astro        # article layout with sidebar TOC + product section
  pages/
    index.astro
    blog/index.astro
    blog/[slug].astro
    categories/[category].astro
    search.astro            # pagefind full-text search
    about.astro
    privacy-policy.astro
    disclaimer.astro
    terms.astro
  styles/
    global.css
```

---

## 3. Content Schema

`src/content.config.ts` — blog collection:

```typescript
z.object({
  title: z.string(),
  description: z.string(),
  pubDate: z.coerce.date(),
  updatedDate: z.coerce.date().optional(),
  category: z.string(),          // must match a slug in categories.ts
  tags: z.array(z.string()).default([]),
  image: z.string().optional(),
  imageAlt: z.string().optional(),
  draft: z.boolean().default(false),

  products: z.array(z.object({
    name: z.string(),
    description: z.string(),
    affiliateUrl: z.string(),
    image: z.string().optional(),
    badge: z.string().optional(),   // e.g. "FSC Certified", "GOTS Organic"
    rating: z.number().min(1).max(5).optional(),
  })).optional(),

})
```

---

## 4. Categories Configuration

`src/data/categories.ts` — single source of truth read by Header, index page, PostCard, and category pages:

```typescript
export const categories = [
  { slug: 'bamboo',   name: 'Bamboo Products',  icon: '🎋', description: 'Kitchenware, decor, and daily essentials made from fast-growing bamboo.' },
  { slug: 'kitchen',  name: 'Kitchen',          icon: '🍳', description: 'Eco-friendly cookware, utensils, and storage for a greener kitchen.' },
  { slug: 'home-decor', name: 'Home Decor',     icon: '🏡', description: 'Sustainable decor that looks good and does good.' },
  { slug: 'daily',    name: 'Daily Essentials', icon: '🌿', description: 'Swaps for everyday plastic items — toothbrushes, bottles, paper.' },
];
```

Pipeline adds new categories by extending this array; Header and all downstream consumers update automatically.

---

## 5. UI & Visual Design

### Color Palette

```css
:root {
  --color-bg: #FAFDF7;          /* near-white with green tint */
  --color-heading: #1A2E1A;     /* deep forest green */
  --color-accent: #3D7A45;      /* primary green — CTAs, links, labels */
  --color-accent-warm: #C17C3A; /* warm brown — secondary emphasis, star ratings */
  --color-muted: #6B7F6B;       /* grey-green — supporting text */
  --color-border: #D4E6D4;      /* light green border */
  --color-surface: #FFFFFF;     /* card backgrounds */
}
```

### Typography

- **Headings:** `Lora` (serif) — warm, editorial quality
- **Body:** `Inter` (sans-serif) — clean, readable

### Component Styles

**ProductCard**
- White surface, green left-border accent stripe
- `EcoBadge` pill labels: `bg-green-100 text-green-800`, small rounded pill
- Buy button: `--color-accent` green
- Fields rendered: image, name, description, badge(s), star rating, affiliate CTA

**ProsConsBlock** (`.callout-pros` / `.callout-cons` CSS classes, injected by rehype)
- Pros: light green background, checkmark icon per item
- Cons: warm brown/amber background, × icon per item
- Styles defined in `global.css` `@layer components`

**EcoInfoBlock** (`.callout-eco` CSS class, injected by rehype)
- Leaf icon + sage-green background
- Used for "Why choose eco alternatives" callouts
- Styles defined in `global.css` `@layer components`

**PostCard**
- White card, rounded corners, category label in accent green
- Image (aspect-video), title, description excerpt, date + reading time

**Header**
- Sticky, `--color-bg` background
- Brand name left, category nav links center/right, search icon
- Category links pulled from `categories.ts`

---

## 6. rehype-callouts Plugin

File: `src/lib/rehype-callouts.ts`

Recognizes blockquote nodes whose first paragraph text starts with `[!pros]`, `[!cons]`, or `[!eco]`. Replaces the blockquote with a `<div class="callout-{type}">` containing the remaining content (marker line removed).

**Supported syntax:**

```markdown
> [!pros]
> - Biodegradable, no plastic waste
> - Extremely fast-growing, renewable

> [!cons]
> - Slightly higher price than conventional alternatives
> - Some items require hand-washing

> [!eco]
> Bamboo absorbs up to 12 tonnes of CO₂ per year — 35% more than equivalent tree coverage.
```

Styles for `.callout-pros`, `.callout-cons`, `.callout-eco` are defined in `global.css` via `@layer components`, applied inside the `prose` context in PostLayout.

---

## 7. PostLayout

Three-column layout (mirrors diy-maker-station):

- **Left:** empty spacer
- **Center (680px):** article content — category label, h1, date, hero image, mobile TOC (details/summary), prose body
- **Right sidebar:** sticky TOC (desktop), ad placement placeholder

Below the article body:
- If `products` frontmatter array is present → render each item as `<ProductCard>`
- Section heading: "Recommended Products"

---

## 8. BaseLayout SEO

- `<title>`, `<meta name="description">`
- Open Graph tags (type, url, title, description, image, site_name)
- Twitter Card tags
- JSON-LD structured data:
  - `WebSite` schema for non-article pages
  - `Article` schema for posts (headline, description, image, author, publisher, datePublished, dateModified)
- `<link rel="canonical">`
- Google Fonts preconnect + stylesheet link

---

## 9. Search

pagefind full-text search, identical to diy-maker-station setup:
- `postbuild` script: `npx pagefind --site dist`
- `src/pages/search.astro` renders the pagefind UI widget

---

## 10. Pages

| Page | Notes |
|---|---|
| `/` | Hero section, category grid (from `categories.ts`), latest 6 posts, newsletter form |
| `/blog/` | All published posts, sorted by date |
| `/blog/[slug]/` | PostLayout |
| `/categories/[category]/` | Filtered posts by category slug |
| `/search/` | pagefind search UI |
| `/about/` | Site mission, eco focus |
| `/privacy-policy/` | Standard |
| `/disclaimer/` | Affiliate disclosure |
| `/terms/` | Standard |

---

## 11. Package Dependencies

Same as diy-maker-station:

```json
{
  "dependencies": {
    "astro": "^6.x",
    "tailwindcss": "^4.x",
    "@tailwindcss/typography": "^0.5.x",
    "@tailwindcss/vite": "^4.x"
  },
  "devDependencies": {
    "@astrojs/sitemap": "^3.x",
    "pagefind": "^1.x",
    "sharp": "^0.35.x"
  }
}
```

---

## 12. Naming Conventions

All component names, variable names, JSON-LD publisher names, and UI copy must use "Eco Home Guide" — no "DIY Maker Station" strings anywhere in the codebase.

Site name: **Eco Home Guide**  
Author default: **Eco Home Guide**  
OG site_name: **Eco Home Guide**

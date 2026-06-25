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


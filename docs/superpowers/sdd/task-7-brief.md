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


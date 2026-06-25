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


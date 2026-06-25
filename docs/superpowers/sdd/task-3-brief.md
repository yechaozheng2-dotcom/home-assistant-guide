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


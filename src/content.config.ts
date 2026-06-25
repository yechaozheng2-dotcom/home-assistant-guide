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
      description: z.string().optional(),
      asin: z.string().optional(),
      affiliateUrl: z.string().optional(),
      image: z.string().optional(),
      badge: z.string().optional(),
      rating: z.number().min(1).max(5).optional(),
    })).optional(),
  }),
});

export const collections = { blog };

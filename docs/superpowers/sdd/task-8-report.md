# Task 8 Report: Core Pages

**Status:** DONE_WITH_CONCERNS  
**Commit:** 2ac5f38  
**Verification:** All 4 pages created verbatim from brief; `npx astro check` shows 0 errors in any `src/pages/` file.

## Concerns

1. **Pre-existing build failure:** `npm run build` fails with `@tailwindcss/vite: Missing field 'tsconfigPaths'` — this was already failing before Task 8 changes (confirmed by checking git stash). The dev server (`npm run dev`) uses a different Vite pipeline and is expected to work. This is a dependency version incompatibility between `@tailwindcss/vite ^4.3.1` and the version of `rolldown`/`vite` in use.

2. **Pre-existing TS error:** `astro.config.mjs` has a `Plugin<any>[]` type mismatch error (pre-existing, in astro config, not in page files).

## What was done

- Created `src/pages/index.astro` — hero section, 4-column category grid (lg), latest 6 posts grid, NewsletterForm
- Created `src/pages/blog/index.astro` — all posts sorted by pubDate desc, post count display
- Created `src/pages/blog/[slug].astro` — `getStaticPaths` maps blog collection, `render()` extracts Content + headings, passes to PostLayout
- Created `src/pages/categories/[category].astro` — `getStaticPaths` from `categories` array, filters posts by category, empty-state message
- All color values use `var(--color-*)` tokens only — no hardcoded hex
- All pages match brief verbatim

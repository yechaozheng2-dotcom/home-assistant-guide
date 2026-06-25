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


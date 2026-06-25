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


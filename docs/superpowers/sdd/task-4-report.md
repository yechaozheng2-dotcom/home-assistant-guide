## Task 4 Report: rehype-callouts Plugin

**Status:** DONE_WITH_CONCERNS

**Commit hash:** 1e6a8c8

**Verification summary:** Plugin created and wired into astro.config.mjs; `npx astro check` passes with 0 new errors introduced by this task (1 pre-existing error on tailwindcss vite plugin line, confirmed present before this task).

**What was done:**
1. Created `src/lib/rehype-callouts.ts` with exact content from brief — visits blockquote hast nodes, detects `[!pros]`/`[!cons]`/`[!eco]` marker paragraphs, replaces blockquote with `<div class="callout-{type}">` keeping remaining children.
2. Confirmed `unist-util-visit@^5.1.0` was already in `package.json` (ran `npm install` which confirmed "up to date").
3. Updated `astro.config.mjs` to import `rehypeCallouts` from `./src/lib/rehype-callouts.ts` and add `markdown: { rehypePlugins: [rehypeCallouts] }`.
4. Committed: `git add src/lib/rehype-callouts.ts astro.config.mjs package.json package-lock.json`.

**Concerns:**
1. **Pre-existing type error (not introduced here):** `npx astro check` reports `ts(2322)` on `astro.config.mjs:11` (`plugins: [tailwindcss()]`) — a rolldown vs rollup type mismatch between the project's vite version and Astro's bundled vite. This error existed before Task 4; verified by stashing changes and re-running the check.
2. **Deprecation warning:** Astro logs `markdown.rehypePlugins is deprecated — pass to unified({...}) from @astrojs/markdown-remark directly instead`. The brief specifies this exact API, so it was followed verbatim. This is a runtime warning, not a type error, and does not break the build.

## Task 10: Build Verification

**Files:**
- No new files — verification only

**Interfaces:**
- Consumes: all prior tasks

- [ ] **Step 1: Run full build**

Run: `npm run build`

Expected: Build completes with no errors. `dist/` created. pagefind index generated in `dist/pagefind/`.

- [ ] **Step 2: Check for "DIY Maker Station" strings**

Run: `grep -r "DIY Maker Station" src/ --include="*.astro" --include="*.ts" --include="*.css"`

Expected: No output (zero matches).

- [ ] **Step 3: Check type safety**

Run: `npx astro check`

Expected: No type errors.

- [ ] **Step 4: Preview build**

Run: `npm run preview`

Open `http://localhost:4321/` and verify:
- Homepage loads with green palette
- Category grid shows all 4 categories
- "Latest Guides" section shows the bamboo article
- Header shows "Eco Home Guide" brand name
- `/blog/best-bamboo-products-2026.../` renders with Lora headings and green accent links
- `/search/` loads pagefind UI

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "feat: complete eco-home-guide initial build"
```

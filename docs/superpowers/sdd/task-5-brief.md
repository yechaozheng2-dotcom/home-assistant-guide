## Task 5: Base Components

**Files:**
- Create: `src/components/EcoBadge.astro`
- Create: `src/components/TableOfContents.astro`
- Create: `src/components/NewsletterForm.astro`
- Create: `src/components/Footer.astro`

**Interfaces:**
- `EcoBadge` consumes: `badge: string` prop
- `TableOfContents` consumes: `headings: { depth: number; slug: string; text: string }[]` prop
- `Footer` consumes: nothing (reads current year inline)

- [ ] **Step 1: Create `src/components/EcoBadge.astro`**

```astro
---
interface Props {
  badge: string;
}
const { badge } = Astro.props;
---

<span class="inline-block text-xs font-semibold px-2 py-0.5 rounded-full bg-green-100 text-green-800">
  {badge}
</span>
```

- [ ] **Step 2: Create `src/components/TableOfContents.astro`**

```astro
---
interface Heading {
  depth: number;
  slug: string;
  text: string;
}

interface Props {
  headings: Heading[];
}

const { headings } = Astro.props;
const filteredHeadings = headings.filter(h => h.depth <= 3);
---

<nav>
  <ul class="space-y-1 text-sm">
    {filteredHeadings.map(heading => (
      <li style={`padding-left: ${(heading.depth - 2) * 12}px`}>
        <a
          href={`#${heading.slug}`}
          class="block py-1 text-[var(--color-muted)] hover:text-[var(--color-accent)] transition-colors leading-snug"
        >
          {heading.text}
        </a>
      </li>
    ))}
  </ul>
</nav>
```

- [ ] **Step 3: Create `src/components/NewsletterForm.astro`**

```astro
---
---

<div class="bg-[var(--color-heading)] text-white rounded-2xl p-8 text-center">
  <h2 class="text-2xl font-bold mb-2">Live Greener, One Swap at a Time</h2>
  <p class="text-[var(--color-muted)] mb-6">Eco product picks, buying guides, and sustainable living tips — straight to your inbox.</p>
  <form class="flex gap-3 max-w-md mx-auto" onsubmit="return false;">
    <input
      type="email"
      placeholder="your@email.com"
      class="flex-1 px-4 py-3 rounded-lg bg-[#2A3B2A] border border-[var(--color-muted)] text-white placeholder-[var(--color-muted)] focus:outline-none focus:border-[var(--color-accent)]"
    />
    <button
      type="submit"
      class="px-6 py-3 bg-[var(--color-accent)] text-white font-semibold rounded-lg hover:opacity-90 transition-opacity"
    >
      Subscribe
    </button>
  </form>
  <p class="text-xs text-[var(--color-muted)] mt-3">Coming soon. Drop your email to be notified at launch.</p>
</div>
```

- [ ] **Step 4: Create `src/components/Footer.astro`**

```astro
---
const year = new Date().getFullYear();
---

<footer class="border-t border-[var(--color-border)] mt-20">
  <div class="max-w-7xl mx-auto px-4 py-10">
    <div class="flex flex-col md:flex-row justify-between items-center gap-4">
      <p class="text-sm text-[var(--color-muted)]">
        © {year} Eco Home Guide. All rights reserved.
      </p>
      <nav class="flex flex-wrap gap-6 text-sm text-[var(--color-muted)]">
        <a href="/about/" class="hover:text-[var(--color-accent)] transition-colors">About</a>
        <a href="/privacy-policy/" class="hover:text-[var(--color-accent)] transition-colors">Privacy Policy</a>
        <a href="/disclaimer/" class="hover:text-[var(--color-accent)] transition-colors">Disclaimer</a>
        <a href="/terms/" class="hover:text-[var(--color-accent)] transition-colors">Terms</a>
      </nav>
    </div>
  </div>
</footer>
```

- [ ] **Step 5: Commit**

```bash
git add src/components/EcoBadge.astro src/components/TableOfContents.astro src/components/NewsletterForm.astro src/components/Footer.astro
git commit -m "feat: add base components (EcoBadge, TOC, Newsletter, Footer)"
```

---


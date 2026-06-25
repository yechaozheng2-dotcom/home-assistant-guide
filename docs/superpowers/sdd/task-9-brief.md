## Task 9: Search & Legal Pages

**Files:**
- Create: `src/pages/search.astro`
- Create: `src/pages/about.astro`
- Create: `src/pages/privacy-policy.astro`
- Create: `src/pages/disclaimer.astro`
- Create: `src/pages/terms.astro`

**Interfaces:**
- All consume: `BaseLayout` (Task 7)

- [ ] **Step 1: Create `src/pages/search.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout
  title="Search — Eco Home Guide"
  description="Search all eco product guides, sustainable living articles, and buying guides on Eco Home Guide."
>
  <div class="max-w-3xl mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold text-[var(--color-heading)] mb-8" style="font-family: 'Lora', serif;">Search</h1>
    <div id="search"></div>
  </div>
</BaseLayout>

<link rel="stylesheet" href="/pagefind/pagefind-ui.css" />
<script src="/pagefind/pagefind-ui.js" is:inline></script>
<script is:inline>
  window.addEventListener('DOMContentLoaded', () => {
    new PagefindUI({
      element: '#search',
      showSubResults: true,
      highlightParam: 'highlight',
    });
  });
</script>
```

- [ ] **Step 2: Create `src/pages/about.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout
  title="About — Eco Home Guide"
  description="Eco Home Guide helps conscious consumers find the best sustainable home products — bamboo kitchenware, eco decor, and plastic-free daily essentials."
>
  <div class="max-w-2xl mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold text-[var(--color-heading)] mb-6" style="font-family: 'Lora', serif;">About Eco Home Guide</h1>
    <div class="prose prose-lg max-w-none prose-a:text-[var(--color-accent)]">
      <p>
        Eco Home Guide exists for one reason: making sustainable shopping easier. There are thousands of "eco-friendly" products out there — and most of them aren't worth the premium.
      </p>
      <p>
        We dig into the materials, certifications, and real-world usability so you can make confident choices for your home without spending hours on research.
      </p>
      <h2>What We Cover</h2>
      <ul>
        <li><strong>Bamboo Products</strong> — kitchenware, decor, and daily essentials from a genuinely renewable resource</li>
        <li><strong>Eco Kitchen</strong> — cookware, storage, and utensils that reduce waste without sacrificing quality</li>
        <li><strong>Home Decor</strong> — sustainable pieces that look good and last</li>
        <li><strong>Daily Essentials</strong> — plastic-free swaps for toothbrushes, bottles, packaging, and more</li>
      </ul>
      <h2>Our Approach</h2>
      <p>
        Every recommendation on this site comes with a clear explanation of why we think it's worth your money — materials, certifications, durability, and honest trade-offs included.
      </p>
      <p>
        We participate in affiliate programs including Amazon Associates. See our <a href="/disclaimer/">Disclaimer</a> for full disclosure.
      </p>
    </div>
  </div>
</BaseLayout>
```

- [ ] **Step 3: Create `src/pages/privacy-policy.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
const domain = 'ecohomeguide.com';
const email = 'hello@ecohomeguide.com';
---

<BaseLayout title="Privacy Policy — Eco Home Guide" description="Privacy policy for Eco Home Guide.">
  <div class="max-w-2xl mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold text-[var(--color-heading)] mb-8" style="font-family: 'Lora', serif;">Privacy Policy</h1>
    <div class="prose prose-lg max-w-none">
      <p><em>Last updated: June 17, 2026</em></p>
      <p>This Privacy Policy describes how Eco Home Guide ("{domain}") collects, uses, and shares information when you visit our website.</p>
      <h2>Information We Collect</h2>
      <p>We collect information you voluntarily provide (such as your email address if you subscribe to our newsletter) and information automatically collected when you visit our site, including IP address, browser type, pages viewed, and time spent on pages via analytics tools.</p>
      <h2>Cookies</h2>
      <p>We use cookies for analytics and advertising purposes. You can control cookie settings through your browser. By using this site, you consent to our use of cookies.</p>
      <h2>Google AdSense</h2>
      <p>We use Google AdSense to display ads. Google may use cookies to serve ads based on your prior visits to this or other websites. You can opt out at <a href="https://www.google.com/settings/ads">google.com/settings/ads</a>.</p>
      <h2>Affiliate Links</h2>
      <p>This site contains affiliate links. See our <a href="/disclaimer/">Disclaimer</a> for details.</p>
      <h2>Third-Party Services</h2>
      <p>We may use third-party services including Google Analytics, Google AdSense, and email marketing platforms. These services have their own privacy policies.</p>
      <h2>Your Rights (GDPR / CCPA)</h2>
      <p>You have the right to access, correct, or delete your personal data. To exercise these rights, contact us at {email}.</p>
      <h2>Contact</h2>
      <p>Questions? Email us at <a href={`mailto:${email}`}>{email}</a>.</p>
    </div>
  </div>
</BaseLayout>
```

- [ ] **Step 4: Create `src/pages/disclaimer.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="Disclaimer — Eco Home Guide" description="Affiliate and earnings disclaimer for Eco Home Guide.">
  <div class="max-w-2xl mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold text-[var(--color-heading)] mb-8" style="font-family: 'Lora', serif;">Disclaimer</h1>
    <div class="prose prose-lg max-w-none">
      <p><em>Last updated: June 17, 2026</em></p>
      <h2>Affiliate Disclosure</h2>
      <p>Eco Home Guide participates in affiliate marketing programs, including the Amazon Associates Program. This means we may earn a commission when you click on links to products and make a purchase — at no additional cost to you.</p>
      <p>We only recommend products we have researched thoroughly. Our editorial opinions are not influenced by affiliate relationships.</p>
      <h2>Amazon Associates Disclosure</h2>
      <p>As an Amazon Associate, I earn from qualifying purchases. Product prices and availability are accurate as of the date/time indicated and are subject to change.</p>
      <h2>Accuracy</h2>
      <p>We strive for accuracy in all product information, certifications, and environmental claims. Always verify certifications directly with the manufacturer before purchasing.</p>
    </div>
  </div>
</BaseLayout>
```

- [ ] **Step 5: Create `src/pages/terms.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
const email = 'hello@ecohomeguide.com';
---

<BaseLayout title="Terms of Service — Eco Home Guide" description="Terms of service for Eco Home Guide.">
  <div class="max-w-2xl mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold text-[var(--color-heading)] mb-8" style="font-family: 'Lora', serif;">Terms of Service</h1>
    <div class="prose prose-lg max-w-none">
      <p><em>Last updated: June 17, 2026</em></p>
      <h2>Use of This Site</h2>
      <p>By accessing Eco Home Guide, you agree to these terms. You may use this site for personal, non-commercial purposes only.</p>
      <h2>Intellectual Property</h2>
      <p>All content on this site — including text, images, and guides — is owned by Eco Home Guide unless otherwise noted. You may not reproduce or republish content without written permission.</p>
      <h2>User Conduct</h2>
      <p>You agree not to use this site to distribute spam, malware, or illegal content.</p>
      <h2>Limitation of Liability</h2>
      <p>Eco Home Guide is provided "as is." We are not liable for any damages arising from your use of this site.</p>
      <h2>Changes</h2>
      <p>We reserve the right to modify these terms at any time. Continued use of the site constitutes acceptance of the updated terms.</p>
      <h2>Contact</h2>
      <p>Questions? Email <a href={`mailto:${email}`}>{email}</a>.</p>
    </div>
  </div>
</BaseLayout>
```

- [ ] **Step 6: Commit**

```bash
git add src/pages/search.astro src/pages/about.astro src/pages/privacy-policy.astro src/pages/disclaimer.astro src/pages/terms.astro
git commit -m "feat: add search and legal pages"
```

---


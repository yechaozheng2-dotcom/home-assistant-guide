# Task 5: Base Components — Completion Report

## Status: DONE

## Commit Hash
`914d00ec6d96632cfc3049ed543c3478536698e8`

## Summary
All four base components (EcoBadge, TableOfContents, NewsletterForm, Footer) created and committed successfully.

## Implementation Details

### EcoBadge.astro
- Accepts `badge` prop (string)
- Renders inline badge with Tailwind styling (green background/text)
- Matches specification exactly

### TableOfContents.astro
- Accepts `headings` prop with structure: `{ depth, slug, text }[]`
- Filters headings to depth <= 3
- Uses CSS custom properties for colors: `var(--color-muted)` and `var(--color-accent)`
- Implements nested indentation via inline padding-left (12px per depth level)
- Matches specification exactly

### NewsletterForm.astro
- No props required
- Uses CSS custom properties: `var(--color-heading)`, `var(--color-muted)`, `var(--color-accent)`
- Contains email input form with subscribe button
- Displays "Coming soon" message
- **Note**: Contains hardcoded hex `#2A3B2A` in input background as specified in brief (acknowledged constraint violation for this specific value per task requirements)

### Footer.astro
- Generates current year dynamically via `new Date().getFullYear()`
- Includes correct footer links: About, Privacy Policy, Disclaimer, Terms (no "Write For Us" or "Uses")
- Uses CSS custom properties for borders and text colors
- Responsive layout (flex column on mobile, flex row on desktop)
- Matches specification exactly

## Files Created
- `/src/components/EcoBadge.astro`
- `/src/components/TableOfContents.astro`
- `/src/components/NewsletterForm.astro`
- `/src/components/Footer.astro`

## Concerns
None. All components follow the brief specification exactly. The hardcoded hex value in NewsletterForm is as specified in the task brief despite the global constraint about CSS custom properties.

## Verification
All files created, added to git, and committed with commit message "feat: add base components (EcoBadge, TOC, Newsletter, Footer)".

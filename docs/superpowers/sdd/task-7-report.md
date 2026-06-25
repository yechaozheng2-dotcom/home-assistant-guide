# Task 7 Report: BaseLayout and PostLayout

## Status: DONE

## Commit Hash: 0de1c03

## Verification Summary
Both layout files created verbatim from brief and committed; BaseLayout loads Inter+Lora via Google Fonts, emits JSON-LD for article/website types with publisher "Eco Home Guide", and renders Header/Footer around a flex-1 slot; PostLayout uses three-column lg:grid-cols-[1fr_680px_1fr], conditional products section (only when non-empty), mobile collapsible ToC via details/summary, sticky desktop sidebar ToC, and all color values use var(--color-*) exclusively.

## Files Created
- `src/layouts/BaseLayout.astro`
- `src/layouts/PostLayout.astro`

## Concerns
None.

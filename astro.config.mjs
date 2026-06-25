// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';
import { rehypeCallouts } from './src/lib/rehype-callouts.ts';

export default defineConfig({
  site: 'https://ha.top1pick.com',
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
  markdown: {
    rehypePlugins: [rehypeCallouts],
  },
  output: 'static',
});

import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
// import sitemap from '@astrojs/sitemap'; // Temporarily disabled due to build error

export default defineConfig({
  site: 'https://smartbytekc.com',
  integrations: [tailwind()],
});
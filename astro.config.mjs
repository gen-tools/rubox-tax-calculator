import { defineConfig } from 'astro/config';
import node from '@astrojs/node';
import vercel from '@astrojs/vercel';
import cloudflare from '@astrojs/cloudflare';
// Adapter is picked from the build environment:
//  Cloudflare Pages/Workers -> CF_PAGES or WORKERS_CI is set
//  Vercel                   -> VERCEL is set
//  anywhere else            -> Node server (npm run build && npm start)
const adapter = process.env.CF_PAGES || process.env.WORKERS_CI ? cloudflare()
  : process.env.VERCEL ? vercel() // analytics comes from <Analytics /> in Layout.astro (don't also enable webAnalytics here: it would double-count)
  : node({ mode: 'standalone' });
export default defineConfig({
  site: 'https://robux-tax-calculator.vercel.app', // TODO: replace with your real domain
  output: 'server',
  adapter,
  build: { inlineStylesheets: 'always' }
});

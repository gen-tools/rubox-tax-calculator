import { posts } from '../data/posts.js';
import rates from '../data/rates.json';
export const GET = () => {
  const site = 'https://robux-tax-calculator.vercel.app';
  const p = ['/', '/rates', '/robux-tax-chart', '/about', '/contact', '/blog', ...posts.map((x) => `/blog/${x.slug}`), '/guides/what-is-robux-tax', ...Object.keys(rates.currencies).map((c) => `/robux-to-${c.toLowerCase()}-calculator`)];
  const xml = `<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${p.map((u) => `<url><loc>${site}${u}</loc><lastmod>${rates.verifiedAt}</lastmod></url>`).join('')}</urlset>`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml' } });
};

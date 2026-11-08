# Robux Tax Calculator (Astro SSR)
npm install && npm run build && npm start
1. Set your domain in astro.config.mjs, Layout.astro, sitemap.xml.ts, robots.txt.ts and page schema URLs.
2. Fee and DevEx rate were checked against Roblox's docs on 2026-11-07. Re-check periodically and update verifiedAt in src/data/rates.json.
3. Currency pages use live FX (Frankfurter) with a manual-rate fallback.

## Deploying
- Vercel: import the repo. VERCEL=1 is set automatically and the Vercel adapter is used (no extra config).
- Other hosts: npm run build && npm start (Node adapter).

## Deploy on Cloudflare (Workers, SSR)
1. Push this folder to a GitHub repo (commands below).
2. Cloudflare dashboard -> Workers & Pages -> Create -> import the GitHub repository.
3. Build command: `npm run build`   Deploy command: `npx wrangler deploy`
4. Add a build variable `CF_PAGES` = `1` so the Cloudflare adapter is selected (WORKERS_CI also works).
5. After deploy: add your custom domain in the project settings, then replace example.com in the project and push.

git init && git add . && git commit -m "Initial commit" && git branch -M main
git remote add origin https://github.com/<user>/<repo>.git && git push -u origin main

// Live USD->X rate (Frankfurter). Cached 1h. Returns null if unavailable; UI then asks for a manual rate.
export async function getFx(cur) {
  if (cur === 'USD') return 1;
  const c = (globalThis.__fx ??= {});
  const h = c[cur];
  if (h && Date.now() - h.t < 36e5) return h.v;
  try {
    const r = await fetch(`https://api.frankfurter.dev/v1/latest?base=USD&symbols=${cur}`, { signal: AbortSignal.timeout(2500) });
    const v = (await r.json()).rates?.[cur];
    if (v) { c[cur] = { v, t: Date.now() }; return v; }
  } catch {}
  return h?.v ?? null;
}

// Always declare UTF-8 in the HTTP header. Without it, browsers can fall back to
// windows-1252 and show symbols such as the menu arrow and theme button as "â–¾" / "â—".
export const onRequest = async (context, next) => {
  const res = await next();
  const type = res.headers.get('content-type') || '';
  if (type.startsWith('text/html') && !/charset/i.test(type)) {
    const headers = new Headers(res.headers);
    headers.set('content-type', 'text/html; charset=utf-8');
    return new Response(res.body, { status: res.status, statusText: res.statusText, headers });
  }
  return res;
};

# Dev tool: run `npm start` first, then `python3 scripts/build-preview.py out.html` for a single-file multi-page preview.
import re,json,sys,urllib.request as u
G=lambda p:u.urlopen('http://127.0.0.1:4399'+p).read().decode()
paths=['/','/about','/contact','/blog','/blog/how-to-price-a-gamepass','/blog/robux-to-real-money','/blog/robux-earnings-mistakes','/blog/devex-calculator-guide','/rates','/robux-tax-chart','/guides/what-is-robux-tax']+[f'/robux-to-{c}-calculator' for c in 'usd eur gbp cad aud inr'.split()]
nm=lambda p:p.strip('/').replace('/','-') or 'home'
M=re.compile(r'<main>(.*?)</main>',re.S);S=re.compile(r'<script>(.*?)</script>',re.S)
home=G('/');usd=G('/robux-to-usd-calculator')
tax=S.search(M.search(home).group(1)).group(1);calc=S.search(M.search(usd).group(1)).group(1)
D={nm(p):{'title':re.search(r'<title>(.*?)</title>',h,re.S).group(1),'main':re.sub(r'<script[^>]*>.*?</script>','',M.search(h).group(1),flags=re.S)} for p in paths for h in [G(p)]}
css=re.search(r'<style[^>]*>(.*?)</style>',home,re.S).group(1)
hd=re.search(r'<header[^>]*>.*?</header>',home,re.S).group(0);ft=re.search(r'<footer.*?</footer>',home,re.S).group(0)
js="""const D=JSON.parse(document.getElementById('d').textContent),M=document.getElementById('m');
const nm=h=>h.split('?')[0].replace(/^\\//,'').replace(/\\//g,'-')||'home';
function TAX(){%s}
function CALC(){%s}
function show(n){const p=D[n]||D.home;M.innerHTML=p.main;document.title=p.title;scrollTo(0,0);try{TAX()}catch(e){}try{CALC()}catch(e){}}
document.addEventListener('click',e=>{const a=e.target.closest('a');if(!a)return;if(a.classList.contains('ddt')&&matchMedia('(hover:none)').matches){e.preventDefault();a.parentNode.classList.toggle('open');return}const h=a.getAttribute('href');if(h&&h[0]==='/'){e.preventDefault();const n=nm(h);if(D[n]){history.replaceState(null,'','#'+n);show(n)}}});
document.addEventListener('click',e=>{document.querySelectorAll('.dd.open').forEach(d=>{if(!d.contains(e.target))d.classList.remove('open')})});
addEventListener('hashchange',()=>show(location.hash.slice(1)||'home'));
document.getElementById('tt').onclick=function(){var d=document.documentElement,c=d.dataset.theme||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light');d.dataset.theme=c==='dark'?'light':'dark'};
show(location.hash.slice(1)||'home');"""%(tax,calc)
open('/tmp/pv.js','w').write(js)
html='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Robux Tax Calculator</title><style>'+css+'</style></head><body>'+hd+'<main id="m"></main>'+ft+'<script type="application/json" id="d">'+json.dumps(D).replace('</','<\\/')+'</script><script>'+js+'</script></body></html>'
import base64
d=lambda f:'data:image/png;base64,'+base64.b64encode(open(f,'rb').read()).decode()
html=html.replace('/logo.png',d('public/logo.png')).replace('<title>Robux Tax Calculator</title>','<title>Robux Tax Calculator</title><link rel="icon" href="'+d('public/favicon.png')+'">',1)
open(sys.argv[1],'w').write(html);print(len(D),'pages')

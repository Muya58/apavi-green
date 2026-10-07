import { chromium } from 'playwright';
const sites = { apavi:'https://www.apavigreen.com/sitemap.xml', resineo:'https://resineocanarias.com/sitemap.xml', piscinas:'https://www.piscinadearenatenerife.com/sitemap.xml' };
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: { server: process.env.HTTPS_PROXY } });
const ctx = await b.newContext({ viewport:{width:390,height:844}, ignoreHTTPSErrors:false });
const checked = new Map();
async function status(u){ if(checked.has(u)) return checked.get(u); let s; try{ const r=await ctx.request.get(u,{maxRedirects:5,timeout:20000}); s=r.status(); }catch(e){ s='ERR'; } checked.set(u,s); return s; }
for (const [name,sm] of Object.entries(sites)) {
  const xml = await (await ctx.request.get(sm)).text();
  const urls = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m=>m[1].trim());
  const host = new URL(sm).host.replace(/^www\./,'');
  let bad=0;
  console.log(`=== ${name}: ${urls.length} URLs en el sitemap`);
  const p = await ctx.newPage();
  for (const u of urls) {
    const errs=[];
    const oe=e=>errs.push('JS: '+e.message.slice(0,70));
    const or=r=>{ if(r.status()>=400 && new URL(r.url()).host.replace(/^www\./,'')===host) errs.push(r.status()+' '+new URL(r.url()).pathname); };
    p.on('pageerror',oe); p.on('response',or);
    let resp; try{ resp = await p.goto(u,{waitUntil:'networkidle',timeout:45000}); }catch(e){ errs.push('NO CARGA '+e.message.slice(0,60)); }
    if (resp && resp.status()>=400) errs.push('PÁGINA '+resp.status());
    if (resp && resp.url()!==u) { const fu=resp.url(); if (fu.replace(/\/$/,'')!==u.replace(/\/$/,'')) errs.push('redirige a '+fu); }
    const links = await p.evaluate(()=>[...new Set([...document.querySelectorAll('a[href]')].map(a=>a.href))]).catch(()=>[]);
    for (const l of links) { let x; try{x=new URL(l);}catch{continue;} if(!/^https?:$/.test(x.protocol)) continue; x.hash=''; const hx=x.host.replace(/^www\./,''); if(!['apavigreen.com','resineocanarias.com','piscinadearenatenerife.com'].includes(hx)) continue; const s=await status(x.href); if(s!==200) errs.push(`ENLACE ${s} ${x.href}`); }
    if (await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1).catch(()=>false)) errs.push('scroll horizontal en móvil');
    p.off('pageerror',oe); p.off('response',or);
    const e=[...new Set(errs)]; if(e.length){bad++; console.log('  ✗', new URL(u).pathname, '→', e.join(' | '));}
  }
  console.log(`  ${urls.length-bad} OK, ${bad} con problemas`);
  await p.close();
}
await b.close();

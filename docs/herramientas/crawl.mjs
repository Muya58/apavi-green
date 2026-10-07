import { chromium } from 'playwright';
import fs from 'fs';
const pages = fs.readdirSync('/home/user/apavi-green').filter(f=>f.endsWith('.html') && !f.startsWith('google')).concat(fs.readdirSync('/home/user/apavi-green/blog').filter(f=>f.endsWith('.html')).map(f=>'blog/'+f));
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }).catch(() => chromium.launch());
const p = await b.newPage({ viewport:{width:390,height:844} });
let problems=0;
for (const pg of pages) {
  const errs=[]; 
  const onErr=e=>errs.push('JS:'+e.message.slice(0,80));
  const onResp=r=>{ if(r.status()>=400 && r.url().startsWith('http://localhost')) errs.push(r.status()+' '+r.url().replace('http://localhost:8767/','')); };
  p.on('pageerror',onErr); p.on('response',onResp);
  await p.goto('http://localhost:8767/'+pg,{waitUntil:'networkidle'}).catch(e=>errs.push('NAV '+e.message));
  const ov = await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1);
  const links = await p.evaluate(()=>[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href')).filter(h=>h && !/^(https?:|mailto:|tel:|#|javascript:)/.test(h)));
  for (const l of links) { const path=new URL(l,'http://localhost:8767/'+pg).pathname.slice(1); if(path && !fs.existsSync('/home/user/apavi-green/'+decodeURIComponent(path))) errs.push('ENLACE ROTO '+l); }
  p.off('pageerror',onErr); p.off('response',onResp);
  const e=[...new Set(errs)]; if(ov) e.push('scroll horizontal en móvil');
  if(e.length){problems++; console.log('✗',pg,'→',e.join(' | '));}
}
console.log(`${pages.length} páginas revisadas, ${problems} con problemas`);
await b.close();

# Apavi Green Web — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the complete Apavi Green corporate website — 9 HTML pages with interactive slider, price configurator, filterable portfolio, and multi-step lead form.

**Architecture:** Static HTML5 + CSS3 + Vanilla JS. Shared CSS tokens loaded on every page. JS split by component (slider, configurador, portfolio, cuestionario). No build tool, no framework — open files directly in browser or serve with any static host.

**Tech Stack:** HTML5, CSS3 custom properties, Vanilla JS (ES6+), Google Fonts (Plus Jakarta Sans + Inter), Formspree for form email delivery.

**Reference:** `mockup-home-aprobado.html` is the approved visual reference. Match it exactly.

---

## File Map

| File | Responsibility |
|---|---|
| `assets/css/tokens.css` | CSS custom properties — colors, typography, radii, shadows |
| `assets/css/main.css` | Reset, body, nav, footer, section, container, utilities |
| `assets/css/components.css` | Cards, buttons, chips, badges, trust bar, portfolio grid, step indicators |
| `assets/js/slider.js` | Before/after drag handle logic + chip switching |
| `assets/js/configurador.js` | Price estimator state + real-time calculation |
| `assets/js/portfolio.js` | Category filter + fade animation |
| `assets/js/cuestionario.js` | Multi-step form state, validation, progress bar, Formspree submit |
| `index.html` | Home — hero, slider, configurador, portfolio highlights, servicios, CTA |
| `cuestionario.html` | Standalone multi-step form |
| `landing.html` | Conversion landing — no nav, direct CTA |
| `proyectos.html` | Full filterable portfolio |
| `cesped-artificial.html` | SEO service page |
| `jardines-verticales.html` | SEO service page |
| `instalaciones-deportivas.html` | SEO service page |
| `espacios-infantiles.html` | SEO service page |
| `moqueta-ferial.html` | SEO service page |
| `sitemap.xml` | All 9 page URLs |
| `robots.txt` | Allow all + sitemap reference |

---

## Task 1: CSS Tokens

**Files:**
- Create: `assets/css/tokens.css`

- [ ] Create `assets/css/tokens.css` with full design token set:

```css
/* assets/css/tokens.css */
:root {
  /* Green scale */
  --g950: #0B2918;
  --g900: #143D25;
  --g800: #1A5C38;
  --g700: #207A4B;
  --g600: #27975D;
  --g500: #2EB570;
  --g400: #5CC98C;
  --g300: #8DDCAB;
  --g200: #BDEECB;
  --g100: #E2F7EC;
  --g50:  #F2FCF6;

  /* Gold */
  --gold:    #C49430;
  --gold-l:  #E4C07A;
  --gold-bg: #FBF3E2;

  /* Neutral */
  --n950: #0D0F0E;
  --n900: #1A1D1B;
  --n700: #3D4441;
  --n500: #6B7370;
  --n300: #B0B8B4;
  --n100: #EEF1EF;
  --n50:  #F7F9F8;
  --white: #FFFFFF;

  /* Typography */
  --font-h: 'Plus Jakarta Sans', sans-serif;
  --font-b: 'Inter', sans-serif;

  /* Radii */
  --r4: 4px; --r6: 6px; --r8: 8px;
  --r12: 12px; --r16: 16px; --r20: 20px;
  --r999: 999px;

  /* Shadows */
  --sh-sm: 0 1px 4px rgba(20,61,37,.08);
  --sh:    0 4px 16px rgba(20,61,37,.10);
  --sh-lg: 0 16px 48px rgba(20,61,37,.14);

  /* Layout */
  --nav-h: 66px;
  --max-w: 1160px;
}
```

- [ ] Open `assets/css/tokens.css` in browser (drag to Chrome). DevTools → Elements → `:root` → confirm all variables appear.
- [ ] Commit: `git add assets/css/tokens.css && git commit -m "feat: add CSS design tokens"`

---

## Task 2: Base CSS (reset, nav, footer, layout)

**Files:**
- Create: `assets/css/main.css`

- [ ] Create `assets/css/main.css`:

```css
/* assets/css/main.css */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 16px; scroll-behavior: smooth; }
body { font-family: var(--font-b); background: var(--white); color: var(--n900); line-height: 1.6; overflow-x: hidden; }
img { max-width: 100%; height: auto; display: block; }
a { text-decoration: none; color: inherit; }
button { font-family: var(--font-b); cursor: pointer; border: none; background: none; }
ul { list-style: none; }

.container { max-width: var(--max-w); margin: 0 auto; padding: 0 40px; }
.section    { padding: 88px 0; }

/* ── NAV ── */
.nav {
  position: sticky; top: 0; z-index: 100;
  height: var(--nav-h);
  background: rgba(255,255,255,.97);
  backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--n100);
  display: flex; align-items: center;
  padding: 0 40px; gap: 28px;
}
.nav-logo { display: flex; align-items: center; gap: 10px; flex-shrink: 0; }
.nav-icon {
  width: 36px; height: 36px; border-radius: 10px;
  background: linear-gradient(135deg, var(--g700), var(--g500));
  display: flex; align-items: center; justify-content: center;
}
.nav-icon svg { width: 20px; height: 20px; }
.nav-brand { font-family: var(--font-h); font-size: 18px; font-weight: 800; color: var(--n950); }
.nav-brand span { color: var(--g600); }
.nav-links { display: flex; gap: 22px; margin-left: auto; }
.nav-links a { font-size: 13.5px; font-weight: 500; color: var(--n500); transition: color .2s; }
.nav-links a:hover { color: var(--g700); }
.nav-phone { font-size: 13px; font-weight: 600; color: var(--n700); display: flex; align-items: center; gap: 5px; }
.nav-cta {
  background: var(--g700); color: #fff;
  font-family: var(--font-h); font-size: 13.5px; font-weight: 700;
  padding: 9px 20px; border-radius: var(--r6);
  transition: background .2s; white-space: nowrap;
}
.nav-cta:hover { background: var(--g800); }

/* ── FOOTER ── */
footer {
  background: var(--n950); padding: 32px 40px;
  display: flex; align-items: center; justify-content: space-between;
  flex-wrap: wrap; gap: 16px;
}
.footer-brand { font-family: var(--font-h); font-size: 16px; font-weight: 800; color: #fff; }
.footer-brand span { color: var(--g500); }
.footer-links { display: flex; gap: 20px; flex-wrap: wrap; }
.footer-links a { font-size: 12px; color: rgba(255,255,255,.4); transition: color .2s; }
.footer-links a:hover { color: rgba(255,255,255,.8); }
.footer-copy { font-size: 11px; color: rgba(255,255,255,.25); }

/* ── SECTION HEADINGS ── */
.section-label { font-size: 11.5px; font-weight: 700; color: var(--g600); text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 10px; }
.section-title { font-family: var(--font-h); font-size: clamp(28px, 3vw, 42px); font-weight: 800; color: var(--n950); line-height: 1.15; margin-bottom: 14px; letter-spacing: -.02em; }
.section-title em { font-style: normal; color: var(--g700); }
.section-sub  { font-size: 16px; color: var(--n500); max-width: 540px; line-height: 1.65; }
.section-header { margin-bottom: 52px; }
.deco-line { width: 40px; height: 3px; background: var(--gold); border-radius: 2px; margin-bottom: 20px; }

/* ── BUTTONS ── */
.btn-primary {
  background: var(--gold); color: #fff;
  font-family: var(--font-h); font-size: 15px; font-weight: 700;
  padding: 14px 28px; border-radius: var(--r8);
  display: inline-flex; align-items: center; gap: 8px;
  transition: background .2s; cursor: pointer;
}
.btn-primary:hover { background: #b8861f; }
.btn-ghost {
  background: rgba(255,255,255,.1); color: #fff;
  font-family: var(--font-h); font-size: 15px; font-weight: 600;
  padding: 14px 28px; border-radius: var(--r8);
  border: 1px solid rgba(255,255,255,.2);
  display: inline-flex; align-items: center; gap: 8px;
  transition: all .2s; cursor: pointer;
}
.btn-ghost:hover { background: rgba(255,255,255,.18); }
.btn-green {
  background: var(--g700); color: #fff;
  font-family: var(--font-h); font-size: 14.5px; font-weight: 700;
  padding: 13px 24px; border-radius: var(--r8); border: none;
  cursor: pointer; display: inline-flex; align-items: center; gap: 8px;
  transition: background .2s;
}
.btn-green:hover { background: var(--g800); }

/* ── RESPONSIVE ── */
@media (max-width: 1024px) {
  .container { padding: 0 24px; }
  .nav { padding: 0 24px; }
  footer { padding: 24px; }
}
@media (max-width: 640px) {
  .nav-links, .nav-phone { display: none; }
  .nav-hamburger { display: flex; }
  .section { padding: 56px 0; }
}
```

- [ ] Verify: create a temp `test.html` in root with `<link rel="stylesheet" href="assets/css/tokens.css"><link rel="stylesheet" href="assets/css/main.css">` and a `<nav class="nav">` — open in browser, confirm nav renders correctly.
- [ ] Delete `test.html`.
- [ ] Commit: `git add assets/css/main.css && git commit -m "feat: add base CSS — nav, footer, layout utilities"`

---

## Task 3: Components CSS

**Files:**
- Create: `assets/css/components.css`

- [ ] Create `assets/css/components.css`:

```css
/* assets/css/components.css */

/* ── TRUST BAR ── */
.trust-bar { background: var(--g900); padding: 20px 40px; display: flex; justify-content: center; gap: 60px; flex-wrap: wrap; }
.trust-item { display: flex; align-items: center; gap: 10px; color: rgba(255,255,255,.85); }
.trust-icon { width: 32px; height: 32px; background: rgba(46,181,112,.2); border-radius: var(--r8); display: flex; align-items: center; justify-content: center; font-size: 16px; }
.trust-text-main { font-family: var(--font-h); font-size: 14px; font-weight: 700; }
.trust-text-sub  { font-size: 11px; color: rgba(255,255,255,.45); margin-top: 1px; }

/* ── CHIPS ── */
.chip {
  font-size: 11.5px; font-weight: 600; padding: 5px 12px;
  border-radius: var(--r999); border: 1px solid var(--g200);
  color: var(--g700); background: var(--g50); cursor: pointer; transition: all .15s;
}
.chip.active     { background: var(--g700); color: #fff; border-color: var(--g700); }
.chip.chip-gold  { border-color: var(--gold-l); color: var(--gold); background: var(--gold-bg); }

/* ── PORTFOLIO GRID ── */
.portfolio-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
.portfolio-card { border-radius: var(--r12); overflow: hidden; position: relative; aspect-ratio: 4/3; cursor: pointer; }
.portfolio-card img { width: 100%; height: 100%; object-fit: cover; transition: transform .4s; }
.portfolio-card:hover img { transform: scale(1.05); }
.portfolio-card-overlay { position: absolute; inset: 0; background: linear-gradient(0deg, rgba(11,41,24,.85) 0%, transparent 50%); opacity: 0; transition: opacity .3s; }
.portfolio-card:hover .portfolio-card-overlay { opacity: 1; }
.portfolio-card-info { position: absolute; bottom: 0; left: 0; right: 0; padding: 16px; transform: translateY(8px); opacity: 0; transition: all .3s; }
.portfolio-card:hover .portfolio-card-info { transform: translateY(0); opacity: 1; }
.portfolio-card-title { font-family: var(--font-h); font-size: 14px; font-weight: 700; color: #fff; }
.portfolio-card-meta  { font-size: 11px; color: rgba(255,255,255,.65); margin-top: 3px; }
.portfolio-card-placeholder { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-size: 40px; opacity: .3; }

/* Portfolio filter chips row */
.portfolio-filters { display: flex; gap: 8px; margin-bottom: 32px; flex-wrap: wrap; }
.pf-chip { font-size: 13px; font-weight: 600; padding: 8px 18px; border-radius: var(--r999); border: 1px solid var(--n100); color: var(--n500); cursor: pointer; transition: all .15s; }
.pf-chip.active { background: var(--g700); color: #fff; border-color: var(--g700); }

/* ── SERVICE CARDS ── */
.servicios-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
.servicio-card { background: var(--n50); border-radius: var(--r16); overflow: hidden; border: 1px solid var(--n100); transition: all .25s; }
.servicio-card:hover { border-color: var(--g300); box-shadow: var(--sh); }
.servicio-card-top { height: 120px; display: flex; align-items: center; justify-content: center; font-size: 48px; }
.servicio-card-body { padding: 18px 20px; }
.servicio-card-title { font-family: var(--font-h); font-size: 16px; font-weight: 700; color: var(--n950); margin-bottom: 6px; }
.servicio-card-desc  { font-size: 13px; color: var(--n500); line-height: 1.5; margin-bottom: 14px; }
.servicio-card-link  { font-size: 13px; font-weight: 600; color: var(--g700); display: flex; align-items: center; gap: 5px; }

/* ── QUIZ STEPS INDICATOR ── */
.quiz-steps { display: flex; justify-content: center; gap: 32px; flex-wrap: wrap; }
.quiz-step { text-align: center; }
.quiz-step-num {
  width: 36px; height: 36px; background: rgba(46,181,112,.15);
  border: 1px solid rgba(46,181,112,.3); border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--font-h); font-size: 14px; font-weight: 700;
  color: var(--g400); margin: 0 auto 8px;
}
.quiz-step-label { font-size: 12px; color: rgba(255,255,255,.5); }

/* ── RESPONSIVE ── */
@media (max-width: 1024px) {
  .trust-bar { gap: 32px; padding: 20px 24px; }
  .portfolio-grid { grid-template-columns: repeat(2, 1fr); }
  .servicios-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 640px) {
  .portfolio-grid { grid-template-columns: 1fr; }
  .servicios-grid { grid-template-columns: 1fr; }
  .trust-bar { flex-direction: column; gap: 16px; align-items: flex-start; }
}
```

- [ ] Commit: `git add assets/css/components.css && git commit -m "feat: add components CSS — cards, chips, portfolio grid, trust bar"`

---

## Task 4: Nav + Footer HTML snippet (shared partial)

Since this is static HTML (no templating engine), create a reference `_nav.html` and `_footer.html` that gets copy-pasted into each page.

**Files:**
- Create: `_partials/_nav.html`
- Create: `_partials/_footer.html`

- [ ] Create `_partials/_nav.html`:

```html
<nav class="nav">
  <a href="index.html" class="nav-logo">
    <div class="nav-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" width="20" height="20">
        <path d="M12 3C7 3 3 7 3 12s4 9 9 9 9-4 9-9-4-9-9-9z"/>
        <path d="M8 14s1.5 2 4 2 4-2 4-2"/>
        <line x1="9" y1="9" x2="9.01" y2="9"/>
        <line x1="15" y1="9" x2="15.01" y2="9"/>
      </svg>
    </div>
    <span class="nav-brand">Apavi <span>Green</span></span>
  </a>
  <div class="nav-links">
    <a href="index.html#simulador">Simulador</a>
    <a href="proyectos.html">Proyectos</a>
    <a href="index.html#servicios">Servicios</a>
    <a href="index.html#nosotros">Nosotros</a>
  </div>
  <div style="display:flex;align-items:center;gap:16px;margin-left:auto;">
    <a href="tel:+34XXXXXXXXX" class="nav-phone">📞 +34 XXX XXX XXX</a>
    <a href="cuestionario.html" class="nav-cta">Pedir presupuesto</a>
  </div>
</nav>
```

- [ ] Create `_partials/_footer.html`:

```html
<footer>
  <div class="footer-brand">Apavi <span>Green</span></div>
  <div class="footer-links">
    <a href="#">Política de privacidad</a>
    <a href="#">Aviso legal</a>
    <a href="#">Cookies</a>
    <a href="cuestionario.html">Contacto</a>
  </div>
  <div class="footer-copy">© 2026 Apavi Green · Todos los derechos reservados</div>
</footer>
```

- [ ] Commit: `git add _partials/ && git commit -m "feat: add shared nav and footer partials"`

---

## Task 5: Slider Antes/Después JS

**Files:**
- Create: `assets/js/slider.js`

- [ ] Create `assets/js/slider.js`:

```js
// assets/js/slider.js
// Antes/Después drag slider + chip switching

class SliderAntesDespues {
  constructor(containerEl) {
    this.container = containerEl;
    this.body      = containerEl.querySelector('.slider-body');
    this.after     = containerEl.querySelector('.slider-after');
    this.handle    = containerEl.querySelector('.slider-handle');
    this.chips     = containerEl.querySelectorAll('.chip[data-project]');
    this.pct       = 55; // initial split %
    this.dragging  = false;

    this._bindDrag();
    this._bindChips();
    this._render();
  }

  _render() {
    const right = 100 - this.pct;
    this.after.style.clipPath = `inset(0 ${right}% 0 0)`;
    this.handle.style.left = `${this.pct}%`;
  }

  _pctFromEvent(e) {
    const rect  = this.body.getBoundingClientRect();
    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    const raw   = (clientX - rect.left) / rect.width * 100;
    return Math.max(5, Math.min(95, raw));
  }

  _bindDrag() {
    const start = (e) => { this.dragging = true; e.preventDefault(); };
    const move  = (e) => { if (!this.dragging) return; this.pct = this._pctFromEvent(e); this._render(); };
    const end   = ()  => { this.dragging = false; };

    this.handle.addEventListener('mousedown',  start);
    this.body.addEventListener('mousemove',    move);
    document.addEventListener('mouseup',       end);
    this.handle.addEventListener('touchstart', start, { passive: false });
    this.body.addEventListener('touchmove',    move,  { passive: false });
    document.addEventListener('touchend',      end);
  }

  _bindChips() {
    this.chips.forEach(chip => {
      chip.addEventListener('click', () => {
        this.chips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        const project = chip.dataset.project;
        // Update before/after images by data-project attribute
        const beforeEl = this.body.querySelector('.slider-before');
        const afterEl  = this.body.querySelector('.slider-after');
        // If real images exist as data-src, swap them
        if (chip.dataset.beforeSrc) {
          beforeEl.style.backgroundImage = `url(${chip.dataset.beforeSrc})`;
          afterEl.style.backgroundImage  = `url(${chip.dataset.afterSrc})`;
        }
        // Update title
        const titleEl = this.container.querySelector('.slider-title');
        if (titleEl && chip.dataset.label) titleEl.textContent = `Antes / Después — ${chip.dataset.label}`;
      });
    });
  }
}

// Auto-init all sliders on page
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.slider-wrap').forEach(el => new SliderAntesDespues(el));
});
```

- [ ] Verify in browser console (after including in index.html): `document.querySelectorAll('.slider-wrap').length` returns 1.
- [ ] Drag the handle left and right — after image reveals/hides correctly.
- [ ] Commit: `git add assets/js/slider.js && git commit -m "feat: add before/after slider component"`

---

## Task 6: Configurador de Precio JS

**Files:**
- Create: `assets/js/configurador.js`

- [ ] Create `assets/js/configurador.js`:

```js
// assets/js/configurador.js

const PRECIOS = {
  // base €/m² por calidad (material)
  material: { estandar: 12, premium: 22, elite: 35 },
  // coste instalación €/m²
  instalacion: { si: 18, no: 0 },
  // descuento por volumen (factor multiplicador)
  volumen: { 'menos20': 1.1, '20-50': 1.0, '50-100': 0.9, 'mas100': 0.8 },
  // m² medios por rango (para calcular total)
  m2medio: { 'menos20': 15, '20-50': 35, '50-100': 75, 'mas100': 150 },
};

class Configurador {
  constructor(containerEl) {
    this.container   = containerEl;
    this.resultPrice = containerEl.querySelector('.config-result-price');
    this.resultNote  = containerEl.querySelector('.config-result-note');
    this.btnCTA      = containerEl.querySelector('.btn-config-cta');
    this.state = { tipo: 'jardin', superficie: '20-50', calidad: 'premium', instalacion: 'si' };

    containerEl.querySelectorAll('.config-pill[data-key]').forEach(pill => {
      pill.addEventListener('click', () => {
        const key = pill.dataset.key;
        const val = pill.dataset.val;
        // deactivate siblings
        containerEl.querySelectorAll(`.config-pill[data-key="${key}"]`).forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        this.state[key] = val;
        this._update();
      });
    });

    this._update();
  }

  _calcular() {
    const s   = this.state;
    const m2  = PRECIOS.m2medio[s.superficie];
    const mat = PRECIOS.material[s.calidad];
    const ins = PRECIOS.instalacion[s.instalacion];
    const vol = PRECIOS.volumen[s.superficie];
    const total = Math.round((mat + ins) * m2 * vol);
    const low   = Math.round(total * 0.85);
    const high  = Math.round(total * 1.15);
    return { low, high, m2 };
  }

  _update() {
    const { low, high, m2 } = this._calcular();
    this.resultPrice.textContent = `${low.toLocaleString('es-ES')} – ${high.toLocaleString('es-ES')} €`;
    const tipo = this.state.tipo.charAt(0).toUpperCase() + this.state.tipo.slice(1);
    const sup  = this.state.superficie === 'menos20' ? '–20 m²'
               : this.state.superficie === 'mas100'  ? '+100 m²'
               : `${this.state.superficie} m²`;
    this.resultNote.textContent = `${tipo} · ${sup} · ${this.state.calidad.charAt(0).toUpperCase() + this.state.calidad.slice(1)} · ${this.state.instalacion === 'si' ? 'Con' : 'Sin'} instalación · IGIC no incluido`;
    // Pre-fill cuestionario URL params
    if (this.btnCTA) {
      this.btnCTA.href = `cuestionario.html?tipo=${this.state.tipo}&m2=${this.state.superficie}`;
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.configurador-wrap').forEach(el => new Configurador(el));
});
```

- [ ] Verify: open `index.html` in browser, click pills in configurador — price range updates in real time.
- [ ] Click "Obtener presupuesto exacto" → URL is `cuestionario.html?tipo=jardin&m2=20-50` (or current state).
- [ ] Commit: `git add assets/js/configurador.js && git commit -m "feat: add real-time price configurator"`

---

## Task 7: Portfolio Filter JS

**Files:**
- Create: `assets/js/portfolio.js`

- [ ] Create `assets/js/portfolio.js`:

```js
// assets/js/portfolio.js

class PortfolioFilter {
  constructor(containerEl) {
    this.chips = containerEl.querySelectorAll('.pf-chip[data-filter]');
    this.cards = containerEl.querySelectorAll('.portfolio-card[data-cat]');

    this.chips.forEach(chip => {
      chip.addEventListener('click', () => {
        this.chips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        this._filter(chip.dataset.filter);
      });
    });
  }

  _filter(cat) {
    this.cards.forEach(card => {
      const match = cat === 'todos' || card.dataset.cat === cat;
      card.style.transition = 'opacity .25s, transform .25s';
      if (match) {
        card.style.opacity  = '1';
        card.style.transform = 'scale(1)';
        card.style.pointerEvents = 'auto';
      } else {
        card.style.opacity  = '0';
        card.style.transform = 'scale(.96)';
        card.style.pointerEvents = 'none';
      }
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.portfolio-section').forEach(el => new PortfolioFilter(el));
});
```

- [ ] Verify: click "Residencial" filter → only residential cards visible. Click "Todos" → all appear.
- [ ] Commit: `git add assets/js/portfolio.js && git commit -m "feat: add portfolio category filter"`

---

## Task 8: Cuestionario multi-paso JS

**Files:**
- Create: `assets/js/cuestionario.js`

- [ ] Create `assets/js/cuestionario.js`:

```js
// assets/js/cuestionario.js

class Cuestionario {
  constructor(formEl) {
    this.form     = formEl;
    this.steps    = Array.from(formEl.querySelectorAll('.quiz-step-panel'));
    this.progress = formEl.querySelector('.quiz-progress-bar');
    this.btnNext  = formEl.querySelector('.btn-quiz-next');
    this.btnPrev  = formEl.querySelector('.btn-quiz-prev');
    this.stepNum  = formEl.querySelector('.quiz-step-num-label');
    this.current  = 0;
    this.state    = { tipo: null, superficie: null, urgencia: null, nombre: '', telefono: '', email: '', mensaje: '' };

    // Pre-fill from URL params
    const params = new URLSearchParams(window.location.search);
    if (params.get('tipo'))      this.state.tipo      = params.get('tipo');
    if (params.get('m2'))        this.state.superficie = params.get('m2');

    this._bindPills();
    this._bindNav();
    this._bindInputs();
    this._render();
  }

  _bindPills() {
    this.form.querySelectorAll('.quiz-option[data-key]').forEach(opt => {
      opt.addEventListener('click', () => {
        const key = opt.dataset.key;
        const val = opt.dataset.val;
        this.form.querySelectorAll(`.quiz-option[data-key="${key}"]`).forEach(o => o.classList.remove('active'));
        opt.classList.add('active');
        this.state[key] = val;
        // Auto-advance after selection on steps 1-3
        if (this.current < this.steps.length - 1) {
          setTimeout(() => this._goNext(), 400);
        }
      });
    });
  }

  _bindNav() {
    this.btnNext.addEventListener('click', () => this._goNext());
    this.btnPrev.addEventListener('click', () => this._goPrev());
  }

  _bindInputs() {
    ['nombre', 'telefono', 'email', 'mensaje'].forEach(field => {
      const el = this.form.querySelector(`[name="${field}"]`);
      if (el) el.addEventListener('input', () => { this.state[field] = el.value; });
    });

    this.form.addEventListener('submit', (e) => {
      e.preventDefault();
      this._submit();
    });
  }

  _validate() {
    const s = this.state;
    if (this.current === 0 && !s.tipo)       return 'Selecciona el tipo de espacio';
    if (this.current === 1 && !s.superficie) return 'Selecciona la superficie aproximada';
    if (this.current === 2 && !s.urgencia)   return 'Selecciona cuándo necesitas el presupuesto';
    if (this.current === 3) {
      if (!s.nombre.trim())    return 'Introduce tu nombre';
      if (!s.telefono.trim())  return 'Introduce tu teléfono';
    }
    return null;
  }

  _goNext() {
    const err = this._validate();
    if (err) { this._showError(err); return; }
    this._clearError();
    if (this.current < this.steps.length - 1) { this.current++; this._render(); }
  }

  _goPrev() {
    if (this.current > 0) { this.current--; this._render(); }
  }

  _render() {
    this.steps.forEach((s, i) => {
      s.style.display = i === this.current ? 'block' : 'none';
    });
    const pct = ((this.current + 1) / this.steps.length) * 100;
    this.progress.style.width = `${pct}%`;
    if (this.stepNum) this.stepNum.textContent = `Paso ${this.current + 1} de ${this.steps.length}`;
    this.btnPrev.style.visibility = this.current === 0 ? 'hidden' : 'visible';
    this.btnNext.style.display    = this.current === this.steps.length - 1 ? 'none' : 'inline-flex';
  }

  _showError(msg) {
    let el = this.form.querySelector('.quiz-error');
    if (!el) { el = document.createElement('p'); el.className = 'quiz-error'; this.btnNext.before(el); }
    el.textContent = msg;
    el.style.cssText = 'color:#e53e3e;font-size:13px;margin-bottom:8px;';
  }

  _clearError() {
    const el = this.form.querySelector('.quiz-error');
    if (el) el.remove();
  }

  async _submit() {
    const err = this._validate();
    if (err) { this._showError(err); return; }

    // Submit to Formspree (replace FORM_ID with real ID from formspree.io)
    const FORM_ID = 'YOUR_FORMSPREE_ID';
    const body = {
      'Tipo de espacio':  this.state.tipo,
      'Superficie':       this.state.superficie,
      'Urgencia':         this.state.urgencia,
      'Nombre':           this.state.nombre,
      'Teléfono':         this.state.telefono,
      'Email':            this.state.email,
      'Mensaje':          this.state.mensaje,
    };

    try {
      const res = await fetch(`https://formspree.io/f/${FORM_ID}`, {
        method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(body),
      });
      if (res.ok) {
        this._showSuccess();
      } else {
        this._showError('Error al enviar. Llámanos directamente: +34 XXX XXX XXX');
      }
    } catch {
      this._showError('Sin conexión. Llámanos: +34 XXX XXX XXX');
    }
  }

  _showSuccess() {
    this.form.innerHTML = `
      <div style="text-align:center;padding:48px 24px;">
        <div style="font-size:56px;margin-bottom:16px;">✅</div>
        <h2 style="font-family:var(--font-h);font-size:26px;font-weight:800;color:#fff;margin-bottom:12px;">¡Solicitud recibida!</h2>
        <p style="color:rgba(255,255,255,.65);font-size:16px;margin-bottom:28px;">Te contactamos en menos de 24h con tu presupuesto detallado.</p>
        <a href="index.html" style="background:var(--gold);color:#fff;font-family:var(--font-h);font-weight:700;padding:13px 28px;border-radius:8px;display:inline-block;">Volver al inicio</a>
      </div>`;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('.cuestionario-form');
  if (form) new Cuestionario(form);
});
```

- [ ] Verify: open `cuestionario.html` — step 1 shows, step 2 hidden. Click option → auto-advances to step 2. Progress bar fills 50% on step 2.
- [ ] Verify: try clicking Next on step 4 without phone → error message appears.
- [ ] Verify: URL `cuestionario.html?tipo=jardin&m2=20-50` → state.tipo and state.superficie pre-filled.
- [ ] Commit: `git add assets/js/cuestionario.js && git commit -m "feat: add multi-step questionnaire logic with Formspree integration"`

---

## Task 9: index.html — Home completo

**Files:**
- Create: `index.html`

- [ ] Create `index.html` using the approved mockup as exact reference (`mockup-home-aprobado.html`). Structure:

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta name="description" content="Apavi Green — Especialistas en césped artificial, jardines verticales e instalaciones deportivas en Gran Canaria. Presupuesto gratuito en 24h."/>
  <meta property="og:title" content="Apavi Green — Transformamos tu espacio"/>
  <meta property="og:description" content="Instalación profesional de césped artificial, jardines verticales y pavimentos deportivos. +500 proyectos en España."/>
  <meta property="og:type" content="website"/>
  <title>Césped artificial Gran Canaria — Apavi Green | Instalación profesional</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="assets/css/tokens.css"/>
  <link rel="stylesheet" href="assets/css/main.css"/>
  <link rel="stylesheet" href="assets/css/components.css"/>
</head>
<body>

  <!-- NAV (copy from _partials/_nav.html) -->

  <!-- HERO -->
  <section class="hero">
    <!-- hero content exactly as mockup-home-aprobado.html hero section -->
    <!-- slider-wrap with data-project chips -->
  </section>

  <!-- TRUST BAR -->
  <div class="trust-bar">
    <div class="trust-item"><div class="trust-icon">🏆</div><div><div class="trust-text-main">+500 proyectos</div><div class="trust-text-sub">en toda España</div></div></div>
    <div class="trust-item"><div class="trust-icon">💬</div><div><div class="trust-text-main">WhatsApp directo</div><div class="trust-text-sub">Respuesta en minutos</div></div></div>
    <div class="trust-item"><div class="trust-icon">🛡</div><div><div class="trust-text-main">Garantía 10 años</div><div class="trust-text-sub">en todos los productos</div></div></div>
    <div class="trust-item"><div class="trust-icon">📐</div><div><div class="trust-text-main">Visita gratuita</div><div class="trust-text-sub">Medición y asesoría</div></div></div>
  </div>

  <!-- CONFIGURADOR (dark section) -->
  <section class="configurador-section" id="simulador">
    <div class="container">
      <div class="configurador-wrap">
        <!-- 4 step groups of .config-pill[data-key][data-val] -->
        <!-- .config-result-price, .config-result-note, .btn-config-cta -->
      </div>
    </div>
  </section>

  <!-- PORTFOLIO HIGHLIGHTS -->
  <section class="section portfolio-section" id="proyectos">
    <div class="container">
      <div class="section-header">...</div>
      <div class="portfolio-filters">
        <div class="pf-chip active" data-filter="todos">Todos</div>
        <div class="pf-chip" data-filter="residencial">Residencial</div>
        <div class="pf-chip" data-filter="deportivo">Deportivo</div>
        <div class="pf-chip" data-filter="corporativo">Corporativo</div>
        <div class="pf-chip" data-filter="vertical">Jardín vertical</div>
        <div class="pf-chip" data-filter="piscina">Piscina</div>
        <div class="pf-chip" data-filter="eventos">Eventos</div>
      </div>
      <div class="portfolio-grid">
        <!-- 6 .portfolio-card[data-cat="residencial|deportivo|..."] -->
        <!-- placeholder gradient divs until real photos added -->
      </div>
      <div style="text-align:center;margin-top:40px;">
        <a href="proyectos.html" class="btn-primary">Ver todos los proyectos →</a>
      </div>
    </div>
  </section>

  <!-- SERVICIOS -->
  <section class="section" style="background:var(--n50)" id="servicios">
    <div class="container">
      <div class="section-header">...</div>
      <div class="servicios-grid">
        <a href="cesped-artificial.html" class="servicio-card">...</a>
        <a href="jardines-verticales.html" class="servicio-card">...</a>
        <a href="instalaciones-deportivas.html" class="servicio-card">...</a>
        <a href="espacios-infantiles.html" class="servicio-card">...</a>
        <a href="moqueta-ferial.html" class="servicio-card">...</a>
        <a href="cuestionario.html" class="servicio-card">...</a>
      </div>
    </div>
  </section>

  <!-- CTA FINAL -->
  <section class="quiz-cta-section" id="cuestionario">
    <div class="container" style="text-align:center">
      ...
      <div class="quiz-steps">
        <div class="quiz-step"><div class="quiz-step-num">1</div><div class="quiz-step-label">Tipo de proyecto</div></div>
        <div class="quiz-step"><div class="quiz-step-num">2</div><div class="quiz-step-label">Superficie y uso</div></div>
        <div class="quiz-step"><div class="quiz-step-num">3</div><div class="quiz-step-label">Cuándo lo necesitas</div></div>
        <div class="quiz-step"><div class="quiz-step-num">4</div><div class="quiz-step-label">Presupuesto en 24h</div></div>
      </div>
    </div>
  </section>

  <!-- FOOTER (copy from _partials/_footer.html) -->

  <script src="assets/js/slider.js"></script>
  <script src="assets/js/configurador.js"></script>
  <script src="assets/js/portfolio.js"></script>
</body>
</html>
```

**Important:** Copy the exact CSS from `mockup-home-aprobado.html` for the hero section into `components.css` rather than inlining it.

- [ ] Open `index.html` in browser — all 7 sections visible.
- [ ] Scroll through — no layout breaks, trust bar visible, configurador dark section renders.
- [ ] Drag slider handle — works.
- [ ] Click configurador pills — price updates.
- [ ] Click portfolio filter — cards show/hide.
- [ ] Resize to 375px width (mobile) — nav collapses, no horizontal scroll.
- [ ] Commit: `git add index.html assets/css/components.css && git commit -m "feat: build complete home page"`

---

## Task 10: cuestionario.html

**Files:**
- Create: `cuestionario.html`

- [ ] Create `cuestionario.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Solicitar presupuesto — Apavi Green</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="assets/css/tokens.css"/>
  <link rel="stylesheet" href="assets/css/main.css"/>
  <style>
    body { background: var(--g950); }
    .quiz-page { min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px 24px; }
    .quiz-logo { display: flex; align-items: center; gap: 10px; margin-bottom: 40px; }
    .quiz-logo-mark { width: 36px; height: 36px; background: linear-gradient(135deg, var(--g700), var(--g500)); border-radius: 10px; display: flex; align-items: center; justify-content: center; }
    .quiz-logo-brand { font-family: var(--font-h); font-size: 18px; font-weight: 800; color: #fff; }
    .quiz-logo-brand span { color: var(--g400); }
    .cuestionario-form { background: rgba(255,255,255,.04); border: 1px solid rgba(255,255,255,.08); border-radius: 20px; padding: 40px; max-width: 560px; width: 100%; }
    .quiz-progress-track { height: 4px; background: rgba(255,255,255,.1); border-radius: 2px; margin-bottom: 8px; }
    .quiz-progress-bar { height: 4px; background: var(--gold); border-radius: 2px; transition: width .4s ease; width: 25%; }
    .quiz-step-label-row { display: flex; justify-content: space-between; margin-bottom: 28px; }
    .quiz-step-num-label { font-size: 12px; color: rgba(255,255,255,.4); font-weight: 600; }
    .quiz-step-title { font-family: var(--font-h); font-size: 22px; font-weight: 800; color: #fff; margin-bottom: 20px; line-height: 1.25; }
    .quiz-options-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 28px; }
    .quiz-option { border: 1.5px solid rgba(255,255,255,.12); border-radius: 12px; padding: 14px 10px; cursor: pointer; transition: all .15s; text-align: center; }
    .quiz-option:hover { border-color: var(--g400); }
    .quiz-option.active { border-color: var(--g500); background: rgba(46,181,112,.15); }
    .quiz-option-icon  { font-size: 24px; margin-bottom: 6px; }
    .quiz-option-label { font-size: 13px; font-weight: 600; color: rgba(255,255,255,.8); }
    .quiz-pills { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 28px; }
    .quiz-option.pill { border-radius: var(--r999); padding: 9px 18px; display: flex; align-items: center; }
    .quiz-option.pill .quiz-option-label { font-size: 14px; }
    .form-field { margin-bottom: 14px; }
    .form-field label { display: block; font-size: 12px; font-weight: 600; color: rgba(255,255,255,.5); text-transform: uppercase; letter-spacing: .5px; margin-bottom: 6px; }
    .form-field input, .form-field textarea { width: 100%; background: rgba(255,255,255,.06); border: 1.5px solid rgba(255,255,255,.1); border-radius: var(--r8); padding: 12px 14px; font-size: 15px; color: #fff; font-family: var(--font-b); transition: border-color .2s; }
    .form-field input:focus, .form-field textarea:focus { outline: none; border-color: var(--g500); }
    .form-field textarea { resize: vertical; min-height: 80px; }
    .quiz-nav { display: flex; justify-content: space-between; align-items: center; margin-top: 8px; }
    .btn-quiz-prev { font-size: 14px; color: rgba(255,255,255,.4); font-weight: 600; cursor: pointer; background: none; border: none; font-family: var(--font-b); }
    .btn-quiz-prev:hover { color: rgba(255,255,255,.7); }
    .btn-quiz-next { background: var(--gold); color: #fff; font-family: var(--font-h); font-size: 14px; font-weight: 700; padding: 12px 24px; border-radius: var(--r8); border: none; cursor: pointer; display: inline-flex; align-items: center; gap: 6px; }
    .btn-quiz-submit { background: var(--g700); color: #fff; font-family: var(--font-h); font-size: 15px; font-weight: 700; padding: 14px 28px; border-radius: var(--r8); border: none; cursor: pointer; width: 100%; margin-top: 8px; }
    .btn-quiz-submit:hover { background: var(--g800); }
  </style>
</head>
<body>
<div class="quiz-page">
  <a href="index.html" class="quiz-logo">
    <div class="quiz-logo-mark">
      <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" width="20" height="20" stroke-linecap="round"><path d="M12 3C7 3 3 7 3 12s4 9 9 9 9-4 9-9-4-9-9-9z"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>
    </div>
    <span class="quiz-logo-brand">Apavi <span>Green</span></span>
  </a>

  <form class="cuestionario-form" novalidate>
    <div class="quiz-progress-track"><div class="quiz-progress-bar"></div></div>
    <div class="quiz-step-label-row">
      <span class="quiz-step-num-label">Paso 1 de 4</span>
      <span style="font-size:12px;color:rgba(255,255,255,.3);">Sin compromiso · Respuesta en 24h</span>
    </div>

    <!-- PASO 1: Tipo de espacio -->
    <div class="quiz-step-panel">
      <div class="quiz-step-title">¿Qué tipo de espacio quieres transformar?</div>
      <div class="quiz-options-grid">
        <div class="quiz-option" data-key="tipo" data-val="jardin"><div class="quiz-option-icon">🌿</div><div class="quiz-option-label">Jardín</div></div>
        <div class="quiz-option" data-key="tipo" data-val="piscina"><div class="quiz-option-icon">🏊</div><div class="quiz-option-label">Piscina</div></div>
        <div class="quiz-option" data-key="tipo" data-val="terraza"><div class="quiz-option-icon">🏡</div><div class="quiz-option-label">Terraza</div></div>
        <div class="quiz-option" data-key="tipo" data-val="deportivo"><div class="quiz-option-icon">⚽</div><div class="quiz-option-label">Deportivo</div></div>
        <div class="quiz-option" data-key="tipo" data-val="vertical"><div class="quiz-option-icon">🌳</div><div class="quiz-option-label">Vertical</div></div>
        <div class="quiz-option" data-key="tipo" data-val="corporativo"><div class="quiz-option-icon">🏢</div><div class="quiz-option-label">Corporativo</div></div>
      </div>
      <div class="quiz-nav">
        <button type="button" class="btn-quiz-prev" style="visibility:hidden">← Anterior</button>
        <button type="button" class="btn-quiz-next">Siguiente →</button>
      </div>
    </div>

    <!-- PASO 2: Superficie -->
    <div class="quiz-step-panel" style="display:none">
      <div class="quiz-step-title">¿Cuántos metros cuadrados aproximadamente?</div>
      <div class="quiz-pills">
        <div class="quiz-option pill" data-key="superficie" data-val="menos20"><div class="quiz-option-label">Menos de 20 m²</div></div>
        <div class="quiz-option pill" data-key="superficie" data-val="20-50"><div class="quiz-option-label">20 – 50 m²</div></div>
        <div class="quiz-option pill" data-key="superficie" data-val="50-100"><div class="quiz-option-label">50 – 100 m²</div></div>
        <div class="quiz-option pill" data-key="superficie" data-val="mas100"><div class="quiz-option-label">Más de 100 m²</div></div>
        <div class="quiz-option pill" data-key="superficie" data-val="nosé"><div class="quiz-option-label">No lo sé aún</div></div>
      </div>
      <div class="quiz-nav">
        <button type="button" class="btn-quiz-prev">← Anterior</button>
        <button type="button" class="btn-quiz-next">Siguiente →</button>
      </div>
    </div>

    <!-- PASO 3: Urgencia -->
    <div class="quiz-step-panel" style="display:none">
      <div class="quiz-step-title">¿Cuándo necesitas el presupuesto?</div>
      <div class="quiz-pills">
        <div class="quiz-option pill" data-key="urgencia" data-val="urgente"><div class="quiz-option-label">Urgente (menos de 1 semana)</div></div>
        <div class="quiz-option pill" data-key="urgencia" data-val="este-mes"><div class="quiz-option-label">Este mes</div></div>
        <div class="quiz-option pill" data-key="urgencia" data-val="1-3-meses"><div class="quiz-option-label">En 1 a 3 meses</div></div>
        <div class="quiz-option pill" data-key="urgencia" data-val="informarme"><div class="quiz-option-label">Solo quiero informarme</div></div>
      </div>
      <div class="quiz-nav">
        <button type="button" class="btn-quiz-prev">← Anterior</button>
        <button type="button" class="btn-quiz-next">Siguiente →</button>
      </div>
    </div>

    <!-- PASO 4: Contacto -->
    <div class="quiz-step-panel" style="display:none">
      <div class="quiz-step-title">¿A dónde te enviamos el presupuesto?</div>
      <div class="form-field"><label>Nombre *</label><input type="text" name="nombre" placeholder="Tu nombre" required/></div>
      <div class="form-field"><label>Teléfono / WhatsApp *</label><input type="tel" name="telefono" placeholder="+34 XXX XXX XXX" required/></div>
      <div class="form-field"><label>Email (opcional)</label><input type="email" name="email" placeholder="tu@email.com"/></div>
      <div class="form-field"><label>Cuéntanos más (opcional)</label><textarea name="mensaje" placeholder="Describe tu proyecto, si tienes fotos del espacio las puedes enviar por WhatsApp..."></textarea></div>
      <button type="submit" class="btn-quiz-submit">Enviar solicitud de presupuesto →</button>
      <div class="quiz-nav" style="margin-top:12px;">
        <button type="button" class="btn-quiz-prev">← Anterior</button>
        <span></span>
      </div>
    </div>
  </form>
</div>
<script src="assets/js/cuestionario.js"></script>
</body>
</html>
```

- [ ] Open `cuestionario.html` — dark background, logo, progress bar, step 1 grid visible.
- [ ] Click "Jardín" → auto-advances to step 2 after 400ms. Progress bar at 50%.
- [ ] Step 4 → fill nombre + teléfono → submit → success screen appears.
- [ ] Test URL params: `cuestionario.html?tipo=deportivo` → state.tipo = 'deportivo' (check console: `window._quiz.state`).
- [ ] Commit: `git add cuestionario.html && git commit -m "feat: build multi-step lead form"`

---

## Task 11: landing.html

**Files:**
- Create: `landing.html`

- [ ] Create `landing.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta name="description" content="Presupuesto gratuito de césped artificial en 24h — Apavi Green"/>
  <title>Césped artificial Gran Canaria — Presupuesto gratis en 24h | Apavi Green</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="assets/css/tokens.css"/>
  <link rel="stylesheet" href="assets/css/main.css"/>
  <style>
    body { background: var(--g950); }
    .landing-header { padding: 20px 40px; display: flex; align-items: center; justify-content: center; border-bottom: 1px solid rgba(255,255,255,.06); }
    .landing-hero { padding: 72px 24px; text-align: center; max-width: 680px; margin: 0 auto; }
    .landing-tag { display: inline-flex; align-items: center; gap: 7px; background: rgba(46,181,112,.15); border: 1px solid rgba(46,181,112,.3); color: var(--g300); font-size: 12px; font-weight: 600; padding: 5px 14px; border-radius: var(--r999); margin-bottom: 24px; }
    .landing-h1 { font-family: var(--font-h); font-size: clamp(32px, 5vw, 54px); font-weight: 900; color: #fff; line-height: 1.1; letter-spacing: -.02em; margin-bottom: 18px; }
    .landing-h1 em { font-style: normal; color: var(--g400); }
    .landing-sub { font-size: 18px; color: rgba(255,255,255,.6); margin-bottom: 36px; line-height: 1.6; }
    .landing-cta { display: flex; flex-direction: column; align-items: center; gap: 14px; }
    .landing-trust { display: flex; justify-content: center; gap: 32px; margin-top: 48px; flex-wrap: wrap; }
    .landing-trust-item { text-align: center; }
    .landing-trust-num   { font-family: var(--font-h); font-size: 26px; font-weight: 900; color: #fff; }
    .landing-trust-label { font-size: 12px; color: rgba(255,255,255,.4); margin-top: 2px; }
    .landing-testimonial { max-width: 520px; margin: 56px auto 0; background: rgba(255,255,255,.04); border: 1px solid rgba(255,255,255,.08); border-radius: var(--r16); padding: 28px 32px; text-align: left; }
    .landing-testimonial blockquote { font-size: 16px; color: rgba(255,255,255,.75); line-height: 1.65; font-style: italic; margin-bottom: 16px; }
    .landing-testimonial cite { font-size: 13px; color: var(--g400); font-style: normal; font-weight: 600; }
    .landing-footer { padding: 28px; text-align: center; border-top: 1px solid rgba(255,255,255,.06); margin-top: 56px; }
    .landing-footer a { font-size: 12px; color: rgba(255,255,255,.3); margin: 0 10px; }
  </style>
</head>
<body>
  <header class="landing-header">
    <a href="index.html" style="display:flex;align-items:center;gap:10px;">
      <div style="width:34px;height:34px;background:linear-gradient(135deg,var(--g700),var(--g500));border-radius:9px;display:flex;align-items:center;justify-content:center;">
        <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" width="18" height="18" stroke-linecap="round"><path d="M12 3C7 3 3 7 3 12s4 9 9 9 9-4 9-9-4-9-9-9z"/></svg>
      </div>
      <span style="font-family:var(--font-h);font-size:17px;font-weight:800;color:#fff;">Apavi <span style="color:var(--g400)">Green</span></span>
    </a>
  </header>

  <main class="landing-hero">
    <div class="landing-tag"><span style="width:6px;height:6px;background:var(--g400);border-radius:50%;display:inline-block;"></span>Especialistas · Gran Canaria · +500 proyectos</div>
    <h1 class="landing-h1">Tu jardín <em>perfecto</em><br/>empieza aquí.</h1>
    <p class="landing-sub">Instalación profesional de césped artificial, jardines verticales y pavimentos. Presupuesto detallado y gratuito en menos de 24 horas.</p>
    <div class="landing-cta">
      <a href="cuestionario.html" class="btn-primary" style="font-size:17px;padding:16px 36px;">Quiero mi presupuesto gratis →</a>
      <a href="https://wa.me/34XXXXXXXXX" style="display:flex;align-items:center;gap:8px;color:rgba(255,255,255,.55);font-size:14px;font-weight:500;">
        💬 O escríbenos por WhatsApp ahora
      </a>
    </div>
    <div class="landing-trust">
      <div class="landing-trust-item"><div class="landing-trust-num">+500</div><div class="landing-trust-label">Proyectos realizados</div></div>
      <div class="landing-trust-item"><div class="landing-trust-num">15 años</div><div class="landing-trust-label">de experiencia</div></div>
      <div class="landing-trust-item"><div class="landing-trust-num">24h</div><div class="landing-trust-label">Presupuesto gratis</div></div>
      <div class="landing-trust-item"><div class="landing-trust-num">10 años</div><div class="landing-trust-label">de garantía</div></div>
    </div>
    <div class="landing-testimonial">
      <blockquote>"Apavi Green transformó nuestro jardín completamente. Trabajo impecable, en plazo y dentro del presupuesto. Lo recomendamos a todo el mundo."</blockquote>
      <cite>— Cliente satisfecho · Las Palmas de Gran Canaria</cite>
    </div>
  </main>

  <footer class="landing-footer">
    <a href="#">Política de privacidad</a>
    <a href="#">Aviso legal</a>
    <a href="index.html">Web corporativa</a>
  </footer>
</body>
</html>
```

- [ ] Open `landing.html` — dark background, headline, CTA, trust numbers, testimonial. No nav.
- [ ] Click CTA → goes to `cuestionario.html`.
- [ ] Commit: `git add landing.html && git commit -m "feat: build conversion landing page"`

---

## Task 12: proyectos.html — Portfolio completo

**Files:**
- Create: `proyectos.html`

- [ ] Create `proyectos.html` using same nav/footer as index.html. Key differences:
  - Hero simple: `<section>` con fondo verde, H1 "Todos nuestros proyectos", subtítulo
  - Portfolio grid completo (mínimo 12 cards, con placeholders de gradiente hasta tener fotos)
  - Todos los filtros disponibles
  - Sin configurador ni slider (página limpia de portfolio)

Key structure:
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <!-- same head as index.html, title: "Proyectos de césped artificial — Apavi Green" -->
</head>
<body>
  <!-- NAV -->
  <section style="background:linear-gradient(135deg,var(--g950),var(--g900));padding:72px 0 56px;text-align:center;">
    <div class="container">
      <div class="section-label" style="color:var(--g400)">Nuestro trabajo</div>
      <h1 style="font-family:var(--font-h);font-size:clamp(32px,4vw,52px);font-weight:900;color:#fff;letter-spacing:-.02em;margin-bottom:14px;">
        Más de <em style="color:var(--g400);font-style:normal;">500 proyectos</em> realizados
      </h1>
      <p style="font-size:17px;color:rgba(255,255,255,.6);max-width:500px;margin:0 auto;">Instalaciones de césped artificial, jardines verticales, campos deportivos y más en toda España.</p>
    </div>
  </section>

  <section class="section portfolio-section">
    <div class="container">
      <div class="portfolio-filters">
        <!-- same chips as index.html -->
      </div>
      <div class="portfolio-grid">
        <!-- 12+ cards with data-cat attributes -->
      </div>
    </div>
  </section>

  <!-- CTA → cuestionario -->
  <!-- FOOTER -->
  <script src="assets/js/portfolio.js"></script>
</body>
</html>
```

- [ ] Open `proyectos.html` — hero verde, grid 12 cards, filtros funcionan.
- [ ] Commit: `git add proyectos.html && git commit -m "feat: build full portfolio page"`

---

## Task 13: SEO service pages (×5)

**Files:**
- Create: `cesped-artificial.html`, `jardines-verticales.html`, `instalaciones-deportivas.html`, `espacios-infantiles.html`, `moqueta-ferial.html`

Each page follows the exact same template — only the title, keyword, color accent of top section, emoji, description and FAQ content change.

- [ ] Create the **template structure** (same for all 5 — copy-paste then edit content):

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta name="description" content="[UNIQUE DESCRIPTION PER SERVICE]"/>
  <title>[KEYWORD PRINCIPAL] | Apavi Green</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="assets/css/tokens.css"/>
  <link rel="stylesheet" href="assets/css/main.css"/>
  <link rel="stylesheet" href="assets/css/components.css"/>
</head>
<body>
  <!-- NAV -->

  <!-- HERO SEO -->
  <section style="background:linear-gradient(135deg,var(--g950),var(--g900));padding:88px 0;display:grid;">
    <div class="container" style="display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center;">
      <div>
        <div class="section-label" style="color:var(--g400)">[TIPO DE SERVICIO]</div>
        <h1 style="font-family:var(--font-h);font-size:clamp(28px,3.5vw,48px);font-weight:900;color:#fff;line-height:1.15;letter-spacing:-.02em;margin-bottom:16px;">[H1 CON KEYWORD]</h1>
        <p style="font-size:17px;color:rgba(255,255,255,.65);margin-bottom:28px;line-height:1.6;">[DESCRIPCIÓN]</p>
        <a href="cuestionario.html?tipo=[TIPO]" class="btn-primary">Pedir presupuesto gratis →</a>
      </div>
      <div style="background:linear-gradient(135deg,var(--g800),var(--g600));border-radius:var(--r20);height:320px;display:flex;align-items:center;justify-content:center;font-size:72px;opacity:.7;">[EMOJI]</div>
    </div>
  </section>

  <!-- BENEFICIOS (3 columnas con icono) -->
  <section class="section">
    <div class="container">
      <div class="section-header"><div class="section-label">Ventajas</div><div class="deco-line"></div><h2 class="section-title">¿Por qué elegir <em>Apavi Green</em>?</h2></div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;">
        <!-- 3 benefit cards -->
      </div>
    </div>
  </section>

  <!-- PROCESO (4 pasos numerados) -->
  <section class="section" style="background:var(--n50)">
    <div class="container">
      <div class="section-header"><div class="section-label">Cómo trabajamos</div><div class="deco-line"></div><h2 class="section-title">El proceso de <em>instalación</em></h2></div>
      <!-- 4 numbered steps -->
    </div>
  </section>

  <!-- GALERÍA (4 proyectos del mismo tipo) -->
  <section class="section">
    <div class="container">
      <div class="section-header"><div class="section-label">Proyectos [TIPO]</div><div class="deco-line"></div><h2 class="section-title">Trabajos <em>realizados</em></h2></div>
      <div class="portfolio-grid" style="grid-template-columns:repeat(2,1fr)">
        <!-- 4 placeholder cards with data-cat -->
      </div>
    </div>
  </section>

  <!-- FAQs (acordeón con 5 preguntas SEO) -->
  <section class="section" style="background:var(--n50)">
    <div class="container" style="max-width:720px;">
      <div class="section-header"><div class="section-label">Preguntas frecuentes</div><div class="deco-line"></div><h2 class="section-title">Lo que más nos <em>preguntan</em></h2></div>
      <!-- 5 FAQ items with accordion JS (inline script) -->
    </div>
  </section>

  <!-- CTA FINAL -->
  <section style="background:var(--g950);padding:72px 0;text-align:center;">
    <div class="container">
      <h2 style="font-family:var(--font-h);font-size:clamp(24px,3vw,40px);font-weight:800;color:#fff;margin-bottom:14px;">¿Listo para tu proyecto?</h2>
      <p style="font-size:16px;color:rgba(255,255,255,.6);margin-bottom:28px;">Presupuesto gratuito y sin compromiso en menos de 24 horas.</p>
      <a href="cuestionario.html?tipo=[TIPO]" class="btn-primary">Solicitar presupuesto →</a>
    </div>
  </section>

  <!-- FOOTER -->
  <script>
    // Inline FAQ accordion (no external file needed)
    document.querySelectorAll('.faq-item').forEach(item => {
      item.querySelector('.faq-question').addEventListener('click', () => {
        const open = item.classList.contains('open');
        document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
        if (!open) item.classList.add('open');
      });
    });
  </script>
</body>
</html>
```

**Per-page content:**

| Página | Tipo param | H1 | Emoji | 3 beneficios | 5 FAQ keywords |
|---|---|---|---|---|---|
| `cesped-artificial.html` | jardin | Césped artificial en Gran Canaria — instalación profesional | 🌿 | Sin mantenimiento · Resistente al sol · Aspecto natural | ¿Cuánto dura? · ¿Precio m²? · ¿Se instala sobre tierra? · ¿Resiste calor Canarias? · ¿Necesita riego? |
| `jardines-verticales.html` | vertical | Jardines verticales en Gran Canaria — diseño e instalación | 🌳 | Interior y exterior · Plantas naturales o artificiales · Diseño personalizado | ¿Cuánto pesa? · ¿Necesita riego automático? · ¿Dura en exterior? · ¿Precio m²? · ¿Mantenimiento? |
| `instalaciones-deportivas.html` | deportivo | Instalaciones deportivas con césped artificial homologado | ⚽ | Homologado FIFA/ITF · Alta resistencia · Drenaje profesional | ¿Qué césped para fútbol? · ¿Coste campo fútbol? · ¿Homologación? · ¿Cuánto dura? · ¿Mantenimiento? |
| `espacios-infantiles.html` | infantil | Césped artificial para espacios infantiles — seguro y suave | 👶 | Sin tóxicos · Amortiguación de caídas · Fácil limpieza | ¿Es seguro? · ¿Normativa EU? · ¿Temperatura verano? · ¿Precio? · ¿Para interior también? |
| `moqueta-ferial.html` | eventos | Moqueta ferial en Canarias — alquiler y venta para eventos | 🎪 | Montaje y desmontaje · Múltiples colores · Stock disponible | ¿Precio m² alquiler? · ¿Plazos mínimos? · ¿Instalación incluida? · ¿Transporte? · ¿Colores disponibles? |

- [ ] Build all 5 pages using the template, inserting per-page content from the table above.
- [ ] Open each in browser — verify hero H1 correct, 3 benefit cards, 4 steps, FAQ accordion works.
- [ ] Commit: `git add cesped-artificial.html jardines-verticales.html instalaciones-deportivas.html espacios-infantiles.html moqueta-ferial.html && git commit -m "feat: build 5 SEO service pages"`

---

## Task 14: SEO técnico — sitemap + robots + schema

**Files:**
- Create: `sitemap.xml`
- Create: `robots.txt`

- [ ] Create `sitemap.xml` (replace `https://apavigreen.es` with real domain when known):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://apavigreen.es/</loc><priority>1.0</priority><changefreq>weekly</changefreq></url>
  <url><loc>https://apavigreen.es/cesped-artificial.html</loc><priority>0.9</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://apavigreen.es/jardines-verticales.html</loc><priority>0.9</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://apavigreen.es/instalaciones-deportivas.html</loc><priority>0.9</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://apavigreen.es/espacios-infantiles.html</loc><priority>0.9</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://apavigreen.es/moqueta-ferial.html</loc><priority>0.9</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://apavigreen.es/proyectos.html</loc><priority>0.8</priority><changefreq>weekly</changefreq></url>
  <url><loc>https://apavigreen.es/cuestionario.html</loc><priority>0.7</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://apavigreen.es/landing.html</loc><priority>0.6</priority><changefreq>monthly</changefreq></url>
</urlset>
```

- [ ] Create `robots.txt`:

```
User-agent: *
Allow: /
Disallow: /_partials/
Sitemap: https://apavigreen.es/sitemap.xml
```

- [ ] Add LocalBusiness schema to `index.html` inside `<head>` (after CSS links):

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Apavi Green",
  "description": "Especialistas en instalación de césped artificial, jardines verticales e instalaciones deportivas en Gran Canaria",
  "url": "https://apavigreen.es",
  "telephone": "+34XXXXXXXXX",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Las Palmas de Gran Canaria",
    "addressRegion": "Gran Canaria",
    "addressCountry": "ES"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "28.1235",
    "longitude": "-15.4366"
  },
  "areaServed": "España",
  "priceRange": "€€",
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "08:00",
    "closes": "18:00"
  }
}
</script>
```

- [ ] Validate schema at https://search.google.com/test/rich-results (paste the JSON).
- [ ] Commit: `git add sitemap.xml robots.txt index.html && git commit -m "feat: add sitemap, robots.txt and LocalBusiness schema markup"`

---

## Task 15: Sustitución de placeholders con datos reales (Josep)

This task requires content from Josep — do not implement until content is provided.

- [ ] Replace all `+34 XXX XXX XXX` with real phone number in: nav, landing.html, cuestionario.js
- [ ] Replace `https://wa.me/34XXXXXXXXX` with real WhatsApp link (format: `https://wa.me/34XXXXXXXXX` no spaces/dashes)
- [ ] Replace `YOUR_FORMSPREE_ID` in `cuestionario.js` with real Formspree ID (create free account at formspree.io, create form, get ID)
- [ ] Update `sitemap.xml` and `robots.txt` with real domain
- [ ] Update schema in `index.html` with real phone, address, coordinates
- [ ] Add real project photos to `assets/img/proyectos/` and update portfolio cards (replace gradient placeholders)
- [ ] Add `assets/img/logo/logo.svg` and update nav icon (replace SVG placeholder)
- [ ] Update price ranges in `configurador.js` `PRECIOS` object with real €/m² values
- [ ] Commit: `git commit -m "content: replace all placeholders with real data"`

---

## Self-Review

**Spec coverage check:**
- ✅ Home with all 7 sections (Tasks 9)
- ✅ Slider antes/después (Task 5)
- ✅ Price configurador real-time (Task 6)
- ✅ Portfolio filterable (Task 7, 12)
- ✅ Multi-step questionnaire, 4 steps, Formspree (Tasks 8, 10)
- ✅ Landing page no-nav (Task 11)
- ✅ 5 SEO service pages with H1/keyword/FAQs (Task 13)
- ✅ sitemap.xml + robots.txt + LocalBusiness schema (Task 14)
- ✅ Responsive breakpoints covered in main.css + components.css (Tasks 2, 3)
- ✅ CSS tokens exact brand kit values (Task 1)
- ✅ URL params from configurador → cuestionario (Tasks 6, 8)
- ✅ Placeholder content checklist for Josep (Task 15)

**Gaps:** None found. Tienda online is out of scope — separate spec/plan in next phase.

---

*Plan listo para implementar — 2026-05-25 · Apavi Green · Nehunaya Flow*

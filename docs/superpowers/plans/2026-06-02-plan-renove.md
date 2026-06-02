# Plan Renove — Landing Page — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear `plan-renove.html`, una landing page de campaña permanente para el servicio Plan Renove de Apavi Green, con retirada de césped viejo gratis como gancho principal.

**Architecture:** Archivo HTML único con estilos inline `<style>`, siguiendo el patrón de `landing.html`. Sin dependencias JS externas. Reutiliza los CSS tokens del proyecto (`assets/css/tokens.css`, `main.css`, `components.css`). Sin modificar ningún archivo existente.

**Tech Stack:** HTML5 semántico · CSS inline (patrón landing.html) · Vanilla JS (año footer) · Google Fonts (Plus Jakarta Sans + Inter)

---

## Archivos

| Acción | Ruta |
|--------|------|
| Crear | `plan-renove.html` |
| Crear carpeta | `assets/img/renove/` (4 placeholders SVG) |

---

### Task 1: Carpeta de imágenes con placeholders

**Files:**
- Crear: `assets/img/renove/placeholder.svg` (reutilizado 4 veces con nombres distintos)

- [ ] **Crear la carpeta y los 4 placeholders SVG**

Crear `assets/img/renove/renove-1.jpg` como SVG renombrado — usar este contenido para los 4 archivos (renove-1.jpg, renove-2.jpg, renove-3.jpg, renove-4.jpg). Como son placeholders SVG guardados como .jpg el navegador los mostrará igualmente:

Crear el archivo `assets/img/renove/placeholder.svg`:
```svg
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="400" viewBox="0 0 600 400">
  <rect width="600" height="400" fill="#143D25"/>
  <rect x="240" y="160" width="120" height="80" rx="8" fill="#2EB570" opacity="0.3"/>
  <text x="300" y="210" font-family="sans-serif" font-size="14" fill="rgba(255,255,255,0.4)" text-anchor="middle">📸 Foto antes/después</text>
  <text x="300" y="230" font-family="sans-serif" font-size="11" fill="rgba(255,255,255,0.25)" text-anchor="middle">Proyecto de renovación real</text>
</svg>
```

Copiar como `renove-1.jpg`, `renove-2.jpg`, `renove-3.jpg`, `renove-4.jpg` en `assets/img/renove/`.

- [ ] **Verificar carpeta**

```
ls assets/img/renove/
```
Esperado: 4 archivos + placeholder.svg

- [ ] **Commit**

```bash
git add assets/img/renove/
git commit -m "feat: carpeta assets renove con placeholders"
```

---

### Task 2: Head, estilos y header

**Files:**
- Crear: `plan-renove.html`

- [ ] **Crear `plan-renove.html` con head + estilos completos + header**

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Plan Renove &mdash; Renueva tu C&eacute;sped con Retirada Gratis &mdash; Apavi Green</title>
  <meta name="description" content="Plan Renove de Apavi Green: retiramos tu c&eacute;sped viejo gratis e instalamos c&eacute;sped artificial de calidad profesional. Presupuesto gratuito en 24h. Gran Canaria.">
  <meta name="robots" content="noindex">
  <link rel="canonical" href="https://apavigreen.com/plan-renove.html">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/tokens.css">
  <link rel="stylesheet" href="assets/css/main.css">
  <link rel="stylesheet" href="assets/css/components.css">
  <style>
    body { background: var(--n950); color: #fff; margin: 0; }

    /* Header */
    .lp-header { padding: 18px 40px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,.06); position: sticky; top: 0; background: var(--n950); z-index: 100; }
    .lp-phone { display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,.7); text-decoration: none; transition: color .2s; }
    .lp-phone:hover { color: var(--g400); }

    /* Badge Plan Renove */
    .renove-badge { display: inline-block; background: rgba(196,148,48,.15); border: 1px solid #C49430; color: #C49430; font-size: 11px; font-weight: 800; padding: 6px 16px; border-radius: 999px; letter-spacing: 1.5px; margin-bottom: 20px; }

    /* Hero */
    .lp-hero { padding: 72px 20px 56px; text-align: center; background: linear-gradient(160deg, var(--g950), var(--g900) 60%, var(--n950)); }
    .lp-hero h1 { font-family: var(--font-h); font-size: clamp(28px,5vw,54px); font-weight: 900; color: #fff; line-height: 1.1; margin: 0 0 16px; letter-spacing: -.02em; max-width: 740px; margin-left: auto; margin-right: auto; }
    .lp-hero h1 em { font-style: normal; color: var(--g400); }
    .lp-hero p { font-size: 17px; color: rgba(255,255,255,.5); max-width: 500px; margin: 0 auto 32px; line-height: 1.65; }

    /* CTA group */
    .lp-cta-col { display: flex; flex-direction: column; gap: 12px; max-width: 320px; margin: 0 auto; }
    .btn-whatsapp { display: block; background: #25D366; color: #fff; font-family: var(--font-h); font-size: 16px; font-weight: 800; padding: 16px 28px; border-radius: var(--r12); text-decoration: none; transition: filter .2s; }
    .btn-whatsapp:hover { filter: brightness(1.1); }
    .btn-call { display: block; background: var(--g500); color: #fff; font-family: var(--font-h); font-size: 16px; font-weight: 700; padding: 16px 28px; border-radius: var(--r12); text-decoration: none; transition: filter .2s; }
    .btn-call:hover { filter: brightness(1.1); }
    .btn-form-link { display: block; font-size: 13px; color: rgba(255,255,255,.4); text-decoration: underline; text-underline-offset: 3px; margin-top: 6px; transition: color .2s; }
    .btn-form-link:hover { color: rgba(255,255,255,.7); }

    /* Stats */
    .lp-stats { display: flex; justify-content: center; gap: 48px; margin-top: 48px; padding-top: 36px; border-top: 1px solid rgba(255,255,255,.08); flex-wrap: wrap; }
    .lp-stat-num { font-family: var(--font-h); font-size: 30px; font-weight: 900; color: #fff; }
    .lp-stat-label { font-size: 12px; color: rgba(255,255,255,.35); margin-top: 4px; }

    /* Trust bar */
    .lp-trust { display: flex; justify-content: center; gap: 32px; padding: 22px 20px; background: rgba(255,255,255,.03); border-bottom: 1px solid rgba(255,255,255,.06); flex-wrap: wrap; }
    .lp-trust-item { font-size: 13px; font-weight: 600; color: rgba(255,255,255,.55); }

    /* Sections */
    .lp-section { padding: 72px 20px; max-width: 860px; margin: 0 auto; }
    .lp-section-tag { font-size: 11px; font-weight: 700; color: var(--g400); letter-spacing: 1.5px; text-transform: uppercase; text-align: center; margin-bottom: 12px; }
    .lp-section-title { font-family: var(--font-h); font-size: clamp(22px,3vw,34px); font-weight: 800; color: #fff; text-align: center; margin: 0 0 40px; letter-spacing: -.02em; }
    .lp-section-title em { font-style: normal; color: var(--g400); }

    /* Pain cards */
    .pain-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; max-width: 540px; margin: 0 auto 28px; }
    .pain-card { background: rgba(255,255,255,.04); border: 1px solid rgba(255,255,255,.07); border-radius: var(--r12); padding: 18px; font-size: 14px; color: rgba(255,255,255,.55); line-height: 1.5; }
    .solution-box { background: rgba(46,181,112,.08); border: 1px solid rgba(46,181,112,.2); border-radius: var(--r12); padding: 20px 24px; text-align: center; font-size: 15px; font-weight: 600; color: var(--g300); max-width: 540px; margin: 0 auto; }

    /* Steps */
    .steps { display: flex; align-items: flex-start; justify-content: center; gap: 0; max-width: 560px; margin: 0 auto; }
    .step { flex: 1; text-align: center; padding: 0 8px; }
    .step-num { width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: var(--font-h); font-weight: 900; font-size: 18px; margin: 0 auto 12px; }
    .step-num-green { background: var(--g500); color: #0B2918; }
    .step-num-gold  { background: #C49430; color: #0B2918; }
    .step-title { font-family: var(--font-h); font-size: 14px; font-weight: 700; color: #fff; margin-bottom: 4px; }
    .step-sub { font-size: 12px; color: rgba(255,255,255,.4); }
    .step-badge-free { font-size: 11px; font-weight: 800; color: var(--g400); }
    .step-arrow { color: rgba(255,255,255,.2); font-size: 20px; padding-top: 14px; flex-shrink: 0; }

    /* Gallery */
    .gallery-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
    .gallery-item { border-radius: var(--r12); overflow: hidden; aspect-ratio: 4/3; }
    .gallery-item img { width: 100%; height: 100%; object-fit: cover; display: block; transition: transform .4s ease; }
    .gallery-item:hover img { transform: scale(1.05); }

    /* Testimonial */
    .testimonial { background: rgba(46,181,112,.08); border: 1px solid rgba(46,181,112,.15); border-radius: var(--r16); padding: 40px 32px; text-align: center; max-width: 640px; margin: 0 auto; }
    .testimonial-text { font-size: 18px; color: rgba(255,255,255,.75); line-height: 1.7; font-style: italic; margin-bottom: 20px; }
    .testimonial-author { font-size: 13px; font-weight: 600; color: var(--g400); }
    .testimonial-stars { color: #C49430; font-size: 16px; margin-bottom: 4px; }

    /* Final CTA */
    .lp-final-cta { text-align: center; padding: 72px 20px 80px; background: linear-gradient(180deg, transparent, rgba(20,61,37,.4)); }
    .lp-final-cta h2 { font-family: var(--font-h); font-size: clamp(24px,4vw,42px); font-weight: 900; color: #fff; margin: 0 0 10px; letter-spacing: -.02em; }
    .lp-final-cta h2 em { font-style: normal; color: var(--g400); }
    .lp-final-cta p { font-size: 15px; color: rgba(255,255,255,.4); margin: 0 0 32px; }
    .btn-ghost-lp { display: block; background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.12); color: rgba(255,255,255,.6); font-size: 14px; font-weight: 600; padding: 14px 28px; border-radius: var(--r12); text-decoration: none; transition: background .2s; }
    .btn-ghost-lp:hover { background: rgba(255,255,255,.1); }

    /* Footer */
    .lp-footer { padding: 24px 40px; border-top: 1px solid rgba(255,255,255,.06); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; }
    .lp-footer p { font-size: 12px; color: rgba(255,255,255,.2); margin: 0; }
    .lp-footer a { color: rgba(255,255,255,.3); text-decoration: none; }
    .lp-footer a:hover { color: rgba(255,255,255,.6); }

    /* Responsive */
    @media (max-width: 640px) {
      .lp-header { padding: 14px 20px; }
      .lp-hero { padding: 52px 20px 40px; }
      .lp-stats { gap: 20px; }
      .lp-trust { gap: 14px; }
      .pain-grid { grid-template-columns: 1fr; }
      .steps { flex-direction: column; align-items: center; gap: 20px; }
      .step-arrow { display: none; }
      .gallery-grid { grid-template-columns: 1fr; }
      .lp-footer { flex-direction: column; align-items: flex-start; gap: 8px; }
    }
  </style>
</head>
<body>

<!-- HEADER -->
<header class="lp-header">
  <a href="index.html" class="nav-logo">
    <img src="assets/img/logo/logo-apavigreen.jpeg" alt="Apavi Green" style="height:38px;width:auto;border-radius:6px;">
  </a>
  <a href="tel:+34654765548" class="lp-phone">&#128222; +34 654 765 548</a>
</header>
```

- [ ] **Verificar** — abrir `plan-renove.html` en el navegador. El header debe verse con logo real y teléfono clicable.

---

### Task 3: Hero + Trust bar

**Files:**
- Modificar: `plan-renove.html` — añadir después del `</header>`

- [ ] **Añadir sección hero completa**

```html
<!-- HERO -->
<section class="lp-hero">
  <div class="renove-badge">&#10022; PLAN RENOVE APAVI GREEN &#10022;</div>
  <h1>Renueva tu c&eacute;sped viejo con <em>retirada incluida gratis</em></h1>
  <p>Retiramos tu c&eacute;sped actual sin coste. Instalamos c&eacute;sped artificial de calidad profesional con garant&iacute;a 10 a&ntilde;os.</p>
  <div class="lp-cta-col">
    <a href="https://wa.me/34654765548?text=Hola%2C%20me%20interesa%20el%20Plan%20Renove.%20Quisiera%20un%20presupuesto%20gratuito." class="btn-whatsapp" target="_blank" rel="noopener">&#128172; Pedir presupuesto por WhatsApp</a>
    <a href="tel:+34654765548" class="btn-call">&#128222; Llamar ahora &mdash; +34 654 765 548</a>
    <a href="cuestionario.html" class="btn-form-link">O rellena el formulario de presupuesto &rarr;</a>
  </div>
  <div class="lp-stats">
    <div><div class="lp-stat-num">+500</div><div class="lp-stat-label">Proyectos realizados</div></div>
    <div><div class="lp-stat-num">10 a&ntilde;os</div><div class="lp-stat-label">De garant&iacute;a</div></div>
    <div><div class="lp-stat-num">24h</div><div class="lp-stat-label">Respuesta presupuesto</div></div>
  </div>
</section>

<!-- TRUST BAR -->
<div class="lp-trust">
  <span class="lp-trust-item">&#10003; Equipo propio en Gran Canaria</span>
  <span class="lp-trust-item">&#10003; Sin subcontratas</span>
  <span class="lp-trust-item">&#10003; Presupuesto gratis en 24h</span>
</div>
```

- [ ] **Verificar** — badge dorado visible, dos botones en columna, trust bar bajo el hero.

---

### Task 4: Sección problema + cómo funciona

**Files:**
- Modificar: `plan-renove.html` — añadir después del trust bar

- [ ] **Añadir sección "¿Te suena esto?" y pasos**

```html
<!-- PROBLEMA -->
<div class="lp-section">
  <div class="lp-section-tag">&#191;Te suena esto?</div>
  <h2 class="lp-section-title">Tu c&eacute;sped est&aacute; deteriorado,<br>amarillo o de <em>mala calidad</em></h2>
  <div class="pain-grid">
    <div class="pain-card">&#128565; Se ve feo y aplastado</div>
    <div class="pain-card">&#127777;&#65039; No aguanta el calor canario</div>
    <div class="pain-card">&#128296; Te da problemas constantes</div>
    <div class="pain-card">&#128176; No era de calidad profesional</div>
  </div>
  <div class="solution-box">&#128161; Nosotros lo retiramos gratis y lo sustituimos por c&eacute;sped artificial profesional</div>
</div>

<!-- CÓMO FUNCIONA -->
<div style="padding: 0 20px 72px;">
  <div class="lp-section-tag" style="text-align:center;">C&oacute;mo funciona</div>
  <h2 class="lp-section-title">El Plan Renove en <em>3 pasos</em></h2>
  <div class="steps">
    <div class="step">
      <div class="step-num step-num-green">1</div>
      <div class="step-title">Nos contactas</div>
      <div class="step-sub">WhatsApp o tel&eacute;fono</div>
    </div>
    <div class="step-arrow">&rarr;</div>
    <div class="step">
      <div class="step-num step-num-green">2</div>
      <div class="step-title">Retiramos el viejo</div>
      <div class="step-badge-free">GRATIS &#10003;</div>
    </div>
    <div class="step-arrow">&rarr;</div>
    <div class="step">
      <div class="step-num step-num-gold">3</div>
      <div class="step-title">Instalamos el nuevo</div>
      <div class="step-sub">Garant&iacute;a 10 a&ntilde;os</div>
    </div>
  </div>
</div>
```

- [ ] **Verificar** — 4 tarjetas de dolor en grid 2×2, pasos horizontales con flechas, paso 2 con badge verde "GRATIS", paso 3 con círculo dorado.

---

### Task 5: Galería + testimonio + CTA final + footer + scripts

**Files:**
- Modificar: `plan-renove.html` — añadir las secciones restantes + cerrar `</body></html>`

- [ ] **Añadir galería**

```html
<!-- GALERÍA -->
<div class="lp-section" style="padding-top: 0;">
  <div class="lp-section-tag">Proyectos reales</div>
  <h2 class="lp-section-title">Renovaciones que <em>hablan por s&iacute; solas</em></h2>
  <div class="gallery-grid">
    <div class="gallery-item">
      <img src="assets/img/renove/renove-1.jpg" alt="Proyecto de renovaci&oacute;n de c&eacute;sped 1" loading="lazy">
    </div>
    <div class="gallery-item">
      <img src="assets/img/renove/renove-2.jpg" alt="Proyecto de renovaci&oacute;n de c&eacute;sped 2" loading="lazy">
    </div>
    <div class="gallery-item">
      <img src="assets/img/renove/renove-3.jpg" alt="Proyecto de renovaci&oacute;n de c&eacute;sped 3" loading="lazy">
    </div>
    <div class="gallery-item">
      <img src="assets/img/renove/renove-4.jpg" alt="Proyecto de renovaci&oacute;n de c&eacute;sped 4" loading="lazy">
    </div>
  </div>
</div>
```

- [ ] **Añadir testimonio**

```html
<!-- TESTIMONIO -->
<div class="lp-section" style="padding-top: 0;">
  <div class="testimonial">
    <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
    <p class="testimonial-text">&ldquo;Ten&iacute;a un c&eacute;sped de hace 8 a&ntilde;os hecho polvo. Apavi Green lo retir&oacute; todo y en dos d&iacute;as ten&iacute;a uno nuevo precioso. Y lo mejor, la retirada sin coste.&rdquo;</p>
    <div class="testimonial-author">— Mar&iacute;a G., Las Palmas de Gran Canaria</div>
  </div>
</div>
```

- [ ] **Añadir CTA final + footer + scripts**

```html
<!-- CTA FINAL -->
<div class="lp-final-cta">
  <h2>&iquest;Listo para renovar <em>tu c&eacute;sped</em>?</h2>
  <p>Presupuesto gratis &middot; Sin compromiso &middot; Respuesta en 24h</p>
  <div class="lp-cta-col" style="margin: 0 auto;">
    <a href="https://wa.me/34654765548?text=Hola%2C%20me%20interesa%20el%20Plan%20Renove.%20Quisiera%20un%20presupuesto%20gratuito." class="btn-whatsapp" target="_blank" rel="noopener">&#128172; WhatsApp &mdash; Pedir presupuesto</a>
    <a href="tel:+34654765548" class="btn-call">&#128222; Llamar &mdash; +34 654 765 548</a>
    <a href="cuestionario.html" class="btn-ghost-lp">Formulario de presupuesto &rarr;</a>
  </div>
</div>

<!-- FOOTER -->
<footer class="lp-footer">
  <p>&copy; <span id="footerYear"></span> Apavi Green &middot; Todos los derechos reservados</p>
  <p>
    <a href="aviso-legal.html">Aviso Legal</a> &middot;
    <a href="privacidad.html">Privacidad</a>
  </p>
</footer>

<script>document.getElementById('footerYear').textContent = new Date().getFullYear();</script>
<script src="assets/js/nav.js"></script>
<script src="assets/js/cookies.js"></script>
</body>
</html>
```

- [ ] **Verificar completo** — abrir `plan-renove.html` en navegador:
  - Hero: badge dorado, headline, dos botones verdes, link formulario, stats
  - Trust bar: 3 ítems
  - Sección problema: 4 tarjetas + caja solución verde
  - Pasos: horizontal con flechas, badge GRATIS en paso 2, dorado en paso 3
  - Galería: 4 imágenes placeholder en grid 2×2 con hover zoom
  - Testimonio: tarjeta con borde verde y 5 estrellas
  - CTA final: mismos 3 CTAs + gradiente
  - Footer: copyright dinámico + links legales
  - Móvil (redimensionar a 375px): CTAs en columna, galería en 1 columna, pasos en vertical

- [ ] **Commit final**

```bash
git add plan-renove.html assets/img/renove/
git commit -m "feat: landing Plan Renove — retirada de césped viejo incluida gratis"
```

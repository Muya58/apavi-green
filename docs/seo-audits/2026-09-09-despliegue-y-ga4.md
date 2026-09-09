# Sesión 4-9 de septiembre 2026 — Despliegue de la auditoría SEO + GA4/GTM

## Resumen

Todos los hallazgos críticos y altos de la auditoría del 4 de septiembre (`2026-09-04-auditoria-seo-apavigreen.md`) están **en producción y verificados en vivo**:

- Teléfono/WhatsApp roto en `proyectos.html` → arreglado, verificado (abre WhatsApp de Apavigreensl)
- 7 rutas de imagen rotas en `proyectos.html` → arregladas
- 3 artículos de blog convertidos de JS a páginas estáticas indexables
- 31 imágenes convertidas a WebP (-68% peso)
- Lazy loading en la galería de proyectos
- Documentos internos (brand-kit, guías, backups) movidos a `docs/internal-pages/`, fuera de producción
- Banner de cookies añadido donde faltaba (home, blog, quienes-somos, resinas-epoxi) — antes solo 12 de 24 páginas lo tenían
- Redes sociales conectadas: Instagram y Facebook → `apavigreensl`
- Plan Renove: las 3 fotos de "Renovaciones que hablan por sí solas" cargan bien (era el bug que arrancó la sesión de hoy)

## Despliegue

- Hosting: AWS, subida manual por FTP (servidor `52.30.159.68`, usuario `apavigreen`)
- `apavigreen.com` (sin www) redirige automáticamente a `www.apavigreen.com` — confirmado en navegador
- Nota técnica pendiente (baja prioridad): todo el código (canonical, sitemap.xml, schema) declara `https://apavigreen.com/...` sin www, pero la versión "real" servida y donde está Search Console es `www.apavigreen.com`. Funciona vía redirect 301, pero sería más limpio alinear todo a www en algún momento.

## GA4 / Google Tag Manager

- Propiedad GA4 creada: `G-P68MBLLY5R`
- Contenedor GTM creado y publicado: `GTM-KVGB6TK4`, con una etiqueta "Etiqueta de Google" (tipo correcto, no "evento de GA4") apuntando al Measurement ID, activador `Initialization - All Pages`
- `assets/js/analytics.js` actualizado para cargar el contenedor GTM (no gtag.js directo) — mismo sistema de antes: solo carga si el usuario acepta "todas" en el banner de cookies (`ag_cookie_consent` en localStorage), evento `ag:consent` disparado desde `cookies.js` en el clic de aceptar
- Verificado en Tiempo Real de GA4 tras aceptar cookies

## Hallazgo de Search Console (contexto, sin resolver)

Datos de 3 meses: 22 clics, 1.190 impresiones, posición media 43, CTR 1,9%. Google ve el sitio (impresiones reales) pero las páginas rankean demasiado abajo para generar clics — típico de dominio joven sin backlinks. `/resinas-epoxi.html` y `/quienes-somos.html` van sorprendentemente bien (posición 12.5 y 3.6). `/cesped-artificial.html` es la página con más impresiones (586) pero peor posición (56.8) — la mayor oportunidad de mejora vía autoridad externa (Google Business Profile, reseñas, backlinks), no más cambios de código.

## Pendiente para otra sesión (prioridad media/baja del informe original)

1. Títulos que se cortan en el SERP (`index.html` 72 car., `blog/jardines-verticales-gran-canaria.html` 82 car.)
2. `title` ≠ `og:title` en `cesped-artificial.html` y `jardines-verticales.html`
3. Plan Renove sublinkado internamente (solo enlazado desde blog.html e index.html)
4. Meta robots inconsistente entre páginas
5. Alinear canonical/sitemap/schema a `www.apavigreen.com` (ver nota de despliegue arriba)
6. Schema LocalBusiness sin `postalCode` ni `geo`
7. Limpieza opcional: archivos sueltos de páginas de servicio (`pavimento-pvc.html`, `landing.html`, etc.) que quedaron mal ubicados dentro de `blog/` en el servidor, de una subida antigua — no rompen nada, se pueden borrar cuando se quiera

## Rama de trabajo

`claude/seo-audit-apavigreen-df8fdh` — todos los commits de esta sesión están ahí, no fusionados a `master` todavía.

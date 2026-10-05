# Auditoría SEO — 5 de octubre 2026

## Alcance y limitación

Auditoría sobre el código del repositorio (rama `claude/seo-audit-apavigreen-df8fdh`). **No he podido acceder a `www.apavigreen.com` en vivo** (el proxy de red de este entorno bloquea el dominio), así que no he podido verificar Search Console, PageSpeed/Core Web Vitals reales, ni confirmar que lo publicado por FTP coincide exactamente con este código. Todo lo de abajo es auditoría estática de las 29 páginas HTML del repo.

## Resumen ejecutivo

El sitio sigue técnicamente sano (sin enlaces rotos, sin JSON-LD inválido, sin imágenes sin `alt`, sin títulos duplicados). Los problemas nuevos son casi todos **efecto colateral de la expansión de zonas del mes pasado**: las páginas nuevas no están enlazadas desde el resto del sitio, y seguimos sin resolver la inconsistencia www que ya se señaló en septiembre.

**Top 3 prioridades:**
1. Las páginas de zona (`zonas.html` + Tenerife/Cádiz/Málaga/Sevilla) están prácticamente aisladas del resto del sitio — solo las enlaza la home.
2. Canonical/schema siguen declarando `apavigreen.com` sin `www`, mientras la web real se sirve en `www.apavigreen.com` (señalado en septiembre, sigue sin corregirse).
3. `cuestionario.html` está en el sitemap pero marcado `noindex` — señal contradictoria para Google.

---

## Hallazgos técnicos (Crawlability / Indexación)

| Issue | Impacto | Evidencia | Fix |
|---|---|---|---|
| Canonical y schema en todo el sitio usan `https://apavigreen.com/...` sin `www`, pero la web vive en `www.apavigreen.com` | Alto | Confirmado en sept. que `apavigreen.com` redirige 301 a `www`; ningún canonical del repo usa `www` | Decidir el dominio "oficial" (recomendado: `www`, es el que usa Search Console) y actualizar canonical/sitemap/schema de las 29 páginas de una vez |
| `cuestionario.html` tiene `<meta name="robots" content="noindex">` pero está en `sitemap.xml` | Medio | `sitemap.xml` línea con `/cuestionario.html`; meta robots del archivo | Quitarla del sitemap (una página noindex no debería estar ahí) |
| Las 5 páginas nuevas de zona no están enlazadas desde ninguna de las 10 páginas de servicio/contenido existentes (`cesped-artificial.html`, `jardines-verticales.html`, `blog.html`, etc.) | Alto | Grep confirma 0 enlaces a `zonas.html` o a las páginas de zona desde esas 10 páginas | Añadir un enlace contextual (ej. en `cesped-artificial.html`: "¿Buscas instalación en Tenerife, Cádiz, Málaga o Sevilla? Ver zonas") — refuerza autoridad temática y evita que dependan solo del enlace de la home |

## Hallazgos on-page

| Issue | Impacto | Evidencia | Fix |
|---|---|---|---|
| `title` ≠ `og:title` en 12 páginas (la mayoría solo difieren en mayúsculas, pero `cesped-artificial.html`, `resinas-epoxi.html`, `quienes-somos.html`, `jardines-verticales.html`, `instalaciones-deportivas.html`, `espacios-infantiles.html` y 4 posts de blog tienen titulares realmente distintos) | Medio | Ver detalle abajo | Igualar `og:title` al `<title>` real, o viceversa si el de OG es mejor para compartir |
| Títulos por encima de 60 car. (riesgo de corte en el SERP): `index.html` (72), `blog/jardines-verticales-gran-canaria.html` (82), `blog.html` (62), `blog/cesped-artificial-piscina.html` (72), `blog/resinas-epoxi-garaje.html` (70), `plan-renove.html` (65) | Medio | Conteo de caracteres renderizados | Acortar a 50-60 car. manteniendo keyword principal al inicio |
| Meta descriptions por encima de 160 car.: `quienes-somos.html` (191), `resinas-epoxi.html` (193), `pavimento-pvc.html` (190), `jardines-verticales.html` (168), `instalaciones-deportivas.html` (162), **`cesped-artificial-sevilla.html` (169, página nueva de este mes)**, y 3 posts de blog | Bajo-Medio | Conteo de caracteres | Recortar a 150-160 car. |
| `plan-renove.html` no tiene `og:title`, `og:description` ni ningún schema JSON-LD | Medio | Grep sobre el archivo | Es una página de conversión importante (Plan Renove) — añadir Open Graph y schema `Service`/`FAQPage` como tienen las demás páginas de servicio |
| `zonas.html` y `proyectos.html` no tienen ningún schema JSON-LD | Bajo | Grep | Añadir al menos `BreadcrumbList` o `ItemList` en `zonas.html` (es nueva, fácil de añadir ahora) |
| `cuestionario.html` no tiene ningún `<h1>` | Bajo | 0 coincidencias de `<h1` | Añadir un H1 visible al formulario (ayuda a accesibilidad y a SEO aunque sea noindex) |

## Lo que sigue bien (no repetir trabajo)
- Sin enlaces internos rotos, sin JSON-LD inválido, sin `<img>` sin `alt`, sin títulos duplicados, sin falta de `lang`/`charset`.
- Las 5 páginas nuevas de zona tienen canonical propio, FAQ schema único por zona, meta OG completos y están en el sitemap — base técnica correcta, solo falta el enlazado interno de vuelta.

## Pendiente de sesiones anteriores, aún sin resolver
1. Alinear canonical/sitemap/schema a `www.apavigreen.com` (ver arriba, ahora más urgente — se ha duplicado el problema en 5 páginas nuevas).
2. `title` ≠ `og:title` (ya señalado en septiembre en 2 páginas, ahora confirmado en 12 — el problema es más extendido de lo que se pensaba).
3. Plan Renove sigue sin sublinkado interno suficiente y ahora también sin OG/schema.
4. Limpieza opcional de archivos sueltos mal ubicados en `/blog/` en el servidor — no verificable desde aquí sin acceso FTP/live.
5. Schema `LocalBusiness` sin `postalCode` ni `geo` (sin cambios desde septiembre).

---

## Plan de acción priorizado

1. **Enlazar las páginas de zona desde el resto del sitio** (crítico, rápido) — 10 páginas a tocar.
2. **Decidir y unificar www vs no-www** en canonical/sitemap/schema (crítico, afecta 29 páginas, hazlo de una vez).
3. **Quitar `cuestionario.html` del sitemap** (1 línea).
4. **Igualar `title`/`og:title`** en las 12 páginas afectadas (rápido).
5. **Acortar títulos y descripciones largas** (rápido, 10 páginas).
6. **Completar `plan-renove.html`** con OG + schema (medio).

## Rama de trabajo

`claude/seo-audit-apavigreen-df8fdh`

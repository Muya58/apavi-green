# Auditoría SEO — apavigreen.com

**Fecha:** 4 de septiembre de 2026
**Alcance:** Auditoría técnica y on-page completa, basada en el código fuente del repositorio (`muya58/apavi-green`, rama `master`), que es lo que se despliega en `apavigreen.com` vía GitHub Pages (archivo `CNAME`).
**Nota metodológica:** El acceso saliente a `apavigreen.com` estaba bloqueado desde este entorno, así que la auditoría se hizo leyendo el código fuente real (HTML, JSON-LD, robots.txt, sitemap.xml) en vez de la web renderizada. Esto es en realidad más fiable para meta tags, schema y estructura — pero **no puede medir Core Web Vitals reales, velocidad de carga ni renderizado móvil real**. Recomendación: correr PageSpeed Insights y el Rich Results Test sobre la URL en vivo tras aplicar las correcciones.

---

## Resumen ejecutivo

El sitio tiene **buenos fundamentos técnicos**: sitemap limpio, robots.txt correcto, canonicals autorreferenciados, un solo H1 por página, meta descriptions únicas en casi todas las páginas, y schema LocalBusiness/Service con NAP (nombre/dirección/teléfono) consistente. Es un sitio bien construido para su tamaño.

Pero hay **3 problemas críticos** que probablemente están costando clientes o visibilidad ahora mismo:

1. **La página de Proyectos tiene el teléfono y WhatsApp rotos** — cualquiera que llegue a `/proyectos.html` desde Google y quiera llamar o escribir, no puede.
2. **3 de los 7 artículos del blog no existen como URL propia** — dependen de JavaScript y no están en el sitemap, lo que arriesga que Google no los indexe bien.
3. **7,7 MB de imágenes casi sin optimizar** (solo 1 archivo `.webp` en todo el sitio) — esto penaliza directamente la velocidad de carga y el Core Web Vital más importante para SEO (LCP).

El resto son mejoras de prioridad media/baja que pulen un sitio que, en general, está bien planteado.

| Severidad | Nº de hallazgos |
|---|---|
| 🔴 Crítico | 3 |
| 🟠 Alto | 3 |
| 🟡 Medio | 4 |
| ⚪ Bajo / oportunidad | 3 |

---

## 🔴 Hallazgos críticos

### 1. Teléfono y WhatsApp rotos en `proyectos.html`
**Impacto:** Alto (conversión directa, no solo SEO)
**Evidencia:** En `proyectos.html` (indexada, prioridad 0.8 en el sitemap) aparecen tres enlaces de contacto con el placeholder sin rellenar:
```
Línea 110: <a href="tel:+34XXXXXXXXX" class="btn-ghost">📞 Llamar ahora</a>
Línea 122: <a href="https://wa.me/34XXXXXXXXX" aria-label="WhatsApp">💬</a>
Línea 145: <a href="https://wa.me/34XXXXXXXXX" class="float-btn float-whatsapp">
```
Todas las demás páginas del sitio usan el número real `+34654765548`. Solo `proyectos.html` (y el archivo plantilla `_partials/_footer.html`, que no se sirve directamente) se quedaron con el placeholder `XXXXXXXXX`.
**Arreglo:** Sustituir las 3 ocurrencias por `tel:+34654765548` y `https://wa.me/34654765548`. Es un cambio de 5 minutos con impacto inmediato en conversión.

### 2. 3 artículos del blog sin URL propia ni entrada en el sitemap
**Impacto:** Alto (indexación)
**Evidencia:** `blog/posts.json` contiene 7 artículos, pero solo 4 tienen página HTML estática propia (`blog/cesped-artificial-piscina.html`, `blog/jardines-verticales-gran-canaria.html`, `blog/precio-cesped-artificial-canarias.html`, `blog/resinas-epoxi-garaje.html`) y son las únicas 4 que aparecen en `sitemap.xml`. Los otros 3 —`cuanto-dura-cesped-artificial`, `jardines-verticales-interior-exterior`, `resinas-epoxi-parking-comunidades`— solo existen como `blog/post.html?slug=...`, una plantilla que:
- Empieza con `<title id="pageTitle">Artículo — Apavi Green</title>` genérico y `<meta name="description" id="pageDesc" content="">` vacío.
- Rellena título, descripción, canonical y contenido **mediante JavaScript** (`fetch('../blog/posts.json')`) después de la carga.
- No tiene entrada en `sitemap.xml`.

Aunque Google puede ejecutar JavaScript, esto añade riesgo real de indexación tardía o incompleta, y mezcla dos arquitecturas de URL (estática vs. con parámetro `?slug=`) para el mismo tipo de contenido.
**Arreglo:** Generar una página HTML estática por artículo (igual que los otros 4) o, como mínimo, añadir las 3 URLs `blog/post.html?slug=...` al sitemap y verificar en Search Console que Google las indexa con el título/descripción correctos tras el renderizado.

### 3. 7,7 MB de imágenes sin optimizar (solo 1 `.webp` en todo el sitio)
**Impacto:** Alto (Core Web Vitals, especialmente LCP en móvil)
**Evidencia:**
```
1.1M  assets/img/proyectos/jardin-vertical-despues1.jpg.png
1.0M  assets/img/servicios/zona-infantil-despues1.jpg.png
584K  assets/img/servicios/cesped-evento-hq.jpg
432K  assets/img/servicios/vertical-evento-hq.jpg
```
Varios nombres de archivo tienen doble extensión (`.jpg.png`), señal de que una foto se guardó como PNG en vez de JPG/WebP — PNG es un formato pésimo para fotografías (sin compresión con pérdida), de ahí el 1 MB+ por imagen. De 52 archivos de imagen en `/assets/img`, solo **1** es `.webp`.
**Arreglo:** Reconvertir el lote completo a WebP (o AVIF) con compresión con pérdida razonable. Una imagen de proyecto de 1.1 MB debería pesar 80–150 KB en WebP sin pérdida visible.

---

## 🟠 Hallazgos de alta prioridad

### 4. `proyectos.html` (la página con más imágenes) no usa `loading="lazy"`
**Impacto:** Alto (velocidad de carga)
**Evidencia:** `index.html` usa `loading="lazy"` en 11 imágenes; `proyectos.html`, que tiene 15 imágenes en una galería, no lo usa en ninguna.
**Arreglo:** Añadir `loading="lazy"` a todas las imágenes de la galería excepto la primera (above the fold).

### 5. Documentos internos publicados y accesibles públicamente
**Impacto:** Medio-Alto (exposición de información + ruido de rastreo)
**Evidencia:** Estos archivos están en la raíz del sitio en producción, con `noindex,nofollow` correcto (no aparecerán en Google), pero **son accesibles directamente por URL** y no están bloqueados en `robots.txt`:
- `brand-kit.html` — "Brand Kit Corporativo"
- `estrategia-redes-sociales.html` — "Estrategia de Redes Sociales 2026"
- `guia-gbp.html` — guía interna de Google Business Profile
- `guia-publicacion.html`, `boceto-landing.html`, `mockup-home-aprobado.html`, `index-old-backup.html`

No es un problema de indexación (el `noindex` funciona), pero sí de **higiene**: cualquiera con el enlace puede ver la estrategia interna de la empresa, y son bytes que Google rastrea sin necesidad.
**Arreglo:** Mover estos archivos fuera del directorio público desplegado (a una carpeta `/docs` o `/interno` no publicada, o a Notion/Drive), o al menos añadir `Disallow:` para ellos en `robots.txt`.

### 6. Enlaces sociales muertos en todas las páginas
**Impacto:** Medio (confianza/E-E-A-T, no ranking directo)
**Evidencia:** En `_partials/_footer.html` (y por tanto en el footer de todas las páginas): `<a href="#" aria-label="Instagram">` y `<a href="#" aria-label="Facebook">` — enlaces vacíos que no llevan a ningún sitio.
**Arreglo:** Añadir las URLs reales de Instagram y Facebook, o quitar los iconos si esos perfiles no existen todavía.

---

## 🟡 Hallazgos de prioridad media

### 7. Títulos que se cortarán en el SERP
| Página | Longitud | Título |
|---|---|---|
| `index.html` | 72 car. | "Césped Artificial en Gran Canaria \| Instalación y Garantía \| Apavi Green" |
| `blog/jardines-verticales-gran-canaria.html` | 82 car. | "Jardines Verticales en Gran Canaria: Ventajas, Tipos y Mantenimiento \| Apavi Green" |

Google trunca alrededor de 55–60 caracteres. La home, que es la página más importante del sitio, tiene el título más largo — justo el que no debería cortarse.
**Arreglo:** Recortar a lo esencial, ej. "Césped Artificial en Gran Canaria — Instalación y Garantía \| Apavi Green" (quitando un segmento) o similar, priorizando la keyword principal en los primeros 55 caracteres.

### 8. `title` y `og:title` no coinciden
**Evidencia:**
- `cesped-artificial.html`: title = *"Césped Artificial Canarias — Instalación \| Apavi Green"*, pero `og:title` = *"Césped Artificial Gran Canaria — Instalación Profesional \| Apavi Green"*.
- `jardines-verticales.html`: mismo patrón, el `og:title` es más largo y distinto del `<title>`.

No es grave para ranking, pero rompe la coherencia de marca cuando alguien comparte la página en redes sociales o WhatsApp (el preview muestra un título distinto al de la pestaña del navegador).
**Arreglo:** Igualar `og:title` al `<title>` en ambas páginas, o unificar el criterio conscientemente si es intencional.

### 9. `plan-renove.html` está sublinkado
**Evidencia:** El "Plan Renove" (retirada gratis + instalación) es una oferta comercial fuerte, pero la página solo recibe enlaces internos desde `blog.html` e `index.html` — no está en el menú principal ni en el footer, a diferencia del resto de servicios.
**Arreglo:** Añadir un enlace a Plan Renove en el footer (columna "Servicios" o "Empresa") para reforzar su relevancia interna y facilitar que Google la rastree con más frecuencia.

### 10. Uso inconsistente de `<meta name="robots">`
**Evidencia:** Páginas indexables como `cesped-artificial.html`, `resinas-epoxi.html`, `proyectos.html` declaran explícitamente `index, follow`, mientras que `index.html`, `blog.html`, `plan-renove.html` y los 4 artículos de blog no declaran la etiqueta (lo cual por defecto también es `index, follow`, así que no hay error de indexación, pero sí inconsistencia de plantilla).
**Arreglo:** Estandarizar: o todas las páginas indexables llevan `<meta name="robots" content="index, follow">` explícito, o ninguna (dejando el comportamiter por defecto). Cualquiera de las dos es válida; lo que conviene evitar es la mezcla.

---

## ⚪ Oportunidades rápidas / prioridad baja

### 11. Nombres de archivo de imagen poco descriptivos y con doble extensión
Ejemplos: `jardin-vertical-despues1.jpg.png`, `zona-infantil-despues1.jpg.png`. Además del problema de formato (hallazgo #3), el nombre de archivo es una señal de SEO de imágenes que aquí se desaprovecha (Google Images indexa por nombre de archivo + alt text).

### 12. Schema LocalBusiness incompleto
El JSON-LD de `LocalBusiness`/`Service` (presente en la mayoría de páginas de servicio, con NAP consistente `+34654765548` / `+34636039736` / Las Palmas de Gran Canaria) no incluye `postalCode` ni coordenadas `geo`. Añadirlos refuerza la señal de negocio local y mejora la coherencia con el perfil de Google Business.

### 13. `cuestionario.html` sin H1
Es el formulario de presupuesto, correctamente marcado `noindex` (no compite por ranking), pero no tener H1 es una pequeña brecha de accesibilidad/estructura que vale la pena cerrar si se retoca la página.

---

## ✅ Lo que ya está bien hecho

- `robots.txt` correcto: permite todo salvo `/_partials/` (parciales de plantilla, correctamente excluidos) y referencia el sitemap.
- `sitemap.xml` limpio: solo URLs canónicas e indexables, con `priority` y `changefreq` bien asignados (home = 1.0, servicios principales = 0.8–0.9).
- Canonicals autorreferenciados en todas las páginas indexables revisadas.
- Un solo `<h1>` por página en todas las páginas de contenido.
- Meta descriptions únicas y en rango (145–195 caracteres) en prácticamente todas las páginas.
- Schema JSON-LD `LocalBusiness`/`Service` presente en las páginas de servicio principales, con teléfono y ciudad consistentes (excepto el caso puntual de `proyectos.html`, hallazgo #1).
- Verificación de Google Search Console ya instalada (`google293869b8da6514af.html` presente en la raíz).
- Páginas legales (`privacidad.html`, `cookies.html`, `aviso-legal.html`) correctamente marcadas `noindex, nofollow`.
- URLs limpias, en español, legibles y sin parámetros innecesarios (con la única excepción de `blog/post.html?slug=`, hallazgo #2).

---

## Plan de acción priorizado

1. **Arreglar teléfono/WhatsApp en `proyectos.html`** — 5 minutos, impacto inmediato en leads. *(Crítico)*
2. **Decidir arquitectura de los 3 artículos de blog huérfanos** — o página estática propia, o añadirlos al sitemap. *(Crítico)*
3. **Reconvertir imágenes a WebP** — empezar por las 10 imágenes más pesadas listadas arriba. *(Crítico)*
4. **Añadir `loading="lazy"` a la galería de `proyectos.html`.** *(Alto)*
5. **Sacar de producción (o bloquear) los archivos internos** (brand-kit, estrategia, guías). *(Alto)*
6. **Rellenar o quitar los enlaces sociales muertos.** *(Alto)*
7. Acortar el título de `index.html` y el del artículo de jardines verticales. *(Medio)*
8. Igualar `title` y `og:title` en las 2 páginas señaladas. *(Medio)*
9. Enlazar Plan Renove desde el footer. *(Medio)*
10. Estandarizar el uso de `<meta name="robots">`. *(Medio)*
11. Renombrar archivos de imagen y añadir `postalCode`/`geo` al schema. *(Bajo)*

---

*Informe generado a partir del código fuente del repositorio en la rama `claude/seo-audit-apavigreen-df8fdh`. Recomendado: repetir la comprobación de Core Web Vitals (PageSpeed Insights) y Rich Results Test sobre la URL en vivo una vez desplegados los cambios.*

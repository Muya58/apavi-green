# 7 oct 2026: recuperación de la web y mejoras

Anterior: [[2026-10-06-RESUMEN-SESION-Y-PLAN-7-OCT]] (rama `claude/eloquent-meitner-0l435q`)

## Qué pasó
- El 6-10 por la noche, un paquete generado desde GitHub sobrescribió el trabajo de la mañana en el servidor.
- El 7-10 el usuario volvió a subir sus archivos desde la oficina y envió un zip con **todos los paquetes FTP del 6-10**: `SUBIR-FTP-2026-10-06` (completo) y `-b, -c, -e, -f, -g, -h, -i, -j, -l, -m, -n, -o, -q, -r`. Las letras a, d, k y p **no existieron** (confirmado por el usuario el 7-10): la reconstrucción está completa.

## Fuente de la verdad
- Rama **`servidor-2026-10-06`** = `master` + paquetes del 6-10 aplicados en orden. Es la copia de lo que hay en el servidor.
- A partir de ahora todo cambio de Apavi sale de esta rama.

## Cambios del 7-10 (paquete `SUBIR-FTP/2026-10-07-recuperacion/`, 23 archivos)
- **Resinas epoxi:** las fotos de obras no se podían pulsar; ahora cada obra se abre en grande (galería con flechas, teclado, deslizar en móvil, contador "Obra X de 15") con botón "Quiero un suelo así".
- **Portada:** sección "Todo el archipiélago canario y Andalucía"; tarjeta "Todas las Islas Canarias" → `zonas.html`; estilos de las tarjetas (no se cargaban desde el 9-9); tildes en Cádiz/Málaga.
- **Páginas hub** `piscinas-de-arena.html` y `suelos-resineo.html` regeneradas con el menú y el pie actuales y canonical con www; vuelven a enlazarse desde las tarjetas de la portada, el pie "Servicios" (20 páginas) y resinas-epoxi.
- **Sitemap:** 29 URLs del 6-10 + 2 páginas hub = 31.
- **proyectos.html:** info@ → web@apavigreen.com.

## Fotos subidas el 6-10 sin usar en ninguna página
- Añadidas a la galería de epoxi: `resina-epoxi-local-gran-superficie.webp` y `resina-epoxi-local-acabado-brillo.webp`. `resina-epoxi-camara.webp` es un duplicado exacto de `resina-epoxi-camara-frigorifica.webp` (mismo archivo); no se añade.

## Comprobación del 7-10 tras la subida
- No se puede abrir apavigreen.com desde la sesión (dominio bloqueado por la red del entorno). Revisión local de las 37 páginas de la rama `servidor-2026-10-06`: enlaces internos, imágenes, errores de JS y scroll horizontal en móvil.
- Todo lo subido hoy, correcto. Se encontraron 3 fallos anteriores, ya arreglados en `SUBIR-FTP/2026-10-07-b-arreglos/`:
  - `assets/js/cookies.js`: los enlaces del banner eran relativos → 404 en `/blog/`. Ahora son `/cookies.html` y `/privacidad.html`.
  - `cookies.html`: la tabla se desbordaba en móvil → contenedor con scroll.
  - `quienes-somos.html`: la rejilla de 2 columnas se desbordaba en móvil → 1 columna por debajo de 760 px.

## ✅ Verificación en vivo (7-10, mañana)
- Dominios permitidos en la red del entorno: ya se pueden revisar las 3 webs en vivo.
- **apavigreen.com:** los 51 archivos de la web (HTML, sitemap, JS, CSS) coinciden con la rama `servidor-2026-10-06` (solo cambian los saltos de línea CRLF del FTP). 31/31 URLs del sitemap correctas en móvil: sin 404, sin errores de JS, sin enlaces rotos, sin scroll horizontal.
- `cuestionario.js` ya muestra "+34 654 765 548"; `analytics.js` con Consent Mode v2 (29-9) por fin en producción.
- **resineocanarias.com:** 7/7 OK. **www.piscinadearenatenerife.com:** 6/6 OK.
- ✅ Carpeta `/2026-10-07-b-arreglos/` borrada del servidor (verificado: 404).
- Lección: las instrucciones van FUERA de la carpeta a subir (`SUBIR-ESTO/`), y se sube su CONTENIDO, no la carpeta.
- Search Console: sitemaps listos (Apavi 31, Résineo 7, Piscinas 6; las 44 URLs dan 200; cada robots.txt apunta a su sitemap). El usuario envía los sitemaps y solicita la indexación (prioridad: home, resinas-epoxi, piscinas-de-arena, suelos-resineo, zonas, Lanzarote, Fuerteventura, caso Carrizal; al día siguiente La Palma, La Gomera y El Hierro).
- ✅ Indexación solicitada en GSC (7-10). Incidencia: un 404 en Fuerteventura era por un punto al final de la URL pegada; la página da 200 también para Googlebot.
- Próximo: el 8-10, solicitar la indexación de La Palma, La Gomera y El Hierro. Dentro de 1-2 semanas, revisar Páginas > Indexadas y Rendimiento.

## Blog: 2 artículos nuevos (7-10)
- `blog/piscina-de-arena-vs-gresite.html` (~840 palabras): comparativa, tabla, FAQ, schema Article+FAQPage+Breadcrumb; enlaza a piscinas-de-arena, piscinadearenatenerife.com y césped Tenerife.
- `blog/suelo-antideslizante-borde-piscina.html` (~850 palabras): normativa (CTE DB SUA 1, clase 3 en piscinas de uso público; DIN 51097; PN18), comparativa de suelos, Résineo; enlaza a suelos-resineo, resineocanarias.com/piscinas y artículos de césped.
- Fotos de Bio.design y Résineo (catálogo del fabricante, con el crédito "Imagen: Bio.design/Résineo"; no se presentan como obras propias) → `assets/img/blog/piscinas/`.
- Categoría nueva "Piscinas" en `posts.json`; sitemap con 33 URLs; enlaces desde las páginas hub.
- Paquete: `SUBIR-FTP/2026-10-07-d-blog-piscinas/` (SUBIR-ESTO + INSTRUCCIONES aparte).

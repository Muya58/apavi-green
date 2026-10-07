# Resumen del 7 oct 2026 y plan para el 8 oct

> **Léelo primero.** Nota de traspaso para retomar mañana.
> Rama de GitHub (copia exacta del servidor): **`servidor-2026-10-06`** en `Muya58/apavi-green`
> Detalle: [[2026-10-07-recuperacion]] · Kit de reseñas: [[2026-10-07-kit-resenas-google]] · Día anterior: [[2026-10-06-RESUMEN-SESION-Y-PLAN-7-OCT]]

## ✅ Hecho hoy
1. **Web recuperada:** el trabajo del 6-10 por la mañana se reconstruyó a partir de los paquetes FTP de la oficina (base, b, c, e–j, l–o, q, r; a, d, k y p no existieron) y está guardado en la rama `servidor-2026-10-06`.
2. **Resinas epoxi:** galería de **17 obras** que se abren en grande (flechas, deslizar en móvil, botón "Quiero un suelo así"). Añadidas 2 obras de locales comerciales. `resina-epoxi-camara.webp` es un duplicado de la de la cámara frigorífica (no se usa).
3. **Portada:** sección "Todo el archipiélago canario y Andalucía" con la tarjeta "Todas las Islas Canarias" → zonas.html. Las tarjetas ya tienen estilo (antes salían sin diseño).
4. **Páginas hub** `piscinas-de-arena.html` y `suelos-resineo.html` regeneradas con el menú y el pie actuales y enlazadas desde la portada, el pie (20 páginas) y resinas-epoxi.
5. **Arreglos:** `cuestionario.js` (el error mostraba "+34 XXX…") y `analytics.js` (Consent Mode v2) por fin en producción; banner de cookies en el blog (404); tabla de cookies y Quiénes somos en el móvil; `proyectos.html` con web@.
6. **Blog:** 2 artículos nuevos en la categoría "Piscinas":
   - `blog/piscina-de-arena-vs-gresite.html`
   - `blog/suelo-antideslizante-borde-piscina.html`
7. **Verificado en vivo** (dominios permitidos en la red del entorno): Apavi 33 URLs, Résineo 7 y Piscinas 6, todas correctas; el servidor coincide con GitHub.
8. **Search Console:** sitemaps enviados; indexación solicitada hasta llegar al cupo diario de Apavi.
9. **Reseñas:** enlace `https://g.page/r/CfyJk8i25aSgEAE/review`, QR verificado, tarjeta para WhatsApp/redes (1080×1350), tarjeta A6 imprimible y mensajes listos → `docs/marketing/`.

## ▶️ Plan para mañana (8 oct), en este orden
### 1. Indexación (Search Console → Inspección de URLs → Solicitar indexación)
Las que no entraron hoy por el cupo:
```
https://www.apavigreen.com/blog/piscina-de-arena-vs-gresite.html
https://www.apavigreen.com/blog/suelo-antideslizante-borde-piscina.html
https://www.apavigreen.com/cesped-artificial-la-palma.html
https://www.apavigreen.com/cesped-artificial-la-gomera.html
https://www.apavigreen.com/cesped-artificial-el-hierro.html
```
Si no se pidieron ayer (cupo propio de cada web):
```
https://resineocanarias.com/
https://resineocanarias.com/piscinas
https://resineocanarias.com/suelos-terrazas
https://www.piscinadearenatenerife.com/
```
⚠️ Pegar las URLs **sin punto ni espacio al final** (ayer un punto final dio un falso 404).

### 2. Reseñas
- Configurar la respuesta rápida `/resena` en WhatsApp Business (texto en el kit).
- Enviar el mensaje a 5-10 clientes recientes (Carrizal, Tafira, Lanzarote, oficinas de epoxi, guardería…). Recordatorio una sola vez a los 5-7 días.
- Abrir el enlace desde el móvil para confirmar que salen las estrellas de la ficha (desde la sesión no se puede: g.page no está permitido).
- Imprimir la tarjeta A6 y meter el QR en presupuestos y facturas.

### 3. Después (cuando se quiera)
- Subida automática a Apavi (GitHub Actions + FTP/SFTP) para no subir a mano.
- Fotos de obras propias de piscinas para sustituir las de catálogo de los artículos.
- En 1-2 semanas: revisar en GSC "Páginas" y "Rendimiento".

## 🔒 Reglas (recordatorio)
- La rama `servidor-2026-10-06` = lo que hay en el servidor. Todo cambio sale de ahí.
- Antes de cualquier paquete FTP: preguntar si se ha cambiado algo en el servidor.
- Paquetes FTP: carpeta `SUBIR-ESTO` (se sube su CONTENIDO a la raíz) + `INSTRUCCIONES.txt` aparte.
- Después de cada subida, comprobar en vivo (los dominios ya están permitidos).

## Cómo retomar
Abrir esta misma sesión ("SEO audit para landing pages") en claude.ai/code, o una nueva con:
> *"Lee `docs/seo-audits/2026-10-07-RESUMEN-Y-PLAN-8-OCT.md` de la rama `servidor-2026-10-06` del repo apavi-green y sigue con el plan del 8 de octubre."*

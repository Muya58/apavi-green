# Resumen de la sesión del 6 oct 2026 y plan para el 7 oct

> **Léelo primero.** Es la nota de traspaso para seguir mañana desde el ordenador del trabajo.
> Detalle completo: [[2026-10-06-auditoria-seo-red-landings]]
> Rama de GitHub: `claude/eloquent-meitner-0l435q` (repo `Muya58/apavi-green`)

---

## 1. Qué se hizo hoy

### Auditoría SEO de la red (apavigreen.com + 2 landings)
- El dominio correcto de la landing de piscinas es **`www.piscinadearenatenerife.com`** (singular). El plural `piscinasdearenatenerife.com` es de un **competidor** (Beach Feel).
- Problemas encontrados: teléfono erróneo en las landings, páginas con muy poco texto, sin enlaces de las landings hacia Apavi.

### Résineo — `resineocanarias.com` ✅ EN VIVO (Vercel)
- Teléfono corregido a **654 765 548**; correo de contacto **web@apavigreen.com**.
- Contenido ampliado: piscinas (~1.000 palabras), suelos-terrazas (~850), tecnología (~700 + ficha técnica), más FAQ y datos para Google.
- Enlaces a Apavi en el pie de las 10 páginas.
- Arreglado el botón "Pedir presupuesto", que era invisible.
- PRs fusionados: [Muya58/resineo-canarias#1](https://github.com/Muya58/resineo-canarias/pull/1) y [Muya58/resineo-canarias#2](https://github.com/Muya58/resineo-canarias/pull/2).

### Bio.design — `www.piscinadearenatenerife.com` ✅ EN VIVO (Vercel)
- Teléfono corregido a **654 765 548**; "Apavi Green" del pie enlaza a apavigreen.com.
- PR fusionado: [Muya58/biodesign-tenerife#1](https://github.com/Muya58/biodesign-tenerife/pull/1).

### Apavi — `www.apavigreen.com` (FTP manual)
- Páginas nuevas **EN VIVO**: `piscinas-de-arena.html` y `suelos-resineo.html`.
- `sitemap.xml` **EN VIVO**, con las 2 páginas nuevas.
- Tarjetas de la portada → páginas nuevas; pie de página "Servicios" con los 2 enlaces nuevos; enlace desde resinas-epoxi.
- PR abierto (documentación y código): [Muya58/apavi-green#2](https://github.com/Muya58/apavi-green/pull/2).
- Garantía: **NO se unifica**. Cada producto mantiene la suya (decisión del usuario).

---

## 2. ⚠️ El problema de hoy (y por qué pasó)

- Por la mañana, desde el trabajo, se subieron por FTP fotos y cambios en muchas páginas de Apavi (epoxi, jardines…). **Esos cambios no estaban en GitHub.**
- Por la noche se subió el paquete `SUBIR-FTP/2026-10-06-piscinas-y-resineo/`, generado desde GitHub (versión del 29-9). **Sobrescribió 15 páginas y el sitemap con versiones antiguas.**
- Páginas afectadas: `index`, `cesped-artificial` (y Cádiz, Málaga, Sevilla, Tenerife), `espacios-infantiles`, `instalaciones-deportivas`, `jardines-verticales`, `pavimento-pvc`, `resinas-epoxi`, `quienes-somos`, `zonas`, `blog/precio-cesped-artificial-canarias`.
- **Las fotos subidas por la mañana siguen en el servidor.** Solo hay que recuperar los HTML.

---

## 3. ✅ Plan para mañana (7 oct), en este orden

**A. Recuperar tu trabajo (en la oficina)**
1. Busca la carpeta desde la que subiste por FTP esta mañana. Pistas: la ruta del panel izquierdo de FileZilla, buscar `*.html` modificados el 6-10, o la carpeta Descargas.
2. Sube por FTP **tus versiones** de las páginas afectadas para recuperar tu trabajo.
   - **NO subas tu `sitemap.xml`**: el del servidor es el bueno.
   - **NO toques** `piscinas-de-arena.html` ni `suelos-resineo.html`.
3. Termina o rectifica lo que necesites en Apavi.

**B. Pasarme los archivos (para que GitHub = servidor)**
4. En GitHub: `Muya58/apavi-green` → **Add file → Upload files** → carpeta `servidor/2026-10-07/` → "Create a new branch" → Commit. También vale un .zip en el chat.
5. Les vuelvo a añadir encima los enlaces a las páginas nuevas (tarjetas de la portada, pie de página, resinas-epoxi) y corrijo `info@` → `web@` en `proyectos.html`.
6. Te enseño qué cambia en cada archivo y te preparo `SUBIR-FTP/2026-10-07-.../` para una segunda subida rápida.

**C. Search Console** (los sitemaps ya están publicados, no hay que subirlos)
- Apavi: enviar `https://www.apavigreen.com/sitemap.xml` y solicitar la indexación de `/piscinas-de-arena.html` y `/suelos-resineo.html`. Si sale "URL no permitida" → avísame y te preparo un sitemap con www.
- Résineo: enviar `https://resineocanarias.com/sitemap.xml` y solicitar la indexación de `/`, `/piscinas` y `/suelos-terrazas`.
- Piscinas: enviar `https://www.piscinadearenatenerife.com/sitemap.xml` y solicitar la indexación de `/`.

**D. Después**
- Artículos del blog: "Piscina de arena vs gresite" y "Suelo antideslizante para el borde de la piscina".
- (Recomendado) Subida automática a Apavi con GitHub Actions para no subir más a mano.

---

## 4. 🔒 Reglas para que no vuelva a pasar

1. **Una sola fuente de la verdad: GitHub.** Todo cambio que hagas en Apavi (desde casa o desde el trabajo) se sube también a GitHub el mismo día.
2. **Antes de cualquier paquete para el FTP**, Claude pregunta: *"¿Has cambiado algo en el servidor desde la última vez?"*. Si la respuesta es sí, primero se descargan del servidor los archivos afectados y se parte de ellos.
3. **Cada paquete de `SUBIR-FTP/` lleva un `LEEME.txt`** con la lista exacta de archivos y qué cambia en cada uno.
4. **Antes de sobrescribir por FTP**, mira en FileZilla la fecha de modificación del servidor: si es de hoy y no la has subido tú desde ese paquete, **para y pregunta**.
5. Las landings (Résineo y Piscinas) se publican **solo desde GitHub/Vercel**: no se tocan por FTP.

---

## 5. Cómo retomar mañana con Claude

En una sesión nueva, desde cualquier ordenador, escribe:

> *"Lee `docs/seo-audits/2026-10-06-RESUMEN-SESION-Y-PLAN-7-OCT.md` de la rama `claude/eloquent-meitner-0l435q` del repo apavi-green y sigue con el plan del 7 de octubre."*

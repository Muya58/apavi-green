# Páginas internas — no publicar

Estos archivos vivían en la raíz del sitio (`apavigreen.com/brand-kit.html`, etc.), accesibles por
cualquiera con el enlace aunque llevaran `noindex, nofollow`. Se movieron aquí el 4 de septiembre
de 2026 como parte de la auditoría SEO (hallazgo #5, prioridad alta) para que no formen parte de lo
que se sube al hosting.

- `boceto-landing.html` — boceto de landing page v2
- `brand-kit.html` — brand kit corporativo
- `estrategia-redes-sociales.html` — estrategia de redes sociales 2026
- `guia-gbp.html` — guía interna de Google Business Profile
- `guia-publicacion.html` — guía de publicación de contenido
- `index-old-backup.html` — copia de seguridad de una versión antigua de la home
- `mockup-home-aprobado.html` — mockup de home aprobado

Al subir el sitio al hosting, **no incluir la carpeta `docs/`** (ni `_partials/`, que tampoco es
pública). Solo debe subirse lo que está referenciado desde `sitemap.xml` y sus assets: los `.html`
de la raíz y `blog/`, más `assets/`, `robots.txt`, `sitemap.xml` y `CNAME`.

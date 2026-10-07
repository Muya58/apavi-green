# 7 oct 2026: recuperación de la web y mejoras

Anterior: [[2026-10-06-RESUMEN-SESION-Y-PLAN-7-OCT]] (rama `claude/eloquent-meitner-0l435q`)

## Qué pasó
- El 6-10 por la noche, un paquete generado desde GitHub sobrescribió el trabajo de la mañana en el servidor.
- El 7-10 el usuario volvió a subir sus archivos desde la oficina y envió un zip con **todos los paquetes FTP del 6-10**: `SUBIR-FTP-2026-10-06` (completo) y `-b, -c, -e, -f, -g, -h, -i, -j, -l, -m, -n, -o, -q, -r`. **Faltan a, d, k y p** (pendiente de confirmar si existieron).

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
- `assets/img/resinas/resina-epoxi-camara.webp`, `resina-epoxi-local-acabado-brillo.webp`, `resina-epoxi-local-gran-superficie.webp` (se pueden añadir a la galería de epoxi si el usuario quiere).

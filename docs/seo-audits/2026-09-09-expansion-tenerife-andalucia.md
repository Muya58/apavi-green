# Sesión 9 de septiembre 2026 — Expansión de zonas: Tenerife, Cádiz, Málaga, Sevilla

## Contexto

El usuario quiere aumentar tráfico web/redes en zonas concretas donde ya hay capacidad real de instalación:

- **Tenerife** (provincia) — mismo equipo y proveedor que Canarias, mismos precios.
- **Cádiz, Málaga, Sevilla** (Andalucía/Península) — equipo y proveedor **distinto**, precios distintos. No se reutilizan las cifras de Canarias.
- Hay obras reales realizadas en estas zonas, pero **no hay fotos disponibles todavía** → no se inventan números de proyectos ni se usan placeholders de foto engañosos; se usa el mismo patrón honesto "Foto del proyecto · Próximamente" que ya existía en `cesped-artificial.html`.
- Precio en Andalucía: **"a consultar"** por decisión del usuario, hasta tener tarifa cerrada con el nuevo proveedor.

## Páginas creadas

1. `cesped-artificial-tenerife.html` — reutiliza precio de Canarias (18-45 €/m² + suplemento insular 1-3 €/m²) porque es el mismo proveedor. FAQ y contenido propios (norte/sur de la isla, exposición solar).
2. `cesped-artificial-cadiz.html` — sin precio, CTA "presupuesto a medida". Contenido propio: viento de Levante, ambiente salino, ciudades reales de la provincia.
3. `cesped-artificial-malaga.html` — sin precio. Contenido propio: Costa del Sol, chalets/urbanizaciones, segunda residencia y vivienda vacacional.
4. `cesped-artificial-sevilla.html` — sin precio. Contenido propio: ahorro de agua, calor extremo del verano sevillano.
5. `zonas.html` — página hub que enlaza Canarias + las 4 zonas nuevas, para evitar páginas huérfanas y repartir enlaces internos.

Cada página tiene: title/meta/OG únicos, canonical propio, schema `Service`+`LocalBusiness` con `areaServed` real de la zona (ciudades reales, no inventadas), schema `FAQPage` con preguntas y respuestas distintas por zona (nada de contenido "plantilla" duplicado palabra por palabra).

## Enlazado interno

- `sitemap.xml` — 5 URLs nuevas añadidas.
- `index.html` — nueva sección "Ahora también en Tenerife y Andalucía" justo después de Proyectos, con tarjetas a las 4 zonas + enlace a `zonas.html`. También añadido enlace en el footer (columna "Empresa").
- Footer de las 4 páginas de zona + `zonas.html` — columna "Zonas" con enlaces cruzados entre ellas.

## Pendiente (no resuelto hoy, requiere info del usuario)

1. **Tarifa real de Andalucía** — en cuanto el usuario tenga precio cerrado con el nuevo proveedor de Península, sustituir el CTA "a consultar" por rangos de precio reales en las 3 páginas de Andalucía (y en el FAQ/schema correspondiente).
2. **Fotos de obras reales en las 4 zonas** — sustituir los placeholders "Próximamente" en cuanto el usuario las tenga, e idealmente subir a `proyectos.html` filtrando por zona.
3. **Redes sociales**: el usuario mencionó también crecer en redes, no solo web. Aún no abordado — pendiente decidir: Google Business Profile por zona, contenido geo-etiquetado en Instagram/Facebook (`apavigreensl`), posible publicidad geo-segmentada. Debe tratarse en otra sesión.
4. Sigue pendiente la lista de baja prioridad del informe original (ver `2026-09-09-despliegue-y-ga4.md`).

## Rama de trabajo

`claude/seo-audit-apavigreen-df8fdh`

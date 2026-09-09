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

## Estrategia de tráfico explicada (misma sesión)

Se explicaron 3 vías no excluyentes para llevar tráfico a estas zonas, con costes/tiempos distintos:

1. **SEO/páginas** (lo ya construido) — gratis, lento (2-6 meses), necesita autoridad (reseñas, Google Business Profile).
2. **Redes sociales orgánicas** (`apavigreensl`) — gratis pero limitado sin fotos reales de las zonas nuevas; solo apoyo, no motor principal.
3. **Publicidad de pago geo-segmentada** (Google Ads / Meta Ads) — la única vía rápida; ~5-10 €/día por zona para empezar. Google Ads = intención de compra directa; Meta Ads = generación de demanda con foto/vídeo (se pueden usar fotos de Canarias siendo honestos).

Recomendación dada: Google Business Profile primero (gratis, ya resuelto hoy) → luego decidir presupuesto de ads.

## Google Business Profile (resuelto hoy)

- Ya existía una ficha de Apavi Green en Google Business Profile.
- El equipo de Andalucía es una **empresa colaboradora/subcontratista** en Cádiz, sin dirección propia conocida → se descartó crear una ficha nueva con dirección inventada (riesgo de suspensión por Google).
- Recomendación aplicada: **una sola ficha**, añadiendo Tenerife, Cádiz, Málaga y Sevilla como áreas de servicio adicionales sobre la ficha existente (mismo teléfono, misma marca Apavi Green de cara al cliente).
- **Usuario confirma: ya está hecho** ("Ya lo tengo").

## Pendiente

1. **Tarifa real de Andalucía** — en cuanto el usuario tenga precio cerrado con el proveedor colaborador de Cádiz, sustituir el CTA "a consultar" por rangos de precio reales en las 3 páginas de Andalucía (y en el FAQ/schema correspondiente).
2. **Fotos de obras reales en las 4 zonas** — sustituir los placeholders "Próximamente" en cuanto el usuario las tenga, e idealmente subir a `proyectos.html` filtrando por zona.
3. **Publicidad de pago (Google Ads / Meta Ads) geo-segmentada** — el usuario va a hablar con sus socios mañana para decidir presupuesto. Siguiente sesión: definir campañas, audiencias y presupuesto por zona una vez tengan luz verde.
4. Sigue pendiente la lista de baja prioridad del informe original (ver `2026-09-09-despliegue-y-ga4.md`).

## Rama de trabajo

`claude/seo-audit-apavigreen-df8fdh`

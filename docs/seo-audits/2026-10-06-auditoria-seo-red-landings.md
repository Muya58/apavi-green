# Auditoría SEO: red Apavi Green + landings satélite

**Fecha:** 6 de octubre de 2026
**Sitios:** `apavigreen.com` (principal), `resineocanarias.com` (Résineo), landing de piscinas de arena Bio.design
**Repos revisados:** `Muya58/apavi-green`, `Muya58/resineo-canarias`, `Muya58/biodesign-tenerife`
**Método:** este entorno no puede abrir las webs en vivo (el proxy bloquea los tres dominios), así que se auditó el código fuente de los tres repos y se comprobó la indexación con búsquedas `site:`. **Pendiente de verificar en Search Console:** cobertura real del índice, Core Web Vitals y consultas.
**✅ Actualización (misma sesión):** el usuario confirma que el dominio correcto es **`piscinadearenatenerife.com` (singular, con www)**. `piscinasdearenatenerife.com` (plural) es de un **competidor** (Beach Feel / Stone Feel), así que no hay que tocarlo. Ver el apartado *Estado de los quick wins* al final.
**Auditorías anteriores:** [[2026-09-04-auditoria-seo-apavigreen]] · [[2026-09-09-expansion-tenerife-andalucia]] · [[2026-09-29-analisis-embudo-ga4]]

---

## Resumen ejecutivo

La web principal tiene una base técnica sólida, gracias a lo que se arregló en septiembre. Las dos landings satélite **no la ayudan ahora mismo, y una de ellas puede que ni siquiera esté en el dominio que creemos**. Hay tres problemas que pesan más que todo lo demás:

1. **Confusión de dominio en la landing de piscinas.** El código y el enlace desde Apavi usan `piscinadearenatenerife.com` (*piscina*, en singular). El dominio que diste, `piscinasdearenatenerife.com` (*piscinas*, en plural), es una web **WordPress de otra empresa** (sistemas "Beach Feel / Stone Feel", autor "damian"). Es la que Google tiene indexada, y le pasa la marca "Piscinas de Arena Tenerife".
2. **Teléfono equivocado en las dos landings.** Las dos usan `+34 654 795 518`, el número que ya se corrigió como erróneo en Apavi (el correcto es `654 765 548`). Rompe la coherencia de NAP en el SEO local y además hace perder llamadas.
3. **Contenido muy fino y sin enlaces a la principal.** Las páginas de Résineo tienen entre 70 y 250 palabras y **ningún enlace a apavigreen.com**. Google no tiene motivos para indexarlas ni para relacionarlas con la marca.

**Diagnóstico global:** necesita trabajo. La red está montada, pero no está conectada.

---

## 1. Hallazgos críticos

| Sitio | Problema | Severidad | Arreglo |
|---|---|---|---|
| Piscinas | ✅ RESUELTO: el dominio bueno es el singular. Dominio del código (`piscinadearenatenerife.com`) ≠ dominio comunicado (`piscinasdearenatenerife.com`). El plural pertenece a un tercero que vende Beach Feel | 🔴 Crítico | Confirmar qué dominio es nuestro. Si es el singular, olvidarse del plural (o intentar comprarlo). Si es el plural, hay que desplegar ahí el repo y quitar el WordPress |
| Piscinas | `index.html` de Apavi (líneas 1837 y 2410) enlaza al singular. Si el nuestro es el plural, ese enlace está roto | 🔴 Crítico | Alinear con el dominio correcto |
| Résineo + Piscinas | Teléfono `+34654795518` en el schema y en los `tel:` (Résineo `index.html:34`; Bio.design `index.html` y 2 enlaces `tel:`) | 🔴 Crítico | Cambiar a `+34654765548` en las dos |
| Résineo | `site:resineocanarias.com` no devuelve ningún resultado. 7 URLs en el sitemap, pero páginas de 70-250 palabras | 🔴 Crítico | Ampliar el contenido (ver §3) y enviar el sitemap en GSC |
| Apavi | En el buscador, para "Apavi Green" sale el **repo público de GitHub** en lugar de la web | 🟠 Alto | Pasar el repo a privado (GitHub Pages permite repos privados con plan Pro) o, como mínimo, poner la URL de la web en la descripción del repo |

## 2. Problemas on-page

| Página | Problema | Severidad | Arreglo |
|---|---|---|---|
| Résineo · todas | Ningún enlace a `apavigreen.com`, solo `mailto:info@apavigreen.com` | 🔴 Crítico | En el footer: "Résineo Canarias es una línea de [Apavi Green](https://apavigreen.com/), instaladores de suelos y césped en Canarias". Y en `quienes-somos`, un enlace contextual |
| Résineo · `piscinas`, `suelos-terrazas`, `realizaciones`, `contacto` | 68-99 palabras: contenido fino | 🟠 Alto | 600-900 palabras en cada una: usos, ventajas, colores, mantenimiento, precio orientativo €/m², FAQ |
| Résineo · `contacto` | "Formulario en preparación": no hay forma de convertir | 🟠 Alto | Formulario real, o WhatsApp + teléfono |
| Résineo · titles | Patrón "X — Resineo by Apavi Green" sin keyword geográfica (p. ej. `piscinas.html`) | 🟡 Medio | "Suelo drenante para piscinas en Canarias · Résineo" |
| Résineo · H1 home | "El suelo que respira tu piscina": bonito, pero sin keyword | 🟡 Medio | Metáfora en el subtítulo; H1 → "Suelos de resina y grava para piscinas y terrazas en Canarias" |
| Résineo · schema | Solo en `index` y `quienes-somos`. Falta `Service` y `FAQPage`. `addressLocality` sin calle | 🟡 Medio | Añadir `Service` por página, `FAQPage` y `parentOrganization` → Apavi Green |
| Résineo · `robots.txt` | `Disallow` a páginas legales: Google no puede leer su `noindex` | ⚪ Bajo | Quitar el `Disallow` y poner `noindex` en el HTML |
| Piscinas · `index` | H1 = logo SVG + texto oculto con clip. Funciona, pero es una señal débil | 🟡 Medio | H1 visible: "Piscinas de arena en Tenerife"; el logo fuera del H1 |
| Piscinas · `contacto`, `realizaciones`, `tecnologia` | 100-193 palabras | 🟠 Alto | 500-800 palabras, con fotos reales y FAQ |
| Piscinas · enlaces a Apavi | Ya enlaza a césped, jardines y resinas ✅ | — | Añadir anchor de marca "Apavi Green" en el footer |
| Apavi · `index` vs `cesped-artificial` | Garantía "8 años" en la home, "10 años" en la página de servicio | 🟡 Medio | Unificar (confianza + coherencia) |
| Apavi · enlaces salientes | Las dos landings se enlazan con `target="_blank"` sin texto descriptivo de servicio en el footer ("Bio.design Tenerife") | ⚪ Bajo | Anchors: "Piscinas de arena en Tenerife", "Suelos Résineo para piscinas" |
| Apavi | No hay ninguna página propia sobre piscinas de arena ni sobre Résineo: toda la autoridad temática se va fuera | 🟠 Alto | Ver §5, estrategia hub & spoke |

## 3. Análisis de huecos de contenido

| Tema / keyword | Por qué | Formato | Prioridad | Esfuerzo |
|---|---|---|---|---|
| "piscina de arena precio" / "cuánto cuesta una piscina de arena" | Alta intención comercial; la competencia (Tropical Pool, Disersan) lo cubre | Artículo en la landing de piscinas | Alta | Media jornada |
| "piscina de arena vs piscina de hormigón / gresite" | Comparativa: etapa de consideración | Artículo comparativo | Alta | Media jornada |
| "suelo antideslizante para piscina" / "borde de piscina drenante" | Problema que resuelve Résineo; poca competencia local | Página de servicio en Résineo | Alta | Media jornada |
| "Résineo precio m²" / "moqueta de mármol" | Búsqueda de marca de producto en la que ningún instalador canario rankea | FAQ + página de precio | Alta | 1-2 h |
| "suelo de resina para terraza exterior Canarias" | Encaja con Résineo y con la página de resinas epoxi de Apavi | Artículo en el blog de Apavi enlazando a Résineo | Media | Media jornada |
| Fichas de realizaciones (1 proyecto = 1 URL) | Hoy son galerías de 66-166 palabras; un caso real con ubicación posiciona en long-tail | Caso de estudio | Media | 1-2 h cada una |
| Páginas de isla (Gran Canaria / Tenerife / Lanzarote) para Résineo | Mismo patrón que funcionó en `cesped-artificial-tenerife` | Landing local | Media | Media jornada cada una |

## 4. Checklist técnico

| Comprobación | Apavi | Résineo | Piscinas |
|---|---|---|---|
| HTTPS / canonical autorreferenciado | ✅ Pasa | ✅ Pasa | ✅ Pasa (dominio por confirmar) |
| Sitemap + robots | ✅ Pasa | ✅ Pasa | ⚠️ Aviso: apunta a `www.piscinadearenatenerife.com` |
| Indexación (`site:`) | ⚠️ No sale en el buscador de prueba; comprobar en GSC | ❌ Falla: 0 resultados | ❌ Falla: el dominio en plural indexado es de otra empresa |
| NAP coherente | ✅ Pasa (654 765 548) | ❌ Falla (654 795 518) | ❌ Falla (654 795 518) |
| Schema | ✅ LocalBusiness, Service, FAQ | ⚠️ Solo LocalBusiness | ✅ LocalBusiness + FAQ + `parentOrganization` |
| Imágenes | ✅ WebP | ⚠️ JPG (hero de 372 KB); pasar a WebP | ⚠️ JPG/PNG (`caustics.png`); pasar a WebP |
| `alt` y `width`/`height` | ✅ | ✅ | ✅ |
| Analítica GA4/GTM | ✅ Consent Mode v2 | ❌ Falla: sin analítica | Revisar |
| Formulario de lead | ✅ | ❌ Falla: "en preparación" | ✅ (Supabase + Resend) |
| Verificación de GSC | ✅ (`google293869b8da6514af.html`) | ✅ mismo archivo, misma cuenta | Comprobar que esté añadida la propiedad del dominio correcto |

## 5. Estrategia: que las landings empujen a la principal (y no al revés)

Hoy la red es tres islas sueltas. Modelo recomendado, **hub & spoke**:

```
                 apavigreen.com  (HUB: marca, autoridad, GBP)
          ┌──────────────┴──────────────┐
  /piscinas-de-arena.html         /suelos-resineo.html     ← páginas NUEVAS en Apavi
   (resumen + enlace)              (resumen + enlace)
          │                              │
 piscinadearenatenerife.com      resineocanarias.com      ← SPOKES: profundidad de producto
          └──────── enlace en footer + contextual a Apavi ┘
```

Reglas:
1. **Cada landing enlaza al hub** con anchor de marca ("Apavi Green") y uno contextual ("instaladores de césped artificial en Canarias"). Es un único dueño con dominios temáticos: está bien siempre que los enlaces sean naturales y no un intercambio masivo.
2. **El hub tiene una página propia por línea** (`/piscinas-de-arena.html`, `/suelos-resineo.html`) de 400-600 palabras, que enlaza a la landing. Así Apavi gana relevancia temática y la landing recibe autoridad.
3. **Nada de contenido duplicado** entre los dominios: textos propios en cada sitio.
4. **Una sola ficha de Google Business Profile** (Apavi), con "Piscinas de arena" y "Suelos de resina" como servicios, y web = apavigreen.com.
5. **Medir cruzado:** el mismo contenedor GTM o propiedad GA4 con *cross-domain* para ver qué landing manda leads.
6. **Escalar:** cuando la landing de Résineo tenga más de 10 páginas con contenido, montarle un blog pequeño. Antes no compensa.

## 6. Oportunidades de keywords (estimación cualitativa, sin datos de Ahrefs/Semrush)

| Keyword | Dificultad est. | Oportunidad | Ranking actual | Intención | Contenido |
|---|---|---|---|---|---|
| piscinas de arena Tenerife | Media (competidor con la marca exacta) | Alta | — | Transaccional | Home de la landing de piscinas |
| piscina de arena precio | Media | Alta | — | Comercial | Artículo + calculadora |
| piscina de arena Canarias | Media (Tropical Pool) | Alta | — | Transaccional | Landing |
| Bio.design Tenerife / concesionario Bio.design | Baja | Alta | — | Navegacional | Home + Quiénes somos |
| Résineo Canarias | Baja | Alta | — | Navegacional | Home de Résineo |
| suelo drenante piscina | Baja-media | Alta | — | Comercial | `piscinas.html` ampliada |
| suelo antideslizante borde piscina | Baja | Alta | — | Comercial | FAQ / sección |
| moqueta de mármol exterior | Baja | Media | — | Comercial | `tecnologia.html` |
| suelo de resina y grava terraza | Baja-media | Media | — | Comercial | `suelos-terrazas.html` |
| pavimento continuo exterior Gran Canaria | Baja | Media | — | Transaccional | Landing local |
| césped artificial Gran Canaria | Alta | Media | Por verificar | Transaccional | Ya cubierto (home Apavi) |
| césped artificial Tenerife | Alta | Media | Por verificar | Transaccional | Ya cubierto |
| resina epoxi garaje Las Palmas | Media | Media | Por verificar | Transaccional | Ya cubierto |
| ¿cuánto dura una piscina de arena? | Baja | Media | — | Informacional | Blog |
| ¿se puede poner Résineo sobre baldosa? | Baja | Media | — | Informacional | FAQ |
| piscina de arena vs gresite | Baja | Media | — | Comercial | Comparativa |

> Para tener volúmenes y dificultad reales hay que conectar Ahrefs o Semrush. El conector de Ahrefs está configurado, pero hoy falló al conectar (proxy 403). Alternativa gratuita: el informe de *Consultas* de Search Console.

## 7. Competencia observada

| Dimensión | Nuestra red | Tropical Pool Canarias | piscinasdearenatenerife.com (Beach Feel) | Ganador |
|---|---|---|---|---|
| Dominio exact-match "piscinas de arena Tenerife" | No (singular) | No | **Sí** | Ellos |
| Contenido / profundidad | Fino en las landings | Medio | Medio (WordPress, varias fichas de producto) | Ellos |
| Indexación | Baja | Indexado | Indexado (≥5 URLs) | Ellos |
| Autoridad de marca Bio.design en Canarias | Concesionario Tenerife | Se anuncia como distribuidor oficial Bio.design de Canarias | — | Empate: hay que dejar clara la zona |
| Schema / técnico | Bueno | Desconocido | Desconocido | Nosotros |

---

## Plan de acción priorizado

### Quick wins (esta semana)
| # | Acción | Impacto | Esfuerzo | Depende de |
|---|---|---|---|---|
| 1 | **Confirmar el dominio real de la landing de piscinas** (singular vs. plural) | Alto | 5 min | Tú |
| 2 | Teléfono `654 765 548` en Résineo y Bio.design (schema + `tel:`) | Alto | 15 min | — |
| 3 | Footer de Résineo con enlace a apavigreen.com + footer de Bio.design con anchor de marca | Alto | 30 min | — |
| 4 | Dar de alta (o revisar) las propiedades de **ambas** landings en Search Console, enviar el sitemap y "Solicitar indexación" de la home | Alto | 30 min | Acceso a GSC |
| 5 | Formulario o WhatsApp en `resineocanarias.com/contacto` | Alto | 1 h | — |
| 6 | Unificar la garantía (8 vs 10 años) en Apavi | Medio | 10 min | Tú decides cuál |
| 7 | Anchors descriptivos en el footer de Apavi hacia las landings | Medio | 10 min | Paso 1 |
| 8 | GA4/GTM en Résineo (mismo contenedor, cross-domain) | Medio | 30 min | — |

### Inversiones estratégicas (este trimestre)
| # | Acción | Impacto | Esfuerzo |
|---|---|---|---|
| 1 | Ampliar las 5 páginas finas de Résineo a 600-900 palabras + FAQ + schema `Service` | Alto | 2-3 días |
| 2 | Crear `/piscinas-de-arena.html` y `/suelos-resineo.html` en Apavi (hub) | Alto | 1 día |
| 3 | 3 artículos de intención comercial: precio piscina de arena, arena vs gresite, suelo drenante para piscina | Alto | 1,5 días |
| 4 | Casos de estudio con fotos reales (1 URL por obra) en ambas landings | Medio-alto | Continuo |
| 5 | Imágenes a WebP en las dos landings | Medio | 2 h |
| 6 | Reseñas en Google Business Profile que mencionen "piscina de arena" y "Résineo" | Alto | Continuo |
| 7 | Directorios y backlinks locales: Bio.design y Résineo (fichas de distribuidor oficial que enlacen a nuestras landings), colegios de arquitectos, páginas amarillas | Alto | 1 día + seguimiento |
| 8 | Decidir sobre el repo público de GitHub (privado, o con la URL de la web) | Medio | 10 min |

---

## Fuentes consultadas
- Búsqueda `site:piscinasdearenatenerife.com`: devuelve `/`, `/piscinas-de-arena-beach-feel-producto`, `/piscinas-de-arena-stone-feel-pool-construccion`, `/author/damian`, `/piscinas-de-arena-presupuesto`
- Búsqueda `site:resineocanarias.com`: 0 resultados
- Competidores: tropicalpoolcanarias.com, piscinasdisersan.com
- Código: `resineo-canarias/index.html`, `biodesign-tenerife/index.html`, `biodesign-tenerife/sitemap.xml`, `apavi-green/index.html:1837,2410`

---

## Estado de los quick wins (6 oct 2026)

| # | Acción | Estado | Dónde |
|---|---|---|---|
| 1 | Confirmar el dominio de piscinas | ✅ Singular `www.piscinadearenatenerife.com` | — |
| 2 | Teléfono 654 765 548 en las landings | ✅ Hecho | Résineo: `index.html` (schema). Bio.design: schema, `aviso-legal`, `contacto` y el mensaje de error de `cuestionario.js` |
| 3 | Enlaces de las landings al hub | ✅ Hecho | Résineo: footer de las 10 páginas enlaza a Apavi (home, césped, resinas) y a piscinas de arena; `parentOrganization` en el schema. Bio.design: "Apavi Green" del footer enlaza a apavigreen.com en 8 páginas |
| 4 | Search Console: propiedades, sitemaps, indexación | ⏳ Pendiente (usuario) | GSC |
| 5 | Contacto de Résineo | 🟡 Parcial: teléfono + WhatsApp añadidos; el formulario sigue pendiente | `resineo-canarias/contacto.html` |
| 6 | Garantía 8 vs 10 años | ❓ Decisión del usuario: ¿8 años es solo el producto Plan Renove (Confort 30 mm) y 10 años la garantía general? | `index.html` (meta + FAQ) |
| 7 | Anchors descriptivos de Apavi hacia las landings | ✅ Hecho, y enlaces a `https://www.piscinadearenatenerife.com/` (evita la redirección) | `index.html` |
| 8 | GA4/GTM en Résineo | ⏳ Pendiente | — |

Ramas: `claude/eloquent-meitner-0l435q` en los tres repos (`apavi-green`, `resineo-canarias`, `biodesign-tenerife`). Las landings se despliegan desde `master` en Vercel: **hasta que se fusionen esas ramas, los cambios no estarán en vivo**.
Nota: en `biodesign-tenerife`, `tests/leads-handler.test.js` ya fallaba antes de estos cambios (dependencias sin instalar en el entorno); el resto de los tests pasa.

---

## Sesión 6 oct (continuación): PRs y contenido de Résineo

**PRs abiertos:**
- [Muya58/apavi-green#2](https://github.com/Muya58/apavi-green/pull/2): informe + enlaces www y anchors descriptivos
- [Muya58/biodesign-tenerife#1](https://github.com/Muya58/biodesign-tenerife/pull/1): teléfono + enlace a Apavi en el footer
- [Muya58/resineo-canarias#1](https://github.com/Muya58/resineo-canarias/pull/1): teléfono, enlaces, **contenido ampliado** y arreglos de CSS

**Résineo: lo hecho (estrategia #1 del plan trimestral)**
- `piscinas` (~1.000 palabras), `suelos-terrazas` (~850) y `tecnologia` (~700 + ficha técnica), con FAQ visible y schema Service/FAQPage.
- `realizaciones`, `quienes-somos` y `contacto` ampliadas sin inventar obras ni precios.
- Home: H1 con keyword; «El suelo que respira tu piscina» pasa a subtítulo.
- Bug corregido: el botón «Pedir presupuesto» de la cabecera era invisible (texto verde sobre fondo verde).
- Datos técnicos verificados con fuentes públicas de Résineo/LRVision: 95-97 % granulado, drenaje de 30-50 L/s/m², PN18, 10 mm sobre hormigón / 30 mm sobre grava, CSTB, hidrolimpiadora máx. 80 bar a 30 cm, vida útil de 10-15 años.

**Pendiente**
1. Fusionar los 3 PRs (las landings no cambian en vivo hasta entonces).
2. GSC: enviar los sitemaps y solicitar la indexación.
3. Decidir la garantía 8 vs 10 años en Apavi.
4. Siguiente paso: páginas hub en Apavi (`/piscinas-de-arena.html`, `/suelos-resineo.html`).
5. Résineo: formulario real de contacto, GA4/GTM, imágenes a WebP y fotos de obras propias cuando las haya.
6. Precio orientativo €/m² de Résineo en cuanto lo tengáis cerrado (sube mucho la conversión y el SEO de "precio").

---

## Sesión 6 oct (3): páginas hub en Apavi (subida manual por FTP)

**Contexto:** apavigreen.com está en AWS y se sube **a mano por FTP**: los cambios no se publican al fusionar el PR. A partir de ahora, cada entrega para Apavi va en una carpeta `SUBIR-FTP/<fecha>-<tema>/` con la misma estructura que el servidor, un `LEEME.txt` y un `.zip`.

**Hecho**
- Nuevas: `piscinas-de-arena.html` (~670 palabras, concesión Bio.design solo en la provincia de Santa Cruz de Tenerife) y `suelos-resineo.html` (~580 palabras, todas las islas). Cada una con FAQ visible + schema `Service` y `FAQPage`, enlace a su landing y enlaces cruzados (Résineo ↔ piscinas de arena, Résineo ↔ resina epoxi, piscinas de arena → césped artificial Tenerife).
- Portada: las tarjetas bento de Bio.design y Résineo apuntan a las páginas internas (ya no abren otra pestaña). En el footer, "Piscinas y moqueta de mármol" (#contacto) se sustituye por los 2 enlaces nuevos; "Nuestras marcas" sigue enlazando a las landings.
- Footer "Servicios" de 13 páginas + 1 artículo del blog: añadidos Piscinas de Arena y Suelo Résineo.
- `resinas-epoxi.html`: enlace contextual a Suelo Résineo.
- `sitemap.xml`: 2 URLs nuevas; lastmod actualizado de home y resinas-epoxi.
- Paquete: `SUBIR-FTP/2026-10-06-piscinas-y-resineo/` (17 archivos) + `.zip`.

**Pendiente**
- El usuario sube el paquete por FTP → comprobar las 2 URLs en vivo → GSC: enviar `https://www.apavigreen.com/sitemap.xml` y solicitar la indexación.
- Artículos del blog: "Piscina de arena vs gresite" y "Suelo antideslizante para el borde de la piscina".
- (Opcional) Despliegue automático por FTP/SFTP con GitHub Actions para no subir a mano.

## Sesión 6 oct (4): garantía unificada a 10 años
- Decisión del usuario: **garantía de 10 años** en toda la comunicación de Apavi.
- `index.html`: meta description, OG, Twitter y schema (oferta Plan Renove + 3 FAQ) → 10 años.
- `plan-renove.html`: texto de la oferta, cifra destacada y paso 4 → 10 años. El testimonio ("césped de hace 8 años") no se toca porque no habla de la garantía.
- **Sin cambiar (pendiente de confirmar):** la tabla de `blog/precio-cesped-artificial-canarias.html` da la garantía por gama (Básico 5 / Estándar 8 / Premium 10 años). Es garantía del producto según la calidad, no la garantía general.
- FTP: `SUBIR-FTP/2026-10-06-piscinas-y-resineo/` actualizado (ya incluye estos cambios) + `SUBIR-FTP/2026-10-06-garantia-10-anos/` por si el primero ya se había subido.

## Sesión 6 oct (5): se revierte la garantía a 10 años
- **Decisión final del usuario:** cada producto mantiene su propia garantía (p. ej. Plan Renove · Confort 30 mm = 8 años; tabla del blog por gamas: 5/8/10). Los "10 años" generales de la portada se quedan como estaban.
- Se deshace el commit de la garantía en `index.html` y `plan-renove.html`. Se elimina el paquete `SUBIR-FTP/2026-10-06-garantia-10-anos/`.
- `SUBIR-FTP/2026-10-06-piscinas-y-resineo/` vuelve a tener 17 archivos (sin `plan-renove.html`), con el `index.html` sin cambios de garantía. **Es el único paquete que hay que subir.**
- Aprendizaje: no unificar cifras de garantía entre productos; si hace falta, aclarar en el texto "según producto".

## ⚠️ Incidente 6 oct (noche): se sobrescribe el trabajo de la mañana en el servidor
- Por la mañana, el usuario hizo cambios en Apavi desde el **ordenador del trabajo** y los subió por FTP: fotos nuevas y cambios en resinas epoxi, jardines verticales y "en todo". **Esos cambios no estaban en GitHub.**
- El paquete `SUBIR-FTP/2026-10-06-piscinas-y-resineo/` se generó desde GitHub (versión del 29-9) y, al subirlo, **sobrescribió 15 HTML + sitemap** con versiones antiguas. El usuario confirma que se ha perdido el trabajo de hoy en esas páginas.
- **Sigue en el servidor:** las fotos subidas hoy (el paquete no llevaba imágenes) y las páginas que no estaban en el paquete.
- **Plan de recuperación:**
  1. Ordenador del trabajo: buscar la carpeta local desde la que se subió por FTP (o la conversación de Claude/herramienta con la que se editó).
  2. Si no hay copia: pedir a Voxia que restaure la copia de seguridad (snapshot de AWS) de hoy anterior a las 21:00, solo de los 15 HTML + sitemap.
  3. Con esas versiones: reaplicar los cambios de enlazado (script `apavi_hubs.py`: footer, bento de la portada, enlace en resinas-epoxi, sitemap) **encima** y generar un paquete nuevo.
  4. Guardar en GitHub la versión real del servidor.
- **Regla nueva (obligatoria):** antes de preparar cualquier paquete para el FTP de Apavi, **preguntar si se ha cambiado algo en el servidor desde la última sincronización** y, si es así, partir de los archivos del servidor (descargarlos por FTP), nunca solo de GitHub. Cualquier cambio que haga el usuario por su cuenta → subirlo también a GitHub.

## ✅ Para mañana (7 oct)
1. En el ordenador del trabajo: localizar los HTML subidos el 6-10 por la mañana (carpeta de FileZilla, Explorador `*.html fechademodificación:...`, Descargas o conversación de Claude).
2. Hacerlos llegar a esta sesión: subirlos a GitHub en `Muya58/apavi-green` → **Add file → Upload files**, a la carpeta `servidor/2026-10-07/` (rama nueva), o adjuntar un .zip en el chat.
3. Claude: reaplicar los enlaces de las páginas hub sobre esas versiones → paquete `SUBIR-FTP/2026-10-07-recuperacion/` → revisión archivo por archivo → subida.
4. Guardar en GitHub la versión real del servidor (fuente de la verdad).
5. Después: GSC (sitemap con www y solicitud de indexación), fusionar los PRs de Résineo y Bio.design y los artículos del blog.

## Fusionados (6 oct, noche)
- [Muya58/resineo-canarias#1](https://github.com/Muya58/resineo-canarias/pull/1) → `master` (df76865). Vercel publica solo; la preview del PR estaba en "Ready".
- [Muya58/biodesign-tenerife#1](https://github.com/Muya58/biodesign-tenerife/pull/1) → `master` (16943e9). Vercel publica solo.
- Comprobado antes de fusionar: ninguno de los dos repos tiene despliegue por FTP (solo `vercel.json`). No afectan a apavigreen.com.
- Pendiente: GSC de las dos landings (sitemap + solicitar la indexación).

## Correo de contacto: web@apavigreen.com
- Indicación del usuario: el correo de contacto es **web@apavigreen.com**.
- Résineo: `info@` → `web@` en el schema y en contacto.html ([Muya58/resineo-canarias#2](https://github.com/Muya58/resineo-canarias/pull/2), fusionado; Vercel lo publica).
- Bio.design: ya usaba `web@`. ✅
- **Apavi (pendiente, para la recuperación de mañana):** `proyectos.html:126` sigue con `info@apavigreen.com` (2 veces). No se toca ahora porque el FTP de Apavi está congelado hasta recuperar el trabajo del 6-10; corregirlo en el paquete de recuperación, partiendo de la versión del servidor.

# Apavi Green — Especificación de Diseño Web

**Fecha:** 2026-05-25  
**Estado:** Aprobado por Josep  
**Referencia visual:** corsua.com + mockup-home-aprobado.html

---

## 1. Objetivo

Construir el sitio web corporativo completo de Apavi Green: empresa especializada en instalación de césped artificial, jardines verticales, instalaciones deportivas, espacios infantiles y moqueta ferial, con base en Gran Canaria y proyectos en toda España.

**Resultados esperados:**
- Generar leads de presupuesto cualificados mediante cuestionario multi-paso
- Posicionar orgánicamente cada servicio en Google (SEO por página de servicio)
- Transmitir profesionalidad y confianza a través del portfolio de proyectos reales
- Ofrecer una experiencia "WOW" con el simulador interactivo antes/después

---

## 2. Identidad visual

### Paleta de color
```
Verde 950:  #0B2918   (fondos oscuros, footer)
Verde 900:  #143D25   (nav, headers, botones primarios)
Verde 700:  #207A4B   (hover, acentos)
Verde 600:  #27975D
Verde 500:  #2EB570   (acento principal, iconos)
Verde 400:  #5CC98C
Verde 300:  #8DDCAB   (texto sobre fondos oscuros)
Verde 100:  #E2F7EC   (fondos de tarjetas)
Verde 50:   #F2FCF6   (fondo sección clara)

Dorado:     #C49430   (CTAs principales, destacados)
Dorado L:   #E4C07A
Dorado BG:  #FBF3E2   (fondo pills premium)

Neutro 950: #0D0F0E
Neutro 900: #1A1D1B   (texto principal)
Neutro 500: #6B7370   (texto secundario)
Neutro 100: #EEF1EF   (bordes, separadores)
Neutro 50:  #F7F9F8   (fondo página)
```

### Tipografía
- **Titulares:** Plus Jakarta Sans (weights: 700, 800, 900)
- **Cuerpo:** Inter (weights: 400, 500, 600)
- **Google Fonts CDN** (ya referenciado en brand kit)

---

## 3. Arquitectura de ficheros

```
Apavi Green/
├── index.html                    ← Home (scroll largo, WOW factor)
├── cesped-artificial.html        ← Página SEO servicio
├── jardines-verticales.html      ← Página SEO servicio
├── instalaciones-deportivas.html ← Página SEO servicio
├── espacios-infantiles.html      ← Página SEO servicio
├── moqueta-ferial.html           ← Página SEO servicio
├── proyectos.html                ← Portfolio filtrable completo
├── cuestionario.html             ← Formulario multi-paso (shared)
├── landing.html                  ← Landing de conversión (sin nav)
├── assets/
│   ├── css/
│   │   ├── tokens.css            ← Variables CSS (colores, tipografía, radios)
│   │   ├── main.css              ← Estilos globales, nav, footer
│   │   └── components.css        ← Componentes reutilizables
│   ├── js/
│   │   ├── slider.js             ← Lógica slider antes/después
│   │   ├── configurador.js       ← Lógica configurador de precio
│   │   ├── portfolio.js          ← Filtros portfolio
│   │   └── cuestionario.js       ← Lógica multi-paso cuestionario
│   └── img/
│       ├── proyectos/            ← Fotos de proyectos (Josep las añade)
│       ├── servicios/            ← Imágenes de cada servicio
│       └── logo/                 ← Logo Apavi Green
├── mockup-home-aprobado.html     ← Referencia visual aprobada
└── docs/
    └── superpowers/
        └── specs/
            └── 2026-05-25-apavigreen-web-design.md
```

**Tecnología:** HTML5 + CSS3 + Vanilla JavaScript. Sin frameworks. Hosting estático (cualquier servidor web o GitHub Pages).

---

## 4. Páginas y secciones

### 4.1 `index.html` — Home

Página larga de scroll con navegación que ancla a secciones. Estructura:

#### Nav (sticky)
- Logo Apavi Green (icono SVG + texto)
- Links: Simulador · Proyectos · Servicios · Nosotros · Blog
- **Nota:** "Nosotros" y "Blog" son placeholders — en la primera versión anclan a sección o se omiten; se construyen como páginas en una segunda fase
- Teléfono + botón "Pedir presupuesto" (→ `cuestionario.html`)

#### Hero
- Fondo degradado verde oscuro (#0B2918 → #207A4B) con efecto noise sutil
- Glow radial derecho en verde 500
- **Izquierda:** tag "Especialistas en césped artificial · Gran Canaria", H1 con `<em>` en verde 400, subtítulo, dos CTAs (dorado → cuestionario, ghost → simulador), 3 stats (proyectos, años, presupuesto 24h)
- **Derecha:** componente Slider Antes/Después (ver §5.1)

#### Trust bar
- Fondo verde 900, 4 items: +500 proyectos · WhatsApp directo · Garantía 10 años · Visita gratuita

#### Configurador de precio `#simulador`
- Fondo neutro 950 (sección oscura)
- Grid 2 columnas: panel de configuración (4 pasos) + caja de resultado
- Pasos: Tipo de espacio · Superficie · Calidad · Instalación incluida
- Resultado: precio estimado en tiempo real + lista de incluidos + botón dorado → cuestionario
- Ver lógica en §5.2

#### Portfolio highlights `#proyectos`
- Grid 3 columnas, 6 proyectos destacados
- Filtros por categoría: Todos · Residencial · Deportivo · Corporativo · Jardín vertical · Piscina · Eventos
- Cards con overlay en hover (título + ubicación + m²)
- CTA "Ver todos los proyectos" → `proyectos.html`

#### Servicios `#servicios`
- Grid 3×2 de tarjetas de servicio
- Cada tarjeta: icono/emoji, título, descripción corta, link → página de servicio (SEO)
- Servicios: Césped Artificial · Jardines Verticales · Instalaciones Deportivas · Espacios Infantiles · Moqueta Ferial · Zonas de Piscina

#### CTA final `#cuestionario`
- Fondo verde 950 con glow central
- H2 + subtítulo + 2 botones (cuestionario + WhatsApp)
- Proceso en 4 pasos visuales: Tipo de proyecto → Superficie y uso → Datos de contacto → Presupuesto en 24h

#### Footer
- Logo · links legales (privacidad, aviso, cookies, contacto) · copyright

---

### 4.2 Páginas de servicio SEO (×5)

Estructura igual para todas — contenido diferente por servicio:

1. **Nav** (mismo que home)
2. **Hero de servicio** — H1 con keyword principal, imagen del servicio, CTA → cuestionario
3. **¿Qué es / beneficios** — bloque explicativo con iconos
4. **Proceso de instalación** — pasos numerados
5. **Galería de proyectos** — 4-6 fotos del tipo específico (→ `proyectos.html`)
6. **Preguntas frecuentes** — acordeón, 5-6 FAQs (SEO snippet)
7. **CTA final** → cuestionario
8. **Footer**

**Páginas y keywords objetivo:**

| Fichero | H1 / keyword principal |
|---|---|
| `cesped-artificial.html` | Césped artificial en Gran Canaria — instalación profesional |
| `jardines-verticales.html` | Jardines verticales en Gran Canaria — diseño e instalación |
| `instalaciones-deportivas.html` | Instalaciones deportivas con césped artificial — homologadas |
| `espacios-infantiles.html` | Césped artificial para espacios infantiles — seguro y resistente |
| `moqueta-ferial.html` | Moqueta ferial en Canarias — alquiler y venta |

---

### 4.3 `proyectos.html` — Portfolio completo

- Header simple + nav
- Grid filtrable completo (todos los proyectos disponibles)
- Filtros: categoría + isla/localización
- Al hacer clic en proyecto: modal o página de detalle con galería, descripción, m² y CTA

---

### 4.4 `cuestionario.html` — Formulario multi-paso

**Punto de entrada compartido** desde home, páginas de servicio y landing.

4 pasos, uno por pantalla, con barra de progreso y transición animada:

| Paso | Pregunta | Tipo de input |
|---|---|---|
| 1 | ¿Qué tipo de espacio quieres transformar? | Grid de opciones con icono (Jardín, Piscina, Terraza, Deportivo, Vertical, Corporativo, Otro) |
| 2 | ¿Cuántos metros cuadrados aproximadamente? | Pills: –20 / 20–50 / 50–100 / +100 / No lo sé |
| 3 | ¿Cuándo necesitas el presupuesto? | Pills: Urgente (–1 sem) / Este mes / En 1–3 meses / Solo informarme |
| 4 | Tus datos de contacto | Nombre + teléfono (requerido) + email (opcional) + mensaje libre |

**Al enviar:**
- Email automático a Apavi Green con el resumen del lead
- Mensaje de confirmación al usuario (pantalla de éxito)
- Integración: `mailto:` fallback o Formspree/Netlify Forms para hosting estático

**Diseño:**
- Fondo verde oscuro con logo en header mínimo
- Sin nav completa (no distracciones)
- Botones Anterior / Siguiente
- Indicador de paso "1 de 4"

---

### 4.5 `landing.html` — Landing de conversión

Página de campaña (Google Ads, redes sociales, email):

- Sin nav completa (solo logo)
- Hero directo con propuesta de valor + CTA → cuestionario
- 3 argumentos de confianza
- Testimonio/s
- CTA final repetido
- Footer mínimo (solo legal)
- **Sin menú de navegación** — elimina distracciones, maximiza conversión

---

## 5. Componentes interactivos

### 5.1 Slider Antes/Después

- **Handle arrastrable** con mouse y touch
- Al arrastrar izquierda/derecha revela la imagen "después" (CSS `clip-path`)
- **Chips de selección** de proyecto (Jardín, Piscina, Terraza, Deportivo, Vertical)
- Al seleccionar chip, cambia las imágenes con fade
- Las imágenes vendrán de `assets/img/proyectos/antes/` y `assets/img/proyectos/despues/`
- Fallback: gradientes verdes mientras no haya fotos reales

### 5.2 Configurador de Precio

- Cada selección actualiza la estimación en tiempo real (sin servidor)
- Tabla de precios base en `configurador.js` (Josep valida los rangos)
- Fórmula: `precio = m² × (precio_base_calidad + coste_instalacion)`
- Mostrar rango "Desde X € hasta Y €" (no precio exacto)
- Al pulsar "Obtener presupuesto exacto" → navega a `cuestionario.html` con parámetros pre-rellenados (tipo de espacio + m²)

### 5.3 Portfolio filtrable

- Filtrado por categoría con JavaScript vanilla (sin librerías)
- Animación fade/scale en el filtrado
- Datos de proyectos en array JS o atributos `data-*` en el HTML
- Hover overlay con título, localización y m²

### 5.4 Cuestionario multi-paso

- Estado en objeto JS `{ paso, tipo, superficie, urgencia, nombre, telefono, email, mensaje }`
- Transición CSS entre pasos (slide o fade)
- Validación antes de avanzar (campos requeridos)
- Barra de progreso animada
- Parámetros URL opcionales para pre-rellenar desde configurador (`?tipo=jardin&m2=50`)

---

## 6. SEO y rendimiento

- `<meta>` description única por página
- `<title>` con keyword + marca (ej: "Césped artificial Gran Canaria | Apavi Green")
- `sitemap.xml` básico con las 9 páginas
- `robots.txt`
- Schema markup `LocalBusiness` en index.html
- Imágenes con `alt` descriptivo y `loading="lazy"`
- Fuentes Google Fonts con `preconnect`
- CSS crítico inline en `<head>` para LCP rápido (opcional, mejora Core Web Vitals)

---

## 7. Responsive

- Breakpoints: móvil (< 640px), tablet (640–1024px), desktop (> 1024px)
- Nav colapsa a hamburger en móvil
- Hero: columna única en móvil (slider debajo del texto)
- Configurador: columna única en tablet/móvil
- Portfolio: 1 columna en móvil, 2 en tablet, 3 en desktop
- Servicios: 1 columna en móvil, 2 en tablet, 3 en desktop

---

## 8. Contenido pendiente de Josep

- [ ] Fotos de proyectos reales (antes/después para slider, portfolio)
- [ ] Logo en SVG o PNG de alta resolución
- [ ] Teléfono y WhatsApp reales
- [ ] Email de destino para el formulario
- [ ] Precio orientativo por m² (para el configurador)
- [ ] Textos de "Quiénes somos" (nosotros, historia, valores)
- [ ] Testimonios de clientes
- [ ] Localización exacta / zona de actuación

---

## 9. Orden de construcción recomendado

1. `tokens.css` + `main.css` — base de estilos y variables
2. `index.html` — home completo (prioridad máxima, es el WOW)
3. `cuestionario.html` — esencial para capturar leads
4. `landing.html` — para campañas inmediatas
5. `proyectos.html` — portfolio completo
6. Páginas de servicio SEO (×5) — en paralelo si es posible

---

*Spec aprobada por Josep · Nehunaya Flow · 2026-05-25*

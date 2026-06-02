# Plan Renove — Landing Page · Spec de diseño
**Fecha:** 2026-06-02  
**Proyecto:** Apavi Green — apavigreen.com  
**Archivo destino:** `plan-renove.html`

---

## Objetivo

Landing page de campaña permanente para el servicio **Plan Renove**: sustitución de césped viejo o deteriorado por césped artificial nuevo, con **retirada del césped existente incluida sin coste**.

No es una landing de temporada — es un servicio fijo del catálogo, accesible desde anuncios y desde el propio sitio.

---

## CTAs y jerarquía de conversión

| Prioridad | Acción | Implementación |
|-----------|--------|----------------|
| Principal | WhatsApp directo | `https://wa.me/34654765548` con texto prefijado |
| Principal | Llamada telefónica | `tel:+34654765548` |
| Secundaria | Formulario de presupuesto | Enlace a `cuestionario.html` |

El formulario aparece como enlace de texto discreto bajo los dos botones principales, y como botón terciario en el CTA final.

---

## Estructura de secciones

### 1. Header minimal
- Logo Apavi Green (imagen real `logo-apavigreen.jpeg`)
- Teléfono clicable a la derecha
- Sin menú de navegación (landing sin distracciones)

### 2. Hero
- **Badge dorado** con texto: `✦ PLAN RENOVE APAVI GREEN ✦`  
  Color: `#C49430` sobre fondo `rgba(196,148,48,.15)`, borde `#C49430`
- **Headline (H1):** "Renueva tu césped viejo con retirada incluida gratis"  
  "retirada incluida gratis" en color verde `#2EB570`
- **Subheadline:** "Retiramos tu césped actual sin coste. Instalamos césped artificial de calidad profesional. Garantía 10 años."
- **CTAs principales** (columna, ancho completo en móvil):
  - Botón WhatsApp (`#25D366`): "💬 Pedir presupuesto por WhatsApp"
  - Botón teléfono (`#2EB570`): "📞 Llamar ahora — +34 654 765 548"
- **CTA secundario:** enlace de texto "O rellena el formulario de presupuesto →"
- **Stats de confianza** (barra inferior del hero):  
  +500 proyectos · 10 años garantía · 24h respuesta

### 3. Trust bar
Franja estrecha con 3 ítems:
- ✓ Equipo propio en Gran Canaria
- ✓ Sin subcontratas
- ✓ Presupuesto gratis en 24h

### 4. Sección "¿Te suena esto?"
Título de sección, seguido de 4 tarjetas de dolor del cliente:
- 😫 Se ve feo y aplastado
- 🌡️ No aguanta el calor canario
- 🔧 Te da problemas constantes
- 💸 No era de calidad profesional

Caja de resolución al final: "💡 Nosotros lo retiramos gratis y lo sustituimos por césped profesional"

### 5. Cómo funciona (3 pasos)
Visualización horizontal con flechas:
1. **Nos contactas** — WhatsApp o teléfono
2. **Retiramos el viejo** — badge `GRATIS ✓` en verde
3. **Instalamos el nuevo** — Garantía 10 años (paso en dorado `#C49430`)

### 6. Galería — proyectos de renovación
Grid 2×2 de fotos antes/después.  
Placeholders hasta que Josep cargue las imágenes reales.  
Las imágenes van en `assets/img/renove/` (carpeta nueva).  
`object-fit: cover` con hover zoom suave.

### 7. Testimonio
Tarjeta centrada con borde verde:
- Texto: placeholder hasta recibir testimonio real
- Autor + ciudad + 5 estrellas

### 8. CTA final
Fondo con gradiente verde oscuro, repetición de los 3 CTAs:
- WhatsApp (principal)
- Teléfono (principal)
- Formulario (terciario, estilo ghost)

Subtexto: "Presupuesto gratis · Sin compromiso · Respuesta en 24h"

### 9. Footer minimal
- Copyright año actual (JS dinámico)
- Enlaces: Aviso Legal · Privacidad

---

## Diseño y estilos

- **Paleta:** idéntica al resto del sitio — tokens de `assets/css/tokens.css`
- **Tipografía:** Plus Jakarta Sans (titulares) + Inter (cuerpo)
- **Fondo:** `var(--n950)` / `#0B2918`
- **Hero background:** `linear-gradient(160deg, var(--g950), var(--g900) 60%, var(--n950))`
- **Badge Plan Renove:** dorado `#C49430` — diferenciador visual respecto a la landing genérica
- **CSS:** estilos inline con `<style>` en el propio archivo (patrón de `landing.html`)
- **noindex:** sí (`<meta name="robots" content="noindex">`) — es landing de campaña
- **Responsive:** breakpoint en 640px, CTAs en columna en móvil

---

## Assets necesarios

| Asset | Estado |
|-------|--------|
| `assets/img/logo/logo-apavigreen.jpeg` | ✅ Existe |
| `assets/img/renove/renove-1.jpg` | ⏳ Josep lo carga |
| `assets/img/renove/renove-2.jpg` | ⏳ Josep lo carga |
| `assets/img/renove/renove-3.jpg` | ⏳ Josep lo carga |
| `assets/img/renove/renove-4.jpg` | ⏳ Josep lo carga |
| Testimonio real | ⏳ Josep lo facilita |

---

## WhatsApp — texto prefijado

El botón de WhatsApp abrirá con mensaje preescrito:  
`https://wa.me/34654765548?text=Hola%2C%20me%20interesa%20el%20Plan%20Renove.%20Quisiera%20un%20presupuesto%20gratuito.`

---

## Archivos a crear / modificar

| Archivo | Acción |
|---------|--------|
| `plan-renove.html` | Crear nuevo |
| `assets/img/renove/` | Crear carpeta (placeholders) |

No se modifica ningún archivo existente.

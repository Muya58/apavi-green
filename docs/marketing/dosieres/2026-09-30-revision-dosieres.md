# 2026-09-30 — Revisión de dosieres actuales

Contexto: [[2026-09-29-utm-y-qr]] · Uso: se envían por **WhatsApp y email**.
Originales en `docs/marketing/dosieres/originales/`.

| Dosier | Formato | Contacto/CTA | Observaciones |
|---|---|---|---|
| Centros deportivos y wellness | Imagen vertical 1024×1536 | Sí (tel., email, web) sin enlaces ni QR | Erratas: "hodel; y teros deportes" |
| Restauración y hospitales (Altro) | Imagen vertical 1024×1536 | **No tiene** | Errata: "10 años de agrantia"; pies de foto "Trabajos realizados" / "Restaurante con pavimento Altro Ensemble™" |
| BIO.design + Résineo | Imagen horizontal 1492×1054 (2 caras) | **No tiene** | "CARAMEL" repetido; nombres en francés (verificar con catálogo oficial) |

## Problemas generales
1. **Resolución baja** (1024 px): en el móvil el texto pequeño no se lee y al ampliar se pixela.
2. **Una sola imagen muy larga**: no hay enlaces clicables (WhatsApp, llamar, web) ni QR.
3. **Marca inconsistente**: logo "APAVI GREEN S.L." gris + "Grupo Greening" en 1 y 2; "APAVIGREEN" / "grupo greening" distintos en 3.
4. **Fotos**: parecen generadas por IA. Si no son obras reales, no rotular como "Trabajos realizados" ni atribuir un producto concreto (riesgo de confianza y de publicidad engañosa). Priorizar fotos reales de obra.
5. Uso de marcas de terceros (Altro, BIO.design, Résineo) y "aplicadores oficiales acreditados": confirmar que hay acreditación/permiso de uso de logotipos.

## Propuesta
- Sistema común: portada · problema/solución · productos · proceso · garantías · **cierre con CTA + QR + botones clicables**.
- Doble salida por dosier: **PDF A4 multipágina con enlaces** (email) + **carrusel 1080×1350** (WhatsApp, última imagen con QR).
- QR/UTM por dosier: `utm_source=dosier-<sector>&utm_medium=whatsapp|email&utm_campaign=dosieres-2026`.

## Antes / después con IA (decisión 30-9)
- Opción recomendada: **foto real del "antes"** (espacio del cliente/prospecto) + **"después" generado por IA** rotulado como *"Simulación del resultado"*. Sirve además como propuesta personalizada de venta.
- Opción ilustrativa: antes y después 100 % IA → rotular *"Imagen ilustrativa"*. No usar en secciones de "trabajos realizados".
- **Nunca** presentar una imagen generada como obra real (riesgo de publicidad engañosa y de confianza).
- Ya existe un antes/después **real**: `assets/img/servicios/Pavimento Antes_despues.jpg` (resina en local, 960 px — válido para WhatsApp/PDF pequeño, no para imprenta).

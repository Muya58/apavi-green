# 2026-09-29 — Análisis del embudo de conversión GA4 (1-28 sept 2026)

## Lo que muestra el informe
- Pasos: first_visit → session_start → page_view → purchase
- 24 usuarios en los 3 primeros pasos (100 %), 0 en Compra. Móvil 16 / desktop 8 (67 % móvil)
- Tiempo transcurrido entre pasos: 0,0 s

## Diagnóstico
1. **Pasos 1-3 no miden nada**: son eventos automáticos que se disparan a la vez en la primera página vista. Por eso 100 % y 0,0 s.
2. **"Compra" siempre será 0**: la web es de captación de leads (presupuestos), no hay ecommerce ni evento `purchase`.
3. **24 usuarios en 28 días = solo quien acepta cookies**: `assets/js/analytics.js` carga GTM únicamente con consentimiento "todas". Sin Consent Mode v2, quien rechaza o ignora el banner es invisible. Tráfico real probablemente 2-4× mayor.
4. **first_visit = session_start = 24** → ningún usuario recurrente (o todos nuevos), coherente con una web recién lanzada y muestra minúscula (parte pueden ser pruebas internas).
5. **No se miden conversiones**: hay 55 enlaces `tel:`, 45 `wa.me`, `mailto:` y 2 formularios (`#contactForm`, `#quizForm`) sin eventos al dataLayer.

## Plan propuesto
- Consent Mode v2 (default denied + update al aceptar) para recuperar modelado de datos.
- Eventos: `click_whatsapp`, `click_telefono`, `click_email`, `generate_lead` (envío de formulario), `quiz_complete`; marcarlos como eventos clave en GA4.
- Nuevo embudo: session_start → vista de página de servicio → click contacto/inicio formulario → generate_lead.
- Excluir tráfico interno (filtro IP) y revisar con segmentos de canal.

## Otros hallazgos
- `aviso-legal.html:60` usa `+34 654 795 518`, distinto del teléfono del resto de la web (`654 765 548`). Verificar cuál es el correcto.

## Seguimiento
- Puntos 1 y 2 implementados → [[2026-09-29-consent-mode-y-eventos-lead]]

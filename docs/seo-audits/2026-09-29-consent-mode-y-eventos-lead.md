# 2026-09-29 — Consent Mode v2 + eventos de lead (puntos 1 y 2 del análisis del embudo)

Contexto: [[2026-09-29-analisis-embudo-ga4]]

## Qué se ha cambiado en el código
- `assets/js/analytics.js`
  - **Consent Mode v2 (modo avanzado)**: GTM se carga siempre con `analytics_storage`, `ad_storage`, `ad_user_data` y `ad_personalization` en `denied` (`wait_for_update: 500`, `ads_data_redaction: true`).
  - Si el usuario ya aceptó "todas", o lo hace en el banner (evento `ag:consent`), se pasa a `consent update` con `analytics_storage: granted`. Los permisos de publicidad se quedan siempre denegados (no hay Ads).
  - **Clics de contacto** (listener delegado, sirve en todas las páginas): `click_whatsapp`, `click_telefono`, `click_email` con `link_location` (`boton_flotante`, `cabecera`, `pie` o id de la sección) y `page_path`.
- `index.html` → formulario `#contactForm`: `generate_lead` con `form_id: contacto_home` cuando Formspree responde OK.
- `assets/js/cuestionario.js` → `generate_lead` con `form_id: cuestionario` al enviar OK. Se sustituye el teléfono provisional `+34 XXX XXX XXX` del mensaje de error por `+34 654 765 548`.
- No se envía ningún dato personal al dataLayer.
- Probado en Chromium (Playwright): consent default → clics → update granted → generate_lead. OK.

## Pendiente en Google Tag Manager (GTM-KVGB6TK4)
1. **Variables** → Nueva → Variable de capa de datos: `link_location`, `form_id` (DLV - link_location, DLV - form_id).
2. **Activador** → Evento personalizado → nombre del evento `^(click_whatsapp|click_telefono|click_email|generate_lead)$`, marcar "Usar coincidencia de expresiones regulares". Nombre: `CE - Leads`.
3. **Etiqueta** → Google Analytics: Evento de GA4
   - ID de medición: `G-P68MBLLY5R`
   - Nombre del evento: `{{Event}}`
   - Parámetros: `link_location` = `{{DLV - link_location}}`, `form_id` = `{{DLV - form_id}}`
   - Activador: `CE - Leads`
4. **Etiqueta de Google** existente: no hace falta tocarla (respeta Consent Mode automáticamente).
5. Vista previa (Tag Assistant) → comprobar los 4 eventos y el estado de consentimiento → **Publicar**.

## Pendiente en GA4
- Administrador → Definiciones personalizadas → dimensiones de evento `link_location` y `form_id`.
- Administrador → Eventos clave: marcar `generate_lead`, `click_whatsapp`, `click_telefono` (y `click_email` si interesa) cuando aparezcan (24-48 h).
- Nuevo embudo: `session_start` → vista de página de servicio → `click_*` → `generate_lead`.

## Nota legal
El modo avanzado envía pings sin cookies antes del consentimiento. Es la configuración que recomienda Google, pero conviene mencionarlo en `cookies.html` y confirmarlo con quien lleve la parte legal. Si se prefiere el modo básico, basta con volver a cargar GTM solo tras aceptar, manteniendo el `consent default`.

- Teléfono del aviso legal corregido a `+34 654 765 548` (confirmado por el cliente).

## PR y siguientes pasos
- PR abierto: https://github.com/Muya58/apavi-green/pull/1 (rama `claude/elegant-darwin-xvdvqo` → `master`). Vigilado por Claude.
- Fusión: en GitHub, pestaña "Files changed" para revisar → "Merge pull request" → "Confirm merge". GitHub Pages publica `master` en apavigreen.com en 1-2 min.
- Para tener más datos: GTM + eventos clave (ver arriba), Google Search Console enlazada a GA4, Google Business Profile con UTM, UTMs en redes/WhatsApp/folletos (QR), excluir tráfico interno, retención de datos a 14 meses, Microsoft Clarity (mapas de calor, respetando consentimiento).

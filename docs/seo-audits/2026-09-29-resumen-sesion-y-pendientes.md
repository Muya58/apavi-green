# 2026-09-29 — Resumen de la sesión y pendientes para el 30-9

Notas del día: [[2026-09-29-analisis-embudo-ga4]] · [[2026-09-29-consent-mode-y-eventos-lead]] · [[2026-09-29-utm-y-qr]]

## Hecho hoy
- Análisis del embudo GA4 (24 usuarios, pasos automáticos, compra = 0 porque la web es de leads).
- Código: Consent Mode v2 + eventos `click_whatsapp`, `click_telefono`, `click_email`, `generate_lead`. Teléfono del aviso legal y del cuestionario corregidos. PR #1 fusionado en `master`.
- GTM: contenedor importado (2 variables, activador `CE - Leads`, etiqueta `GA4 - Evento - Leads`). **Sin publicar todavía.**
- Descubierto: la web se publica por **FTP** (no GitHub) → `CLAUDE.md` creado con el flujo.
- Incidencias: dominio sin www sin SSL (apex → 54.170.183.243 Caddy; www → balanceador AWS con cert que ya cubre el apex) y FTP `53.30.159.68:21` sin conexión.
- Email al proveedor (Redes System + Voxia) preparado: `docs/entregas/email-proveedor-ssl-ftp-2026-09-29.eml`.
- Enlaces UTM por canal + 5 QR verificados (folleto, tríptico, lona, tarjeta, furgoneta): `docs/marketing/`.

## Pendiente — mañana 30-9
1. **Enviar el email al proveedor** (mejor "Responder a todos" en el hilo "ApaviGreen - Alojamiento web").
2. **Diseño del folleto y/o tríptico** con el QR ya puesto. El usuario traerá **fotos** y **cambios** de contenido.
   - QR a usar: `docs/marketing/qr/folleto.svg` / `triptico.svg` (llevan a cuestionario.html con UTM).
   - Colores de marca: verde oscuro #08100B / #0E1912, verdes #2EB570 / #5CC98C, dorado de botones (web). Tipos: Plus Jakarta Sans (títulos) + Inter (texto).
   - Tel./WhatsApp: +34 654 765 548. Web: www.apavigreen.com.
3. Cambiar los enlaces UTM en Google Business Profile, Instagram, Facebook, WhatsApp y firma de email.

## Pendiente — cuando responda el proveedor
- Subir por FTP `docs/entregas/subir-por-ftp-2026-09-29.zip` (index.html, aviso-legal.html, assets/js/analytics.js, assets/js/cuestionario.js).
- Comprobar aviso legal con 654 765 548 → Vista previa GTM con `https://www.apavigreen.com` → **Publicar** GTM.
- GA4: marcar eventos clave, dimensiones `link_location` / `form_id`, retención 14 meses, filtro de tráfico interno.
- Verificar que `https://apavigreen.com` redirige a www con SSL.

## Ideas en cola
- Microsoft Clarity (mapas de calor) respetando consentimiento.
- Mencionar Consent Mode en `cookies.html`.
- Alinear canonical/sitemap/schema a `www.apavigreen.com`.

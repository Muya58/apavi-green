# Apavi Green — web apavigreen.com

## Despliegue (IMPORTANTE)
- La web se publica **siempre por FTP** (lo sube el cliente a mano). **No** se despliega desde GitHub: fusionar a `master` no publica nada.
- Servidor FTP guardado por el cliente: `53.30.159.68:21` (dio timeout el 29-9-2026; verificar datos con el proveedor).
- Al terminar cada cambio: generar un zip con **solo los archivos de la web modificados** (manteniendo carpetas, sin `docs/`) en `docs/entregas/subir-por-ftp-AAAA-MM-DD.zip`, enviarlo al usuario e indicar en qué carpeta va cada archivo.
- Dominio y DNS los gestiona una **empresa externa**: cualquier cambio de DNS/SSL/redirecciones se pide por email (ver `docs/entregas/`).
- Versión canónica servida: `https://www.apavigreen.com` (AWS, balanceador `awselb`, IP 54.72.89.210, cert. Amazon que cubre apex y *.). El apex apunta a 54.170.183.243 (Caddy, sin SSL) — incidencia abierta 29-9-2026.
- El archivo `CNAME` es residual de GitHub Pages y no se usa.

## Proveedor de hosting / redes
- Hilo de referencia: "ApaviGreen - Alojamiento web" (4-8-2026).
- Redes System: soporte@redessystem.com, José Aperi Crespo (jose.aperi@redessystem.com)
- Voxia: soportetecnico@voxia.es, Rafael Fuentes (rafael.fuentes@voxia.es)
- Correos de Apavi Green: web@apavigreen.com (usuario), info@apavigreen.com

## Analítica
- GTM `GTM-KVGB6TK4` → GA4 `G-P68MBLLY5R`. Cargado desde `assets/js/analytics.js` con Consent Mode v2.
- Eventos al dataLayer: `click_whatsapp`, `click_telefono`, `click_email`, `generate_lead` (form_id).

## Contacto
- Teléfono/WhatsApp correcto: +34 654 765 548.

## Notas de trabajo
- Registro diario en `docs/seo-audits/AAAA-MM-DD-*.md` (formato Obsidian, enlaces `[[...]]`). Actualizar al final de cada tarea.

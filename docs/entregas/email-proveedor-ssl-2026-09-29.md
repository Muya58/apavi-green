**Asunto:** Urgente – apavigreen.com (sin www) sin certificado SSL y acceso FTP caído

Hola,

Os escribimos porque hemos detectado que el dominio **apavigreen.com (sin www)** no se puede abrir desde ningún navegador ni dispositivo:

- Chrome: "Este sitio web no puede proporcionar una conexión segura" (ERR_SSL_PROTOCOL_ERROR)
- Safari (iPhone, con datos móviles): "no ha podido establecer una conexión segura con el servidor"

La versión **www.apavigreen.com** sí funciona correctamente.

Según la comprobación que hemos hecho (SSL Shopper), `apavigreen.com` apunta a la IP **54.170.183.243**, un servidor **Caddy**, y **no tiene ningún certificado SSL instalado**. Parece que es un servicio de redirección que solo funciona por http.

Esto nos está haciendo perder visitas (mucha gente escribe el dominio sin www, y también aparece así en folletos y QR) y afecta al posicionamiento en Google.

**Lo que necesitamos:**
1. Que `https://apavigreen.com` tenga un **certificado SSL válido** (por ejemplo, Let's Encrypt).
2. Que `http://apavigreen.com` y `https://apavigreen.com` hagan una **redirección 301 a `https://www.apavigreen.com`**, conservando la ruta (por ejemplo, `apavigreen.com/zonas.html` → `https://www.apavigreen.com/zonas.html`).
3. Que `www.apavigreen.com` siga funcionando exactamente como ahora.

La forma más sencilla suele ser apuntar el registro A de `apavigreen.com` (@) al mismo servidor que `www` y hacer la redirección desde allí, o activar SSL en el servicio de redirección actual.

**Además**, no podemos conectar por FTP al servidor: la conexión a `53.30.159.68:21` agota el tiempo de espera ("No se pudo conectar al servidor"). ¿Nos podéis confirmar los datos de acceso actuales (servidor, protocolo FTP/SFTP, puerto y carpeta de la web) y si hay alguna restricción por IP? Tenemos pendiente subir una actualización de la web.

¿Nos podéis confirmar cuándo podréis hacerlo y avisarnos cuando esté listo para comprobarlo?

Muchas gracias,
Un saludo,

[Tu nombre]
Apavi Green
+34 654 765 548

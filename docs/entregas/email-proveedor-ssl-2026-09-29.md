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

Hemos comprobado que `www.apavigreen.com` está detrás de un balanceador de AWS (IP 54.72.89.210, servidor `awselb/2.0`) con un certificado de Amazon que **ya incluye `apavigreen.com` y `*.apavigreen.com`**. Por tanto, creemos que bastaría con apuntar el dominio raíz (`apavigreen.com` / `@`) a ese mismo balanceador (registro ALIAS/ANAME, o A-Alias si usáis Route 53) en lugar del servidor actual (54.170.183.243), y añadir en el balanceador la regla de redirección 301 de `apavigreen.com` a `https://www.apavigreen.com`.

**Además**, no podemos conectar por FTP al servidor: la conexión a `53.30.159.68:21` (la IP que teníamos guardada) agota el tiempo de espera ("No se pudo conectar al servidor"). ¿Nos podéis confirmar los datos de acceso actuales (servidor, protocolo FTP/SFTP, puerto y carpeta de la web) y si hay alguna restricción por IP? Tenemos pendiente subir una actualización de la web.

¿Nos podéis confirmar cuándo podréis hacerlo y avisarnos cuando esté listo para comprobarlo?

Muchas gracias,
Un saludo,

[Tu nombre]
Apavi Green
+34 654 765 548

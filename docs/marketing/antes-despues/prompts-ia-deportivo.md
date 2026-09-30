# Prompts IA — Antes/Después dosier deportivo (opción B, "Imagen ilustrativa")

Herramienta gratuita: **Google AI Studio** (aistudio.google.com) → modelo de imagen *Nano Banana* (Gemini … Image).
Hazlo en **dos pasos en la misma conversación** para que el "después" mantenga el encuadre.

## Paso 1 — ANTES (formato vertical 4:5)
> Foto realista tipo reportaje, formato vertical 4:5, tomada a la altura de los ojos desde una esquina de una pista polideportiva exterior antigua en un club deportivo de Canarias, tarde soleada. El suelo de hormigón está muy desgastado: pintura verde grisácea descolorida y agrietada, zonas desconchadas, manchas de humedad, hierbas en las grietas, líneas blancas borradas, hojas secas. Valla metálica oxidada, canasta de baloncesto con tablero gastado, palmeras y un edificio bajo blanco al fondo. Luz natural, sin personas, sin texto, sin logotipos.

## Paso 2 — DESPUÉS (sobre la imagen anterior)
> Usa exactamente la imagen anterior y mantén idénticos el encuadre, la perspectiva, la valla, la canasta, las palmeras, el edificio y la luz. Cambia solo el suelo: nueva pista con pavimento de resina deportiva acrílica, zona de juego azul y perímetro verde, superficie lisa y uniforme sin juntas, líneas blancas nuevas y nítidas de baloncesto y fútbol sala. Valla limpia y repintada en verde oscuro, tablero de canasta nuevo. Sin personas, sin texto, sin logotipos.

Descarga las 2 imágenes y pásaselas a Claude → se montan con `plantillas/antes_despues.py` usando `--rotulo "Imagen ilustrativa"`.
URL del QR: `https://www.apavigreen.com/instalaciones-deportivas.html?utm_source=dosier-deportivo&utm_medium=whatsapp&utm_campaign=dosieres-2026`

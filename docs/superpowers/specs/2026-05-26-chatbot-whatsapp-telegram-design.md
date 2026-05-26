# Chatbot WhatsApp + Telegram — Apavi Green
**Fecha:** 2026-05-26  
**Estado:** Aprobado  
**Stack:** Node.js · Railway · Supabase · Claude API · Meta Cloud API · Telegram Bot API · Resend

---

## 1. Objetivo

Construir un sistema de chatbot inteligente para WhatsApp y Telegram que:
1. Saluda y atiende al cliente de forma natural
2. Cualifica al lead recogiendo datos esenciales mediante un flujo guiado
3. Responde preguntas libres usando Claude AI (FAQs sobre servicios, zonas, garantías, precios)
4. Notifica a Apavi Green al instante cuando un lead está completo
5. Guarda todos los leads en Supabase con posibilidad de exportar a Excel y migrar en el futuro a Airtable o GoHighLevel

---

## 2. Arquitectura general

```
Cliente (WhatsApp / Telegram)
        ↓
   Bot Server (Node.js · Railway)
        ├── Webhook Receiver  → normaliza mensajes de ambos canales
        ├── Conversation Engine (State Machine) → gestiona el flujo
        ├── Claude API        → responde preguntas libres (FAQs)
        ├── Supabase          → persiste leads y conversaciones
        └── Notifier          → WhatsApp/Telegram + Email a Apavi Green
```

### Módulos principales

| Módulo | Responsabilidad |
|---|---|
| `webhook/` | Recibe y valida mensajes de Meta Cloud API y Telegram Bot API |
| `engine/` | Máquina de estados que controla el flujo de conversación |
| `ai/` | Integración con Claude API para respuestas libres |
| `db/` | Cliente Supabase: lectura y escritura de leads y conversaciones |
| `notifier/` | Envío de notificaciones a operadores (mensajería + email) |
| `config/` | Variables de entorno, constantes de servicios, knowledge base |

---

## 3. Flujo de conversación (State Machine)

### Estados

```
GREETING → FAQ_OR_QUALIFY → ASK_NAME → ASK_PHONE → ASK_TYPE → ASK_ADDRESS → ASK_AREA → CONFIRM → COMPLETED
```

### Descripción de cada estado

| Estado | Mensaje del bot | Acción esperada |
|---|---|---|
| `GREETING` | "Hola 👋 Soy el asistente de Apavi Green. ¿En qué puedo ayudarte?" | Cliente responde libremente |
| `FAQ_OR_QUALIFY` | Claude decide si responder o iniciar cualificación | Pregunta libre → Claude responde y vuelve · Solicita presupuesto → inicia flujo |
| `ASK_NAME` | "¿Cómo te llamas?" | Recoge nombre |
| `ASK_PHONE` | "¿Cuál es tu número de contacto?" | Recoge teléfono |
| `ASK_TYPE` | "¿Qué tipo de proyecto necesitas? [Césped · Vertical · Deportivo · Infantil · Moqueta]" | Recoge tipo |
| `ASK_ADDRESS` | "¿En qué dirección o municipio es la instalación?" | Recoge dirección |
| `ASK_AREA` | "¿Aproximadamente cuántos m² son?" | Recoge superficie |
| `CONFIRM` | Resumen de datos + "¿Es correcto?" | Confirma o corrige |
| `COMPLETED` | "✅ ¡Perfecto! Te contactamos en menos de 24h 🌿" | Dispara notificaciones |

### Regla de interrupción

En **cualquier estado**, si el cliente hace una pregunta libre, Claude la responde y el bot vuelve exactamente al estado anterior sin perder datos ya recogidos.

---

## 4. Base de datos (Supabase)

### Tabla `leads`

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | UUID | Clave primaria, auto-generada |
| `name` | text | Nombre del cliente |
| `phone` | text | Teléfono de contacto |
| `project_type` | text | cesped / vertical / deportivo / infantil / moqueta |
| `address` | text | Dirección o municipio |
| `area_m2` | numeric | Superficie aproximada |
| `channel` | text | whatsapp / telegram |
| `status` | text | nuevo / contactado / presupuestado / cerrado |
| `created_at` | timestamptz | Fecha y hora del lead |

### Tabla `conversations`

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | UUID | Clave primaria |
| `contact_id` | text | ID del usuario en WhatsApp o Telegram |
| `channel` | text | whatsapp / telegram |
| `state` | text | Estado actual del flujo |
| `messages` | JSONB | Historial completo de mensajes |
| `lead_id` | UUID | FK a `leads` cuando se completa |
| `updated_at` | timestamptz | Última actividad |

### Portabilidad
La estructura es estándar SQL, exportable a Excel en un clic desde Supabase. Migración futura a Airtable o GoHighLevel: exportar CSV e importar directamente, sin cambios en el código del bot.

---

## 5. Inteligencia artificial (Claude API)

### Cuándo se activa
- En `GREETING` / `FAQ_OR_QUALIFY` para interpretar la intención del cliente
- En cualquier estado cuando el cliente hace una pregunta libre

### Knowledge base (system prompt)
```
Eres el asistente virtual de Apavi Green, empresa especializada en:
- Césped artificial, resinas epoxi, jardines verticales, instalaciones deportivas,
  espacios infantiles y moqueta ferial
- Zona de trabajo: Gran Canaria y toda España
- Garantía: 10 años en todos los productos
- Presupuesto: gratuito, sin compromiso, respuesta en menos de 24h
- Instalación: equipo propio, profesional, más de 500 proyectos realizados

Responde siempre en español, de forma breve y amable. Si el cliente quiere
un presupuesto, indícale que le harás unas preguntas para preparárselo.
No inventes precios exactos. Sé honesto y profesional.
```

---

## 6. Notificaciones

### Al completar un lead — Mensaje WhatsApp/Telegram a Apavi Green
```
🟢 NUEVO LEAD — Apavi Green

👤 [Nombre]
📞 [Teléfono]
🏗️ [Tipo de proyecto]
📍 [Dirección]
📐 [m²]
📲 Canal: [WhatsApp / Telegram]
🕐 [Fecha y hora]
```

### Al completar un lead — Email a info@apavigreen.com
- **Asunto:** `🟢 Nuevo lead — [Nombre] · [Tipo] · [m²]m²`
- **Cuerpo:** mismos datos + enlace al panel de Supabase
- **Proveedor:** Resend (gratuito hasta 3.000 emails/mes)

### Al cliente
```
✅ ¡Perfecto [Nombre]! Hemos recibido tu solicitud.
Nuestro equipo te contactará en menos de 24h
para preparar tu presupuesto gratuito. 🌿
```

---

## 7. Stack técnico

| Componente | Tecnología | Coste |
|---|---|---|
| Servidor | Node.js 20 LTS | — |
| Hosting | Railway | Gratis (hasta 500h/mes) |
| Base de datos | Supabase (PostgreSQL) | Gratis (hasta 500MB) |
| IA | Claude API (Anthropic) | Pay-per-use (~$0.001/msg) |
| WhatsApp | Meta Cloud API | Gratis (1.000 conv/mes) |
| Telegram | Telegram Bot API | Gratis |
| Email | Resend | Gratis (3.000/mes) |
| **Total estimado** | | **~0€/mes** al inicio |

---

## 8. Variables de entorno necesarias

```env
# Meta (WhatsApp)
WHATSAPP_TOKEN=
WHATSAPP_PHONE_NUMBER_ID=
WHATSAPP_VERIFY_TOKEN=

# Telegram
TELEGRAM_BOT_TOKEN=

# Supabase
SUPABASE_URL=
SUPABASE_SERVICE_KEY=

# Claude API
ANTHROPIC_API_KEY=

# Resend (email)
RESEND_API_KEY=
NOTIFICATION_EMAIL=info@apavigreen.com

# Notificación a operadores
OPERATOR_WHATSAPP=34XXXXXXXXX
OPERATOR_TELEGRAM_CHAT_ID=
```

---

## 9. Estructura de carpetas del proyecto

```
apavi-chatbot/
├── src/
│   ├── webhook/
│   │   ├── whatsapp.js     # Receptor y validador Meta Cloud API
│   │   └── telegram.js     # Receptor Telegram Bot API
│   ├── engine/
│   │   ├── states.js       # Definición de estados y transiciones
│   │   └── handler.js      # Lógica principal del flujo
│   ├── ai/
│   │   └── claude.js       # Cliente Claude API + knowledge base
│   ├── db/
│   │   └── supabase.js     # Operaciones CRUD leads y conversaciones
│   ├── notifier/
│   │   ├── messaging.js    # Notificación WhatsApp/Telegram a operadores
│   │   └── email.js        # Notificación email vía Resend
│   └── config/
│       └── index.js        # Variables de entorno y constantes
├── index.js                # Entry point, servidor Express
├── package.json
├── .env.example
└── railway.toml            # Configuración de despliegue
```

---

## 10. Fases de implementación

| Fase | Contenido |
|---|---|
| **1. Infraestructura** | Proyecto Node.js, Railway, Supabase (tablas), variables de entorno |
| **2. Telegram** | Bot básico funcional con flujo completo en Telegram |
| **3. Claude AI** | Integración FAQ mode + knowledge base |
| **4. Notificaciones** | Mensajería a operadores + email Resend |
| **5. WhatsApp** | Meta Cloud API, webhook, verificación, flujo completo |
| **6. Testing** | Pruebas end-to-end en ambos canales, ajuste de respuestas |

---

## 11. Fuera de alcance (primera versión)

- Panel de administración web propio (se usa Supabase Studio)
- Integración con calendario / agenda automática
- Pagos o transacciones
- Multiidioma (solo español en v1)
- Integración con GoHighLevel o Airtable (preparado para migración futura)

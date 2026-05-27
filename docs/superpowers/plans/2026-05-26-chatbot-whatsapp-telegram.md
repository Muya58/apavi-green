# Chatbot WhatsApp + Telegram — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a hybrid guided + AI chatbot for WhatsApp and Telegram that qualifies leads (name, phone, project type, address, m²) and notifies Apavi Green via messaging + email.

**Architecture:** Node.js Express server on Railway receives webhooks from Meta Cloud API (WhatsApp) and Telegram Bot API, routes messages through a state machine, uses Claude Haiku for FAQ responses and intent detection, persists leads and conversations in Supabase, and sends operator notifications via WhatsApp/Telegram + Resend email.

**Tech Stack:** Node.js 20, Express 4, @anthropic-ai/sdk, @supabase/supabase-js, axios, resend, uuid, dotenv, jest

**Project location:** `C:\Users\josep\Apavi Green\apavi-chatbot\`

---

## File Map

| File | Responsibility |
|---|---|
| `index.js` | Express server, route registration, Telegram webhook setup |
| `src/config/index.js` | Load env vars, constants, knowledge base text |
| `src/db/supabase.js` | Supabase client, CRUD for leads and conversations |
| `src/engine/states.js` | State names, messages, project type map, helper validators |
| `src/engine/handler.js` | State machine logic — routes each message to correct state handler |
| `src/ai/claude.js` | Claude Haiku client, intent detection, FAQ responses |
| `src/notifier/email.js` | Resend email to info@apavigreen.com |
| `src/notifier/messaging.js` | WhatsApp + Telegram messages to operators |
| `src/webhook/telegram.js` | Parse Telegram updates, send Telegram messages |
| `src/webhook/whatsapp.js` | Parse Meta webhooks, verify token, send WhatsApp messages |
| `tests/engine.test.js` | Unit tests for pure functions in states.js |
| `.env.example` | Template for all required environment variables |
| `railway.toml` | Railway deployment configuration |

---

## Task 1: Project Scaffold

**Files:**
- Create: `C:\Users\josep\Apavi Green\apavi-chatbot\` (new project)
- Create: `package.json`
- Create: `.gitignore`
- Create: `.env.example`
- Create: `railway.toml`
- Create all `src/` subdirectories

- [ ] **Step 1: Create project folder and init git**

```bash
cd "C:/Users/josep/Apavi Green"
mkdir apavi-chatbot
cd apavi-chatbot
git init
```

- [ ] **Step 2: Create package.json**

Create `C:\Users\josep\Apavi Green\apavi-chatbot\package.json`:

```json
{
  "name": "apavi-chatbot",
  "version": "1.0.0",
  "description": "Chatbot WhatsApp + Telegram para Apavi Green",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "test": "jest --runInBand"
  },
  "dependencies": {
    "@anthropic-ai/sdk": "^0.24.0",
    "@supabase/supabase-js": "^2.43.0",
    "axios": "^1.7.0",
    "dotenv": "^16.4.0",
    "express": "^4.19.0",
    "resend": "^3.2.0",
    "uuid": "^9.0.0"
  },
  "devDependencies": {
    "jest": "^29.7.0",
    "nodemon": "^3.1.0"
  },
  "engines": {
    "node": ">=20.0.0"
  }
}
```

- [ ] **Step 3: Create .gitignore**

Create `C:\Users\josep\Apavi Green\apavi-chatbot\.gitignore`:

```
node_modules/
.env
*.log
.DS_Store
```

- [ ] **Step 4: Create .env.example**

Create `C:\Users\josep\Apavi Green\apavi-chatbot\.env.example`:

```env
# Meta (WhatsApp Business API)
WHATSAPP_TOKEN=
WHATSAPP_PHONE_NUMBER_ID=
WHATSAPP_VERIFY_TOKEN=apavi-verify-2026

# Telegram Bot
TELEGRAM_BOT_TOKEN=

# Supabase
SUPABASE_URL=
SUPABASE_SERVICE_KEY=

# Anthropic (Claude)
ANTHROPIC_API_KEY=

# Resend (email)
RESEND_API_KEY=
NOTIFICATION_EMAIL=info@apavigreen.com

# Operator notifications (who receives lead alerts)
OPERATOR_WHATSAPP=34XXXXXXXXX
OPERATOR_TELEGRAM_CHAT_ID=

# Server
PORT=3000
# Set this when deploying to Railway (auto-set by Railway)
# RAILWAY_PUBLIC_DOMAIN=your-app.railway.app
# Or set manually:
# WEBHOOK_URL=https://your-app.railway.app
```

- [ ] **Step 5: Create railway.toml**

Create `C:\Users\josep\Apavi Green\apavi-chatbot\railway.toml`:

```toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "node index.js"
healthcheckPath = "/"
healthcheckTimeout = 30
restartPolicyType = "on_failure"
restartPolicyMaxRetries = 3
```

- [ ] **Step 6: Create folder structure**

```bash
cd "C:/Users/josep/Apavi Green/apavi-chatbot"
mkdir -p src/config src/db src/engine src/ai src/notifier src/webhook tests
```

- [ ] **Step 7: Install dependencies**

```bash
cd "C:/Users/josep/Apavi Green/apavi-chatbot"
npm install
```

Expected output: `added XX packages` with no errors.

- [ ] **Step 8: Commit**

```bash
cd "C:/Users/josep/Apavi Green/apavi-chatbot"
git add .
git commit -m "chore: project scaffold — Node.js chatbot Apavi Green"
```

---

## Task 2: Config Module

**Files:**
- Create: `src/config/index.js`

- [ ] **Step 1: Create config/index.js**

Create `src/config/index.js`:

```js
require('dotenv').config();

const config = {
  whatsapp: {
    token: process.env.WHATSAPP_TOKEN,
    phoneNumberId: process.env.WHATSAPP_PHONE_NUMBER_ID,
    verifyToken: process.env.WHATSAPP_VERIFY_TOKEN || 'apavi-verify-2026',
    apiUrl: 'https://graph.facebook.com/v19.0'
  },
  telegram: {
    token: process.env.TELEGRAM_BOT_TOKEN,
    apiUrl: 'https://api.telegram.org'
  },
  supabase: {
    url: process.env.SUPABASE_URL,
    key: process.env.SUPABASE_SERVICE_KEY
  },
  anthropic: {
    apiKey: process.env.ANTHROPIC_API_KEY
  },
  resend: {
    apiKey: process.env.RESEND_API_KEY,
    from: 'Apavi Green <notificaciones@apavigreen.com>',
    to: process.env.NOTIFICATION_EMAIL || 'info@apavigreen.com'
  },
  operators: {
    whatsapp: process.env.OPERATOR_WHATSAPP,
    telegramChatId: process.env.OPERATOR_TELEGRAM_CHAT_ID
  },
  port: process.env.PORT || 3000
};

const required = [
  'WHATSAPP_TOKEN', 'WHATSAPP_PHONE_NUMBER_ID',
  'TELEGRAM_BOT_TOKEN',
  'SUPABASE_URL', 'SUPABASE_SERVICE_KEY',
  'ANTHROPIC_API_KEY',
  'RESEND_API_KEY',
  'OPERATOR_WHATSAPP', 'OPERATOR_TELEGRAM_CHAT_ID'
];

const missing = required.filter(k => !process.env[k]);
if (missing.length > 0) {
  console.warn(`⚠️  Missing env vars: ${missing.join(', ')}`);
}

module.exports = config;
```

- [ ] **Step 2: Verify config loads without crashing**

```bash
cd "C:/Users/josep/Apavi Green/apavi-chatbot"
node -e "const c = require('./src/config'); console.log('Config OK, port:', c.port);"
```

Expected output: `⚠️  Missing env vars: ...` (warnings, not errors) then `Config OK, port: 3000`

- [ ] **Step 3: Commit**

```bash
git add src/config/index.js
git commit -m "feat: config module with env var loading and validation"
```

---

## Task 3: Supabase Tables

**Where:** Supabase dashboard SQL editor (https://supabase.com → project → SQL Editor)

- [ ] **Step 1: Create project on supabase.com**

1. Go to https://supabase.com and sign in with GitHub or email
2. Click "New project"
3. Name: `apavi-chatbot`
4. Database password: save it securely
5. Region: `West EU (Ireland)` → closest to Spain
6. Click "Create new project" and wait ~2 minutes

- [ ] **Step 2: Run SQL to create tables**

In Supabase dashboard → SQL Editor → New query, paste and run:

```sql
-- Enable UUID extension
create extension if not exists "uuid-ossp";

-- Leads table: one row per qualified lead
create table leads (
  id uuid default uuid_generate_v4() primary key,
  name text not null,
  phone text not null,
  project_type text not null,
  address text not null,
  area_m2 numeric not null,
  channel text not null check (channel in ('whatsapp', 'telegram')),
  status text not null default 'nuevo'
    check (status in ('nuevo', 'contactado', 'presupuestado', 'cerrado')),
  created_at timestamptz default now()
);

-- Conversations table: one row per active conversation
create table conversations (
  id uuid primary key,
  contact_id text not null,
  channel text not null check (channel in ('whatsapp', 'telegram')),
  state text not null default 'GREETING',
  messages jsonb default '[]'::jsonb,
  lead_id uuid references leads(id),
  updated_at timestamptz default now()
);

-- Fast lookup by contact
create index on conversations(contact_id, channel);
```

Expected: "Success. No rows returned."

- [ ] **Step 3: Verify tables in Table Editor**

In Supabase → Table Editor, verify `leads` and `conversations` appear with correct columns.

- [ ] **Step 4: Get API credentials**

In Supabase → Settings → API:
- Copy **Project URL** → this is `SUPABASE_URL`
- Copy **service_role secret** (NOT anon key) → this is `SUPABASE_SERVICE_KEY`

- [ ] **Step 5: Create .env file with real credentials**

Create `C:\Users\josep\Apavi Green\apavi-chatbot\.env` (copy from .env.example, fill in SUPABASE_URL and SUPABASE_SERVICE_KEY — other vars can be filled later):

```env
SUPABASE_URL=https://xxxxxxxxxxxx.supabase.co
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIs...
```

- [ ] **Step 6: No code commit for this task** (SQL lives in Supabase, credentials in .env which is gitignored)

---

## Task 4: Supabase Client Module

**Files:**
- Create: `src/db/supabase.js`
- Create: `tests/engine.test.js` (partial — DB mock setup)

- [ ] **Step 1: Create src/db/supabase.js**

```js
const { createClient } = require('@supabase/supabase-js');
const config = require('../config');

const supabase = createClient(config.supabase.url, config.supabase.key);

/**
 * Load active conversation for a contact. Returns null if none found.
 */
async function getConversation(contactId, channel) {
  const { data, error } = await supabase
    .from('conversations')
    .select('*')
    .eq('contact_id', contactId)
    .eq('channel', channel)
    .neq('state', 'COMPLETED')
    .order('updated_at', { ascending: false })
    .limit(1)
    .maybeSingle();

  if (error) throw error;
  return data;
}

/**
 * Insert or update a conversation row.
 */
async function saveConversation(conv) {
  const { data, error } = await supabase
    .from('conversations')
    .upsert({
      id: conv.id,
      contact_id: conv.contact_id,
      channel: conv.channel,
      state: conv.state,
      messages: conv.messages,
      lead_id: conv.lead_id || null,
      updated_at: new Date().toISOString()
    }, { onConflict: 'id' })
    .select()
    .single();

  if (error) throw error;
  return data;
}

/**
 * Insert a new lead row. Returns the created lead with its id.
 */
async function saveLead(leadData) {
  const { data, error } = await supabase
    .from('leads')
    .insert({
      name: leadData.name,
      phone: leadData.phone,
      project_type: leadData.project_type,
      address: leadData.address,
      area_m2: parseFloat(leadData.area_m2),
      channel: leadData.channel,
      status: 'nuevo'
    })
    .select()
    .single();

  if (error) throw error;
  return data;
}

module.exports = { getConversation, saveConversation, saveLead };
```

- [ ] **Step 2: Smoke test DB connection**

```bash
cd "C:/Users/josep/Apavi Green/apavi-chatbot"
node -e "
const { getConversation } = require('./src/db/supabase');
getConversation('test-123', 'telegram')
  .then(r => console.log('DB OK, result:', r))
  .catch(e => console.error('DB ERROR:', e.message));
"
```

Expected output: `DB OK, result: null`

- [ ] **Step 3: Commit**

```bash
git add src/db/supabase.js
git commit -m "feat: supabase client with getConversation, saveConversation, saveLead"
```

---

## Task 5: State Machine

**Files:**
- Create: `src/engine/states.js`
- Create: `tests/engine.test.js`

- [ ] **Step 1: Create src/engine/states.js**

```js
const STATES = {
  GREETING:    'GREETING',
  ASK_NAME:    'ASK_NAME',
  ASK_PHONE:   'ASK_PHONE',
  ASK_TYPE:    'ASK_TYPE',
  ASK_ADDRESS: 'ASK_ADDRESS',
  ASK_AREA:    'ASK_AREA',
  CONFIRM:     'CONFIRM',
  COMPLETED:   'COMPLETED'
};

const MESSAGES = {
  GREETING:
    '👋 ¡Hola! Soy el asistente virtual de *Apavi Green*.\n\n' +
    'Instalamos césped artificial, jardines verticales, instalaciones deportivas y más ' +
    'en Gran Canaria y toda España.\n\n' +
    '¿En qué puedo ayudarte hoy?',

  ASK_NAME:
    '¡Perfecto! Para prepararte el presupuesto necesito unos datos rápidos. 📋\n\n' +
    '¿Cómo te llamas?',

  ASK_PHONE:
    '¿Cuál es tu número de teléfono de contacto? 📱',

  ASK_TYPE:
    '¿Qué tipo de proyecto necesitas?\n\n' +
    '1️⃣ Césped artificial\n' +
    '2️⃣ Jardín vertical\n' +
    '3️⃣ Instalación deportiva\n' +
    '4️⃣ Espacio infantil\n' +
    '5️⃣ Moqueta ferial\n\n' +
    'Escribe el número o el nombre del servicio.',

  ASK_ADDRESS:
    '¿En qué dirección o municipio sería la instalación? 📍',

  ASK_AREA:
    '¿Aproximadamente cuántos m² son? 📐',

  CONFIRM: (d) =>
    'Déjame confirmar los datos:\n\n' +
    `👤 *Nombre:* ${d.name}\n` +
    `📞 *Teléfono:* ${d.phone}\n` +
    `🏗️ *Proyecto:* ${d.project_type}\n` +
    `📍 *Dirección:* ${d.address}\n` +
    `📐 *Superficie:* ${d.area_m2} m²\n\n` +
    '¿Es todo correcto? Responde *Sí* para confirmar o *No* para corregir.',

  COMPLETED: (name) =>
    `✅ ¡Perfecto, ${name}! Hemos recibido tu solicitud.\n\n` +
    'Nuestro equipo te contactará en menos de 24h para preparar tu presupuesto gratuito. 🌿\n\n' +
    '¡Hasta pronto!'
};

// Maps user input → normalized project type label
const PROJECT_TYPE_MAP = {
  '1': 'Césped artificial',
  '2': 'Jardín vertical',
  '3': 'Instalación deportiva',
  '4': 'Espacio infantil',
  '5': 'Moqueta ferial',
  'cesped':    'Césped artificial',
  'césped':    'Césped artificial',
  'vertical':  'Jardín vertical',
  'jardin':    'Jardín vertical',
  'jardín':    'Jardín vertical',
  'deportivo': 'Instalación deportiva',
  'deportiva': 'Instalación deportiva',
  'deporte':   'Instalación deportiva',
  'infantil':  'Espacio infantil',
  'niños':     'Espacio infantil',
  'ninos':     'Espacio infantil',
  'moqueta':   'Moqueta ferial',
  'ferial':    'Moqueta ferial',
  'feria':     'Moqueta ferial'
};

/** Returns normalized project type or null if not recognized */
function parseProjectType(text) {
  return PROJECT_TYPE_MAP[text.toLowerCase().trim()] || null;
}

/** Returns true if text looks like a phone number */
function isPhoneNumber(text) {
  return /^[\+\s\d\-\(\)]{7,15}$/.test(text.trim());
}

/** Extracts the first number from text, or null */
function extractArea(text) {
  const match = text.match(/\d+(\.\d+)?/);
  return match ? parseFloat(match[0]) : null;
}

/** Returns true if text is likely a free question, not structured data */
function isLikelyQuestion(text) {
  if (text.includes('?')) return true;
  const lower = text.toLowerCase();
  return ['cuánto', 'cuanto', 'qué', 'que ', 'cómo', 'como ', 'cuándo', 'cuando',
          'dónde', 'donde', 'tienen', 'hacen', 'ofrecen', 'garantía', 'garantia',
          'precio', 'coste', 'cuesta'].some(w => lower.startsWith(w) || lower.includes(w));
}

module.exports = { STATES, MESSAGES, parseProjectType, isPhoneNumber, extractArea, isLikelyQuestion };
```

- [ ] **Step 2: Create tests/engine.test.js**

```js
const {
  parseProjectType,
  isPhoneNumber,
  extractArea,
  isLikelyQuestion
} = require('../src/engine/states');

describe('parseProjectType', () => {
  test('parses numeric option 1 → Césped artificial', () => {
    expect(parseProjectType('1')).toBe('Césped artificial');
  });
  test('parses numeric option 3 → Instalación deportiva', () => {
    expect(parseProjectType('3')).toBe('Instalación deportiva');
  });
  test('parses text "cesped" (without accent)', () => {
    expect(parseProjectType('cesped')).toBe('Césped artificial');
  });
  test('parses text "jardín" (with accent)', () => {
    expect(parseProjectType('jardín')).toBe('Jardín vertical');
  });
  test('returns null for unrecognized input', () => {
    expect(parseProjectType('piscina')).toBeNull();
  });
  test('is case insensitive', () => {
    expect(parseProjectType('CESPED')).toBe('Césped artificial');
  });
});

describe('isPhoneNumber', () => {
  test('accepts Spanish mobile +34 format', () => {
    expect(isPhoneNumber('+34 612 345 678')).toBe(true);
  });
  test('accepts plain 9-digit number', () => {
    expect(isPhoneNumber('612345678')).toBe(true);
  });
  test('rejects a name', () => {
    expect(isPhoneNumber('Juan García')).toBe(false);
  });
  test('rejects address text', () => {
    expect(isPhoneNumber('Calle Mayor 5, Las Palmas')).toBe(false);
  });
});

describe('extractArea', () => {
  test('extracts plain integer', () => {
    expect(extractArea('85')).toBe(85);
  });
  test('extracts number from sentence', () => {
    expect(extractArea('unos 120 metros cuadrados')).toBe(120);
  });
  test('extracts decimal', () => {
    expect(extractArea('45.5 m2')).toBe(45.5);
  });
  test('returns null when no number present', () => {
    expect(extractArea('no lo sé')).toBeNull();
  });
});

describe('isLikelyQuestion', () => {
  test('detects question mark', () => {
    expect(isLikelyQuestion('¿Cuánto cuesta el césped?')).toBe(true);
  });
  test('detects question without mark', () => {
    expect(isLikelyQuestion('cuánto cuesta')).toBe(true);
  });
  test('detects "precio" keyword', () => {
    expect(isLikelyQuestion('el precio del metro cuadrado')).toBe(true);
  });
  test('does not flag a normal name', () => {
    expect(isLikelyQuestion('María García')).toBe(false);
  });
  test('does not flag a normal address', () => {
    expect(isLikelyQuestion('Avenida Mesa y López 10')).toBe(false);
  });
});
```

- [ ] **Step 3: Run tests — verify they pass**

```bash
cd "C:/Users/josep/Apavi Green/apavi-chatbot"
npx jest tests/engine.test.js --verbose
```

Expected output: `Tests: 15 passed, 15 total`

- [ ] **Step 4: Commit**

```bash
git add src/engine/states.js tests/engine.test.js
git commit -m "feat: state machine definitions + unit tests (all passing)"
```

---

## Task 6: Claude AI Module

**Files:**
- Create: `src/ai/claude.js`

- [ ] **Step 1: Create src/ai/claude.js**

```js
const Anthropic = require('@anthropic-ai/sdk');
const config = require('../config');

const client = new Anthropic({ apiKey: config.anthropic.apiKey });

const KNOWLEDGE_BASE = `Eres el asistente virtual de Apavi Green, empresa instaladora profesional con sede en Gran Canaria.

SERVICIOS QUE OFRECEMOS:
- Césped artificial: residencial, comercial y deportivo. Productos premium de alta calidad.
- Jardines verticales: naturales y artificiales, para interior y exterior.
- Instalaciones deportivas: canchas de fútbol, pádel, tenis, zonas multideporte con césped FIFA.
- Espacios infantiles: suelo amortiguador de seguridad, cumple normativa europea EN 1177.
- Moqueta ferial: alquiler y venta para stands y eventos.
- Resinas epoxi: suelos de resina para garajes, comercios y espacios industriales.

ZONA DE TRABAJO: Gran Canaria principalmente. También trabajamos en toda España.

GARANTÍA: 10 años en todos nuestros productos e instalaciones.

PRESUPUESTO: Completamente gratuito, sin compromiso. Respuesta garantizada en menos de 24 horas.

EXPERIENCIA: Más de 500 proyectos realizados. Equipo propio de instaladores certificados.

PRECIOS: No des precios exactos porque dependen de los materiales, la superficie y las condiciones. Di siempre que el presupuesto es gratuito y personalizado.

INSTRUCCIONES DE COMPORTAMIENTO:
- Responde SIEMPRE en español.
- Sé breve (máximo 3-4 líneas), amable y profesional.
- Usa emojis con moderación (1-2 por mensaje).
- No inventes precios ni plazos exactos.
- Si el cliente quiere un presupuesto, dile que necesitas hacerle unas preguntas rápidas.
- Nunca digas que eres Claude o que estás hecho por Anthropic. Eres el asistente de Apavi Green.`;

/**
 * Detect if the user's message indicates they want a quote or installation info.
 * Returns boolean.
 */
async function isQualificationRequest(text) {
  const response = await client.messages.create({
    model: 'claude-haiku-20240307',
    max_tokens: 5,
    system: 'Responde únicamente "si" o "no". ¿El siguiente mensaje indica que el usuario quiere solicitar un presupuesto o información sobre contratar una instalación?',
    messages: [{ role: 'user', content: text }]
  });
  const answer = response.content[0].text.toLowerCase().trim();
  return answer.startsWith('si') || answer.startsWith('sí');
}

/**
 * Generate a FAQ response using the Apavi Green knowledge base.
 * conversationHistory: array of { role: 'user'|'bot', content: string }
 */
async function getFAQResponse(text, conversationHistory = []) {
  // Convert history to Anthropic message format (last 6 messages for context)
  const messages = [
    ...conversationHistory.slice(-6).map(m => ({
      role: m.role === 'bot' ? 'assistant' : 'user',
      content: m.content
    })),
    { role: 'user', content: text }
  ];

  const response = await client.messages.create({
    model: 'claude-haiku-20240307',
    max_tokens: 300,
    system: KNOWLEDGE_BASE,
    messages
  });

  return response.content[0].text;
}

module.exports = { isQualificationRequest, getFAQResponse };
```

- [ ] **Step 2: Verify Claude module loads (requires ANTHROPIC_API_KEY in .env)**

```bash
cd "C:/Users/josep/Apavi Green/apavi-chatbot"
node -e "const ai = require('./src/ai/claude'); console.log('Claude module OK');"
```

Expected: `Claude module OK`

- [ ] **Step 3: Commit**

```bash
git add src/ai/claude.js
git commit -m "feat: Claude AI module with intent detection and FAQ responses"
```

---

## Task 7: Conversation Handler

**Files:**
- Create: `src/engine/handler.js`

- [ ] **Step 1: Create src/engine/handler.js**

```js
const { v4: uuidv4 } = require('uuid');
const { STATES, MESSAGES, parseProjectType, isPhoneNumber, extractArea, isLikelyQuestion } = require('./states');
const { getConversation, saveConversation, saveLead } = require('../db/supabase');
const { isQualificationRequest, getFAQResponse } = require('../ai/claude');
const { notifyOperators } = require('../notifier/messaging');
const { sendLeadEmail } = require('../notifier/email');

/**
 * Main entry point: receives a message from any channel and returns the bot's reply.
 * @param {string} contactId  - Unique user ID on the channel (phone number or chat id)
 * @param {string} channel    - 'whatsapp' or 'telegram'
 * @param {string} text       - User's message text
 * @returns {Promise<string>} - Bot's reply text
 */
async function handleMessage(contactId, channel, text) {
  // Load existing conversation or create a new one
  let conv = await getConversation(contactId, channel);
  if (!conv) {
    conv = {
      id: uuidv4(),
      contact_id: contactId,
      channel,
      state: STATES.GREETING,
      data: {},
      messages: [],
      lead_id: null
    };
  }

  // Ensure data object exists (safety for legacy rows)
  if (!conv.data) conv.data = {};

  // Log incoming message
  conv.messages.push({ role: 'user', content: text, ts: new Date().toISOString() });

  let response;

  switch (conv.state) {

    case STATES.GREETING: {
      const wantsQuote = await isQualificationRequest(text);
      if (wantsQuote) {
        conv.state = STATES.ASK_NAME;
        response = MESSAGES.ASK_NAME;
      } else {
        const faq = await getFAQResponse(text, conv.messages);
        response = faq + '\n\n💬 ¿Te gustaría recibir un presupuesto gratuito?';
      }
      break;
    }

    case STATES.ASK_NAME: {
      if (isLikelyQuestion(text)) {
        const faq = await getFAQResponse(text, conv.messages);
        response = faq + '\n\n¿Y tu nombre para el presupuesto?';
      } else if (text.trim().length >= 2) {
        conv.data.name = text.trim();
        conv.state = STATES.ASK_PHONE;
        response = MESSAGES.ASK_PHONE;
      } else {
        response = '¿Podrías decirme tu nombre completo? 😊';
      }
      break;
    }

    case STATES.ASK_PHONE: {
      if (isLikelyQuestion(text)) {
        const faq = await getFAQResponse(text, conv.messages);
        response = faq + `\n\n📞 ¿Y tu teléfono, ${conv.data.name}?`;
      } else if (isPhoneNumber(text)) {
        conv.data.phone = text.trim();
        conv.state = STATES.ASK_TYPE;
        response = MESSAGES.ASK_TYPE;
      } else {
        response = 'Por favor, introduce un número de teléfono válido (ej: 612 345 678) 📱';
      }
      break;
    }

    case STATES.ASK_TYPE: {
      const projectType = parseProjectType(text);
      if (projectType) {
        conv.data.project_type = projectType;
        conv.state = STATES.ASK_ADDRESS;
        response = MESSAGES.ASK_ADDRESS;
      } else if (isLikelyQuestion(text)) {
        const faq = await getFAQResponse(text, conv.messages);
        response = faq + '\n\n¿Qué tipo de proyecto te interesa? (escribe el número del 1 al 5)';
      } else {
        response = 'Por favor, elige una opción:\n\n1️⃣ Césped · 2️⃣ Vertical · 3️⃣ Deportivo · 4️⃣ Infantil · 5️⃣ Moqueta';
      }
      break;
    }

    case STATES.ASK_ADDRESS: {
      if (isLikelyQuestion(text)) {
        const faq = await getFAQResponse(text, conv.messages);
        response = faq + '\n\n¿Y la dirección o municipio de la instalación?';
      } else if (text.trim().length >= 3) {
        conv.data.address = text.trim();
        conv.state = STATES.ASK_AREA;
        response = MESSAGES.ASK_AREA;
      } else {
        response = 'Indícame la dirección o municipio donde se haría la instalación 📍';
      }
      break;
    }

    case STATES.ASK_AREA: {
      const area = extractArea(text);
      if (area && area > 0) {
        conv.data.area_m2 = area;
        conv.state = STATES.CONFIRM;
        response = MESSAGES.CONFIRM(conv.data);
      } else if (isLikelyQuestion(text)) {
        const faq = await getFAQResponse(text, conv.messages);
        response = faq + '\n\n¿Y aproximadamente cuántos m² son?';
      } else {
        response = 'Dime los metros cuadrados aproximados (ej: 85, 200...) 📐';
      }
      break;
    }

    case STATES.CONFIRM: {
      const t = text.toLowerCase().trim();
      const confirmed = ['sí', 'si', 'correcto', 'ok', 'yes', 'vale', 'exacto', 'perfecto'].some(w => t.includes(w));
      const denied = ['no', 'mal', 'incorrecto', 'error', 'cambiar'].some(w => t.includes(w));

      if (confirmed) {
        // Save lead to database
        const lead = await saveLead({ ...conv.data, channel });
        conv.lead_id = lead.id;
        conv.state = STATES.COMPLETED;
        response = MESSAGES.COMPLETED(conv.data.name);

        // Fire notifications — non-blocking, errors logged but don't crash
        notifyOperators(lead).catch(err => console.error('[Notifier] messaging error:', err.message));
        sendLeadEmail(lead).catch(err => console.error('[Notifier] email error:', err.message));
      } else if (denied) {
        // Reset qualification data, start over
        conv.data = {};
        conv.state = STATES.ASK_NAME;
        response = 'Sin problema, empecemos de nuevo. ¿Cómo te llamas?';
      } else {
        response = 'Por favor, responde *Sí* para confirmar o *No* para corregir los datos.';
      }
      break;
    }

    case STATES.COMPLETED: {
      // Start a fresh conversation
      conv = {
        id: uuidv4(),
        contact_id: contactId,
        channel,
        state: STATES.GREETING,
        data: {},
        messages: [{ role: 'user', content: text, ts: new Date().toISOString() }],
        lead_id: null
      };
      const wantsQuote = await isQualificationRequest(text);
      if (wantsQuote) {
        conv.state = STATES.ASK_NAME;
        response = MESSAGES.ASK_NAME;
      } else {
        const faq = await getFAQResponse(text, []);
        response = faq + '\n\n💬 ¿Te gustaría que te preparemos un presupuesto?';
      }
      break;
    }

    default: {
      conv.state = STATES.GREETING;
      response = MESSAGES.GREETING;
    }
  }

  // Log bot response
  conv.messages.push({ role: 'bot', content: response, ts: new Date().toISOString() });

  // Persist conversation state
  await saveConversation(conv);

  return response;
}

module.exports = { handleMessage };
```

- [ ] **Step 2: Verify handler module loads without syntax errors**

```bash
cd "C:/Users/josep/Apavi Green/apavi-chatbot"
node -e "require('./src/engine/handler'); console.log('Handler OK');"
```

Expected: `Handler OK`

- [ ] **Step 3: Commit**

```bash
git add src/engine/handler.js
git commit -m "feat: conversation handler — state machine with Claude AI interrupt"
```

---

## Task 8: Email Notifier

**Files:**
- Create: `src/notifier/email.js`

**Prerequisite:** Create a free Resend account at https://resend.com, get API key, add to `.env` as `RESEND_API_KEY`.

- [ ] **Step 1: Create src/notifier/email.js**

```js
const { Resend } = require('resend');
const config = require('../config');

const resend = new Resend(config.resend.apiKey);

/**
 * Send lead notification email to Apavi Green operators.
 * @param {object} lead - Lead row from Supabase
 */
async function sendLeadEmail(lead) {
  const date = new Date(lead.created_at).toLocaleString('es-ES', {
    timeZone: 'Atlantic/Canary',
    day: '2-digit', month: '2-digit', year: 'numeric',
    hour: '2-digit', minute: '2-digit'
  });

  const subject = `🟢 Nuevo lead — ${lead.name} · ${lead.project_type} · ${lead.area_m2}m²`;

  const html = `
<!DOCTYPE html>
<html lang="es">
<body style="font-family:sans-serif;max-width:520px;margin:0 auto;padding:20px;color:#1a1d1b;">
  <div style="background:#143D25;padding:20px;border-radius:8px 8px 0 0;">
    <h2 style="color:#fff;margin:0;">🟢 Nuevo lead cualificado</h2>
    <p style="color:rgba(255,255,255,.7);margin:4px 0 0;">Apavi Green · Chatbot</p>
  </div>
  <table style="width:100%;border-collapse:collapse;border:1px solid #e5e5e5;border-top:none;border-radius:0 0 8px 8px;">
    <tr><td style="padding:12px 16px;background:#f8f8f8;font-weight:600;width:140px;">👤 Nombre</td><td style="padding:12px 16px;">${lead.name}</td></tr>
    <tr><td style="padding:12px 16px;background:#f0f0f0;font-weight:600;">📞 Teléfono</td><td style="padding:12px 16px;">${lead.phone}</td></tr>
    <tr><td style="padding:12px 16px;background:#f8f8f8;font-weight:600;">🏗️ Proyecto</td><td style="padding:12px 16px;">${lead.project_type}</td></tr>
    <tr><td style="padding:12px 16px;background:#f0f0f0;font-weight:600;">📍 Dirección</td><td style="padding:12px 16px;">${lead.address}</td></tr>
    <tr><td style="padding:12px 16px;background:#f8f8f8;font-weight:600;">📐 Superficie</td><td style="padding:12px 16px;">${lead.area_m2} m²</td></tr>
    <tr><td style="padding:12px 16px;background:#f0f0f0;font-weight:600;">📲 Canal</td><td style="padding:12px 16px;">${lead.channel === 'whatsapp' ? 'WhatsApp' : 'Telegram'}</td></tr>
    <tr><td style="padding:12px 16px;background:#f8f8f8;font-weight:600;">🕐 Fecha</td><td style="padding:12px 16px;">${date}</td></tr>
  </table>
  <div style="margin-top:20px;text-align:center;">
    <p style="color:#666;font-size:14px;">Lead guardado en Supabase · Estado: <strong>nuevo</strong></p>
  </div>
</body>
</html>`;

  await resend.emails.send({
    from: config.resend.from,
    to: config.resend.to,
    subject,
    html
  });

  console.log(`[Email] Lead notification sent to ${config.resend.to}`);
}

module.exports = { sendLeadEmail };
```

- [ ] **Step 2: Verify module loads**

```bash
node -e "require('./src/notifier/email'); console.log('Email notifier OK');"
```

Expected: `Email notifier OK`

- [ ] **Step 3: Commit**

```bash
git add src/notifier/email.js
git commit -m "feat: email notifier via Resend with styled HTML template"
```

---

## Task 9: Messaging Notifier

**Files:**
- Create: `src/notifier/messaging.js`

- [ ] **Step 1: Create src/notifier/messaging.js**

```js
const axios = require('axios');
const config = require('../config');

/**
 * Format lead data as a clean notification message.
 */
function formatLeadMessage(lead) {
  const date = new Date(lead.created_at).toLocaleString('es-ES', {
    timeZone: 'Atlantic/Canary',
    day: '2-digit', month: '2-digit', year: 'numeric',
    hour: '2-digit', minute: '2-digit'
  });

  return (
    `🟢 *NUEVO LEAD — Apavi Green*\n\n` +
    `👤 ${lead.name}\n` +
    `📞 ${lead.phone}\n` +
    `🏗️ ${lead.project_type}\n` +
    `📍 ${lead.address}\n` +
    `📐 ${lead.area_m2} m²\n` +
    `📲 Canal: ${lead.channel === 'whatsapp' ? 'WhatsApp' : 'Telegram'}\n` +
    `🕐 ${date}`
  );
}

/**
 * Send WhatsApp message to the operator number.
 */
async function sendWhatsAppToOperator(message) {
  if (!config.operators.whatsapp || !config.whatsapp.token) {
    console.warn('[Notifier] WhatsApp operator not configured, skipping.');
    return;
  }
  await axios.post(
    `${config.whatsapp.apiUrl}/${config.whatsapp.phoneNumberId}/messages`,
    {
      messaging_product: 'whatsapp',
      to: config.operators.whatsapp,
      type: 'text',
      text: { body: message }
    },
    {
      headers: {
        Authorization: `Bearer ${config.whatsapp.token}`,
        'Content-Type': 'application/json'
      }
    }
  );
  console.log('[Notifier] WhatsApp notification sent to operator');
}

/**
 * Send Telegram message to the operator chat.
 */
async function sendTelegramToOperator(message) {
  if (!config.operators.telegramChatId || !config.telegram.token) {
    console.warn('[Notifier] Telegram operator not configured, skipping.');
    return;
  }
  await axios.post(
    `${config.telegram.apiUrl}/bot${config.telegram.token}/sendMessage`,
    {
      chat_id: config.operators.telegramChatId,
      text: message,
      parse_mode: 'Markdown'
    }
  );
  console.log('[Notifier] Telegram notification sent to operator');
}

/**
 * Send lead notification to ALL configured operator channels.
 * Both run in parallel; one failure does not block the other.
 */
async function notifyOperators(lead) {
  const message = formatLeadMessage(lead);
  const results = await Promise.allSettled([
    sendWhatsAppToOperator(message),
    sendTelegramToOperator(message)
  ]);
  results.forEach((r, i) => {
    if (r.status === 'rejected') {
      console.error(`[Notifier] channel ${i} error:`, r.reason.message);
    }
  });
}

module.exports = { notifyOperators };
```

- [ ] **Step 2: Verify module loads**

```bash
node -e "require('./src/notifier/messaging'); console.log('Messaging notifier OK');"
```

Expected: `Messaging notifier OK`

- [ ] **Step 3: Commit**

```bash
git add src/notifier/messaging.js
git commit -m "feat: messaging notifier — WhatsApp + Telegram alerts to operators"
```

---

## Task 10: Telegram Webhook

**Files:**
- Create: `src/webhook/telegram.js`

**Prerequisite:** Create a Telegram bot via @BotFather, get the token, add to `.env` as `TELEGRAM_BOT_TOKEN`.

- [ ] **Step 1: Create src/webhook/telegram.js**

```js
const axios = require('axios');
const config = require('../config');
const { handleMessage } = require('../engine/handler');

/**
 * Send a text message to a Telegram chat.
 */
async function sendTelegramMessage(chatId, text) {
  await axios.post(
    `${config.telegram.apiUrl}/bot${config.telegram.token}/sendMessage`,
    {
      chat_id: chatId,
      text,
      parse_mode: 'Markdown'
    }
  );
}

/**
 * Express handler for POST /webhook/telegram
 * Telegram sends updates here; we always reply 200 first, then process.
 */
async function handleTelegramWebhook(req, res) {
  res.sendStatus(200); // Acknowledge to Telegram immediately

  const update = req.body;
  const message = update.message || update.edited_message;

  if (!message || !message.text) return; // Ignore non-text updates (photos, stickers, etc.)

  const chatId = message.chat.id.toString();
  const text = message.text.trim();

  if (!text) return;

  try {
    const reply = await handleMessage(chatId, 'telegram', text);
    await sendTelegramMessage(chatId, reply);
  } catch (err) {
    console.error('[Telegram] Handler error:', err.message);
    await sendTelegramMessage(chatId,
      'Lo siento, ha ocurrido un error. Por favor, inténtalo de nuevo en unos minutos. 🙏'
    ).catch(() => {});
  }
}

/**
 * Register the webhook URL with Telegram.
 * Called once on server start when RAILWAY_PUBLIC_DOMAIN or WEBHOOK_URL is set.
 */
async function setTelegramWebhook(webhookUrl) {
  const response = await axios.post(
    `${config.telegram.apiUrl}/bot${config.telegram.token}/setWebhook`,
    { url: `${webhookUrl}/webhook/telegram` }
  );
  return response.data;
}

module.exports = { handleTelegramWebhook, sendTelegramMessage, setTelegramWebhook };
```

- [ ] **Step 2: Verify module loads**

```bash
node -e "require('./src/webhook/telegram'); console.log('Telegram webhook OK');"
```

Expected: `Telegram webhook OK`

- [ ] **Step 3: Commit**

```bash
git add src/webhook/telegram.js
git commit -m "feat: Telegram webhook handler and message sender"
```

---

## Task 11: WhatsApp Webhook

**Files:**
- Create: `src/webhook/whatsapp.js`

**Prerequisite:** Meta Developer account + WhatsApp Business app set up (done in Task 12 setup steps).

- [ ] **Step 1: Create src/webhook/whatsapp.js**

```js
const axios = require('axios');
const config = require('../config');
const { handleMessage } = require('../engine/handler');

/**
 * Send a WhatsApp text message to a recipient.
 */
async function sendWhatsAppMessage(to, text) {
  await axios.post(
    `${config.whatsapp.apiUrl}/${config.whatsapp.phoneNumberId}/messages`,
    {
      messaging_product: 'whatsapp',
      to,
      type: 'text',
      text: { body: text }
    },
    {
      headers: {
        Authorization: `Bearer ${config.whatsapp.token}`,
        'Content-Type': 'application/json'
      }
    }
  );
}

/**
 * Express handler for GET /webhook/whatsapp
 * Meta calls this to verify the webhook endpoint.
 */
function handleWhatsAppVerification(req, res) {
  const mode      = req.query['hub.mode'];
  const token     = req.query['hub.verify_token'];
  const challenge = req.query['hub.challenge'];

  if (mode === 'subscribe' && token === config.whatsapp.verifyToken) {
    console.log('[WhatsApp] Webhook verified ✅');
    return res.status(200).send(challenge);
  }
  console.warn('[WhatsApp] Webhook verification failed — token mismatch');
  return res.sendStatus(403);
}

/**
 * Express handler for POST /webhook/whatsapp
 * Meta sends message events here.
 */
async function handleWhatsAppWebhook(req, res) {
  res.sendStatus(200); // Acknowledge to Meta immediately

  const body = req.body;
  if (body.object !== 'whatsapp_business_account') return;

  const entry   = body.entry?.[0];
  const change  = entry?.changes?.[0];
  const value   = change?.value;
  const messages = value?.messages;

  if (!messages || messages.length === 0) return;

  const msg = messages[0];
  if (msg.type !== 'text') {
    // Non-text message (image, audio, etc.) — send a polite fallback
    await sendWhatsAppMessage(msg.from,
      'Por ahora solo puedo procesar mensajes de texto. Por favor, escribe tu consulta 😊'
    ).catch(() => {});
    return;
  }

  const from = msg.from;
  const text = msg.text.body.trim();

  if (!text) return;

  try {
    const reply = await handleMessage(from, 'whatsapp', text);
    await sendWhatsAppMessage(from, reply);
  } catch (err) {
    console.error('[WhatsApp] Handler error:', err.message);
    await sendWhatsAppMessage(from,
      'Lo siento, ha ocurrido un error. Por favor, inténtalo de nuevo en unos minutos. 🙏'
    ).catch(() => {});
  }
}

module.exports = { handleWhatsAppVerification, handleWhatsAppWebhook, sendWhatsAppMessage };
```

- [ ] **Step 2: Verify module loads**

```bash
node -e "require('./src/webhook/whatsapp'); console.log('WhatsApp webhook OK');"
```

Expected: `WhatsApp webhook OK`

- [ ] **Step 3: Commit**

```bash
git add src/webhook/whatsapp.js
git commit -m "feat: WhatsApp webhook — Meta Cloud API verification and message handling"
```

---

## Task 12: Express Server + Railway Deploy

**Files:**
- Create: `index.js`

- [ ] **Step 1: Create index.js**

```js
require('dotenv').config();
const express = require('express');
const config = require('./src/config');
const { handleTelegramWebhook, setTelegramWebhook } = require('./src/webhook/telegram');
const { handleWhatsAppVerification, handleWhatsAppWebhook } = require('./src/webhook/whatsapp');

const app = express();
app.use(express.json());

// ── Health check ──────────────────────────────────────────
app.get('/', (req, res) => {
  res.json({ status: 'ok', service: 'Apavi Green Chatbot', ts: new Date().toISOString() });
});

// ── Telegram ──────────────────────────────────────────────
app.post('/webhook/telegram', handleTelegramWebhook);

// ── WhatsApp ──────────────────────────────────────────────
app.get('/webhook/whatsapp', handleWhatsAppVerification);   // Meta verification
app.post('/webhook/whatsapp', handleWhatsAppWebhook);       // Incoming messages

// ── Start ─────────────────────────────────────────────────
app.listen(config.port, async () => {
  console.log(`🤖 Apavi Green Chatbot running on port ${config.port}`);

  // Auto-register Telegram webhook when deployed on Railway
  const domain = process.env.RAILWAY_PUBLIC_DOMAIN || process.env.WEBHOOK_URL;
  if (domain && config.telegram.token) {
    const webhookUrl = domain.startsWith('http') ? domain : `https://${domain}`;
    try {
      const result = await setTelegramWebhook(webhookUrl);
      if (result.ok) {
        console.log(`✅ Telegram webhook registered: ${webhookUrl}/webhook/telegram`);
      } else {
        console.warn('[Telegram] Webhook registration returned:', result);
      }
    } catch (err) {
      console.error('[Telegram] Failed to register webhook:', err.message);
    }
  } else {
    console.log('ℹ️  Telegram webhook not registered (set RAILWAY_PUBLIC_DOMAIN or WEBHOOK_URL)');
  }
});
```

- [ ] **Step 2: Test server starts locally**

```bash
cd "C:/Users/josep/Apavi Green/apavi-chatbot"
node index.js
```

Expected output:
```
⚠️  Missing env vars: WHATSAPP_TOKEN, ...  (warnings, normal without full .env)
🤖 Apavi Green Chatbot running on port 3000
```

Open browser at `http://localhost:3000` — expected: `{"status":"ok","service":"Apavi Green Chatbot",...}`

Press Ctrl+C to stop.

- [ ] **Step 3: Commit server**

```bash
git add index.js
git commit -m "feat: Express server with Telegram + WhatsApp routes and auto webhook registration"
```

- [ ] **Step 4: Create GitHub repo and push**

1. Go to https://github.com/new
2. Name: `apavi-chatbot`
3. Private repo ✅
4. Don't add README (we have code already)
5. Click "Create repository"
6. Run:

```bash
cd "C:/Users/josep/Apavi Green/apavi-chatbot"
git remote add origin https://github.com/TU_USUARIO/apavi-chatbot.git
git push -u origin master
```

- [ ] **Step 5: Deploy to Railway**

1. Go to https://railway.app and sign in with GitHub
2. Click "New Project" → "Deploy from GitHub repo"
3. Select `apavi-chatbot`
4. Railway detects Node.js automatically → click "Deploy"
5. Wait ~2 minutes for first deploy

- [ ] **Step 6: Set environment variables in Railway**

In Railway → your project → Variables, add ALL variables from `.env.example` with real values:

```
WHATSAPP_TOKEN=...
WHATSAPP_PHONE_NUMBER_ID=...
WHATSAPP_VERIFY_TOKEN=apavi-verify-2026
TELEGRAM_BOT_TOKEN=...
SUPABASE_URL=...
SUPABASE_SERVICE_KEY=...
ANTHROPIC_API_KEY=...
RESEND_API_KEY=...
NOTIFICATION_EMAIL=info@apavigreen.com
OPERATOR_WHATSAPP=34XXXXXXXXX
OPERATOR_TELEGRAM_CHAT_ID=...
```

Railway redeploys automatically after saving variables.

- [ ] **Step 7: Get Railway public URL**

In Railway → your project → Settings → Domains → copy the URL (e.g. `apavi-chatbot.railway.app`)

- [ ] **Step 8: Test health endpoint**

Open browser: `https://apavi-chatbot.railway.app/`

Expected: `{"status":"ok","service":"Apavi Green Chatbot",...}`

- [ ] **Step 9: Register WhatsApp webhook in Meta Dashboard**

1. Go to https://developers.facebook.com → your app → WhatsApp → Configuration
2. Webhook URL: `https://apavi-chatbot.railway.app/webhook/whatsapp`
3. Verify token: `apavi-verify-2026`
4. Click "Verify and Save"
5. Subscribe to `messages` field

- [ ] **Step 10: Test Telegram bot end-to-end**

1. Find your bot on Telegram (the username you set with @BotFather)
2. Send `/start`
3. Bot should reply with the GREETING message
4. Complete the full qualification flow
5. Verify lead appears in Supabase → Table Editor → leads
6. Verify you received WhatsApp/Telegram notification
7. Verify you received email

- [ ] **Step 11: Test WhatsApp end-to-end**

1. In Meta Dashboard → WhatsApp → API Setup → send a test message to your WhatsApp number
2. Complete the full qualification flow
3. Verify lead saved in Supabase and notifications received

- [ ] **Step 12: Final commit**

```bash
git add .
git commit -m "feat: full chatbot deployed on Railway — WhatsApp + Telegram + Supabase + Claude AI"
git push
```

---

## External Accounts Needed (before Task 12)

| Service | URL | What to get |
|---|---|---|
| Supabase | https://supabase.com | SUPABASE_URL + SUPABASE_SERVICE_KEY |
| Telegram @BotFather | Telegram app | TELEGRAM_BOT_TOKEN |
| Meta Developers | https://developers.facebook.com | WHATSAPP_TOKEN + WHATSAPP_PHONE_NUMBER_ID |
| Anthropic | https://console.anthropic.com | ANTHROPIC_API_KEY |
| Resend | https://resend.com | RESEND_API_KEY |
| Railway | https://railway.app | (deploy, no token needed locally) |
| GitHub | https://github.com | (repo hosting) |

/* assets/js/configurador.js — Real-time price configurator */

const PRECIOS = {
  tipo: {
    'residencial':  { label: 'Residencial',         base: 18, desc: 'Jardines y terrazas privadas' },
    'deportivo':    { label: 'Deportivo',            base: 28, desc: 'Pistas deportivas homologadas' },
    'comercial':    { label: 'Comercial / Eventos',  base: 22, desc: 'Exposiciones y eventos' },
    'infantil':     { label: 'Espacio infantil',     base: 24, desc: 'Con acolchado de seguridad' },
    'vertical':     { label: 'Jardín vertical',      base: 45, desc: 'Por m² de pared cubierta' },
  },
  calidad: {
    'standard': { label: 'Estándar',  mult: 1.0, pile: '25mm' },
    'premium':  { label: 'Premium',   mult: 1.35, pile: '35mm' },
    'elite':    { label: 'Elite',     mult: 1.70, pile: '45mm' },
  },
  superficie: {
    's':   { label: 'Hasta 50 m²',   m2: 35,  discount: 0 },
    'm':   { label: '50 – 150 m²',   m2: 100, discount: 0.05 },
    'l':   { label: '150 – 300 m²',  m2: 225, discount: 0.10 },
    'xl':  { label: 'Más de 300 m²', m2: 350, discount: 0.15 },
  },
  instalacion: {
    'base':      { label: 'Sin preparación', extra: 0,  hint: 'Superficie ya preparada' },
    'prep':      { label: 'Con preparación', extra: 8,  hint: 'Incluye limpieza y nivelación' },
    'completa':  { label: 'Llave en mano',   extra: 14, hint: 'Preparación + bordillos + relleno' },
  },
};

class Configurador {
  constructor(containerSelector) {
    this.el = document.querySelector(containerSelector);
    if (!this.el) return;

    this.state = {
      tipo:        'residencial',
      calidad:     'standard',
      superficie:  'm',
      instalacion: 'prep',
    };

    this._bindPills();
    this._update();
  }

  /* ── bind all pill groups ── */
  _bindPills() {
    Object.keys(this.state).forEach(key => {
      const pills = this.el.querySelectorAll(`[data-config="${key}"]`);
      pills.forEach(pill => {
        pill.addEventListener('click', () => {
          pills.forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          this.state[key] = pill.dataset.value;
          this._update();
        });
      });
    });
  }

  /* ── calculate & render ── */
  _update() {
    const t = PRECIOS.tipo[this.state.tipo];
    const c = PRECIOS.calidad[this.state.calidad];
    const s = PRECIOS.superficie[this.state.superficie];
    const i = PRECIOS.instalacion[this.state.instalacion];

    const pricePerM2 = (t.base * c.mult) + i.extra;
    const subtotal   = pricePerM2 * s.m2;
    const discount   = subtotal * s.discount;
    const total      = Math.round(subtotal - discount);
    const perM2shown = Math.round(pricePerM2 * (1 - s.discount));

    // Update price display
    const priceEl = this.el.querySelector('#configPrice');
    const noteEl  = this.el.querySelector('#configNote');
    const m2El    = this.el.querySelector('#configM2');

    if (priceEl) priceEl.textContent = `Desde ${total.toLocaleString('es-ES')}€`;
    if (noteEl)  noteEl.textContent  = `≈ ${perM2shown}€/m² · ${s.label}${s.discount > 0 ? ` · ${(s.discount*100).toFixed(0)}% descuento` : ''}`;
    if (m2El)    m2El.textContent    = `${perM2shown}€/m²`;

    // Build query string for cuestionario
    this._buildCTA(perM2shown, total);
  }

  _buildCTA(perM2, total) {
    const btn = this.el.querySelector('#configCTA');
    if (!btn) return;
    const params = new URLSearchParams({
      tipo:        this.state.tipo,
      calidad:     this.state.calidad,
      superficie:  this.state.superficie,
      instalacion: this.state.instalacion,
      precio:      total,
    });
    btn.href = `cuestionario.html?${params.toString()}`;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new Configurador('#configuradorApp');
});

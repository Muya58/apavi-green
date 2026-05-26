/* assets/js/cuestionario.js — Multi-step lead form (4 steps) + Formspree */

const FORMSPREE_ID = 'YOUR_FORMSPREE_ID'; // ← Reemplazar con el ID real

class Cuestionario {
  constructor(selector) {
    this.el = document.querySelector(selector);
    if (!this.el) return;

    this.steps    = Array.from(this.el.querySelectorAll('[data-step]'));
    this.progress = this.el.querySelector('#quizProgress');
    this.current  = 1;
    this.total    = this.steps.length;
    this.data     = {};

    this._prefill();
    this._bindPills();
    this._bindNav();
    this._bindSubmit();
    this._renderStep();
  }

  /* ── Pre-fill from URL params (from configurador) ── */
  _prefill() {
    const params = new URLSearchParams(window.location.search);
    const map = {
      tipo:        '[data-field="tipo"]',
      calidad:     '[data-field="calidad"]',
      superficie:  '[data-field="superficie"]',
      instalacion: '[data-field="instalacion"]',
    };
    params.forEach((val, key) => {
      this.data[key] = val;
      const pill = this.el.querySelector(`[data-field="${key}"][data-value="${val}"]`);
      if (pill) pill.classList.add('active');
    });
  }

  /* ── Auto-advance on pill click ── */
  _bindPills() {
    this.el.querySelectorAll('[data-field][data-value]').forEach(pill => {
      pill.addEventListener('click', () => {
        const field = pill.dataset.field;
        // Deactivate siblings
        this.el.querySelectorAll(`[data-field="${field}"]`).forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        this.data[field] = pill.dataset.value;

        // Auto-advance after short delay (feel)
        if (this.current < this.total) {
          setTimeout(() => this._next(), 280);
        }
      });
    });
  }

  /* ── Prev / Next buttons ── */
  _bindNav() {
    this.el.querySelectorAll('[data-action="prev"]').forEach(btn => {
      btn.addEventListener('click', () => this._prev());
    });
    this.el.querySelectorAll('[data-action="next"]').forEach(btn => {
      btn.addEventListener('click', () => this._next());
    });
  }

  /* ── Submit ── */
  _bindSubmit() {
    const form = this.el.querySelector('form');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      // Gather text fields
      const nombre   = form.querySelector('[name="nombre"]')?.value.trim() || '';
      const telefono = form.querySelector('[name="telefono"]')?.value.trim() || '';
      const email    = form.querySelector('[name="email"]')?.value.trim() || '';
      const notas    = form.querySelector('[name="notas"]')?.value.trim() || '';

      if (!nombre || !telefono) {
        this._showError('Por favor rellena nombre y teléfono.');
        return;
      }

      const payload = { nombre, telefono, email, notas, ...this.data };

      const submitBtn = form.querySelector('[type="submit"]');
      submitBtn.disabled = true;
      submitBtn.textContent = 'Enviando…';

      try {
        const res = await fetch(`https://formspree.io/f/${FORMSPREE_ID}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify(payload),
        });

        if (res.ok) {
          this._showSuccess(nombre);
        } else {
          throw new Error('Error en el servidor');
        }
      } catch (err) {
        this._showError('Hubo un problema. Llámanos directamente al +34 XXX XXX XXX.');
        submitBtn.disabled = false;
        submitBtn.textContent = 'Enviar solicitud';
      }
    });
  }

  /* ── Navigation ── */
  _next() {
    if (this.current < this.total) {
      this.current++;
      this._renderStep();
    }
  }
  _prev() {
    if (this.current > 1) {
      this.current--;
      this._renderStep();
    }
  }

  /* ── Render active step ── */
  _renderStep() {
    this.steps.forEach(step => {
      const n = parseInt(step.dataset.step);
      step.style.display = n === this.current ? '' : 'none';
    });

    // Progress bar
    if (this.progress) {
      const pct = ((this.current - 1) / (this.total - 1)) * 100;
      this.progress.style.width = `${pct}%`;
    }

    // Step counter elements
    const counterEl = this.el.querySelector('#quizStepCounter');
    if (counterEl) counterEl.textContent = `${this.current} / ${this.total}`;
  }

  /* ── Feedback ── */
  _showSuccess(nombre) {
    this.el.innerHTML = `
      <div class="quiz-success">
        <div class="quiz-success-icon">✅</div>
        <h2>¡Gracias, ${nombre}!</h2>
        <p>Hemos recibido tu solicitud. Nos pondremos en contacto contigo en menos de 24 horas para preparar tu presupuesto personalizado.</p>
        <a href="index.html" class="btn-primary" style="margin-top:24px;display:inline-flex;">Volver al inicio</a>
      </div>
    `;
  }

  _showError(msg) {
    let err = this.el.querySelector('.quiz-error');
    if (!err) {
      err = document.createElement('p');
      err.className = 'quiz-error';
      this.el.querySelector('form')?.prepend(err);
    }
    err.textContent = msg;
    err.style.cssText = 'color:#e05151;font-size:13px;margin-bottom:12px;font-weight:600;';
  }
}

/* ── Nav hamburger (shared helper) ── */
function initHamburger() {
  const btn    = document.getElementById('navHamburger');
  const mobile = document.getElementById('navMobile');
  if (!btn || !mobile) return;
  btn.addEventListener('click', () => {
    mobile.classList.toggle('open');
  });
}

document.addEventListener('DOMContentLoaded', () => {
  new Cuestionario('#cuestionarioApp');
  initHamburger();
});

/* assets/js/slider.js — Antes/Después drag slider */

class SliderAntesDespues {
  constructor(wrapSelector) {
    this.wrap   = document.querySelector(wrapSelector);
    if (!this.wrap) return;

    this.body   = this.wrap.querySelector('.slider-body');
    this.after  = this.wrap.querySelector('.slider-after');
    this.handle = this.wrap.querySelector('.slider-handle');
    this.chips  = this.wrap.querySelectorAll('[data-slider-chip]');

    this.pos    = 55; // initial % (after panel shows from left)
    this.dragging = false;

    this._render();
    this._bindDrag();
    this._bindChips();
  }

  /* ── render clip-path ── */
  _render() {
    const right = 100 - this.pos;
    this.after.style.clipPath  = `inset(0 ${right}% 0 0)`;
    this.handle.style.left     = `${this.pos}%`;
  }

  /* ── drag (mouse + touch) ── */
  _bindDrag() {
    const start = (e) => {
      this.dragging = true;
      this.body.style.cursor = 'ew-resize';
      e.preventDefault();
    };
    const move = (e) => {
      if (!this.dragging) return;
      const rect = this.body.getBoundingClientRect();
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      let pct = ((clientX - rect.left) / rect.width) * 100;
      this.pos = Math.min(Math.max(pct, 2), 98);
      this._render();
    };
    const end = () => {
      this.dragging = false;
      this.body.style.cursor = 'ew-resize';
    };

    this.handle.addEventListener('mousedown', start);
    this.body.addEventListener('mousedown', start);
    window.addEventListener('mousemove', move);
    window.addEventListener('mouseup', end);

    this.handle.addEventListener('touchstart', start, { passive: false });
    this.body.addEventListener('touchstart', start, { passive: false });
    window.addEventListener('touchmove', move, { passive: false });
    window.addEventListener('touchend', end);
  }

  /* ── project chips ── */
  _bindChips() {
    this.chips.forEach(chip => {
      chip.addEventListener('click', () => {
        this.chips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');

        const before = chip.dataset.before;
        const after  = chip.dataset.after;
        const title  = chip.dataset.title;
        const meta   = chip.dataset.meta;

        // Update background images if provided, else keep gradient placeholders
        if (before) {
          this.wrap.querySelector('.slider-before').style.backgroundImage = `url('${before}')`;
          this.wrap.querySelector('.slider-before').style.backgroundSize  = 'cover';
          this.wrap.querySelector('.slider-before').style.backgroundPosition = 'center';
        }
        if (after) {
          this.after.style.backgroundImage    = `url('${after}')`;
          this.after.style.backgroundSize     = 'cover';
          this.after.style.backgroundPosition = 'center';
        }

        // Update title/meta in slider header
        const titleEl = this.wrap.querySelector('.slider-title');
        if (titleEl && title) titleEl.textContent = title;

        // Animate handle back to center
        this.pos = 55;
        this._render();
      });
    });
  }
}

/* Init on DOM ready */
document.addEventListener('DOMContentLoaded', () => {
  new SliderAntesDespues('#sliderWrap');
});

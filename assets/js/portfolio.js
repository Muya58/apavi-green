/* assets/js/portfolio.js — Filterable portfolio grid */

class PortfolioFilter {
  constructor(containerSelector) {
    this.container = document.querySelector(containerSelector);
    if (!this.container) return;

    this.chips  = this.container.querySelectorAll('[data-filter]');
    this.cards  = this.container.querySelectorAll('[data-category]');
    this.active = 'all';

    this._bindChips();
  }

  _bindChips() {
    this.chips.forEach(chip => {
      chip.addEventListener('click', () => {
        this.chips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        this.active = chip.dataset.filter;
        this._filter();
      });
    });
  }

  _filter() {
    this.cards.forEach(card => {
      const cat = card.dataset.category;
      const show = this.active === 'all' || cat === this.active;

      if (show) {
        card.style.opacity   = '0';
        card.style.transform = 'scale(0.95)';
        card.style.display   = '';
        // Trigger reflow then animate in
        requestAnimationFrame(() => {
          requestAnimationFrame(() => {
            card.style.transition = 'opacity .3s ease, transform .3s ease';
            card.style.opacity    = '1';
            card.style.transform  = 'scale(1)';
          });
        });
      } else {
        card.style.transition = 'opacity .2s ease, transform .2s ease';
        card.style.opacity    = '0';
        card.style.transform  = 'scale(0.95)';
        setTimeout(() => {
          if (this.active !== 'all' && card.dataset.category !== this.active) {
            card.style.display = 'none';
          }
        }, 200);
      }
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new PortfolioFilter('#portfolioSection');
});

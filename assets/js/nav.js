/* assets/js/nav.js — Shared nav hamburger + scroll-shadow */

document.addEventListener('DOMContentLoaded', () => {
  // Hamburger
  const btn    = document.getElementById('navHamburger');
  const mobile = document.getElementById('navMobile');
  if (btn && mobile) {
    btn.addEventListener('click', () => mobile.classList.toggle('open'));
    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!btn.contains(e.target) && !mobile.contains(e.target)) {
        mobile.classList.remove('open');
      }
    });
  }

  // Add shadow on scroll
  const nav = document.getElementById('nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.style.boxShadow = window.scrollY > 10 ? '0 4px 20px rgba(20,61,37,.12)' : '';
    }, { passive: true });
  }
});

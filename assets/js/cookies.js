/* assets/js/cookies.js — Banner de consentimiento de cookies LOPDGDD/RGPD */
(function () {
  'use strict';

  var STORAGE_KEY = 'ag_cookie_consent';
  var CONSENT_VERSION = '1'; // incrementar si cambia la política

  function getConsent() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      var obj = JSON.parse(raw);
      if (obj.version !== CONSENT_VERSION) return null;
      return obj;
    } catch (e) { return null; }
  }

  function saveConsent(type) {
    var obj = {
      version: CONSENT_VERSION,
      type: type, // 'all' | 'necessary'
      date: new Date().toISOString()
    };
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(obj)); } catch (e) {}
  }

  function hideBanner(banner) {
    banner.classList.remove('cb-visible');
    setTimeout(function () { banner.remove(); }, 400);
  }

  function buildBanner() {
    var banner = document.createElement('div');
    banner.id = 'cookieBanner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-modal', 'false');
    banner.setAttribute('aria-label', 'Aviso de cookies');
    banner.innerHTML =
      '<div class="cb-inner">' +
        '<div class="cb-text">' +
          '<p class="cb-title">&#127850; Este sitio usa cookies</p>' +
          '<p class="cb-desc">Usamos cookies propias esenciales para el funcionamiento del sitio. Puedes aceptar tambi&eacute;n cookies anal&iacute;ticas para mejorar tu experiencia. Consulta nuestra <a href="cookies.html" class="cb-link">Pol&iacute;tica de Cookies</a> y <a href="privacidad.html" class="cb-link">Pol&iacute;tica de Privacidad</a>.</p>' +
        '</div>' +
        '<div class="cb-actions">' +
          '<button class="cb-btn cb-btn-secondary" id="cbNecessary">Solo necesarias</button>' +
          '<button class="cb-btn cb-btn-primary" id="cbAcceptAll">Aceptar todas</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(banner);

    // Mostrar con animacion
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        banner.classList.add('cb-visible');
      });
    });

    document.getElementById('cbAcceptAll').addEventListener('click', function () {
      saveConsent('all');
      hideBanner(banner);
    });

    document.getElementById('cbNecessary').addEventListener('click', function () {
      saveConsent('necessary');
      hideBanner(banner);
    });
  }

  function init() {
    if (getConsent()) return; // ya tiene consentimiento guardado
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', buildBanner);
    } else {
      buildBanner();
    }
  }

  init();
})();

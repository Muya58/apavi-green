/* assets/js/analytics.js — Carga Google Tag Manager solo si el usuario acepta cookies analíticas (cookies.js) */
(function () {
  'use strict';

  var GTM_ID = 'GTM-KVGB6TK4';
  var STORAGE_KEY = 'ag_cookie_consent';
  var CONSENT_VERSION = '1';
  var loaded = false;

  function getConsent() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      var obj = JSON.parse(raw);
      if (obj.version !== CONSENT_VERSION) return null;
      return obj;
    } catch (e) { return null; }
  }

  function loadGTM() {
    if (loaded) return;
    loaded = true;

    window.dataLayer = window.dataLayer || [];
    dataLayer.push({ 'gtm.start': new Date().getTime(), event: 'gtm.js' });

    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtm.js?id=' + GTM_ID;
    document.head.appendChild(s);
  }

  var consent = getConsent();
  if (consent && consent.type === 'all') loadGTM();

  // cookies.js dispara este evento en cuanto el usuario pulsa "Aceptar todas",
  // para no perder el evento de página vista de la visita en curso.
  window.addEventListener('ag:consent', function (e) {
    if (e.detail && e.detail.type === 'all') loadGTM();
  });
})();

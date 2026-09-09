/* assets/js/analytics.js — Carga GA4 solo si el usuario acepta cookies analíticas (cookies.js) */
(function () {
  'use strict';

  var GA_MEASUREMENT_ID = 'G-XXXXXXXXXX'; // TODO: sustituir por el Measurement ID real de GA4
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

  function loadGA4() {
    if (loaded || GA_MEASUREMENT_ID.indexOf('XXXX') !== -1) return;
    loaded = true;

    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag('js', new Date());
    gtag('config', GA_MEASUREMENT_ID, { anonymize_ip: true });

    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_MEASUREMENT_ID;
    document.head.appendChild(s);
  }

  var consent = getConsent();
  if (consent && consent.type === 'all') loadGA4();

  // cookies.js dispara este evento en cuanto el usuario pulsa "Aceptar todas",
  // para no perder el evento de página vista de la visita en curso.
  window.addEventListener('ag:consent', function (e) {
    if (e.detail && e.detail.type === 'all') loadGA4();
  });
})();

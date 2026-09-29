/* assets/js/analytics.js — Google Tag Manager con Consent Mode v2 + medición de leads
 *
 * - Consent Mode v2 (modo avanzado): GTM se carga siempre, pero con todos los
 *   permisos denegados por defecto. Sin consentimiento, GA4 solo envía pings
 *   sin cookies (sin identificadores) que Google usa para modelar el tráfico.
 *   Al pulsar "Aceptar todas" (cookies.js → evento ag:consent) se concede
 *   analytics_storage y GA4 pasa a medir con normalidad.
 * - Leads: los clics en WhatsApp / teléfono / email se envían al dataLayer.
 *   Los formularios envían 'generate_lead' desde su propio script.
 *   Nunca se envían datos personales (nombre, teléfono, email del usuario).
 */
(function () {
  'use strict';

  var GTM_ID = 'GTM-KVGB6TK4';
  var STORAGE_KEY = 'ag_cookie_consent';
  var CONSENT_VERSION = '1';

  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }

  function getConsent() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      var obj = JSON.parse(raw);
      if (obj.version !== CONSENT_VERSION) return null;
      return obj;
    } catch (e) { return null; }
  }

  function consentState(granted) {
    var v = granted ? 'granted' : 'denied';
    return {
      analytics_storage: v,
      // La web no usa publicidad: los permisos de anuncios quedan siempre denegados.
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied'
    };
  }

  // ── 1. Consentimiento por defecto (antes de cargar GTM) ──
  var defaults = consentState(false);
  defaults.wait_for_update = 500;
  gtag('consent', 'default', defaults);
  gtag('set', 'ads_data_redaction', true);

  var consent = getConsent();
  if (consent && consent.type === 'all') {
    gtag('consent', 'update', consentState(true));
  }

  // cookies.js dispara este evento al elegir en el banner.
  window.addEventListener('ag:consent', function (e) {
    var granted = !!(e.detail && e.detail.type === 'all');
    gtag('consent', 'update', consentState(granted));
  });

  // ── 2. Carga de GTM ──
  dataLayer.push({ 'gtm.start': new Date().getTime(), event: 'gtm.js' });
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtm.js?id=' + GTM_ID;
  document.head.appendChild(s);

  // ── 3. Medición de clics de contacto ──
  function linkLocation(a) {
    if (a.closest('.float-btn')) return 'boton_flotante';
    if (a.closest('nav, header')) return 'cabecera';
    if (a.closest('footer')) return 'pie';
    var section = a.closest('section[id], [id]');
    return section ? section.id : 'contenido';
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var name = null;

    if (/^tel:/i.test(href)) name = 'click_telefono';
    else if (/^mailto:/i.test(href)) name = 'click_email';
    else if (/(wa\.me|api\.whatsapp\.com|web\.whatsapp\.com)/i.test(href)) name = 'click_whatsapp';
    if (!name) return;

    dataLayer.push({
      event: name,
      link_location: linkLocation(a),
      page_path: location.pathname
    });
  }, true);
})();

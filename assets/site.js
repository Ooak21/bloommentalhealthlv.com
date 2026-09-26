/* Bloom Mental Health · site behaviour: phone menu, contact form -> Bloom CRM, request-appointment frame sizing, GA lead events. */
(function () {
  // ---- where visitors come from (2026-09-25) ----
  // First touch is kept for good (localStorage), last touch per visit (sessionStorage). Ad/campaign tags,
  // referrer and pages only. It rides along with the contact form, the request card and the chat.
  var KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'gbraid', 'wbraid', 'fbclid', 'msclkid'];
  function store(kind) { try { return kind === 'first' ? window.localStorage : window.sessionStorage; } catch (_) { return null; } }
  function read(kind) { var st = store(kind); try { return st ? JSON.parse(st.getItem('bloom-attr-' + kind) || 'null') : null; } catch (_) { return null; } }
  function write(kind, v) { var st = store(kind); try { if (st) st.setItem('bloom-attr-' + kind, JSON.stringify(v)); } catch (_) {} }
  (function capture() {
    var q; try { q = new URLSearchParams(location.search); } catch (_) { return; }
    var touch = {}, tagged = false;
    KEYS.forEach(function (k) { var v = q.get(k); if (v) { touch[k] = v.slice(0, 200); tagged = true; } });
    var ref = document.referrer || '';
    var external = ref && ref.indexOf(location.origin) !== 0 && ref.indexOf('app.bloommentalhealthlv.com') < 0;
    if (external) touch.referrer = ref.slice(0, 300);
    touch.landing_page = location.pathname;
    touch.at = new Date().toISOString();
    // A new visit (no touch yet this session) or a new campaign/referrer replaces the last touch.
    if (!read('last') || tagged || external) write('last', touch);
    if (!read('first')) write('first', touch);
  })();
  window.bloomAttribution = function () {
    var last = read('last') || {}, first = read('first') || {}, out = {};
    KEYS.concat(['referrer', 'landing_page']).forEach(function (k) { if (last[k]) out[k] = last[k]; });
    if (first.at && first.at !== last.at) {
      if (first.utm_source) out.first_utm_source = first.utm_source;
      if (first.utm_medium) out.first_utm_medium = first.utm_medium;
      if (first.utm_campaign) out.first_utm_campaign = first.utm_campaign;
      if (first.referrer) out.first_referrer = first.referrer;
      if (first.landing_page) out.first_landing_page = first.landing_page;
    }
    if (first.at) out.first_seen = first.at;
    out.page = location.pathname;
    return out;
  };

  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
  }

  function track(name, params) { try { if (typeof gtag === 'function') gtag('event', name, params || {}); } catch (_) {} }

  // Contact form: writes a lead + message into the Bloom CRM (PHI stays in the CRM; the team gets a no-detail heads-up email).
  var form = document.getElementById('contact-form');
  if (form) {
    var msg = form.querySelector('.form-msg');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = (form.elements['name'].value || '').trim();
      var email = (form.elements['email'].value || '').trim();
      var subject = (form.elements['subject'].value || '').trim();
      var body = (form.elements['message'].value || '').trim();
      msg.className = 'form-msg';
      if (!name || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) { msg.textContent = 'Please add your name and a valid email address.'; msg.className = 'form-msg err'; return; }
      var parts = name.split(/\s+/); var first = parts.shift(); var last = parts.join(' ') || '';
      var btn = form.querySelector('button[type=submit]'); btn.disabled = true; msg.textContent = 'Sending…';
      fetch('https://usable-horse-871.convex.site/lead', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ first_name: first, last_name: last, email: email, source: 'website_contact', source_detail: subject.slice(0, 200), message: body.slice(0, 4000), attribution: window.bloomAttribution() })
      }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok && j.ok !== false, j: j }; }); })
        .then(function (res) {
          if (!res.ok) throw new Error((res.j && res.j.error) || 'send failed');
          form.reset(); msg.textContent = 'Thank you, ' + first + '. Your message is in. A member of our team will reach out within one business day.';
          track('generate_lead', { source: 'contact_form' });
        })
        .catch(function () { msg.textContent = 'Something went wrong. Please call 702-350-1419 or try again in a moment.'; msg.className = 'form-msg err'; })
        .then(function () { btn.disabled = false; });
    });
  }

  // Request-an-appointment page: the intake card lives on app.bloommentalhealthlv.com and reports its height + a sent signal.
  var frame = document.getElementById('bloom-inquiry');
  if (frame) {
    // The card lives on another origin and cannot read this page's URL, so hand it the visitor's tags.
    if (frame.dataset.src && !frame.getAttribute('src')) {
      var src = frame.dataset.src;
      try { src += (src.indexOf('?') < 0 ? '?' : '&') + 'attr=' + encodeURIComponent(JSON.stringify(window.bloomAttribution())); } catch (_) {}
      frame.setAttribute('src', src);
    }
    window.addEventListener('message', function (e) {
      if (e.origin !== 'https://app.bloommentalhealthlv.com') return;
      var d = e.data || {};
      if (d.bloomInquiry === 'height' && d.height > 300) { frame.style.height = (d.height + 24) + 'px'; frame.style.minHeight = '0'; }
      if (d.bloomInquiry === 'sent') { try { frame.scrollIntoView({ behavior: 'smooth', block: 'start' }); } catch (_) {} track('generate_lead', { source: 'request_appointment' }); }
    });
  }
})();

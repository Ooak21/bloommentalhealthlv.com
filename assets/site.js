/* Bloom Mental Health · site behaviour: phone menu, contact form -> Bloom CRM, request-appointment frame sizing, GA lead events. */
(function () {
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
        body: JSON.stringify({ first_name: first, last_name: last, email: email, source: 'website_contact', source_detail: subject.slice(0, 200), message: body.slice(0, 4000), consent: false })
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
    window.addEventListener('message', function (e) {
      if (e.origin !== 'https://app.bloommentalhealthlv.com') return;
      var d = e.data || {};
      if (d.bloomInquiry === 'height' && d.height > 300) { frame.style.height = (d.height + 24) + 'px'; frame.style.minHeight = '0'; }
      if (d.bloomInquiry === 'sent') { try { frame.scrollIntoView({ behavior: 'smooth', block: 'start' }); } catch (_) {} track('generate_lead', { source: 'request_appointment' }); }
    });
  }
})();

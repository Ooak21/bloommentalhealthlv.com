/* Bloom Mental Health · website chat (2026-09-25). Talks to the practice system's assistant (Convex action vee:chat on
   usable-horse-871). Answers from the practice's published facts, sends appointment requests to the front desk,
   routes any crisis to 988 / 911. The conversation follows the visitor from page to page for this visit only. */
(function () {
  var API = 'https://usable-horse-871.convex.cloud/api/action';
  var KEY = 'bloom-chat';
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  function track(name, params) { try { if (typeof gtag === 'function') gtag('event', name, params || {}); } catch (_) {} }
  function load() { try { return JSON.parse(sessionStorage.getItem(KEY) || 'null'); } catch (_) { return null; } }
  function save() { try { sessionStorage.setItem(KEY, JSON.stringify(state)); } catch (_) {} }
  var state = load() || { sid: 'web-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 10), msgs: [], open: false, sent: false };

  var GREETING = "Hi, I'm Bloom's virtual assistant. I can answer questions about our services, providers, insurance and pricing, or send your appointment request to our front desk. Please don't share medical details here.";
  var CHIPS = ['Do you take my insurance?', 'I would like an appointment', 'Do you see children?', '¿Hablan español?'];

  var root = document.createElement('div');
  root.className = 'chat';
  root.innerHTML =
    '<button class="chat-fab" type="button" aria-expanded="false" aria-controls="chatPanel">' +
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v11H9l-5 4V5Z"/></svg><span>Questions? Chat with us</span></button>' +
    '<section class="chat-panel" id="chatPanel" role="dialog" aria-label="Chat with Bloom Mental Health" hidden>' +
      '<header class="chat-head"><div><b>Bloom Mental Health</b><span>Questions &amp; appointment requests</span></div>' +
        '<button class="chat-x" type="button" aria-label="Close chat">&times;</button></header>' +
      '<p class="chat-crisis">In crisis? Call or text <a href="tel:988">988</a> or call <a href="tel:911">911</a>. This chat is not monitored around the clock.</p>' +
      '<div class="chat-log" aria-live="polite"></div>' +
      '<div class="chat-chips"></div>' +
      '<form class="chat-form" autocomplete="off"><label class="sr" for="chatIn">Your message</label>' +
        '<input id="chatIn" maxlength="600" placeholder="Type your question…"><button type="submit" aria-label="Send">' +
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12h15M13 6l6 6-6 6"/></svg></button></form>' +
      '<p class="chat-fine">An automated assistant. Answers come only from our published information. By chatting you agree to our <a href="/privacy/">Privacy Policy</a>.</p>' +
    '</section>';
  document.body.appendChild(root);

  var fab = root.querySelector('.chat-fab'), panel = root.querySelector('.chat-panel'), log = root.querySelector('.chat-log');
  var form = root.querySelector('.chat-form'), input = root.querySelector('#chatIn'), chips = root.querySelector('.chat-chips');
  var busy = false;

  function bubble(role, text, cta) {
    var d = document.createElement('div');
    d.className = 'chat-msg ' + (role === 'user' ? 'me' : 'them');
    var p = document.createElement('p'); p.textContent = text; d.appendChild(p);
    if (cta && cta.url) {
      var a = document.createElement('a'); a.className = 'chat-cta'; a.href = cta.url; a.textContent = cta.label + ' →';
      try { var u = new URL(cta.url); if (u.origin === location.origin) a.href = u.pathname; } catch (_) {}
      d.appendChild(a);
    }
    log.appendChild(d);
    log.scrollTop = log.scrollHeight;
  }
  function render() {
    log.innerHTML = '';
    bubble('assistant', GREETING);
    state.msgs.forEach(function (m) { bubble(m.role, m.content, m.cta); });
    chips.innerHTML = '';
    if (!state.msgs.length) CHIPS.forEach(function (c) {
      var b = document.createElement('button'); b.type = 'button'; b.textContent = c;
      b.addEventListener('click', function () { send(c); });
      chips.appendChild(b);
    });
  }
  function setOpen(open) {
    state.open = open; save();
    panel.hidden = !open; root.classList.toggle('open', open);
    fab.setAttribute('aria-expanded', String(open));
    if (open) { render(); setTimeout(function () { input.focus(); }, reduce ? 0 : 80); }
  }
  function typing(on) {
    var t = log.querySelector('.chat-typing');
    if (on && !t) { t = document.createElement('div'); t.className = 'chat-msg them chat-typing'; t.innerHTML = '<p><i></i><i></i><i></i></p>'; log.appendChild(t); log.scrollTop = log.scrollHeight; }
    if (!on && t) t.remove();
  }
  function send(text) {
    text = (text || '').trim(); if (!text || busy) return;
    busy = true; input.value = ''; chips.innerHTML = '';
    state.msgs.push({ role: 'user', content: text.slice(0, 600) }); save();
    bubble('user', text); typing(true);
    var payload = {
      path: 'vee:chat', format: 'json',
      args: { messages: state.msgs.slice(-12).map(function (m) { return { role: m.role, content: m.content }; }), session_id: state.sid,
              attribution: window.bloomAttribution ? window.bloomAttribution() : undefined }
    };
    fetch(API, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
      .then(function (r) { return r.json(); })
      .then(function (j) {
        var v = j && j.status === 'success' ? j.value : null;
        var reply = (v && v.reply) || 'Sorry, I could not answer that right now. Please call us at 702-350-1419.';
        typing(false);
        var m = { role: 'assistant', content: reply }; if (v && v.cta) m.cta = v.cta;
        state.msgs.push(m); save(); bubble('assistant', reply, m.cta);
        if (v && v.captured && !state.sent) { state.sent = true; save(); track('generate_lead', { source: 'chat' }); }
        if (v && v.crisis) track('chat_crisis_shown');
      })
      .catch(function () { typing(false); bubble('assistant', 'Sorry, I am having trouble connecting. Please call us at 702-350-1419.'); })
      .then(function () { busy = false; });
  }

  fab.addEventListener('click', function () { setOpen(!state.open); if (state.open) track('chat_open'); });
  root.querySelector('.chat-x').addEventListener('click', function () { setOpen(false); fab.focus(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && state.open) { setOpen(false); fab.focus(); } });
  form.addEventListener('submit', function (e) { e.preventDefault(); send(input.value); });
  if (state.open && innerWidth > 760) setOpen(true);
})();

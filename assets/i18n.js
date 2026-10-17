/* Bloom Mental Health · English / Español (2026-10-16, Michelle: "Is there a button to translate the words in Spanish?").
   Same approach as Vitality: one button in the header flips the page, its forms and the chat between English and Spanish
   in place, and the choice follows the visitor from page to page. The Spanish lives in assets/es.js (built from
   tools/content_es.py) and only loads for visitors who pick it. Text is matched on the exact English string, one text
   node at a time; anything without a Spanish line stays English (window.__bloomMiss lists it). Elements marked
   class="notrans" or translate="no" are never touched (chat messages, typed text). */
(function () {
  var KEY = 'bloom_lang';
  var html = document.documentElement;
  var me = document.currentScript;
  var ES_SRC = (me && me.getAttribute('data-es')) || '/assets/es.js';
  var path = location.pathname;
  var lang = 'en';
  try { lang = localStorage.getItem(KEY) === 'es' ? 'es' : 'en'; } catch (_) {}
  window.bloomLang = lang;

  var ES = null, loading = null, mo = null;
  var texts = new Map();   // text node -> its English
  var attrs = [];          // [element, attribute, English]
  var enTitle = document.title;
  var ATTRS = ['placeholder', 'aria-label', 'alt', 'title'];
  var miss = window.__bloomMiss = {};

  function load() {
    if (ES) return Promise.resolve(ES);
    if (loading) return loading;
    loading = new Promise(function (ok, no) {
      var s = document.createElement('script');
      s.src = ES_SRC; s.async = true;
      s.onload = function () { ES = window.BLOOM_ES; ES.re = (ES.r || []).map(function (p) { return [new RegExp(p[0]), p[1]]; }); ok(ES); };
      s.onerror = function () { loading = null; no(new Error('es.js failed')); };
      document.head.appendChild(s);
    });
    return loading;
  }

  function skip(el) { return !el || (el.closest && el.closest('.notrans,[translate="no"],script,style,noscript,textarea')); }
  // A text box's hint (placeholder) translates; what is typed in it never does.
  function skipAttr(el) { return !el || (el.closest && el.closest('.notrans,[translate="no"]')); }

  // Most specific first: this page inside this heading, this page, everywhere, then the patterns with a name in them.
  function look(k, el) {
    var h = el && el.closest ? el.closest('h1,h2,h3,h4') : null;
    if (h && ES.s[path + ' ' + h.tagName.toLowerCase() + '|' + k] != null) return ES.s[path + ' ' + h.tagName.toLowerCase() + '|' + k];
    if (ES.s[path + '|' + k] != null) return ES.s[path + '|' + k];
    if (ES.d[k] != null) return ES.d[k];
    for (var i = 0; i < ES.re.length; i++) if (ES.re[i][0].test(k)) return k.replace(ES.re[i][0], ES.re[i][1]);
    if (/[A-Za-z]/.test(k) && !ES.same[k]) miss[k] = (miss[k] || 0) + 1;
    return null;
  }

  function doText(n) {
    if (texts.has(n) || skip(n.parentElement)) return;
    var o = n.nodeValue; if (!o) return;
    var k = o.replace(/\s+/g, ' ').trim(); if (!k) return;
    var t = look(k, n.parentElement); if (t == null || t === k) return;
    texts.set(n, o);
    n.nodeValue = o.match(/^\s*/)[0] + t + o.match(/\s*$/)[0];
  }
  function doAttrs(el) {
    if (skipAttr(el)) return;
    ATTRS.forEach(function (a) {
      if (!el.hasAttribute(a)) return;
      var o = el.getAttribute(a), k = o.replace(/\s+/g, ' ').trim(); if (!k) return;
      for (var i = 0; i < attrs.length; i++) if (attrs[i][0] === el && attrs[i][1] === a) return;
      var t = look(k, el); if (t == null || t === k) return;
      attrs.push([el, a, o]); el.setAttribute(a, t);
    });
  }
  function walk(root) {
    if (root.nodeType === 3) { doText(root); return; }
    if (root.nodeType !== 1) return;
    doAttrs(root);
    if (skip(root)) return;
    var w = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT, { acceptNode: function (n) {
      if (n.nodeType === 1) return skip(n) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_SKIP;
      return NodeFilter.FILTER_ACCEPT;
    } });
    var list = [], c;
    while ((c = w.nextNode())) list.push(c);
    list.forEach(doText);
    root.querySelectorAll('[' + ATTRS.join('],[') + ']').forEach(doAttrs);
  }

  // Page scripts keep writing English after load (form messages, the sound button, the menu label, the chat): follow them.
  function watch() {
    if (mo) return;
    mo = new MutationObserver(function (recs) {
      recs.forEach(function (r) {
        if (r.type === 'childList') r.addedNodes.forEach(walk);
        else if (r.type === 'characterData') { texts.delete(r.target); doText(r.target); }
        else if (r.type === 'attributes') {
          attrs = attrs.filter(function (x) { return !(x[0] === r.target && x[1] === r.attributeName); });
          doAttrs(r.target);
        }
      });
      mo.takeRecords(); // our own writes, not theirs
    });
    mo.observe(document.body, { childList: true, subtree: true, characterData: true, attributes: true, attributeFilter: ATTRS });
  }
  function unwatch() { if (mo) { mo.disconnect(); mo = null; } }

  function toSpanish() {
    walk(document.body);
    var t = ES.d[enTitle]; if (t) document.title = t;
    if (mo) mo.takeRecords();
    watch();
  }
  function toEnglish() {
    unwatch();
    texts.forEach(function (o, n) { if (n.isConnected) n.nodeValue = o; });
    attrs.forEach(function (x) { if (x[0].isConnected) x[0].setAttribute(x[1], x[2]); });
    texts.clear(); attrs = [];
    document.title = enTitle;
  }

  function paintButtons() {
    document.querySelectorAll('[data-lang-toggle]').forEach(function (b) {
      var es = lang === 'es';
      b.textContent = es ? 'English' : 'Español';
      b.setAttribute('lang', es ? 'en' : 'es');
      b.setAttribute('aria-label', es ? 'View this page in English' : 'Ver esta página en español');
    });
  }
  function tellFrame() {
    var f = document.getElementById('bloom-inquiry');
    if (f && f.contentWindow) try { f.contentWindow.postMessage({ bloomLang: lang }, 'https://app.bloommentalhealthlv.com'); } catch (_) {}
  }
  function announce() {
    html.lang = lang;
    window.bloomLang = lang;
    paintButtons();
    tellFrame();
    try { document.dispatchEvent(new CustomEvent('bloomlang', { detail: lang })); } catch (_) {}
  }
  function reveal() { html.classList.remove('es-wait'); }

  function set(next) {
    if (next === lang || (next !== 'es' && next !== 'en')) return;
    lang = next;
    try { localStorage.setItem(KEY, lang); } catch (_) {}
    try { if (typeof gtag === 'function') gtag('event', 'language_switch', { language: lang }); } catch (_) {}
    if (lang === 'es') load().then(function () { if (lang === 'es') { toSpanish(); announce(); } }, function () { lang = 'en'; announce(); });
    else { toEnglish(); announce(); }
  }
  window.bloomSetLang = set;

  function start() {
    document.addEventListener('click', function (e) {
      var b = e.target.closest && e.target.closest('[data-lang-toggle]');
      if (b) { e.preventDefault(); set(lang === 'es' ? 'en' : 'es'); }
    });
    paintButtons();
    if (lang !== 'es') { reveal(); return; }
    load().then(function () { toSpanish(); announce(); reveal(); }, function () { lang = 'en'; announce(); reveal(); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();

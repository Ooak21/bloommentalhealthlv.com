/* Bloom Mental Health · "Still Water" behaviour by Isaac: the waterfall pour, the water surface, the fountain lens and the water sound.
   Multi-page version: every page is still a place on the water, and following a link glides you to it. */
/* ---------- hero video: pour in once, then loop; the flower is uncovered as the water falls ---------- */
(() => {
  if (!document.getElementById("falls")) return;
  const wrap = document.getElementById('falls');
  const intro = document.getElementById('intro');
  const loop = document.getElementById('loop');
  const mark = document.getElementById('mark');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let revealed = false;
  const setRv = v => mark.style.setProperty('--rv', v.toFixed(3));
  function uncover(){ revealed = true; setRv(1.3); mark.classList.add('shown'); }
  // where the front of the pouring water is, measured from the intro clip frame by frame (30 fps)
  const FRONT = [0.122, 0.133, 0.144, 0.144, 0.156, 0.172, 0.2, 0.211, 0.222, 0.222, 0.239, 0.256, 0.283, 0.3, 0.317, 0.317, 0.328, 0.35, 0.378, 0.4, 0.417, 0.417, 0.433, 0.45, 0.489, 0.506, 0.528, 0.528, 0.544, 0.567, 0.606, 0.628, 0.65, 0.65, 0.672, 0.689, 0.739, 0.756, 0.783, 0.783, 0.806, 0.828, 0.878, 0.906, 0.933, 0.933, 0.961, 0.978, 0.989, 0.994, 1.0, 1.0, 1.0, 1.0];
  function frontAt(t){
    const f = t * 30, i = Math.floor(f);
    if (i >= FRONT.length - 1) return 1;
    return FRONT[i] + (FRONT[i + 1] - FRONT[i]) * (f - i);
  }
  function follow(){
    if (revealed) return;
    const h = wrap.getBoundingClientRect(), m = mark.getBoundingClientRect();
    // the clip is cropped to cover the hero, so map its height onto the screen the same way
    const scale = Math.max(h.width / 1280, h.height / 720), shownH = 720 * scale, offY = (h.height - shownH) / 2;
    const frontY = h.top + offY + frontAt(intro.currentTime) * shownH;
    const rv = (frontY - m.top) / Math.max(1, m.height);   // the flower is uncovered only where the water has passed
    setRv(Math.max(0, rv));
    if (rv > 0.02) mark.classList.add('shown');
    if (intro.currentTime * 30 >= FRONT.length - 1 && rv >= 1){ uncover(); return; }
    requestAnimationFrame(follow);
  }
  // if the video can't play, pour the flower in on a timer instead
  function fallback(){
    if (revealed) return;
    const t0 = performance.now();
    mark.classList.add('shown');
    (function step(){
      const k = Math.min(1, (performance.now() - t0) / 1700);
      setRv(k * 1.3);
      if (k < 1) requestAnimationFrame(step); else uncover();
    })();
  }
  const toLoop = () => {
    if (wrap.classList.contains('looping')) return;
    loop.currentTime = 0;
    loop.play().catch(() => {});
    wrap.classList.add('looping');
    uncover();
  };
  if (reduce) uncover();
  intro.addEventListener('ended', toLoop);
  intro.addEventListener('error', () => { fallback(); toLoop(); });
  intro.play().then(() => { if (!revealed) requestAnimationFrame(follow); }).catch(() => { fallback(); toLoop(); });
})();
/* ---------- nav + reveals ---------- */
(() => {
  const nav = document.getElementById('nav');
  const onScroll = () => nav.classList.toggle('solid', window.scrollY > window.innerHeight * 0.6);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

})();

/* reveal: content drifts up into place as it enters (always readable at rest) */
function armReveals(root){
  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.remove('pre'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -8% 0px' });
  root.querySelectorAll('.rise').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.top > innerHeight) { el.classList.add('pre'); io.observe(el); }
  });
}
armReveals(document);
/* ---------- the water: black, crystal-clear surface; every page is a place on it ---------- */
const Water = (() => {
  const canvas = document.getElementById('water');
  const gl = canvas.getContext('webgl', { antialias: false, alpha: false, powerPreference: 'high-performance' });
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const hooks = [];
  if (!gl) return {
    ripple(){}, place(){}, onDrop(fn){ hooks.push(fn); }, speed: 0, busy: false,
    glide(to, ms, mid){ return new Promise(res => { setTimeout(() => { mid && mid(); }, ms * 0.45); setTimeout(res, ms); }); }
  };

  const MAX = 14;
  const CAM_Y = 1.25, TILT = 0.26, FOCAL = 1.45;

  const vs = `attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}`;
  const fs = `
  precision highp float;
  uniform vec2 uRes; uniform float uTime; uniform vec2 uCam; uniform float uCamY; uniform float uRoll;
  uniform vec2 uDir; uniform float uSwell; uniform float uWake;
  uniform vec4 uR[${MAX}];
  const float TILT=${TILT.toFixed(3)}; const float FOCAL=${FOCAL.toFixed(3)};

  float waves(vec2 p, float t, float fade){
    // while travelling, the surface stretches along the path and a swell rolls with you
    float along = dot(p, uDir);
    p += uDir * (along / (1.0 + uWake * 2.5) - along);
    float s = 1.0 + uSwell * 1.4;
    float h = 0.0;
    h += sin(dot(p, vec2(0.60, 0.80))*1.3 + t*0.55)*0.030 * s;
    h += sin(dot(p, vec2(-0.75,0.66))*1.9 + t*0.70)*0.020 * s;
    h += sin(dot(p, vec2(0.20,-0.98))*2.7 + t*0.95)*0.012 * s;
    h += (sin(dot(p, vec2(0.93,0.37))*6.1 + t*1.6)*0.0045
        + sin(dot(p, vec2(-0.41,0.91))*8.3 + t*2.1)*0.0030
        + sin(dot(p, vec2(0.70,-0.71))*11.7 + t*2.7)*0.0018) * fade * s;
    h += sin(along * 2.2 - t * 3.2) * 0.022 * uSwell;           // long rollers moving with you
    h += sin(along * 5.0 - t * 5.0 + p.x * 0.7) * 0.006 * uSwell * fade;
    for(int i=0;i<${MAX};i++){
      vec4 r = uR[i];
      float age = t - r.z;
      if(r.w <= 0.0 || age < 0.0 || age > 7.0) continue;
      float d = length(p - r.xy);
      float x = d - age*0.9;
      h += sin(x*16.0) * exp(-x*x*5.0) * exp(-age*0.75) * r.w * 0.035 / (1.0 + d*1.5);
    }
    return h;
  }

  vec3 sky(vec3 r){
    vec3 L = normalize(vec3(0.0, 0.11, 1.0));
    float s = max(dot(r, L), 0.0);
    vec3 c = vec3(0.0);
    c += vec3(1.0) * pow(s, 1400.0) * 1.4;
    c += vec3(0.85,0.92,0.95) * pow(s, 90.0) * 0.22;
    c += vec3(0.6,0.7,0.75) * pow(s, 8.0) * 0.05;
    c += vec3(0.7,0.78,0.82) * exp(-abs(r.y - 0.02) * 40.0) * 0.05;
    vec3 A = normalize(vec3(-0.8, 0.22, 0.6)), B = normalize(vec3(0.85, 0.3, 0.45));
    c += vec3(0.9) * pow(max(dot(r,A),0.0), 700.0) * 0.45;
    c += vec3(0.9) * pow(max(dot(r,B),0.0), 800.0) * 0.4;
    return c;
  }

  void main(){
    vec2 uv = (gl_FragCoord.xy - 0.5*uRes) / uRes.y;
    float cr = cos(uRoll), sr = sin(uRoll);
    uv = vec2(cr*uv.x - sr*uv.y, sr*uv.x + cr*uv.y);        // a gentle lean into the turn
    vec3 ro = vec3(uCam.x, uCamY, uCam.y);
    vec3 rd = normalize(vec3(uv.x, uv.y - TILT, FOCAL));
    vec3 col;
    if(rd.y > -0.0005){
      col = sky(rd) * 0.18;
    } else {
      float t = -uCamY / rd.y;
      vec3 p = ro + rd * t;
      float fade = exp(-t*0.09);
      float e = 0.012 + t*0.002;
      float hx = waves(p.xz + vec2(e,0.0), uTime, fade) - waves(p.xz - vec2(e,0.0), uTime, fade);
      float hz = waves(p.xz + vec2(0.0,e), uTime, fade) - waves(p.xz - vec2(0.0,e), uTime, fade);
      vec3 n = normalize(vec3(-hx/(2.0*e), 1.0, -hz/(2.0*e)));
      vec3 r = reflect(rd, n);
      float fres = 0.02 + 0.98 * pow(1.0 - max(dot(n, -rd), 0.0), 5.0);
      col = sky(r) * fres * 1.6;
      col += vec3(0.006,0.008,0.009) * fade;
      col *= exp(-t*0.03);
    }
    col *= 1.0 - 0.35*dot(uv*0.8, uv*0.8);
    col = pow(max(col, 0.0), vec3(0.92));
    gl_FragColor = vec4(col, 1.0);
  }`;

  const sh = (type, src) => { const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) console.error(gl.getShaderInfoLog(s)); return s; };
  const prog = gl.createProgram();
  gl.attachShader(prog, sh(gl.VERTEX_SHADER, vs));
  gl.attachShader(prog, sh(gl.FRAGMENT_SHADER, fs));
  gl.linkProgram(prog); gl.useProgram(prog);
  gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 3,-1, -1,3]), gl.STATIC_DRAW);
  const loc = gl.getAttribLocation(prog, 'p'); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
  const U = n => gl.getUniformLocation(prog, n);
  const uRes = U('uRes'), uTime = U('uTime'), uCam = U('uCam'), uCamY = U('uCamY'), uRoll = U('uRoll');
  const uDir = U('uDir'), uSwell = U('uSwell'), uWake = U('uWake'), uR = U('uR');

  const ripples = new Float32Array(MAX * 4); let slot = 0;
  let W = 0, H = 0;
  function resize(){
    const scale = Math.min(devicePixelRatio || 1, 1.5) * (innerWidth < 760 ? 0.85 : 1);
    W = canvas.clientWidth; H = canvas.clientHeight;
    canvas.width = Math.round(W * scale); canvas.height = Math.round(H * scale);
    gl.viewport(0, 0, canvas.width, canvas.height);
  }
  resize(); addEventListener('resize', resize);

  const t0 = performance.now();
  const now = () => (performance.now() - t0) / 1000;
  const SCROLL = 0.0055;                       // how far a page's scroll carries you forward
  let anchor = [0, 0];                         // where the current page sits on the water
  let cam = [0, 0], camY = CAM_Y, roll = 0, lastCam = [0, 0], speed = 0;
  let dir = [0, 1], swell = 0, wake = 0;
  let trip = null;

  function toWater(px, py){
    const uvx0 = (px - W/2) / H, uvy0 = (H/2 - py) / H;
    const c = Math.cos(roll), s = Math.sin(roll);
    const uvx = c*uvx0 - s*uvy0, uvy = s*uvx0 + c*uvy0;
    let dx = uvx, dy = uvy - TILT, dz = FOCAL;
    const len = Math.hypot(dx, dy, dz); dx/=len; dy/=len; dz/=len;
    if (dy >= -0.01) return null;
    const t = -camY / dy;
    return [cam[0] + dx*t, cam[1] + dz*t];
  }
  function ripple(px, py, strength, kind){
    const p = toWater(px, py); if (!p) return;
    hooks.forEach(fn => fn(kind || 'drop', strength, px / W));
    ripples.set([p[0], p[1], now(), strength], slot * 4);
    slot = (slot + 1) % MAX;
  }
  function rippleAt(x, z, strength){
    ripples.set([x, z, now(), strength], slot * 4);
    slot = (slot + 1) % MAX;
  }

  let lastMove = 0, lx = 0, ly = 0;
  addEventListener('pointermove', e => {
    const t = performance.now();
    if (trip || t - lastMove < 110 || Math.hypot(e.clientX - lx, e.clientY - ly) < 24) return;
    lastMove = t; lx = e.clientX; ly = e.clientY;
    ripple(e.clientX, e.clientY, 0.55, 'hover');
  }, { passive: true });
  addEventListener('pointerdown', e => { if (!trip) ripple(e.clientX, e.clientY, 1.4, 'tap'); }, { passive: true });

  const ease = x => x < 0.5 ? 4*x*x*x : 1 - Math.pow(-2*x + 2, 3) / 2;

  // glide across the surface to another place on the water
  function glide(to, ms, onMid){
    return new Promise(resolve => {
      const from = [cam[0], cam[1]];
      const vx = to[0] - from[0], vz = to[1] - from[1], L = Math.hypot(vx, vz) || 1;
      dir = [vx / L, vz / L];
      trip = { start: performance.now(), ms, from, to, onMid, midDone: false, resolve, nextWake: 0 };
      hooks.forEach(fn => fn('depart', 1, 0.5 + dir[0] * 0.4));
      if (reduce) requestAnimationFrame(frame);
    });
  }

  let nextDrop = 1.2;
  function frame(){
    const t = now();
    if (trip){
      const x = Math.min(1, (performance.now() - trip.start) / trip.ms);
      const k = ease(x), bump = Math.sin(Math.PI * x);
      cam = [trip.from[0] + (trip.to[0] - trip.from[0]) * k, trip.from[1] + (trip.to[1] - trip.from[1]) * k];
      camY = CAM_Y + bump * 0.18 + Math.sin(x * Math.PI * 3) * 0.03 * bump;   // rise and bob over the swell
      roll = -dir[0] * bump * 0.035;                                         // lean the way you're heading
      swell = bump; wake = bump;
      if (!reduce && x > trip.nextWake && x < 0.85){                         // the water parts around you
        trip.nextWake = x + 0.07;
        const side = (Math.random() < 0.5 ? -1 : 1) * (1.2 + Math.random() * 1.6);
        const ahead = 3 + Math.random() * 5;
        rippleAt(cam[0] + dir[0] * ahead - dir[1] * side, cam[1] + dir[1] * ahead + dir[0] * side, 0.9);
      }
      if (!trip.midDone && x >= 0.45){ trip.midDone = true; trip.onMid && trip.onMid(); }
      if (x >= 1){
        anchor = [trip.to[0], trip.to[1]];
        const r = trip.resolve; trip = null; camY = CAM_Y; roll = 0; swell = 0; wake = 0;
        hooks.forEach(fn => fn('arrive', 1, 0.5));
        r();
      }
    } else {
      const target = [anchor[0], anchor[1] + scrollY * SCROLL];
      cam = [cam[0] + (target[0] - cam[0]) * 0.06, cam[1] + (target[1] - cam[1]) * 0.06];
    }
    speed = speed * 0.9 + Math.hypot(cam[0] - lastCam[0], cam[1] - lastCam[1]) * 10; lastCam = cam.slice();
    const drift = Math.sin(t * 0.07) * 0.35;
    if (!reduce && !trip && t > nextDrop){
      nextDrop = t + 1.4 + Math.random() * 2.2;
      ripple(W * (0.15 + Math.random() * 0.7), H * (0.62 + Math.random() * 0.33), 0.7 + Math.random() * 0.5);
    }
    gl.uniform2f(uRes, canvas.width, canvas.height);
    gl.uniform1f(uTime, t);
    gl.uniform2f(uCam, cam[0] + drift, cam[1]);
    gl.uniform1f(uCamY, camY);
    gl.uniform1f(uRoll, roll);
    gl.uniform2f(uDir, dir[0], dir[1]);
    gl.uniform1f(uSwell, swell);
    gl.uniform1f(uWake, wake);
    gl.uniform4fv(uR, ripples);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    if (!reduce || trip) requestAnimationFrame(frame);
  }
  if (reduce){ addEventListener('scroll', () => requestAnimationFrame(frame), { passive:true }); }
  frame();

  return {
    ripple, glide,
    place(to){ anchor = [to[0], to[1]]; cam = [to[0], to[1]]; },
    onDrop(fn){ hooks.push(fn); },
    get speed(){ return trip ? 0.6 : speed; },
    get busy(){ return !!trip; }
  };
})();

/* ---------- moving between pages: glide across the water, then arrive on the next page ---------- */
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const main = document.querySelector('main.page');
  const D = 40;
  // every section of the site is a place on the water: ahead, right, behind, left; the request lies furthest ahead, toward the light
  const PLACE = { '': [0, 0], 'about-us': [0, D], 'providers': [D * 0.7, D * 0.7], 'services': [D, 0], 'insurance': [D * 0.7, -D * 0.7],
    'faq': [0, -D], 'contact': [-D, 0], 'for-providers': [-D * 0.7, D * 0.7], 'request-appointment': [0, D * 2] };
  const placeOf = path => { const k = path.replace(/^\/+/, '').split('/')[0]; return PLACE[k] || [0, 0]; };
  function setDrift(dir){
    main.style.setProperty('--dx', (dir[0] * 32) + 'vw');
    main.style.setProperty('--dy', (-dir[1] * 12) + 'vh');
    main.style.setProperty('--s-in', String(1 - dir[1] * 0.07));
    main.style.setProperty('--s-out', String(1 + dir[1] * 0.07));
  }
  const here = placeOf(location.pathname);
  Water.place(here);

  // arriving: the page floats in from the direction you travelled
  let arrived = null;
  try { arrived = JSON.parse(sessionStorage.getItem('bloom-glide') || 'null'); sessionStorage.removeItem('bloom-glide'); } catch (e) {}
  if (arrived && !reduce && main && Date.now() - arrived.t < 8000){
    const dir = arrived.dir;
    setDrift(dir);
    main.classList.add('enter');
    Water.place([here[0] - dir[0] * 10, here[1] - dir[1] * 10]);
    requestAnimationFrame(() => requestAnimationFrame(() => { main.classList.remove('enter'); main.classList.add('arrive'); Water.glide(here, 1300); }));
    setTimeout(() => main.classList.remove('arrive'), 1500);
  }

  document.addEventListener('click', e => {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    const a = e.target.closest('a[href]'); if (!a || a.target === '_blank' || a.hasAttribute('download')) return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin) return;
    if (url.pathname === location.pathname){ if (!url.hash){ e.preventDefault(); scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); } return; }
    if (reduce || !main || Water.busy) return;
    e.preventDefault();
    const a0 = here, b = placeOf(url.pathname);
    const L = Math.hypot(b[0] - a0[0], b[1] - a0[1]) || 1;
    const dir = [(b[0] - a0[0]) / L || 0, (b[1] - a0[1]) / L || 1];
    setDrift(dir);
    document.body.classList.add('traveling');
    main.classList.add('leave');
    try { sessionStorage.setItem('bloom-glide', JSON.stringify({ dir, t: Date.now() })); } catch (err) {}
    let gone = false; const leave = () => { if (!gone){ gone = true; location.href = url.href; } };
    Water.glide([a0[0] + dir[0] * 10, a0[1] + dir[1] * 10], 1100, leave);
    setTimeout(leave, 1300);
  });
  // coming back with the browser buttons should never leave a faded page behind
  addEventListener('pageshow', ev => { if (ev.persisted && main){ main.classList.remove('leave', 'enter'); document.body.classList.remove('traveling'); } });
})();

/* ---------- nature scenes: the films play only while you can see them, and drift as you scroll ---------- */
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const scenes = [...document.querySelectorAll('.scene')];
  if (!scenes.length) return;
  const io = new IntersectionObserver(es => es.forEach(e => {
    const v = e.target.querySelector('video'); e.target.classList.toggle('lit', e.isIntersecting);
    if (!v || reduce) return;
    if (e.isIntersecting) v.play().catch(() => {}); else v.pause();
  }), { rootMargin: '10% 0px' });
  scenes.forEach(s => io.observe(s));
  if (reduce) return;
  let ticking = false;
  function paint(){
    ticking = false;
    scenes.forEach(s => {
      const r = s.getBoundingClientRect(); if (r.bottom < 0 || r.top > innerHeight) return;
      const k = (r.top + r.height / 2 - innerHeight / 2) / innerHeight;       // -1 .. 1 as it passes
      const m = s.querySelector('.scene-media > *'); if (!m) return;
      m.style.setProperty('--py', (k * -60).toFixed(1) + 'px');
      m.style.setProperty('--sz', (1.06 + Math.abs(k) * 0.04).toFixed(3));
    });
  }
  addEventListener('scroll', () => { if (!ticking){ ticking = true; requestAnimationFrame(paint); } }, { passive: true });
  paint();
})();

/* ---------- calls and emails count as contact in GA (no personal details sent) ---------- */
(() => {
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href^="tel:"],a[href^="mailto:"]'); if (!a) return;
    try { if (typeof gtag === 'function') gtag('event', a.href.startsWith('tel:') ? 'call_click' : 'email_click', { link_location: a.closest('header,footer,main') ? a.closest('header,footer,main').tagName.toLowerCase() : 'page' }); } catch (err) {}
  });
})();
/* ---------- the office fountain in the arch ripples like it sits under the water ---------- */
(() => {
  const fig = document.getElementById("lens"); if (!fig) return;
  const vid = document.getElementById('lensVid');
  const cv = document.getElementById('lensGl');
  // No-WebGL path: CSS :hover brings the color back for a mouse; a tap toggles it on touch.
  fig.addEventListener('pointerdown', e => { if (e.pointerType === 'touch' && !fig.classList.contains('gl')) fig.classList.toggle('color'); });
  const gl = cv.getContext('webgl', { premultipliedAlpha: false });
  if (!gl) return;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const N = 10;
  const fs = `precision highp float;
  varying vec2 v; uniform sampler2D T; uniform float uT; uniform float uA; uniform float uS; uniform vec4 uR[${N}];
  void main(){
    vec2 uv = v, off = vec2(0.0);
    for(int i=0;i<${N};i++){
      vec4 r = uR[i]; float age = uT - r.z;
      if(r.w <= 0.0 || age < 0.0 || age > 3.5) continue;
      vec2 d = (uv - r.xy) * vec2(uA, 1.0); float dist = length(d);
      float x = dist - age * 0.32;
      float w = sin(x * 70.0) * exp(-x * x * 500.0) * exp(-age * 1.4) * r.w;
      off += normalize(d + 1e-5) * w * 0.012;
    }
    off += vec2(sin(uv.y * 22.0 + uT * 0.8), cos(uv.x * 18.0 + uT * 0.6)) * 0.0012;
    vec3 c = texture2D(T, uv + off).rgb;
    // Black and white at rest (Isaac's look: desaturated, a little more contrast, a little darker); uS eases to full color on hover.
    float g = dot(c, vec3(0.299, 0.587, 0.114));
    vec3 bw = vec3(clamp((g - 0.5) * 1.25 + 0.42, 0.0, 1.0));
    c = mix(bw, c, smoothstep(0.0, 1.0, uS));
    c += length(off) * 6.0;
    gl_FragColor = vec4(c, 1.0);
  }`;
  const vs = `attribute vec2 p; varying vec2 v; void main(){ v = vec2(p.x*0.5+0.5, 0.5-p.y*0.5); gl_Position = vec4(p,0.,1.); }`;
  const mk = (t, src) => { const s = gl.createShader(t); gl.shaderSource(s, src); gl.compileShader(s); return s; };
  const pr = gl.createProgram(); gl.attachShader(pr, mk(gl.VERTEX_SHADER, vs)); gl.attachShader(pr, mk(gl.FRAGMENT_SHADER, fs));
  gl.linkProgram(pr); if (!gl.getProgramParameter(pr, gl.LINK_STATUS)) return; gl.useProgram(pr);
  gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 3,-1, -1,3]), gl.STATIC_DRAW);
  const pl = gl.getAttribLocation(pr, 'p'); gl.enableVertexAttribArray(pl); gl.vertexAttribPointer(pl, 2, gl.FLOAT, false, 0, 0);
  const uT = gl.getUniformLocation(pr, 'uT'), uA = gl.getUniformLocation(pr, 'uA'), uR = gl.getUniformLocation(pr, 'uR'), uS = gl.getUniformLocation(pr, 'uS');
  // Color on hover (Luis 9/27): sat eases toward its target every frame, ~1s either way. Touch has no hover, so a tap toggles it.
  let sat = 0, satTo = 0, lastF = performance.now();
  const rip = new Float32Array(N * 4); let slot = 0;
  const t0 = performance.now(); const now = () => (performance.now() - t0) / 1000;
  let visible = false, ready = false, running = false;

  let tex = null;
  function upload(){
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, gl.RGB, gl.UNSIGNED_BYTE, vid);
  }
  function load(){
    try {
      tex = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, tex);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      upload();
      ready = true; size(); draw(); fig.classList.add('gl'); kick();
    } catch (e) { ready = false; fig.classList.remove('gl'); /* the plain video stays */ }
  }
  function size(){
    const r = cv.getBoundingClientRect(), d = Math.min(devicePixelRatio || 1, 2);
    cv.width = Math.max(1, Math.round(r.width * d)); cv.height = Math.max(1, Math.round(r.height * d));
    gl.viewport(0, 0, cv.width, cv.height);
  }
  function draw(){
    if (vid.readyState >= 2){ try { upload(); } catch (e) { ready = false; fig.classList.remove('gl'); return; } }
    const tf = performance.now(), dt = Math.min(0.5, (tf - lastF) / 1000); lastF = tf;
    sat = reduce ? satTo : sat + (satTo - sat) * (1 - Math.exp(-dt * 3.2));
    gl.uniform1f(uT, now()); gl.uniform1f(uA, cv.width / cv.height); gl.uniform1f(uS, sat); gl.uniform4fv(uR, rip);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
  }
  function loop(){ if (!visible || reduce || !ready){ running = false; return; } draw(); requestAnimationFrame(loop); }
  function kick(){ if (ready && visible && !running && !reduce){ running = true; requestAnimationFrame(loop); } }

  function add(e, s){
    const r = cv.getBoundingClientRect();
    rip.set([(e.clientX - r.left) / r.width, (e.clientY - r.top) / r.height, now(), s], slot * 4);
    slot = (slot + 1) % N;
    if (reduce && ready) draw();
  }
  let last = 0, lx = 0, ly = 0;
  fig.addEventListener('pointermove', e => {
    const t = performance.now();
    if (t - last < 90 || Math.hypot(e.clientX - lx, e.clientY - ly) < 14) return;
    last = t; lx = e.clientX; ly = e.clientY; add(e, 0.8);
  });
  const setSat = (on) => { satTo = on ? 1 : 0; fig.classList.toggle('color', on); if (reduce && ready) draw(); };
  fig.addEventListener('pointerenter', e => { add(e, 1.2); if (e.pointerType !== 'touch') setSat(true); });
  fig.addEventListener('pointerleave', e => { if (e.pointerType !== 'touch') setSat(false); });
  fig.addEventListener('pointerdown', e => { add(e, 1.8); if (e.pointerType === 'touch') setSat(!satTo); });
  new IntersectionObserver(es => {
    visible = es[0].isIntersecting;
    if (visible) vid.play().catch(() => {}); else vid.pause();
    kick();
  }).observe(fig);
  addEventListener('resize', () => { if (ready){ size(); draw(); } });
  if (vid.readyState >= 2) load(); else vid.addEventListener('loadeddata', load, { once: true });
})();

/* ---------- soundtrack: moving water, built from bubbles and spray ---------- */
(() => {
  const btn = document.getElementById('sound');
  const txt = document.getElementById('soundTxt');
  const LEVEL = 0.5;
  let wanted = true;
  try { if (localStorage.getItem('bloom-sound') === 'off') wanted = false; } catch (e) {}
  let ctx = null, master = null, muffle = null, bubBus = null, timer = null, nextT = 0, whiteBuf = null;
  const rnd = Math.random;

  function noise(kind, secs){
    const len = Math.floor(ctx.sampleRate * secs), fade = 4000;
    const buf = ctx.createBuffer(2, len, ctx.sampleRate);
    for (let ch = 0; ch < 2; ch++){
      const d = buf.getChannelData(ch); let last = 0;
      for (let i = 0; i < len; i++){
        const w = rnd() * 2 - 1;
        if (kind === 'white') d[i] = w * 0.5; else { last = (last + 0.02 * w) / 1.02; d[i] = last * 3.2; }
      }
      for (let i = 0; i < fade; i++){ const k = i / fade; d[len - fade + i] = d[len - fade + i] * (1 - k) + d[i] * k; }
    }
    const s = ctx.createBufferSource(); s.buffer = buf; s.loop = true; s.loopStart = fade / ctx.sampleRate;
    s.start(0, rnd() * secs * 0.8); return s;
  }
  const filter = (type, f, q) => { const b = ctx.createBiquadFilter(); b.type = type; b.frequency.value = f; b.Q.value = q; return b; };

  // one bubble: a short tone whose pitch rises as it pops, the sound running water is made of
  function bubble(t, f, dur, g, pan){
    const o = ctx.createOscillator(); o.type = 'sine';
    o.frequency.setValueAtTime(f, t);
    o.frequency.exponentialRampToValueAtTime(f * (1.5 + rnd() * 0.9), t + dur);
    const e = ctx.createGain();
    e.gain.setValueAtTime(0.0001, t);
    e.gain.linearRampToValueAtTime(g, t + 0.004);
    e.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    const p = ctx.createStereoPanner ? ctx.createStereoPanner() : null;
    if (p){ p.pan.value = pan; o.connect(e).connect(p).connect(bubBus); } else o.connect(e).connect(bubBus);
    o.start(t); o.stop(t + dur + 0.03);
  }

  // a rush of filtered noise that sweeps from one pitch to another: the whoosh of travel, the splash of a dive
  function burst(t, dur, f0, f1, g, attack){
    if (!whiteBuf){
      whiteBuf = ctx.createBuffer(1, ctx.sampleRate * 3, ctx.sampleRate);
      const d = whiteBuf.getChannelData(0); for (let i = 0; i < d.length; i++) d[i] = rnd() * 2 - 1;
    }
    const s = ctx.createBufferSource(); s.buffer = whiteBuf;
    const f = ctx.createBiquadFilter(); f.type = 'bandpass'; f.Q.value = 0.8;
    f.frequency.setValueAtTime(f0, t); f.frequency.exponentialRampToValueAtTime(f1, t + dur);
    const e = ctx.createGain();
    e.gain.setValueAtTime(0.0001, t);
    e.gain.linearRampToValueAtTime(g, t + dur * attack);
    e.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    s.connect(f).connect(e).connect(master); s.start(t, rnd()); s.stop(t + dur + 0.05);
  }

  function build(){
    const AC = window.AudioContext || window.webkitAudioContext; if (!AC) return false;
    ctx = new AC();
    master = ctx.createGain(); master.gain.value = 0;
    const tame = ctx.createDynamicsCompressor(); tame.threshold.value = -18; tame.ratio.value = 4;
    muffle = ctx.createBiquadFilter(); muffle.type = 'lowpass'; muffle.frequency.value = 18000; muffle.Q.value = 0.5;
    master.connect(muffle).connect(tame).connect(ctx.destination);

    // spray: the bright hiss of water falling onto water
    const spray = ctx.createGain(); spray.gain.value = 0.07;
    noise('white', 5).connect(filter('highpass', 1800, 0.5)).connect(filter('lowpass', 7000, 0.5)).connect(spray).connect(master);
    // body: the fuller splash underneath, kept soft so it never turns into wind
    const body = ctx.createGain(); body.gain.value = 0.12;
    noise('brown', 7).connect(filter('bandpass', 900, 0.6)).connect(body).connect(master);
    // both breathe with the same slow 9-second swell as the waves
    const swell = ctx.createOscillator(); swell.frequency.value = 1 / 9;
    const sw1 = ctx.createGain(); sw1.gain.value = 0.025; swell.connect(sw1).connect(spray.gain);
    const sw2 = ctx.createGain(); sw2.gain.value = 0.04;  swell.connect(sw2).connect(body.gain);
    swell.start();

    // bubbles: the trickle and babble
    bubBus = ctx.createGain(); bubBus.gain.value = 0.9;
    bubBus.connect(filter('lowpass', 5000, 0.4)).connect(master);
    nextT = ctx.currentTime + 0.05;
    timer = setInterval(() => {
      const ahead = ctx.currentTime + 0.2;
      while (nextT < ahead){
        const wave = 0.75 + 0.35 * Math.sin(2 * Math.PI * nextT / 9);
        const rate = 34 * wave + Math.min(Water.speed, 1) * 30;
        const f = 380 + Math.pow(rnd(), 2) * 1900;
        const dur = 0.018 + rnd() * 0.05 * (900 / f);
        bubble(nextT, f, dur, 0.012 + rnd() * 0.035, rnd() * 1.6 - 0.8);
        nextT += -Math.log(1 - rnd()) / rate;
      }
    }, 50);

    // the droplets you see land on the water make a sound too
    Water.onDrop((kind, strength, x) => {
      if (!ctx || !wanted || ctx.state !== 'running') return;
      const t = ctx.currentTime + 0.01, pan = x * 1.6 - 0.8;
      if (kind === 'depart'){ burst(t, 2.3, 260, 1300, 0.1, 0.45); burst(t + 0.3, 1.8, 1800, 700, 0.04, 0.5); return; }
      if (kind === 'arrive'){ burst(t, 1.4, 900, 280, 0.06, 0.15); for (let i = 0; i < 10; i++) bubble(t + rnd() * 0.6, 400 + rnd() * 900, 0.04 + rnd() * 0.05, 0.02 + rnd() * 0.03, rnd() * 1.2 - 0.6); return; }
      if (kind === 'plunge' || kind === 'surface'){
        burst(t, 0.7, kind === 'plunge' ? 1400 : 2200, kind === 'plunge' ? 500 : 3500, 0.35, 0.05);
        for (let i = 0; i < 26; i++) bubble(t + rnd() * 0.9, 300 + rnd() * 1300, 0.03 + rnd() * 0.07, 0.03 + rnd() * 0.05, rnd() * 1.6 - 0.8);
        muffle.frequency.cancelScheduledValues(t);
        muffle.frequency.setTargetAtTime(kind === 'plunge' ? 420 : 18000, t, kind === 'plunge' ? 0.08 : 0.35);
        return;
      }
      if (kind === 'hover'){ if (rnd() < 0.35) bubble(t, 900 + rnd() * 900, 0.04, 0.02, pan); return; }
      const f = 650 + rnd() * 650;
      bubble(t, f, 0.11 + rnd() * 0.05, kind === 'tap' ? 0.1 : 0.06, pan);
      bubble(t + 0.03 + rnd() * 0.03, f * 1.8, 0.05, 0.025, pan);
    });
    return true;
  }

  function fadeTo(v, secs){
    if (!ctx) return;
    const t = ctx.currentTime;
    master.gain.cancelScheduledValues(t);
    master.gain.setValueAtTime(master.gain.value, t);
    master.gain.linearRampToValueAtTime(v, t + secs);
  }
  function start(){
    if (!ctx && !build()) return;
    ctx.resume().then(() => fadeTo(LEVEL, 5)).catch(() => {});
  }
  function paint(){
    btn.classList.toggle('on', wanted);
    btn.setAttribute('aria-pressed', String(wanted));
    txt.textContent = wanted ? 'Sound on' : 'Sound off';
  }
  paint();

  // browsers only allow sound after the first tap, click or key press, so it begins then
  const first = e => {
    if (e.target.closest && e.target.closest('#sound')) return;
    ['pointerdown','keydown','touchend'].forEach(ev => removeEventListener(ev, first, true));
    if (wanted) start();
  };
  ['pointerdown','keydown','touchend'].forEach(ev => addEventListener(ev, first, true));
  if (wanted) { try { start(); } catch (e) {} }

  btn.addEventListener('click', () => {
    wanted = !wanted; paint();
    try { localStorage.setItem('bloom-sound', wanted ? 'on' : 'off'); } catch (e) {}
    if (wanted) start(); else fadeTo(0, 1.2);
  });
})();

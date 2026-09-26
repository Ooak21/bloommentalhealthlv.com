#!/usr/bin/env python3
"""Build bloommentalhealthlv.com from tools/content.py.

    python3 tools/build.py            # writes every page + sitemap, robots, llms.txt, llms-full.txt, AGENTS.md, services.json
    python3 tools/build.py --submit   # the same, then pings IndexNow (only after the push is live)

Pages are committed output; GitHub Pages serves them as-is. Edit content.py, never the generated HTML.
"""
import datetime, html, json, os, re, sys, urllib.request

sys.path.insert(0, os.path.dirname(__file__))
from content import *  # noqa

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()
P = PRACTICE
E = html.escape
ORG_ID = SITE + "/#organization"
PAGES = []  # (path, title, text-for-llms-full)

ICONS = {
    "drop": '<path d="M17 3C17 3 7 15 7 21a10 10 0 0 0 20 0C27 15 17 3 17 3Z"/><path d="M12 22a5 5 0 0 0 5 5"/>',
    "rings": '<circle cx="17" cy="17" r="3"/><circle cx="17" cy="17" r="8"/><circle cx="17" cy="17" r="14"/>',
    "waves": '<path d="M3 13c3.5-3 7-3 10.5 0s7 3 10.5 0 7-3 7-3"/><path d="M3 20c3.5-3 7-3 10.5 0s7 3 10.5 0 7-3 7-3"/><path d="M3 27c3.5-3 7-3 10.5 0s7 3 10.5 0 7-3 7-3"/>',
    "shield": '<path d="M17 3 5 8v8c0 7.5 5.1 13 12 15 6.9-2 12-7.5 12-15V8L17 3Z"/><path d="M12 17l3.5 3.5L22 14"/>',
}
ARROW = '<span class="arrow" aria-hidden="true"><svg viewBox="0 0 18 18"><path d="M2 9h13M10 4l5 5-5 5"/></svg></span>'
def icon(k): return f'<svg viewBox="0 0 34 34" aria-hidden="true">{ICONS[k]}</svg>'
PROV = {p["slug"]: p for p in PROVIDERS}
SVC = {s["slug"]: s for s in SERVICES}
ADDR_ONE = f'{P["street"]}, {P["city"]}, {P["region"]} {P["zip"]}'

# ------------------------------------------------------------------ schema
def org():
    return {
        "@context": "https://schema.org", "@type": ["MedicalClinic", "MedicalBusiness"], "@id": ORG_ID,
        "name": P["name"], "url": SITE + "/", "logo": SITE + "/assets/logo.png", "image": SITE + "/assets/share.jpg",
        "description": "Outpatient psychiatric care in Las Vegas, Nevada for children, adolescents, adults and older adults: psychiatric evaluations, medication management, therapy, substance use care and telehealth.",
        "telephone": P["phone_e164"], "faxNumber": P["fax_e164"], "email": P["email"],
        "address": {"@type": "PostalAddress", "streetAddress": P["street"], "addressLocality": P["city"], "addressRegion": P["region"], "postalCode": P["zip"], "addressCountry": P["country"]},
        "areaServed": [{"@type": "City", "name": "Las Vegas"}, {"@type": "State", "name": "Nevada"}],
        "medicalSpecialty": "Psychiatric", "isAcceptingNewPatients": True,
        "availableLanguage": P["languages"], "knowsLanguage": P["languages"],
        "healthPlanNetworkId": None,
        "employee": [{"@id": f'{SITE}/providers/{p["slug"]}/#person'} for p in PROVIDERS],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@id": f'{SITE}/services/{s["slug"]}/#service'}} for s in SERVICES]},
        "potentialAction": {"@type": "ReserveAction", "target": SITE + "/request-appointment/", "name": "Request an appointment"},
    }
def clean(o):
    if isinstance(o, dict): return {k: clean(v) for k, v in o.items() if v is not None}
    if isinstance(o, list): return [clean(v) for v in o]
    return o
def website():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": P["name"], "inLanguage": "en-US", "publisher": {"@id": ORG_ID}}
def webpage(kind, path, title, desc):
    return {"@context": "https://schema.org", "@type": kind, "@id": SITE + path + "#webpage", "url": SITE + path, "name": title, "description": desc,
            "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": ORG_ID}, "inLanguage": "en-US", "dateModified": TODAY}
def crumbs_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(trail)]}
def person_ld(p):
    return {
        "@context": "https://schema.org", "@type": "Person", "@id": f'{SITE}/providers/{p["slug"]}/#person',
        "name": p["name"], "honorificSuffix": p["creds"], "jobTitle": "Psychiatric Mental Health Nurse Practitioner",
        "url": f'{SITE}/providers/{p["slug"]}/', "worksFor": {"@id": ORG_ID}, "knowsLanguage": p["languages"], "knowsAbout": p["focus"],
        "identifier": {"@type": "PropertyValue", "propertyID": "NPI", "value": p["npi"]},
        "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "Board certification", "name": "PMHNP-BC, Psychiatric-Mental Health Nurse Practitioner (Board Certified)"},
        "alumniOf": {"@type": "CollegeOrUniversity", "name": p["alumni"]} if p.get("alumni") else None,
        "description": p["short"],
    }
def service_ld(s):
    return {"@context": "https://schema.org", "@type": "Service", "@id": f'{SITE}/services/{s["slug"]}/#service', "name": s["name"],
            "serviceType": s["name"], "description": s["short"], "url": f'{SITE}/services/{s["slug"]}/', "provider": {"@id": ORG_ID},
            "areaServed": {"@type": "City", "name": "Las Vegas"}, "availableLanguage": P["languages"]}
def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

# ------------------------------------------------------------------ shell
NAV = [("/", "Home"), ("/about-us/", "About"), ("/providers/", "Providers"), ("/services/", "Services"), ("/insurance/", "Insurance"), ("/contact/", "Contact")]

def page(path, title, desc, body, ld, og_image="/assets/share.jpg", noindex=False):
    here = "/" + path.strip("/").split("/")[0] + "/" if path != "/" else "/"
    links = "\n".join(f'    <li><a href="{u}"{" aria-current=\"page\"" if u == here else ""}>{n}</a></li>' for u, n in NAV)
    lds = "\n".join(f'<script type="application/ld+json">{json.dumps(clean(x), ensure_ascii=False, separators=(",", ":"))}</script>' for x in ld)
    robots = '<meta name="robots" content="noindex, nofollow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
{robots}
<link rel="canonical" href="{SITE}{path}">
<link rel="icon" href="/assets/favicon.png" type="image/png">
<meta name="theme-color" content="#000000">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{P["name"]}">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:alt" content="Bloom Mental Health, psychiatric care in Las Vegas">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(title)}">
<meta name="twitter:description" content="{E(desc)}">
<meta name="twitter:image" content="{SITE}{og_image}">
<meta name="geo.region" content="US-NV">
<meta name="geo.placename" content="Las Vegas">
<link rel="alternate" type="text/plain" title="LLM brief (llms.txt)" href="/llms.txt">
<link rel="alternate" type="text/plain" title="Full site text (llms-full.txt)" href="/llms-full.txt">
<link rel="alternate" type="text/markdown" title="For AI agents (AGENTS.md)" href="/AGENTS.md">
<link rel="alternate" type="application/json" title="Services (services.json)" href="/services.json">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Manrope:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/sw.css">
{lds}
<!-- Google tag (gtag.js) · GA4 {GA4} -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA4}');</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<canvas id="water" aria-hidden="true"></canvas>

<header class="nav" id="nav">
  <a class="brand" href="/"><img src="/assets/water/bloom-logo-light.webp" alt="Bloom Mental Health" width="644" height="254"></a>
  <ul class="links">
{links}
  </ul>
  <div class="nav-end">
    <a class="pill pill-line" href="tel:{P["phone"].replace("-", "")}">{P["phone"]}</a>
    <button class="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
  </div>
</header>

<main class="page" id="main">
{body}
</main>

<footer>
  <div class="foot-grid">
    <div>
      <a class="foot-logo" href="/"><img src="/assets/water/bloom-logo-light.webp" alt="Bloom Mental Health" width="644" height="254" loading="lazy"></a>
      <p class="body">Our goal is to create a safe and welcoming space where individuals feel heard, understood, and empowered throughout their journey to better mental health.</p>
      <p class="crisis" style="margin-top:22px">In crisis? Call or text <strong>988</strong> (Suicide and Crisis Lifeline) or call <strong>911</strong>. Bloom is an outpatient practice, not an emergency service.</p>
    </div>
    <div>
      <h4>Visit &amp; Contact</h4>
      <address>
        {P["street"]}<br>
        {P["city"]}, {P["region"]} {P["zip"]}<br>
        Phone: <a href="tel:{P["phone"].replace("-", "")}">{P["phone"]}</a><br>
        Fax: {P["fax"]}<br>
        <a href="mailto:{P["email"]}">{P["email"]}</a>
      </address>
      <p class="body" style="margin-top:16px;font-size:14px">{P["times"]}.</p>
    </div>
    <div>
      <h4>Explore</h4>
      <ul>
        <li><a href="/about-us/">About Us</a></li>
        <li><a href="/providers/">Our Providers</a></li>
        <li><a href="/services/">Services</a></li>
        <li><a href="/insurance/">Insurance &amp; Pricing</a></li>
        <li><a href="/faq/">FAQ</a></li>
        <li><a href="/for-providers/">For Referring Providers</a></li>
        <li><a href="/request-appointment/">Request an Appointment</a></li>
      </ul>
    </div>
  </div>
  <div class="legal">
    <span>Copyright &copy; 2026 Bloom Mental Health. All Rights Reserved.</span>
    <a href="#main" data-top>Back to top &uarr;</a>
  </div>
</footer>

<div class="toast" id="toast" role="status" hidden></div>

<button class="sound on" id="sound" type="button" aria-pressed="true" aria-label="Water sound">
  <span class="bars" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
  <span class="txt" id="soundTxt">Sound on</span>
</button>

<script src="/assets/sw.js" defer></script>
<script src="/assets/site.js" defer></script>
</body>
</html>
'''
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(doc)
    if not noindex: PAGES.append((path, title, text_of(body)))

def text_of(body):
    t = re.sub(r"<(script|style|video|svg|iframe)[\s\S]*?</\1>", " ", body)
    t = re.sub(r"<(h1|h2|h3)[^>]*>", "\n\n## ", t)
    t = re.sub(r"<(p|li|summary|figcaption|address|br)[^>]*>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t]+", " ", t); t = re.sub(r"\n\s*\n\s*\n+", "\n\n", t)
    return "\n".join(l.strip() for l in t.splitlines()).strip()

# ------------------------------------------------------------------ blocks
def scene(key, inner, cls="", tag="section", label=None):
    lab = f' aria-label="{E(label)}"' if label else ""
    return f'''<{tag} class="scene {cls}"{lab}>
    <div class="scene-media" aria-hidden="true"><video muted loop playsinline preload="none" poster="/assets/scenes/{key}.webp" src="/assets/scenes/{key}.mp4"></video></div>
    <div class="scene-inner rise">
{inner}
    </div>
    <p class="scene-cap" aria-hidden="true">{E(SCENES[key])}</p>
  </{tag}>'''

def hero_scene(key, eyebrow, h1, lede="", actions="", trail=None, short=True):
    cr = ""
    if trail:
        parts = [f'<a href="{u}">{E(n)}</a>' for n, u in trail[:-1]] + [f'<span aria-current="page">{E(trail[-1][0])}</span>']
        cr = '<nav class="crumbs" aria-label="Breadcrumb">' + ' <span aria-hidden="true">/</span> '.join(parts) + '</nav>'
    return f'''  <section class="hero hero-scene{" hero-short" if short else ""}">
    <div class="scene-media" aria-hidden="true"><video muted loop playsinline autoplay preload="metadata" poster="/assets/scenes/{key}.webp" src="/assets/scenes/{key}.mp4"></video></div>
    <div class="hero-inner">
      {cr}
      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      {f'<p class="lede">{lede}</p>' if lede else ''}
      {f'<div class="actions">{actions}</div>' if actions else ''}
    </div>
  </section>'''

REQ = '<a class="pill pill-solid" href="/request-appointment/">Request Appointment</a>'
def begin(title_id):
    return f'''  <section class="scene" aria-labelledby="{title_id}">
    <div class="scene-media" aria-hidden="true"><video muted loop playsinline preload="none" poster="/assets/scenes/cloud-light.webp" src="/assets/scenes/cloud-light.mp4"></video></div>
    <div class="scene-inner">
      <p class="label rise">Your First Step</p>
      <h2 id="{title_id}" class="rise">Begin your journey toward <em>emotional wellness</em> today</h2>
      <div class="begin-row rise">
        <p class="body">We are accepting new patients, in person in Las Vegas and by telehealth. {E(P["times"])}.</p>
        {REQ}
      </div>
    </div>
  </section>'''

def svc_rows(items, cls="svc-list"):
    rows = "\n".join(f'''      <li><a class="svc rise" href="/services/{s["slug"]}/">
        <h3>{E(s["name"])}</h3>
        <p>{E(s["short"])}</p>
        {ARROW}
      </a></li>''' for s in items)
    return f'    <ul class="{cls}">\n{rows}\n    </ul>'

def member_card(p, h="h3"):
    tags = "".join(f"<li>{E(x)}</li>" for x in p["focus"][:4])
    lang = " · ".join(p["languages"])
    return f'''      <a class="member rise" href="/providers/{p["slug"]}/">
        <span class="monogram" aria-hidden="true">{p["initials"]}</span>
        <{h}>{E(p["name"])}</{h}>
        <span class="cred">{E(p["creds"])}</span>
        <p>{E(p["short"])}</p>
        <ul class="tags">{tags}</ul>
        <span class="more">Languages: {E(lang)} &nbsp;·&nbsp; Read bio &rarr;</span>
      </a>'''

# ------------------------------------------------------------------ pages
def home():
    panes = [
        ("drop", "What guides our compassionate care", "Providing thoughtful and supportive mental health care in a safe, judgment-free environment."),
        ("rings", "Our approach to mental wellness", "Every treatment plan is tailored to your unique emotional, mental, and wellness needs."),
        ("waves", "Personal care ethics &amp; principles", "Helping individuals achieve balance, clarity, healing, and long-term emotional well-being."),
        ("shield", "Care rooted in understanding", "Your privacy, comfort, and trust are always respected throughout your care journey."),
    ]
    pane_html = "\n".join(f'''        <article class="pane rise">
          {icon(i)}
          <h3>{h}</h3>
          <p>{t}</p>
        </article>''' for i, h, t in panes)
    body = f'''  <!-- 1. Hero: Isaac's waterfall -->
  <section class="hero" id="top">
    <div class="falls" id="falls" aria-hidden="true">
      <img class="mark" id="mark" src="/assets/water/lotus-mark.webp" alt="">
      <video id="loop" muted loop playsinline preload="auto" src="/assets/water/loop.mp4"></video>
      <video id="intro" muted autoplay playsinline preload="auto" src="/assets/water/intro.mp4"></video>
    </div>
    <div class="hero-inner">
      <p class="eyebrow">Psychiatric Care in Las Vegas</p>
      <h1>Healing begins with <em>support</em> &amp; understanding</h1>
      <p class="lede">Whole-person outpatient psychiatric care for children, teens, adults and older adults: evaluations, medication management, therapy and telehealth, in English, Spanish and Tagalog.</p>
      <div class="actions">
        {REQ}
        <a class="pill pill-line" href="/services/">Our Services</a>
      </div>
    </div>
    <div class="hero-foot">
      <div class="values"><span>Accepting New Patients</span><span>Telehealth Available</span><span>Evenings &amp; Weekends</span></div>
    </div>
  </section>

  <!-- 2. Your path to better mental wellness -->
  <section class="band" aria-labelledby="path-title">
    <div class="path">
      <div class="path-head rise">
        <p class="label">Our Care</p>
        <h2 id="path-title">Your path to better <em>mental wellness</em></h2>
        <p class="body">At Bloom Mental Health, we are committed to providing personalized psychiatric care in a safe, supportive, and compassionate environment.</p>
      </div>
      <div class="panes">
{pane_html}
      </div>
    </div>
  </section>

  <!-- 3. Scene: the lake and the willow -->
  {scene("lake-willow", '''      <p class="label">Meeting You Where You Are</p>
      <h2>Mental health is only one part of <em>your story</em></h2>
      <p class="body">Our providers treat the whole person, not simply a diagnosis. Beyond the clinic, they work with nonprofit organizations and community outreach to bring care closer to the people who need it.</p>
      <div class="actions"><a class="pill pill-line" href="/providers/">Meet Our Providers</a></div>''', label="Meeting you where you are")}

  <!-- 4. Why choose Bloom: the office fountain -->
  <section class="band" id="why" aria-labelledby="why-title">
    <div class="why">
      <div class="rise">
        <p class="triad"><span>Compassionate</span><span>Personalized</span><span>Confidential</span></p>
        <h2 id="why-title">Why choose <em>Bloom Mental Health</em></h2>
        <p class="body">We provide compassionate and personalized mental health care focused on emotional wellness, healing, and long-term support. Our goal is to create a safe and welcoming space where individuals feel heard, understood, and empowered throughout their journey to better mental health.</p>
        <a class="pill pill-line" href="/about-us/">About Us</a>
      </div>
      <figure class="lens rise" id="lens">
        <video id="lensVid" src="/assets/water/office-fountain.mp4" muted loop autoplay playsinline preload="auto" aria-label="The water fountain in the Bloom Mental Health office"></video>
        <canvas id="lensGl" aria-hidden="true"></canvas>
        <figcaption>A safe and welcoming space</figcaption>
      </figure>
    </div>
  </section>

  <!-- 5. Services -->
  <section class="band" id="home-services" aria-labelledby="svc-title">
    <div class="svc-head rise">
      <div>
        <p class="label">Services &amp; Clinical Support</p>
        <h2 id="svc-title">A full continuum of outpatient psychiatric care, <em>tailored to you</em></h2>
      </div>
      <a class="pill pill-line" href="/services/">View All Services</a>
    </div>
{svc_rows(SERVICES[:6])}
  </section>

  <!-- 6. Scene: Red Rock, rooted in Las Vegas -->
  {scene("red-rock", f'''      <p class="label">Rooted in Las Vegas</p>
      <h2>Care close to home, <em>in your language</em></h2>
      <p class="body">Our office is at {E(ADDR_ONE)}, with telehealth for visits from home. We see children, adolescents, adults and older adults, with bilingual providers who speak Spanish and Tagalog.</p>
      <div class="actions"><a class="pill pill-line" href="/contact/">Directions &amp; Contact</a></div>''', label="Rooted in Las Vegas")}

  <!-- 7. Providers -->
  <section class="band" aria-labelledby="team-title">
    <div class="row-head rise">
      <div>
        <p class="label">Our Providers</p>
        <h2 id="team-title">Board-certified psychiatric <em>nurse practitioners</em></h2>
      </div>
      <a class="pill pill-line" href="/providers/">All Providers</a>
    </div>
    <div class="team">
{chr(10).join(member_card(p) for p in PROVIDERS)}
    </div>
  </section>

  <!-- 8. Insurance -->
  <section class="band" aria-labelledby="ins-title">
    <div class="row-head rise">
      <div>
        <p class="label">Insurance &amp; Pricing</p>
        <h2 id="ins-title">Most major plans, and <em>simple self-pay</em></h2>
      </div>
      <a class="pill pill-line" href="/insurance/">Insurance Details</a>
    </div>
    <ul class="plans rise">{"".join(f"<li>{E(x)}</li>" for x in INSURANCE)}</ul>
    <p class="note rise" style="margin-top:22px">Self-pay: ${P["self_pay"]["initial"]} initial visit, ${P["self_pay"]["follow_up"]} follow-up. Plan participation and benefits can change, so please call to confirm your coverage.</p>
  </section>

{begin("begin-title")}'''
    title = "Bloom Mental Health | Psychiatric Care & Medication Management in Las Vegas"
    desc = "Outpatient psychiatric care in Las Vegas for all ages: evaluations, medication management, ADHD, anxiety, depression, therapy and telehealth. English, Spanish and Tagalog. Accepting new patients."
    page("/", title, desc, body, [org(), website(), webpage("WebPage", "/", title, desc)])

def about():
    facts = [("Who we see", "Children, adolescents, adults and older adults."), ("Languages", "English, Spanish and Tagalog."),
             ("When", P["times"] + "."), ("Where", f"{ADDR_ONE}, and by telehealth.")]
    fact_html = "\n".join(f'<div class="fact rise"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in facts)
    mvv = [("drop", "Mission", "To provide compassionate, personalized, and accessible mental health care that supports healing, emotional wellness, and long-term balance."),
           ("rings", "Vision", "To create a community where individuals feel empowered, understood, and supported in their journey toward emotional well-being."),
           ("waves", "Values", "We are guided by compassion, trust, respect, confidentiality, and a commitment to providing patient-centered mental health care.")]
    mvv_html = "\n".join(f'''      <li class="mvv-row rise">
        <div class="mvv-key">{icon(i)}<h3>{h}</h3></div>
        <p>{t}</p>
      </li>''' for i, h, t in mvv)
    body = f'''{hero_scene("pine-forest", "About Us", "Compassionate mental health care focused on <em>healing, growth</em> &amp; emotional wellness", "", REQ + '<a class="pill pill-line" href="/providers/">Our Providers</a>', [("Home", "/"), ("About Us", "/about-us/")], short=False)}

  <section class="band" aria-labelledby="ab-title">
    <div class="intro-grid">
      <div class="rise">
        <p class="label">About us</p>
        <h2 id="ab-title">About <em>Bloom Mental Health</em></h2>
      </div>
      <p class="statement rise">At Bloom Mental Health, we are committed to providing personalized psychiatric care in a safe, supportive, and compassionate environment.</p>
      <figure class="still rise"><img src="/assets/water/office-tea-bar.jpg" alt="The coffee and tea bar in the Bloom Mental Health office" loading="lazy"></figure>
    </div>
  </section>

  <section class="band band-tight" aria-label="Who we serve">
    <div class="facts">
{fact_html}
    </div>
  </section>

  <section class="band" aria-label="Mission, vision and values">
    <ul class="mvv">
{mvv_html}
    </ul>
  </section>

{scene("lake-willow", '''      <p class="label">Our Providers</p>
      <h2>A team that believes in <em>meeting people where they are</em></h2>
      <p class="body">Five board-certified psychiatric mental health nurse practitioners, several of them nursing educators, with backgrounds in critical care, long-term care, pediatrics and substance use treatment.</p>
      <div class="actions"><a class="pill pill-line" href="/providers/">Meet the Team</a></div>''', label="Our providers")}

{begin("ab-begin-title")}'''
    title = "About Bloom Mental Health | Psychiatric Practice in Las Vegas, NV"
    desc = "Bloom Mental Health is a whole-person outpatient psychiatric practice in Las Vegas serving children, teens, adults and older adults, in English, Spanish and Tagalog."
    page("/about-us/", title, desc, body, [org(), webpage("AboutPage", "/about-us/", title, desc), crumbs_ld([("Home", "/"), ("About Us", "/about-us/")])])

def providers():
    body = f'''{hero_scene("lake-willow", "Our Providers", "Board-certified care from people who <em>genuinely listen</em>", "Every Bloom provider is a board-certified Psychiatric Mental Health Nurse Practitioner (PMHNP-BC) who treats the whole person, not simply a diagnosis.", REQ, [("Home", "/"), ("Providers", "/providers/")])}

  <section class="band band-tight" aria-label="Providers">
    <div class="team">
{chr(10).join(member_card(p, "h2") for p in PROVIDERS)}
    </div>
  </section>

{begin("pv-begin-title")}'''
    title = "Our Providers | Psychiatric Nurse Practitioners at Bloom Mental Health, Las Vegas"
    desc = "Meet Bloom Mental Health's board-certified psychiatric mental health nurse practitioners in Las Vegas, including Spanish-speaking providers and specialists in children, ADHD and autism."
    ld = [org(), webpage("CollectionPage", "/providers/", title, desc), crumbs_ld([("Home", "/"), ("Providers", "/providers/")])] + [person_ld(p) for p in PROVIDERS]
    page("/providers/", title, desc, body, ld)
    for p in PROVIDERS: provider(p)

def provider(p):
    path = f'/providers/{p["slug"]}/'
    trail = [("Home", "/"), ("Providers", "/providers/"), (p["name"], path)]
    mine = [s for s in SERVICES if p["slug"] in s["providers"] and s["providers"] != ALL]
    paras = "\n".join(f"<p>{E(x)}</p>" for x in p["bio"])
    quote = f'<p class="lead-quote">{E(p["quote"])}</p>' if p.get("quote") else ""
    related = f'''
      <h3>Care {E(p["name"].split()[0])} provides</h3>
      <ul>{"".join(f'<li><a href="/services/{s["slug"]}/">{E(s["name"])}</a></li>' for s in mine)}</ul>''' if mine else ""
    body = f'''{hero_scene("leaves-light", E(p["creds"]), E(p["name"]), E(p["role"]), REQ, trail)}

  <section class="band band-tight" aria-label="Biography">
    <div class="prose">
      <aside class="prose-side rise">
        <div class="bio-head"><span class="monogram" aria-hidden="true">{p["initials"]}</span></div>
        <p class="label" style="margin-top:30px">Areas of focus</p>
        <ul class="tags">{"".join(f"<li>{E(x)}</li>" for x in p["focus"])}</ul>
        <p class="label" style="margin-top:30px">Languages</p>
        <ul class="tags">{"".join(f"<li>{E(x)}</li>" for x in p["languages"])}</ul>
        <p class="note" style="margin-top:30px">NPI {p["npi"]}</p>
      </aside>
      <div class="prose-main rise">
        <h2>Meet <em>{E(p["name"].split()[0])}</em></h2>
        {paras}
        {quote}{related}
      </div>
    </div>
  </section>

{begin("p-begin-title")}'''
    title = f'{p["name"]}, {p["creds"]} | Bloom Mental Health, Las Vegas'
    desc = f'{p["name"]}, {p["creds"]}, is a board-certified psychiatric mental health nurse practitioner at Bloom Mental Health in Las Vegas. {p["short"]}'[:300]
    page(path, title, desc, body, [org(), webpage("ProfilePage", path, title, desc) | {"mainEntity": {"@id": f"{SITE}{path}#person"}}, person_ld(p), crumbs_ld(trail)])

def services():
    body = f'''{hero_scene("leaves-light", "Services", "A full continuum of outpatient psychiatric care, <em>tailored to you</em>", "From a first evaluation to long-term medication management, therapy and intensive outpatient support, in the office or by telehealth.", REQ + '<a class="pill pill-line" href="/insurance/">Insurance &amp; Pricing</a>', [("Home", "/"), ("Services", "/services/")], short=False)}

  <section class="band band-tight" aria-label="All services">
    <p class="label rise">Services &amp; Clinical Support</p>
{svc_rows(SERVICES, "svc-list all")}
  </section>

{begin("svc-begin-title")}'''
    title = "Psychiatric Services in Las Vegas | Bloom Mental Health"
    desc = "Psychiatric evaluations, medication management, ADHD, anxiety and depression, bipolar, PTSD, child and adolescent care, autism, therapy, substance use and MAT, IOP and telehealth in Las Vegas."
    il = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f'{SITE}/services/{s["slug"]}/', "name": s["name"]} for i, s in enumerate(SERVICES)]}
    page("/services/", title, desc, body, [org(), webpage("CollectionPage", "/services/", title, desc), il, crumbs_ld([("Home", "/"), ("Services", "/services/")])] + [service_ld(s) for s in SERVICES])
    for s in SERVICES: service(s)

def service(s):
    path = f'/services/{s["slug"]}/'
    trail = [("Home", "/"), ("Services", "/services/"), (s["name"], path)]
    paras = "\n".join(f"<p>{E(x)}</p>" for x in s["body"])
    helps = "".join(f"<li>{E(x)}</li>" for x in s["helps"])
    who = [PROV[k] for k in s["providers"]] if s["providers"] else []
    team = ""
    if who:
        team = f'''
  <section class="band" aria-labelledby="who-title">
    <div class="row-head rise"><div><p class="label">Providers</p><h2 id="who-title">Who you may <em>see</em></h2></div></div>
    <div class="team">
{chr(10).join(member_card(p) for p in who)}
    </div>
  </section>'''
    others = [x for x in SERVICES if x["slug"] != s["slug"]][:0]
    body = f'''{hero_scene(s["scene"], "Services", E(s["name"]), E(s["short"]), REQ + '<a class="pill pill-line" href="/services/">All Services</a>', trail)}

  <section class="band band-tight" aria-label="{E(s["name"])}">
    <div class="prose">
      <aside class="prose-side rise">
        {icon(s["icon"]).replace("<svg ", '<svg style="width:40px;height:40px;stroke:var(--accent);fill:none;stroke-width:1" ')}
        <p class="label" style="margin-top:26px">At a glance</p>
        <ul class="tags"><li>In office, Las Vegas</li><li>Telehealth</li><li>English · Spanish · Tagalog</li><li>Accepting new patients</li></ul>
      </aside>
      <div class="prose-main rise">
        <h2>{E(s["title"])}</h2>
        {paras}
        <h3>When it may help</h3>
        <ul>{helps}</ul>
        <h3>What you can expect</h3>
        <ul>{"".join(f"<li>{E(x)}</li>" for x in EXPECT)}</ul>
        <p class="note">Services, availability and age ranges can change. Please contact our office at <a href="tel:{P["phone"].replace("-", "")}">{P["phone"]}</a> to confirm before your visit. If you are in crisis, call or text 988 or call 911.</p>
      </div>
    </div>
  </section>
{team}

{begin("s-begin-title")}'''
    title = f'{s["title"]} | Bloom Mental Health'
    desc = f'{s["short"]} Outpatient care at Bloom Mental Health, {P["city"]}, NV, in person or by telehealth. Accepting new patients.'
    page(path, title, desc, body, [org(), webpage("MedicalWebPage", path, title, desc) | {"mainEntity": {"@id": f"{SITE}{path}#service"}}, service_ld(s), crumbs_ld(trail)])

def insurance():
    body = f'''{hero_scene("red-rock", "Insurance &amp; Pricing", "Coverage that works for you, and <em>simple self-pay</em>", "We are credentialed with most major plans in Nevada, and offer straightforward self-pay pricing.", REQ, [("Home", "/"), ("Insurance & Pricing", "/insurance/")])}

  <section class="band band-tight" aria-labelledby="cred-title">
    <p class="label rise">Credentialed Insurances</p>
    <h2 id="cred-title" class="rise" style="margin-bottom:40px">Plans we <em>accept</em></h2>
    <ul class="plans rise">{"".join(f"<li>{E(x)}</li>" for x in INSURANCE)}</ul>
    <p class="label rise" style="margin-top:60px">Pending Credentialing</p>
    <ul class="plans pending rise">{"".join(f"<li>{E(x)}</li>" for x in INSURANCE_PENDING)}</ul>
    <p class="note rise" style="margin-top:26px">Because insurance participation and plan benefits can change, please contact our office at <a href="tel:{P["phone"].replace("-", "")}">{P["phone"]}</a> to confirm your coverage before your first visit.</p>
  </section>

  <section class="band" aria-labelledby="price-title">
    <p class="label rise">New Patients &amp; Cash Pricing</p>
    <h2 id="price-title" class="rise" style="margin-bottom:40px">Self-pay <em>visits</em></h2>
    <div class="prices rise">
      <div class="price"><b>${P["self_pay"]["initial"]}</b><span>Initial visit (self-pay)</span></div>
      <div class="price"><b>${P["self_pay"]["follow_up"]}</b><span>Follow-up visit (self-pay)</span></div>
    </div>
    <ul class="tags rise" style="margin-top:30px"><li>We are currently accepting new patients</li><li>Telehealth available</li><li>Early mornings, evenings, Saturdays &amp; Sundays</li></ul>
  </section>

{begin("ins-begin-title")}'''
    title = "Insurance & Self-Pay Pricing | Bloom Mental Health, Las Vegas"
    desc = "Bloom Mental Health accepts Aetna, Carelon (BCBS), CareSource, Evernorth (Cigna), Medicare, UHC / Optum, UMR, Alignment and Medicaid FFS. Self-pay: $90 initial, $50 follow-up."
    page("/insurance/", title, desc, body, [org(), webpage("WebPage", "/insurance/", title, desc), crumbs_ld([("Home", "/"), ("Insurance & Pricing", "/insurance/")])])

def for_providers():
    reasons = "\n".join(f'<div class="reason rise"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in REFER_REASONS)
    body = f'''{hero_scene("pine-forest", "For Referring Providers", "Partnering for better <em>mental health</em>", "A referral resource for the colleagues who trust us with their patients' care. We are accepting new patients, and we aim to make referring as simple and collaborative as possible for your practice.", f'<a class="pill pill-solid" href="tel:{P["phone"].replace("-", "")}">Call {P["phone"]}</a>', [("Home", "/"), ("For Referring Providers", "/for-providers/")])}

  <section class="band band-tight" aria-labelledby="how-title">
    <div class="prose">
      <aside class="prose-side rise">
        <p class="label">How to refer</p>
        <div class="info">
          <div><h3>Fax</h3><p>{P["fax"]}</p></div>
          <div><h3>Phone</h3><p><a href="tel:{P["phone"].replace("-", "")}">{P["phone"]}</a></p></div>
          <div><h3>Email</h3><p><a href="mailto:{P["email"]}">{P["email"]}</a></p></div>
        </div>
      </aside>
      <div class="prose-main rise">
        <h2 id="how-title">Referring a patient to <em>Bloom</em></h2>
        <p>We provide compassionate, whole-person outpatient psychiatric care for children, adolescents, adults and older adults, with bilingual providers who speak Spanish and Tagalog and telehealth available.</p>
        <h3>Before referral</h3>
        <ul>{"".join(f"<li>{E(x)}</li>" for x in BEFORE_REFERRAL)}</ul>
        <h3>What patients can expect</h3>
        <ul>{"".join(f"<li>{E(x)}</li>" for x in EXPECT)}</ul>
        <p class="note">A referral does not guarantee an appointment, diagnosis, medication, or insurance coverage. Clinical decisions are based on the patient's individual assessment and needs. Please contact our office to confirm current age ranges, services, availability, and insurance participation before referring. See <a href="/insurance/">insurance</a> and <a href="/services/">services</a>.</p>
      </div>
    </div>
  </section>

  <section class="band" aria-labelledby="who-title">
    <p class="label rise">Who May Benefit From Referral</p>
    <h2 id="who-title" class="rise" style="margin-bottom:26px">When to <em>consider Bloom</em></h2>
    <p class="body rise" style="margin-bottom:44px">Consider Bloom Mental Health when a patient may benefit from outpatient psychiatric assessment, diagnosis, medication management, or ongoing psychiatric follow-up.</p>
    <div class="reasons">
{reasons}
    </div>
    <div class="alert rise" style="margin-top:44px">
      <h3>Urgent / Emergency Needs</h3>
      <p>Bloom Mental Health is an outpatient practice. Patients experiencing an immediate safety concern, medical emergency, or acute psychiatric crisis requiring a higher level of care should be directed to the appropriate emergency or crisis service rather than a routine outpatient referral.</p>
    </div>
  </section>'''
    title = "Refer a Patient | Outpatient Psychiatry in Las Vegas | Bloom Mental Health"
    desc = "Referral guide for clinicians: how to refer a patient to Bloom Mental Health in Las Vegas, who may benefit, insurance, and what patients can expect. Fax 702-357-5249."
    page("/for-providers/", title, desc, body, [org(), webpage("WebPage", "/for-providers/", title, desc), crumbs_ld([("Home", "/"), ("For Referring Providers", "/for-providers/")])])

def faq():
    items = "\n".join(f'      <details class="rise"><summary>{E(q)}</summary>\n        <p>{E(a)}</p></details>' for q, a in FAQ)
    body = f'''{hero_scene("cloud-light", "FAQ", "Answers to common questions about our <em>mental health services</em>", "", "", [("Home", "/"), ("FAQ", "/faq/")])}

  <section class="band band-tight" aria-label="Frequently asked questions">
    <div class="faq">
{items}
    </div>
  </section>

{begin("faq-begin-title")}'''
    title = "FAQ | Bloom Mental Health, Las Vegas Psychiatric Care"
    desc = "Answers about new patients, insurance, self-pay pricing, telehealth, languages, ages served and what to expect at Bloom Mental Health in Las Vegas."
    page("/faq/", title, desc, body, [org(), webpage("WebPage", "/faq/", title, desc), faq_ld(FAQ), crumbs_ld([("Home", "/"), ("FAQ", "/faq/")])])

def contact():
    tel = P["phone"].replace("-", "")
    body = f'''{hero_scene("red-rock", "Contact Us", "Reach out for personalized mental health support <em>&amp; guidance</em>", "Send us a message below and a member of our team will reach out within one business day. Ready to book? Use the appointment request instead.", f'<a class="pill pill-solid" href="#contact-form" data-scroll>Send a message</a><a class="pill pill-line" href="/request-appointment/">Request an appointment</a><span class="or-call">or call <a href="tel:{tel}">{P["phone"]}</a></span>', [("Home", "/"), ("Contact", "/contact/")])}

  <section class="band band-tight" aria-label="Send a message">
    <div class="contact-grid">
      <form class="form glass rise" id="contact-form" novalidate>
        <p class="form-intro">Tell us what you need. No medical details are necessary here; we will ask when we call.</p>
        <div class="field-row">
          <div class="field"><label for="c-name">Your name</label><input id="c-name" name="name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="c-email">Your email</label><input id="c-email" name="email" type="email" autocomplete="email" required></div>
        </div>
        <div class="field"><label for="c-subject">Subject</label><input id="c-subject" name="subject" type="text"></div>
        <div class="field"><label for="c-message">Your message <span class="opt">(optional)</span></label><textarea id="c-message" name="message" rows="5"></textarea></div>
        <div class="form-foot">
          <button class="pill pill-solid" type="submit">Send message</button>
          <p class="form-msg" role="status"></p>
        </div>
        <p class="crisis">If you are in crisis or thinking about harming yourself, call or text <strong>988</strong> or call <strong>911</strong>. This form is not monitored around the clock.</p>
      </form>

      <aside class="info rise" aria-label="Office details">
        <div>
          <h3>Visit</h3>
          <p>{P["street"]}<br>{P["city"]}, {P["region"]} {P["zip"]}</p>
          <a class="pill pill-line pill-small" href="{MAPS_DIR}" target="_blank" rel="noopener">Get directions</a>
        </div>
        <div><h3>Call</h3><p><a href="tel:{tel}">{P["phone"]}</a></p></div>
        <div><h3>Fax</h3><p>{P["fax"]}</p></div>
        <div><h3>Email</h3><p><a href="mailto:{P["email"]}">{P["email"]}</a></p></div>
        <div><h3>Hours</h3><p style="font-size:clamp(18px,1.5vw,22px)">{E(P["times"])}.</p></div>
      </aside>
    </div>
  </section>

  <section class="band band-tight" aria-label="Map">
    <iframe class="map rise" title="Map to Bloom Mental Health, {E(ADDR_ONE)}" src="{MAPS_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
  </section>'''
    title = "Contact Bloom Mental Health | 2450 Chandler Ave, Las Vegas, NV"
    desc = f"Contact Bloom Mental Health in Las Vegas: call {P['phone']}, fax {P['fax']}, or send a message. {ADDR_ONE}."
    page("/contact/", title, desc, body, [org(), webpage("ContactPage", "/contact/", title, desc), crumbs_ld([("Home", "/"), ("Contact", "/contact/")])])

def request():
    tel = P["phone"].replace("-", "")
    body = f'''{hero_scene("cloud-light", "Get Started", "Request an <em>appointment</em>", "Tell us a little about what you need and the best way to reach you. A person from our team calls or emails you back to set a time.", "", [("Home", "/"), ("Request an Appointment", "/request-appointment/")])}

  <section class="band band-tight" aria-label="Appointment request">
    <div class="request-wrap glass rise">
      <div class="appt-head" style="margin-bottom:26px">
        <span>Bloom Mental Health</span>
        <span>{E(ADDR_ONE)}</span>
        <a href="tel:{tel}">{P["phone"]}</a>
      </div>
      <iframe id="bloom-inquiry" class="request-frame" title="Request an appointment with Bloom Mental Health" src="https://app.bloommentalhealthlv.com/inquiry.html" loading="eager" allow="clipboard-write"></iframe>
      <p class="crisis" style="margin-top:26px">You can also call <a href="tel:{tel}">{P["phone"]}</a>. If you are in crisis or thinking about harming yourself, call or text <strong>988</strong> (Suicide and Crisis Lifeline) or call <strong>911</strong>. This form is not monitored around the clock.</p>
    </div>
  </section>'''
    title = "Request an Appointment | Bloom Mental Health, Las Vegas"
    desc = "Request a psychiatric appointment at Bloom Mental Health in Las Vegas, in person or by telehealth. We are accepting new patients."
    page("/request-appointment/", title, desc, body, [org(), webpage("WebPage", "/request-appointment/", title, desc) | {"potentialAction": {"@type": "ReserveAction", "target": SITE + "/request-appointment/"}}, crumbs_ld([("Home", "/"), ("Request an Appointment", "/request-appointment/")])])

def notfound():
    body = f'''{hero_scene("lake-willow", "Page not found", "This page has <em>drifted away</em>", "The page you are looking for is not here. Try our services, or request an appointment.", REQ + '<a class="pill pill-line" href="/services/">Our Services</a>', None, short=False)}'''
    page("/404.html", "Page not found | Bloom Mental Health", "Page not found.", body, [], noindex=True)

# ------------------------------------------------------------------ discovery files
def discovery():
    urls = [p for p, _, _ in PAGES]
    prio = lambda u: "1.0" if u == "/" else "0.9" if u in ("/services/", "/request-appointment/", "/providers/") else "0.8" if u.count("/") <= 2 else "0.7"
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><priority>{prio(u)}</priority></url>" for u in urls]
    sm.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")

    bots = ["Googlebot", "Bingbot", "DuckDuckBot", "Applebot", "Twitterbot", "facebookexternalhit", "LinkedInBot",
            "GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "Claude-Web", "Claude-SearchBot", "Claude-User", "anthropic-ai",
            "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "Amazonbot", "DuckAssistBot", "meta-externalagent", "CCBot", "*"]
    rb = "\n".join(f"User-agent: {b}" for b in bots) + """
Allow: /
Allow: /llms.txt
Allow: /llms-full.txt
Allow: /AGENTS.md
Allow: /services.json
Disallow: /tools/
Disallow: /README.md
Disallow: /request-appointment/thank-you/

Sitemap: """ + SITE + "/sitemap.xml\n"
    open(os.path.join(ROOT, "robots.txt"), "w").write(rb)

    L = [f"# {P['name']}", "",
         "> Outpatient psychiatric practice in Las Vegas, Nevada. Board-certified psychiatric mental health nurse practitioners (PMHNP-BC) providing psychiatric evaluations, medication management, therapy, substance use care (MAT), intensive outpatient programming and telehealth for children, adolescents, adults and older adults, in English, Spanish and Tagalog. Accepting new patients.", "",
         f"- Site: {SITE}", f"- Address: {ADDR_ONE}, United States", f"- Phone: {P['phone']}", f"- Fax: {P['fax']} (referrals)", f"- Email: {P['email']}",
         f"- Request an appointment: {SITE}/request-appointment/", f"- When: {P['times']}. No clock hours are published; do not state specific hours.",
         f"- Ages: {', '.join(P['ages'])}", f"- Languages: {', '.join(P['languages'])}", "", "## Services"]
    L += [f"- [{s['name']}]({SITE}/services/{s['slug']}/): {s['short']}" for s in SERVICES]
    L += ["", "## Providers (all PMHNP-BC)"]
    L += [f"- [{p['name']}, {p['creds']}]({SITE}/providers/{p['slug']}/): {p['short']} Languages: {', '.join(p['languages'])}." for p in PROVIDERS]
    L += ["", "## Insurance and pricing", f"- Credentialed: {', '.join(INSURANCE)}.", f"- Pending credentialing: {', '.join(INSURANCE_PENDING)}.",
          f"- Self-pay: ${P['self_pay']['initial']} initial visit, ${P['self_pay']['follow_up']} follow-up visit.",
          "- Participation and benefits change; tell people to call the office to confirm coverage.", "",
          "## Pages", f"- [About]({SITE}/about-us/)", f"- [Providers]({SITE}/providers/)", f"- [Services]({SITE}/services/)", f"- [Insurance & pricing]({SITE}/insurance/)",
          f"- [FAQ]({SITE}/faq/)", f"- [Contact]({SITE}/contact/)", f"- [For referring providers]({SITE}/for-providers/)", f"- [Full site text]({SITE}/llms-full.txt)", "",
          "## Facts to respect",
          "- Bloom is an outpatient practice. Crisis: call or text 988 (US Suicide and Crisis Lifeline) or call 911. The website and forms are not emergency services.",
          "- Do not state clock hours, provider availability on specific days, or which provider speaks Tagalog.",
          "- Do not describe Bloom as accepting a plan listed as pending.",
          "- A referral does not guarantee an appointment, diagnosis, medication, or coverage.",
          "- Agents sending traffic: append ?utm_source=<agent>&utm_medium=ai-agent to links."]
    open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(L) + "\n")

    full = [f"# {P['name']} · full site text", f"> Generated {TODAY} from the live pages by tools/build.py. Source of truth: {SITE}", ""]
    for u, t, txt in PAGES:
        full += [f"\n---\n\n# {t}", f"URL: {SITE}{u}", "", txt]
    open(os.path.join(ROOT, "llms-full.txt"), "w").write("\n".join(full) + "\n")

    open(os.path.join(ROOT, "AGENTS.md"), "w").write(f"""# For agents · {P['name']}

Outpatient psychiatric practice at {ADDR_ONE}. Phone {P['phone']}, fax {P['fax']}.

- To book: send people to {SITE}/request-appointment/ (a person calls or emails back). Do not promise times.
- Facts: {SITE}/llms.txt (brief), {SITE}/llms-full.txt (every page), {SITE}/services.json (services, providers, insurance).
- Crisis is out of scope: 988 or 911.
- No patient information is collected or held on this website; the request form hands off to the practice's system.
""")
    sj = {"name": P["name"], "url": SITE, "address": ADDR_ONE, "phone": P["phone"], "fax": P["fax"], "languages": P["languages"], "ages": P["ages"],
          "accepting_new_patients": True, "telehealth": True, "times": P["times"], "self_pay": P["self_pay"],
          "insurance": {"credentialed": INSURANCE, "pending": INSURANCE_PENDING},
          "services": [{"name": s["name"], "summary": s["short"], "url": f"{SITE}/services/{s['slug']}/"} for s in SERVICES],
          "providers": [{"name": p["name"], "credentials": p["creds"], "npi": p["npi"], "languages": p["languages"], "focus": p["focus"], "url": f"{SITE}/providers/{p['slug']}/"} for p in PROVIDERS],
          "updated": TODAY}
    open(os.path.join(ROOT, "services.json"), "w").write(json.dumps(sj, indent=2, ensure_ascii=False) + "\n")

def indexnow():
    key = "5a439565c76be06b18ca2675bc119ba9"
    urls = [SITE + u for u, _, _ in PAGES] + [SITE + x for x in ("/sitemap.xml", "/llms.txt", "/llms-full.txt", "/AGENTS.md", "/services.json")]
    body = json.dumps({"host": "bloommentalhealthlv.com", "key": key, "keyLocation": f"{SITE}/{key}.txt", "urlList": urls}).encode()
    for ep in ("https://api.indexnow.org/indexnow", "https://www.bing.com/indexnow"):
        req = urllib.request.Request(ep, data=body, headers={"Content-Type": "application/json; charset=utf-8"})
        try:
            with urllib.request.urlopen(req, timeout=20) as r: print(ep, r.status)
        except Exception as e: print(ep, "ERR", e)

if __name__ == "__main__":
    home(); about(); providers(); services(); insurance(); for_providers(); faq(); contact(); request(); notfound()
    discovery()
    print(f"built {len(PAGES)} indexable pages")
    if "--submit" in sys.argv: indexnow()

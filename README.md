# bloommentalhealthlv.com

Static site for Bloom Mental Health (Las Vegas psychiatric care). Hand-written HTML/CSS/JS, no build step, served by GitHub Pages.

- Pages: `/`, `/about-us/`, `/services/`, `/faq/`, `/contact/`, `/request-appointment/`
- Forms post to the Bloom CRM (Convex `/lead`): the request card is an iframe of `app.bloommentalhealthlv.com/inquiry.html`; the contact form posts `source: website_contact`.
- Analytics: GA4 `G-FC50JVCNET`. Discoverability: `robots.txt`, `sitemap.xml`, `llms.txt`, JSON-LD per page, IndexNow key file.
- Deploy: push to `main`. No PHI in this repo, ever.

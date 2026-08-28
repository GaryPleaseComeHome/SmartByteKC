# Integration Specs: SmartByteKC

## 1. Google Business Profile
- Location schema (JSON-LD) included in all pages.
- Review widget: Async load via `gbp.js` after idle callback.

## 2. Google Forms (Quote/Booking)
- Two forms: Residential, Commercial.
- `forms.js` handles client-side validation, honeypot, and `fetch` submission.

## 3. Google Analytics (GA4)
- `analytics.js` loads only after user interaction.
- Events: `page_view`, `cta_click`, `form_submit`, etc.

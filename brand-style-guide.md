# SmartByteKC Brand Style Guide

**Version:** 2.0  
**Status:** Production-Ready  
**Last Updated:** August 2026

---

## 1. Brand Essence

### Core Promise
> **Smart Technology. Simplified.**

### Positioning
SmartByteKC is Kansas City's trusted technology partner — the neighbor who happens to be an expert. We bridge the gap between enterprise-grade infrastructure and residential warmth, delivering peace of mind through precision engineering and plain-English communication.

### Brand Personality
| Dimension | Residential Expression | Commercial Expression |
|-----------|------------------------|----------------------|
| **Tone** | Warm, approachable, reassuring | Professional, authoritative, precise |
| **Voice** | "We're neighbors who happen to be experts" | "We deliver infrastructure that scales" |
| **Vocabulary** | Plain English, contractions, active voice | Industry terminology welcome, outcomes-first |
| **Empathy** | Lead with pain points (dead zones, confusion) | Lead with outcomes (uptime, security, compliance) |
| **Authority** | Earned through explanation | Established through credentials |

### Values (The Three Pillars)
1. **Explain, Never Confuse** — Technology shouldn't feel like black magic
2. **Control Systems Discipline** — Engineered precision, built to last
3. **100% Local** — Kansas City neighbors, not a distant call center

---

## 2. Visual Identity

### 2.1 Logo System

#### Primary Logo
- **Mark:** Custom brain-to-USB icon (sideways brain profile transitioning to USB-A plug)
- **Wordmark:** "SmartByte" in system font weight 700 + "KC" in brand accent weight 700
- **Lockup:** Horizontal only (mark left, wordmark right)
- **Clear Space:** 1× mark height on all sides

#### Logo Variants
| Variant | Use Case | Background |
|---------|----------|------------|
| Primary (Emerald mark + White/Charcoal type) | Light backgrounds | `#FFFFFF`, `#F5F5F7` |
| Reversed (White mark + White type) | Dark backgrounds | `#1D1D1F`, `#000000` |
| Monochrome (Charcoal) | Single-color print | Any |
| Favicon | Browser tab, app icon | Mark only, 32×32, 16×16 |

#### Do Not
- Stretch, rotate, or recolor the mark
- Place on busy imagery without overlay
- Use "SBKC" abbreviation externally
- Separate mark from wordmark in primary lockup

### 2.2 Color Palette

#### Primary Neutrals (The Canvas)
| Token | Hex | RGB | HSL | Role |
|-------|-----|-----|-----|------|
| `--color-white` | `#FFFFFF` | 255,255,255 | 0,0%,100% | Pure white — page backgrounds, card surfaces |
| `--color-gray-50` | `#F5F5F7` | 245,245,247 | 240,8%,96% | Light section backgrounds (Apple-style) |
| `--color-gray-100` | `#E5E5EA` | 229,229,234 | 240,5%,90% | Borders, dividers, disabled states |
| `--color-gray-300` | `#D1D1D6` | 209,209,214 | 240,5%,82% | Secondary borders, input borders |
| `--color-gray-500` | `#86868B` | 134,134,139 | 240,2%,53% | Placeholder text, secondary icons |
| `--color-gray-700` | `#48484A` | 72,72,74 | 240,1%,29% | Secondary text on light |
| `--color-gray-900` | `#1D1D1F` | 29,29,31 | 240,3%,12% | Primary text on light, dark button fills |
| `--color-black` | `#000000` | 0,0,0 | 0,0%,0% | Immersive section backgrounds |

#### Brand Accent (The Signal)
| Token | Hex | RGB | HSL | Role |
|-------|-----|-----|-----|------|
| `--color-emerald-400` | `#34D399` | 52,211,153 | 158,71%,52% | Primary interactive: links, focus rings, CTAs |
| `--color-emerald-500` | `#10B981` | 16,185,129 | 158,84%,39% | CTA backgrounds, active states |
| `--color-emerald-600` | `#059669` | 5,150,105 | 158,94%,30% | Hover states, pressed states |
| `--color-emerald-900` | `#064E3B` | 6,78,59 | 158,86%,16% | Dark section accent backgrounds |

#### Semantic Colors
| Token | Light Mode | Dark Mode | Role |
|-------|------------|-----------|------|
| `--color-text-primary` | `#1D1D1F` | `#FFFFFF` | Body text, headings |
| `--color-text-secondary` | `#48484A` | `#A1A1AA` | Descriptions, captions |
| `--color-text-tertiary` | `#86868B` | `#71717A` | Placeholders, metadata |
| `--color-border-subtle` | `#E5E5EA` | `#272729` | Card borders, dividers |
| `--color-border-focus` | `#10B981` | `#34D399` | Focus rings, active inputs |
| `--color-surface` | `#FFFFFF` | `#1D1D1F` | Card backgrounds |
| `--color-surface-elevated` | `#F5F5F7` | `#272729` | Elevated cards, modals |
| `--color-overlay` | `rgba(29,29,31,0.6)` | `rgba(0,0,0,0.7)` | Modal backdrops |

#### Status Colors (Sparing Use)
| Token | Light | Dark | Use |
|-------|-------|------|-----|
| `--color-success` | `#15BE53` | `#22C55E` | Success states, checkmarks |
| `--color-warning` | `#F59E0B` | `#FBBF24` | Warnings, pending states |
| `--color-error` | `#EF4444` | `#F87171` | Errors, destructive actions |

### 2.3 Typography

#### Font Stacks
```css
/* Primary — System font with SF Pro / Inter fallback */
--font-sans: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, 'Helvetica Neue', Arial, sans-serif;

/* Monospace — For code, technical specs */
--font-mono: ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;
```

#### Type Scale (Fluid, Clamp-Based)
| Role | Size (clamp) | Weight | Line Height | Letter Spacing | Font |
|------|--------------|--------|-------------|----------------|------|
| **Display Hero** | `clamp(2.5rem, 6vw, 4.5rem)` | 300 | 1.05 | -0.04em | Sans |
| **Section Heading** | `clamp(2rem, 4vw, 3.5rem)` | 400 | 1.10 | -0.03em | Sans |
| **Card Heading** | `clamp(1.25rem, 2.5vw, 1.75rem)` | 600 | 1.20 | -0.02em | Sans |
| **Body Large** | `clamp(1.125rem, 1.5vw, 1.25rem)` | 400 | 1.70 | -0.01em | Sans |
| **Body** | `1rem` | 400 | 1.70 | -0.01em | Sans |
| **Body Small** | `0.875rem` | 400 | 1.60 | -0.005em | Sans |
| **Caption** | `0.75rem` | 400 | 1.50 | 0 | Sans |
| **Button** | `1rem` | 500 | 1.00 | 0 | Sans |
| **Code** | `0.875rem` | 400 | 1.80 | 0 | Mono |

#### Weight Strategy
- **300 (Light):** Display hero only — whisper authority
- **400 (Regular):** Body text, most UI — the workhorse
- **500 (Medium):** Buttons, emphasis, navigation
- **600 (Semibold):** Card headings, important labels
- **700 (Bold):** Logo wordmark, rare emphasis only

#### Optical Sizing Principle
Headlines compress (tight line-height, negative tracking); body opens (generous line-height, relaxed tracking). This creates rhythm: dense impact above, comfortable reading below.

### 2.4 Spacing System

**Base Unit:** 4px  
**Scale:** `4, 8, 12, 16, 24, 32, 48, 64, 96, 128` (multiply base by 1, 2, 3, 4, 6, 8, 12, 16, 24, 32)

#### Component-Specific Overrides
| Component | Padding | Gap | Margin |
|-----------|---------|-----|--------|
| Section (vertical) | — | — | 96px / 128px (lg) |
| Container (horizontal) | 24px / 32px (lg) | — | auto |
| Card | 32px / 40px (lg) | 24px | — |
| Button | 16px 32px | 12px | — |
| Input | 12px 16px | — | 8px (field gap) |
| Nav Item | — | 32px | — |

### 2.5 Border Radius Scale
| Token | Value | Use |
|-------|-------|-----|
| `--radius-sm` | 4px | Badges, small tags |
| `--radius-md` | 8px | Buttons, inputs, standard cards |
| `--radius-lg` | 12px | Feature cards, image containers |
| `--radius-xl` | 16px | Hero cards, modals |
| `--radius-full` | 9999px | Pill CTAs, avatar, tags |

### 2.6 Shadow & Elevation

| Level | Token | Value | Use |
|-------|-------|-------|-----|
| None | `--shadow-none` | `none` | Flat sections |
| Subtle | `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | Hover hints, dividers |
| Card | `--shadow-md` | `0 4px 12px rgba(0,0,0,0.08), 0 2px 4px rgba(0,0,0,0.04)` | Standard cards |
| Elevated | `--shadow-lg` | `0 12px 28px rgba(0,0,0,0.12), 0 4px 8px rgba(0,0,0,0.06)` | Dropdowns, modals |
| Immersive | `--shadow-xl` | `0 24px 48px rgba(0,0,0,0.16), 0 8px 16px rgba(0,0,0,0.08)` | Hero cards, floating panels |
| Focus | `--shadow-focus` | `0 0 0 3px rgba(16,185,129,0.4)` | Keyboard focus (emeral-d) |

**Philosophy:** Shadows are soft, diffused, and rare. Elevation primarily comes from background contrast (dark card on darker bg, light card on lighter bg).

### 2.7 Motion & Animation

#### Easing Curves
```css
--ease-smooth: cubic-bezier(0.25, 0.46, 0.45, 0.94);  /* Default — natural, premium */
--ease-snappy: cubic-bezier(0.2, 0.6, 0.2, 1);         /* UI responses — fast, crisp */
--ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);      /* Playful, overshoot — sparing */
```

#### Duration Scale
| Token | Duration | Use |
|-------|----------|-----|
| `--duration-instant` | 0ms | State changes (active, focus) |
| `--duration-fast` | 150ms | Hover, tap feedback |
| `--duration-base` | 200ms | Standard transitions |
| `--duration-smooth` | 300ms | Panel slides, modal entry |
| `--duration-slow` | 500ms | Page transitions, complex sequences |

#### Motion Principles
1. **Respect `prefers-reduced-motion`** — All non-essential animation disabled
2. **Purposeful only** — Motion clarifies state, shows continuity, gives tactility
3. **No loops** — No infinite animations without user action
4. **Stagger with intent** — 50-100ms stagger for lists, never decorative
5. **Performance first** — Transform/opacity only; no layout thrashing

#### Key Animations
- **Fade In Up:** `opacity: 0 → 1`, `transform: translateY(20px) → 0` (300ms, `--ease-smooth`)
- **Scale Press:** `transform: scale(0.98)` (instant, on `:active`)
- **Glow Pulse:** `box-shadow: 0 0 0 0 → 0 0 20px 4px rgba(16,185,129,0)` (2s, infinite, hero CTA only)
- **Slide Panel:** `transform: translateX(100%) → 0` (300ms, `--ease-smooth`, mobile nav)
- **Reveal Text:** Per-word/line stagger (50ms, `--ease-snappy`, hero headlines)

### 2.8 Iconography

- **Style:** Outline, 2px stroke weight, 24×24px base grid
- **Source:** Lucide (consistent, open-source, tree-shakeable)
- **Sizes:** 16px (inline), 20px (UI), 24px (default), 32px (feature), 48px (hero)
- **Color:** Inherit `currentColor` — adapts to context
- **Rounded caps/joins** for approachability

### 2.9 Imagery Rules

| Aspect | Specification |
|--------|---------------|
| **Hero** | Full-bleed, 16:9, subtle overlay (`rgba(29,29,31,0.4)`), high-res photography only |
| **Service Cards** | 4:3, object-fit: cover, consistent lighting |
| **Team** | 1:1, natural light, environmental (not studio) |
| **Project Work** | 16:9 or 4:3, before/after pairs aligned |
| **Placeholder** | SVG pattern (subtle grid) + `--color-gray-100`/`--color-gray-800` |
| **Format** | WebP/AVIF primary, JPEG fallback; `loading="lazy"` below fold |
| **Optimization** | Hero ≤100KB, Cards ≤50KB, Thumbnails ≤20KB |

---

## 3. Component Library Specs

### 3.1 Buttons

#### Primary (Filled)
```css
.btn--primary {
  background: var(--color-emerald-500);
  color: var(--color-white);
  border: none;
  padding: 16px 32px;
  border-radius: var(--radius-md);
  font: 500 1rem/1 var(--font-sans);
  transition: background var(--duration-fast) var(--ease-snappy),
              transform var(--duration-instant),
              box-shadow var(--duration-fast) var(--ease-snappy);
}
.btn--primary:hover { background: var(--color-emerald-600); transform: translateY(-1px); box-shadow: var(--shadow-lg); }
.btn--primary:active { background: var(--color-emerald-600); transform: scale(0.98); }
.btn--primary:focus-visible { outline: none; box-shadow: var(--shadow-focus); }
```

#### Secondary (Outline)
```css
.btn--secondary {
  background: transparent;
  color: var(--color-emerald-500);
  border: 2px solid var(--color-emerald-500);
  padding: 14px 30px; /* 2px border offset */
  border-radius: var(--radius-md);
  font: 500 1rem/1 var(--font-sans);
  transition: background var(--duration-fast) var(--ease-snappy),
              color var(--duration-fast) var(--ease-snappy),
              border-color var(--duration-fast) var(--ease-snappy);
}
.btn--secondary:hover { background: var(--color-emerald-500); color: var(--color-white); }
.btn--secondary:focus-visible { outline: none; box-shadow: var(--shadow-focus); }
```

#### Pill CTA (Apple-style "Learn More")
```css
.btn--pill {
  background: transparent;
  color: var(--color-emerald-500);
  border: 2px solid var(--color-emerald-500);
  padding: 10px 24px;
  border-radius: var(--radius-full);
  font: 500 0.875rem/1 var(--font-sans);
  text-decoration: underline;
  text-underline-offset: 2px;
  transition: background var(--duration-fast) var(--ease-snappy),
              color var(--duration-fast) var(--ease-snappy);
}
.btn--pill:hover { background: var(--color-emerald-500); color: var(--color-white); text-decoration: none; }
```

#### Ghost (Minimal)
```css
.btn--ghost {
  background: transparent;
  color: var(--color-text-primary);
  border: none;
  padding: 12px 16px;
  border-radius: var(--radius-md);
  font: 400 1rem/1 var(--font-sans);
}
.btn--ghost:hover { background: var(--color-gray-100); } /* light */ / `var(--color-gray-800)` /* dark */
```

### 3.2 Cards

#### Service Card (Bento-style)
```css
.card--service {
  background: var(--color-surface);
  border: 1px solid var(--color-border-subtle);
  border-radius: var(--radius-xl);
  padding: 32px 40px;
  transition: border-color var(--duration-base) var(--ease-smooth),
              box-shadow var(--duration-base) var(--ease-smooth),
              transform var(--duration-base) var(--ease-smooth);
}
.card--service:hover {
  border-color: var(--color-emerald-500);
  box-shadow: var(--shadow-lg);
  transform: translateY(-4px);
}
.card--service:has(:focus-visible) { box-shadow: var(--shadow-focus); }
```

#### Feature Card (Why Us)
```css
.card--feature {
  background: var(--color-surface-elevated);
  border: 1px solid var(--color-border-subtle);
  border-radius: var(--radius-xl);
  padding: 32px;
  text-align: center;
  transition: border-color var(--duration-base) var(--ease-smooth);
}
.card--feature:hover { border-color: var(--color-emerald-500); }
```

#### Icon Wrapper (Shared)
```css
.icon-wrapper {
  width: 56px; height: 56px;
  border-radius: var(--radius-lg);
  background: rgba(16,185,129,0.1);
  border: 1px solid rgba(16,185,129,0.2);
  display: flex; align-items: center; justify-content: center;
  color: var(--color-emerald-500);
  transition: transform var(--duration-fast) var(--ease-snappy),
              background var(--duration-fast) var(--ease-snappy);
}
.card:hover .icon-wrapper { transform: scale(1.05); background: rgba(16,185,129,0.15); }
```

### 3.3 Forms

#### Input Field
```css
.form-input {
  width: 100%;
  padding: 12px 16px;
  background: var(--color-surface);
  border: 1px solid var(--color-border-subtle);
  border-radius: var(--radius-md);
  font: 400 1rem/1.5 var(--font-sans);
  color: var(--color-text-primary);
  transition: border-color var(--duration-fast) var(--ease-snappy),
              box-shadow var(--duration-fast) var(--ease-snappy);
}
.form-input::placeholder { color: var(--color-text-tertiary); }
.form-input:hover { border-color: var(--color-gray-300); } /* light */ / `var(--color-gray-600)` /* dark */
.form-input:focus { outline: none; border-color: var(--color-border-focus); box-shadow: var(--shadow-focus); }
.form-input:invalid:not(:placeholder-shown) { border-color: var(--color-error); }
```

#### Label
```css
.form-label {
  display: block;
  font: 500 0.75rem/1 var(--font-sans);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-text-secondary);
  margin-bottom: 8px;
}
```

#### Select
```css
.form-select {
  appearance: none;
  background-image: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2'><path d='M6 9l6 6 6-6'/></svg>");
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-size: 20px;
  padding-right: 44px;
}
```

### 3.4 Navigation

#### Desktop
- Height: 72px (scrolled) / 80px (top)
- Background: `rgba(29,29,31,0.8)` / `rgba(255,255,255,0.8)` + `backdrop-filter: saturate(180%) blur(20px)`
- Links: 1rem, weight 500, color inherits, hover → emerald
- CTA: Primary button, always visible

#### Mobile
- Hamburger button (24px touch target)
- Full-screen overlay panel (slide from right, 300ms)
- Links: 1.25rem, weight 500, generous tap targets (48px min)
- Phone CTA + Primary CTA stacked at bottom

### 3.5 Footer
- Background: `--color-black` (dark) / `--color-gray-50` (light)
- 4-column grid (Brand, Services, Company, Contact)
- Divider: `1px solid var(--color-border-subtle)`
- Copyright: Caption size, `--color-text-tertiary`

---

## 4. Voice & Copy Guidelines

### 4.1 Universal Rules
- **One idea per sentence.** Maximum 25 words.
- **Lead with benefit, follow with feature.**
- **Active voice.** "We install" not "Installation is provided."
- **Contractions welcome** (residential), sparing (commercial).
- **No exclamation marks** in commercial copy. Max 1 per page residential.
- **No jargon for jargon's sake.** Define or replace: "VLAN" → "separate secure networks."
- **Scannable structure:** H2 every 2-3 paragraphs, bullets for proof points.

### 4.2 Residential Voice (Warm, Approachable)

| Do | Don't |
|----|-------|
| "Dead zones? We'll fix that." | "Eliminate Wi-Fi coverage gaps." |
| "Your home theater, finally wire-free." | "Concealed cabling solutions for AV." |
| "We explain every option in plain English." | "Transparent consultation methodology." |
| "Vince answers the phone." | "Direct technician dispatch." |

**Tone markers:** "You," "your home," "peace of mind," "neighbors," "hassle-free," "done right."

### 4.3 Commercial Voice (Professional, Authoritative)

| Do | Don't |
|----|-------|
| "Infrastructure that scales with your business." | "Scalable IT infrastructure solutions." |
| "99.9% uptime. Contractual SLAs." | "We keep your systems running." |
| "Compliance-ready cabling and access control." | "We do structured cabling and door access." |
| "Dedicated account management." | "You'll have a point of contact." |

**Tone markers:** "Outcomes," "uptime," "compliance," "SLAs," "infrastructure," "deployment," "partnership."

### 4.4 Before/After Examples

| Context | Before (Generic) | After (SmartByteKC) |
|---------|------------------|---------------------|
| **Hero Residential** | "Best IT services in KC for homes and businesses." | "Dead zones? Buffering? We'll fix that. Smart home tech installed and explained — right here in Kansas City." |
| **Hero Commercial** | "Professional IT consulting and network services." | "Infrastructure that grows with you. Managed IT, security, and cabling for KC businesses — backed by SLAs." |
| **Service Description** | "We provide network security services including firewalls and monitoring." | "Sleep better knowing your network is monitored 24/7. We design, install, and watch over commercial-grade security — so you don't have to." |
| **CTA** | "Contact us today!" | "Talk to Vince. Get a straight answer." (Residential) / "Request a proposal. See the plan." (Commercial) |

---

## 5. Page Anatomy & Content Structure

### 5.1 Home
| Section | Purpose | Key Elements |
|---------|---------|--------------|
| **Hero** | Value prop in ≤8 words | Headline, subheadline, dual CTA (Residential/Commercial paths) |
| **Trust Bar** | Immediate credibility | License/insured, KC metro, 5★ reviews, response time |
| **Three Pillars** | Segment entry points | Residential / Commercial / Support — card links |
| **Featured Services** | Top 3 services | Bento cards → detail modals |
| **Why Us** | Differentiation | 3 value props with icons |
| **Social Proof** | Trust | 3 testimonials (named, specific), Google Reviews widget |
| **Footer CTA** | Final conversion | "Talk to Vince" + phone |

### 5.2 Services (Category Index → Detail Modals)
| Category | Services |
|----------|----------|
| **Network & Security** | Mesh Wi-Fi 6E/7, Cat6/6A cabling, 4K IP cameras/NVR, UniFi access control, rack cleanup |
| **Audio & Video** | Concealed TV mounts, home theater, multi-room audio, outdoor AV, commercial signage |
| **Tech Support** | On-site audits, smart home hub setup, device troubleshooting, data migration/backup |
| **Commercial** | Office drops/server racks, guest Wi-Fi/VLANs, door access, POS wiring, managed IT |

**Modal Pattern:** Problem → Solution → Proof (3 bullets) → CTA. No separate URLs.

### 5.3 Residential (Landing)
- Lead: "Peace of mind for your connected home."
- Sections: Smart Home, Networking, Security, Audio/Video, Support Plans
- Each: Pain point → Solution → "What it looks like" (photo) → CTA
- Support Plans: Tier cards (Essential / Pro / Premier) with monthly pricing

### 5.4 Commercial (Landing)
- Lead: "Infrastructure that grows with you."
- Sections: Managed IT, Cybersecurity, Cloud & Backup, Compliance, VoIP, Cabling
- Each: Outcome → Capability → Proof metric → CTA
- Case Study: One featured project (anonymized) with results

### 5.5 About
- Founder story (Vince) — 2 paragraphs, photo
- Team: 3-4 headshots, names, roles, one-line specialties
- Values: 3 cards (Explain, Engineer, Local)
- Certifications: UniFi, CompTIA, Low Voltage license, Insurance badges
- Timeline: Founded → Milestones → Today

### 5.6 Contact / Quote
- **Progressive disclosure form:**
  1. Path selector: "I'm a homeowner" / "I represent a business"
  2. Residential path: Name, Phone, Email, Service dropdown, Details
  3. Commercial path: Company, Name, Phone, Email, Project scope, Timeline, Budget range
- Honeypot field, client-side validation
- Submit → Google Forms (via Netlify Function proxy)
- Success: Inline thank-you + "Vince will call within 2 hours" + direct phone link

---

## 6. Do / Don't Visual Checklist

### ✅ Do
- [ ] Generous whitespace — 96px+ section spacing
- [ ] Thin headline weights (300-400), tight line-height (1.05-1.10)
- [ ] Single accent color (emerald) — ONLY for interactive elements
- [ ] System font stack, self-hosted WOFF2 subsets
- [ ] Semantic HTML5: header, main, section, article, footer, nav
- [ ] Logical heading order (h1 → h2 → h3, never skip)
- [ ] Focus visible on ALL interactive elements
- [ ] Color contrast ≥4.5:1 (text), ≥3:1 (UI elements)
- [ ] Alt text on every image (descriptive, not keyword-stuffed)
- [ ] `prefers-reduced-motion` respected globally
- [ ] Critical CSS inlined, non-critical lazy-loaded
- [ ] Images: WebP/AVIF, srcset/sizes, lazy loading, hero fetchpriority
- [ ] Netlify `_headers`: immutable assets 1yr, HTML no-cache
- [ ] Form works without JS (native submit), JS enhances only

### ❌ Don't
- [ ] No gradients on backgrounds (solid color fields only)
- [ ] No stock illustrations or generic "tech" imagery
- [ ] No pill-radius on rectangular cards (max 16px)
- [ ] No utility-first frameworks (Tailwind, etc.) — write the CSS
- [ ] No external CDN for runtime (fonts, icons, scripts local)
- [ ] No auto-play video, no parallax, no infinite loops
- [ ] No centered body copy (left-aligned only)
- [ ] No weight 800/900 anywhere
- [ ] No positive letter-spacing on headlines
- [ ] No borders on cards (use background contrast + subtle shadow)
- [ ] No more than 2 font weights per page (300/400 or 400/500/600)
- [ ] No decorative icons without purpose
- [ ] No fake metrics or placeholder testimonials

---

## 7. Implementation Checklist (Netlify)

### Build Config (`netlify.toml`)
```toml
[build]
  publish = "site"
  command = "" # Static site — no build step

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/*"
  [headers.values]
    Cache-Control = "public, max-age=0, must-revalidate"
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Permissions-Policy = "camera=(), microphone=(), geolocation=()"

[[redirects]]
  from = "/services/*"
  to = "/services.html"
  status = 200

[[redirects]]
  from = "/residential/*"
  to = "/residential.html"
  status = 200

[[redirects]]
  from = "/commercial/*"
  to = "/commercial.html"
  status = 200
```

### Performance Budget
| Asset | Target (gz) |
|-------|-------------|
| HTML (per page) | ≤8 KB |
| CSS (total) | ≤15 KB |
| JS (total) | ≤10 KB |
| Hero Image | ≤100 KB |
| Card Images | ≤50 KB |
| Fonts (subset) | ≤30 KB |
| **Total Page Weight** | **≤250 KB** |

### Core Web Vitals Targets
- **LCP:** <2.5s (3G)
- **CLS:** <0.1
- **TBT:** <200ms
- **INP:** <200ms

---

## 8. Accessibility Commitment (WCAG 2.1 AA)

- **Semantic landmarks:** banner, main, navigation, contentinfo, region[aria-label]
- **Skip link:** First focusable element → main content
- **Focus order:** Logical, visible, never trapped
- **Color:** Never sole conveyor of meaning
- **Text resize:** 200% zoom without horizontal scroll
- **Language:** `lang="en"` on html, `lang` on any foreign phrases
- **Forms:** Labels associated, errors announced, autocomplete attributes
- **Images:** `alt=""` for decorative, descriptive for content
- **ARIA:** Only where native HTML insufficient (modal, tabs, live regions)
- **Testing:** axe-core, keyboard-only, screen reader (NVDA/VoiceOver)

---

## 9. Reserved: Future Extensions

- **Dark Mode Toggle:** System preference default, manual override persisted in localStorage
- **Multi-language:** Spanish (KC metro) — `hreflang`, translated copy
- **Component Library:** Storybook documentation for internal reuse
- **Design Tokens:** Figma sync via Tokens Studio plugin

---

*End of Brand Style Guide v2.0*
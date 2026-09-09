# Product

## Register

brand

## Users

Three visitors, in order of value:

1. **A Kenyan business owner or founder** evaluating whether to hire Ian for an AI copilot or
   platform build (Equation consultancy, KES 400K–800K engagements). Arrives from LinkedIn or a
   referral, on a phone, in daylight, between meetings. Needs to decide in under a minute whether
   this person can be trusted with money flows, customer data and a real product. Job to be done:
   "prove you have shipped real things I can check."
2. **A hiring manager or tech lead** (Kenya, remote-first EU/US) screening a senior full-stack
   candidate. Skims work, stack, and career history; wants a CV and evidence, not adjectives.
3. **A developer reader of Dev Genus** (10k+ reads on Medium) who wants the person behind the
   essays: what he builds, how he thinks, where to follow.

## Product Purpose

A single-page static portfolio at ianodad.github.io/IanAderaPortfolio (GitHub Pages) for Ian
Odhiambo Adera, Senior Full Stack Developer, Nairobi. It exists to convert a skeptical visitor into
one of three actions: email Ian, download the CV, or read Dev Genus. Success means a visitor can
verify every claim on the page with one click (live product, repo, article, PDF) and leaves with a
clear picture of what Ian ships: money-safe M-Pesa systems, retrieval systems that cite their
sources, agentic pipelines, and cinematic scroll sites.

## Brand Personality

Plain-English senior engineer. Direct, evidence-first, quietly witty. Three words:
**load-bearing, deadpan, verifiable.** Emotional goal for the visitor: confidence, then
curiosity ("how was this made?"). Nairobi is native context, not a theme: M-Pesa, KES, East
African B2B are spoken about the way a local speaks about them.

Ian's own rule for claims: label evidence, inference and speculation; never let a guess wear the
costume of fact. The site should practice that rule visibly.

## Anti-references

- **The current live site** (React-in-one-file, Tailwind CDN): dark navy glow, gradient text
  on the name, typed.js "I am a Technical Writer|", magnetic cursor, particle trail,
  glassmorphism cards, section names like "Tech Arsenal", "Career Logs", "2026 Frontiers".
  The exact look a visitor would call "AI made that."
- **Terminal-native dark mode** (green-black ground, phosphor amber, mono everywhere). Already
  tried in the 2026-08 gauntlet build; it is the second-order developer-portfolio reflex.
- **Editorial-typographic** (italic display serif, mono labels, ruled columns, no imagery).
- Identical icon-heading-text card grids; hero-metric stat rows; skill progress bars;
  "Available for hire" pulsing green dots; generic centered stack hero.
- Fabricated anything: fake testimonials, fake metrics, fake UI screenshots, stock "developer
  at laptop" photos.

## Design Principles

1. **Practice what you preach.** Every claim on the page links to something checkable. The
   verification mechanic is the design, not a footnote.
2. **Show the product, not the adjective.** Real screenshots of real live sites, real dates,
   real links. Where there is no proof, say less. (Test counts are welcome only when Ian
   supplies a number from a repo; none are on the page today.)
3. **Built in daylight.** The site is read on phones in bright equatorial light by busy people.
   Light theme, high contrast, fast, no gimmick that needs a mouse.
4. **One decisive voice per fold.** Long scroll, one idea per section, deliberate pacing.
   Sections may differ in treatment; the voice never does.
5. **Deadpan over hype.** Humor comes from stating real facts flatly ("0 wallet funds lost.
   Ever."), never from exclamation marks or emoji.

## Accessibility & Inclusion

- WCAG 2.2 AA minimum: text contrast ≥ 4.5:1, focus-visible on every interactive element,
  semantic landmarks and headings, keyboard-complete navigation.
- `prefers-reduced-motion` respected: all scroll and entrance motion collapses to static.
- Works without JavaScript for all content (JS only enhances).
- Mobile-first: 390px wide must look intentional, no horizontal scroll; tap targets ≥ 44px.
- Low-bandwidth friendly for Kenyan mobile data: images compressed, lazy-loaded below the fold,
  no heavy runtime (no React/Babel in the browser).

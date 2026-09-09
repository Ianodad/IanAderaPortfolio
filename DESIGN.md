# Design System: Ian Adera Portfolio ("Receipts")

## Concept

Every claim comes with its receipt. The page is laid out like a paper trail from Nairobi
commerce: a till slip, an M-Pesa confirmation, a stamped gazette notice. Light paper, dark ink,
one oxide-red accent that stamps the parts you can verify. No glass, no glow, no gradients.

Scene sentence: a founder on a phone, on a Westlands cafe terrace at 3pm in bright equatorial
daylight, deciding in 40 seconds whether this developer can be trusted with a money flow.
Bright ambient light forces a light theme.

Color strategy: **Committed**. Oxide red carries the hero band and the closing band (roughly
35% of the scroll) and every "verify" mark in between. Body sections sit on warm paper.

Named references: Klim Type Foundry's single-color drench energy (translated from orange to
murram red); Swiss road-signage grids for the ruled layout; the M-Pesa confirmation SMS for the
shape of the microcopy (fact, amount, reference, timestamp).

Aesthetic lane rejected on purpose: glass-dark-gradient (the old site), terminal-native dark
(the 2026-08 gauntlet build), editorial italic serif.

## Color (OKLCH, tokens)

| Token | Value | Role |
|---|---|---|
| `--paper` | `oklch(0.965 0.012 78)` | Page ground. Warm, never pure white. |
| `--paper-2` | `oklch(0.935 0.016 78)` | Alternate section ground, table stripes. |
| `--ink` | `oklch(0.23 0.018 60)` | Body text and headings. Never `#000`. |
| `--ink-2` | `oklch(0.45 0.02 60)` | Secondary text, dates, stack lines. |
| `--rule` | `oklch(0.23 0.018 60 / 0.16)` | Hairline rules for the visible grid. |
| `--oxide` | `oklch(0.53 0.165 38)` | The accent. Hero and contact band ground, index numbers, large link text. |
| `--oxide-deep` | `oklch(0.44 0.145 38)` | Hover and pressed state of oxide elements; ALL oxide-colored text under 20px on paper. |
| `--oxide-tint` | `oklch(0.92 0.04 45)` | Faint wash for status chips and image mats. |
| `--on-oxide` | `oklch(0.975 0.012 78)` | Text on oxide ground. |
| `--on-oxide-dim` | `oklch(0.93 0.03 70)` | Secondary text on oxide ground. Solid, not translucent. Lightness measured at build time with `scripts/check-contrast.py`: `0.90` computed to 4.21:1 on oxide, below the 4.5:1 floor for its actual (sub-24px) use, so it was raised to `0.93`, which measures 4.62:1. |

Contrast is measured, not assumed: the build must run a WCAG contrast check (a short Python
script is fine) for every text/ground pair actually used and record the numbers in the build
report. Hard floors: 4.5:1 for any text under 24px, 3:1 at or above 24px bold. If a pair fails,
adjust lightness of the token, not the copy. The review estimated on-oxide on the original oxide
at ≈4.6:1 and the translucent dim at ≈3.1:1, which is why both were changed above.

Dark mode: none. The scene forces light. `color-scheme: light` declared.

## Typography

One family, chosen for its width axis: **Archivo** (variable, Google Fonts, `wdth` 62–125,
`wght` 100–900). Condensed heavy cuts for display and section titles (poster / road-sign
energy, as in the approved Mock A), normal width for body, narrow medium cuts for labels and
receipt lines. No monospace anywhere on the page; that is a deliberate refusal of the
"developer = mono" costume.

Receipt block (hero and contact): four rows of narrow uppercase text with dotted leaders
(`LOCATION ........ NAIROBI, EAT UTC+3`). Build the leader with a flex row and a
`border-bottom: 2px dotted var(--rule)` spacer element, not with typed periods.

Load: `https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&display=swap`
with `<link rel="preconnect">` to both Google font hosts. Fallback stack:
`"Archivo", "Helvetica Neue", Arial, sans-serif`.

| Role | Size | Width | Weight | Notes |
|---|---|---|---|---|
| Display (hero name) | sized to fill the container width, roughly `clamp(4rem, 17.5vw, 17rem)` | 62–70 (condensed) | 800 | Line-height 0.85, letter-spacing -0.01em, uppercase. Set as one line on ≥ 640px; two lines ("IAN" / "ADERA") below that. |
| H2 (section) | `clamp(2.25rem, 5vw, 4.5rem)` | 70 | 800 | Line-height 0.95, letter-spacing -0.01em. Condensed, matching the display. |
| H3 (project name) | `clamp(1.5rem, 2.6vw, 2.25rem)` | 100 | 700 | Line-height 1.05. |
| Body | `1.0625rem` (17px) | 100 | 400 | Line-height 1.55, measure 60–68ch. |
| Lead | `clamp(1.25rem, 2vw, 1.5rem)` | 100 | 400 | Line-height 1.35. |
| Label / eyebrow | `0.75rem` | 75 | 600 | Uppercase, letter-spacing 0.12em. |
| Receipt line | `0.9375rem` | 62 | 500 | `font-variant-numeric: tabular-nums`. Used for stack lists, dates, URLs. |
| Index number | `clamp(3rem, 6vw, 5.5rem)` | 62 | 300 | Oxide. Sits beside each project. |

Scale ratio between steps ≥ 1.3. Light text on oxide gets line-height +0.05.

## Layout

- Container: `max-width: 1320px`, side padding `clamp(1.25rem, 4vw, 3.5rem)`.
- Grid: 12 columns on ≥ 900px, 6 on tablet, 1 on phone. Column rules are drawn with hairlines
  (`--rule`) on the outer container edges and between major sections, so the grid is visible,
  like a printed form.
- Vertical rhythm on a 8px base; section padding `clamp(4rem, 10vw, 9rem)` top and bottom.
  Tight groupings inside (project meta rows at 8–12px), generous separation between projects
  (`clamp(3rem, 7vw, 6rem)`).
- Hero is LEFT-aligned. Never a centered stack.
- Project entries alternate 7/5 and 5/7 column splits at ≥ 900px only. Between 640px and 899px
  the Work section is single column (text above image), same as phone but with the phone's
  full-bleed image replaced by a container-width image. Never a card. The screenshot sits in a
  1px `--rule` frame with a 2px `--oxide-tint` mat, no shadow.
- Bleed mechanics at ≥ 900px: the image column uses a negative outer margin
  (`margin-inline-end: calc(-1 * (100vw - 100%) / 2)` on the right side, mirrored on the left,
  computed against the container) so the image passes over the container hairline and stops at
  the viewport edge. The container hairlines stay fixed; the image crosses them. Guard against
  horizontal scroll with `overflow-x: clip` on the section.
- Career and Writing are ledger tables: date column narrow (wdth 62), company/role wide, one
  line of description. Row rules only, no vertical lines, no zebra background on desktop.
- Phone (< 640px): single column, images full-bleed, each project's index number shrinks to
  2.5rem and sits above that project's H3. Ledger tables collapse to stacked rows with a fixed
  anatomy, every time: eyebrow (date, narrow uppercase) → heading (company, then role) → body
  (description) → receipt line (tech). Row rules stay.
- Print: oxide bands become paper with a 2px oxide top rule; images print at container width;
  every external link prints its URL after the text (`a[href^="http"]::after`); no motion.

## Components

- **Verify link**: text link, oxide, underline 1.5px offset 0.18em; on hover the underline
  thickens to 3px and the arrow glyph "↗" shifts 2px up-right. Every project, article, role
  with a public artifact carries one. Label pattern: `Live ↗ anasa-heights.vercel.app`.
- **Status chip**: narrow uppercase label in `--oxide-tint` ground with `--oxide-deep` text,
  no radius beyond 2px. Values: LIVE, PRIVATE BETA, IN DEVELOPMENT, UNREACHABLE (only if a
  link fails a check the day it is built).
- **Stamp**: a rotated (-6deg) 1.5px outline block with two lines of narrow uppercase text,
  used ONCE, in the hero ("NAIROBI · EAT UTC+3 / OPEN TO REMOTE"), in `--on-oxide` on the oxide
  ground. Contact gets a receipt block instead (see BRIEF §8), not a second stamp.
- **Buttons**: only two on the page (Email, CV PDF). Rectangular, 2px radius, 48px tall,
  oxide fill with on-oxide text on paper; on oxide ground they invert (paper fill, oxide text).
- **Nav**: static top bar, not sticky, not glass. Name left, four text links, CV link right.
  On phone the links wrap into a second row; no hamburger.
- **Focus**: 2px solid oxide outline with 3px offset on every interactive element.

## Motion

- Page load: hero name and lead fade up 16px over 700ms, `cubic-bezier(0.22, 1, 0.36, 1)`,
  staggered 80ms. Nothing else animates on load.
- Scroll: project screenshots reveal with a `clip-path: inset(0 0 100% 0)` to `inset(0)` wipe
  over 900ms when 20% visible. Ledger rows fade in with a 40ms stagger.
- Hover: link underline growth (120ms), image `scale(1.015)` (400ms), nothing bounces.
- `prefers-reduced-motion: reduce` removes every transition and shows final states.
- No smooth-scroll library, no GSAP, no cursor effects, no parallax.

## Imagery

Real screenshots of the live projects, captured 2026-09-09 at 1440×900, exported as WebP with
JPEG fallback at 1600w and 800w. Alt text describes the product ("ANASA Heights hero: a
scroll-scrubbed aerial flight over Westlands toward a 34-floor tower"), not "screenshot".
Projects with no live URL get no image; the entry is typographic. No stock photography, no
portrait unless Ian supplies one.

## Voice and copy

Plain-English senior engineer. Deadpan. No exclamation marks, no emoji, no em dashes. Section
titles are nouns or flat statements ("Work", "Career", "Writing", "Stack", "Contact"). Facts
carry their dates. Where there is no proof, the copy says less.

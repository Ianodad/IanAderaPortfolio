# Build Review: "Receipts" portfolio

Reviewer: independent, read-only. Sources read in order: DESIGN.md, .planning/BRIEF.md,
.planning/CONTENT.md, .planning/EXEC-SPEC.md, index.html, assets/css/style.css, assets/js/main.js,
scripts/check-links.sh, scripts/check-contrast.py, .planning/BUILD-REPORT.md, every PNG/JPG in
.planning/shots/new/, .planning/mocks/mock-A-small.jpg, ~/.claude/skills/impeccable/SKILL.md,
~/.claude/skills/impeccable/reference/brand.md. `check-contrast.py` and `check-links.sh` were both
re-run independently (not just read) and reproduced the build report's numbers exactly. The
screenshots were also pixel-scanned and, where a defect was suspected, cross-checked against a
fresh, independently-driven browser load (Playwright, `http.server` on 8913) rather than trusted
on sight.

---

## A. Fact audit

Method: every visible sentence in `index.html` was traced to `.planning/CONTENT.md` or
`BRIEF.md` §8. `Description:` fields in CONTENT.md were extracted programmatically (28 of them)
and diffed against the corresponding `.work-desc` / `.ledger-body` text; every en/em dash in
CONTENT.md was also grep'd (`\x{2013}`, `\x{2014}`) so nothing could be missed by eye.

- **index.html:165 — BLOCK.** Chipukizi description reads "Nursery school site for ages **1 to
  6** in Nairobi." CONTENT.md:160 has "ages **1–6**" (en dash, U+2013). The allowed transform is
  em dash (U+2014) → comma/period; an en-dash number range silently became the words "to". No
  fact changed (same age range), but per the letter of the audit rule this is not verbatim and
  not the licensed transform. Trivial one-word fix: revert to "ages 1–6" or, if en dashes are
  themselves unwanted in body copy, "ages 1 through 6" is closer to a defensible substitution
  than swallowing the dash into "to" without flagging it as a divergence (BUILD-REPORT.md does
  not mention this change at all).
- **index.html:145,167 — FIX, not BLOCK (field label, not narrative copy).** "Vanilla JS" appears
  for both Nairobi Iconic Buildings and Chipukizi; CONTENT.md:152,161 both say "Vanilla-JS"
  (hyphenated). Same pattern at index.html:189 ("Next.js 16, React 19, Astra DB" vs
  CONTENT.md:170 "Next.js-16, React-19, Astra-DB"). This is a tech-stack label, not a sentence,
  so I'm not tagging it BLOCK, but it is a consistent, unflagged departure from verbatim source
  text across three entries. Reasonable normalization (nobody writes "Next.js-16" outside that
  markdown table) but should have been logged as a divergence.
- **index.html:266-269, throughout Career/Writing — NIT.** Dates are reformatted consistently
  ("Sept 2024 - Present" → "Sept 2024 to present", "July 2022 - Dec 2022" → "Jul 2022 to Dec
  2022"). Structured data, not narrative sentences, no fact changed, applied uniformly. Not
  blocking, but also unflagged in BUILD-REPORT.md.
- **index.html:267-269 — NIT.** "Endeavor Streaming — Remote" (CONTENT.md:89, em dash) was split:
  company = "Endeavor Streaming", role = "Senior Frontend Developer, Remote". Restructuring of a
  field, not a fabricated fact. Fine.
- **Every other sentence checked** (hero lead, hero role line, receipt blocks ×2, stamp, about
  strip, Work/Pipeline/Writing intros, all 8 project descriptions with em dashes present in
  source, all 6 Career descriptions, all 6 essay descriptions, Stack rows, contact heading,
  footer, meta description, title) **traces verbatim to CONTENT.md or BRIEF §8**, with only the
  licensed em-dash → comma substitution applied where CONTENT.md had one (confirmed at
  index.html:99,121,143,209,229,238,346,367 among others).
- **URL audit — PASS.** All 19 external hrefs (5 live project links, DiraAi, GitHub ×2, LinkedIn,
  Medium ×7, Archivo stylesheet, 2 preconnect origins) match CONTENT.md/BRIEF §8 character-for-
  character. Independently re-ran `scripts/check-links.sh index.html`: identical output to
  BUILD-REPORT.md (9× 200, 6× 403 Medium bot-block, 1× 000 DiraAi, 2× 404 on bare preconnect
  origins with no path — expected, the actual font stylesheet 200s). `og:image` at index.html:12
  uses an absolute URL (`https://ianodad.github.io/IanAderaPortfolio/img/nairobi-1600.jpg`); README.md
  confirms this is the real Pages URL, not fabricated.

## B. Ban audit

Grepped across index.html, style.css, main.js for every banned pattern: gradients,
backdrop-filter, background-clip, `#000`/`#fff`, monospace, `border-left`/`border-right` as accent,
em dash (U+2014), emoji, exclamation marks, Inter/reflex-reject fonts, icon fonts, CDN scripts,
React/Tailwind runtime remnants.

- **Zero hits, all categories — PASS.** No gradient, no backdrop-filter, no background-clip:text,
  no `#000`/`#fff` literal, no monospace font-family, no oversized border-left/right accents, no
  U+2014 anywhere in the shipped files, no emoji, no exclamation marks in copy (only false-positive
  match was `<!DOCTYPE html>`), no Inter (the only "inter"/"mono" grep hits were substrings inside
  "Monochrome" and "IntersectionObserver" — false positives, verified by reading context), no
  `fa-`/Font Awesome, no CDN `<script src>` tags, no React/Tailwind/Babel/Typed.js runtime code
  (the only "React"/"Tailwind" occurrences are tech-stack facts inside copy, e.g. index.html:382).
- **Font check against impeccable's reflex-reject list — PASS.** Archivo is not on the list
  (Fraunces, Newsreader, Lora, Crimson*, Playfair, Cormorant*, Syne, IBM Plex*, Space Mono, Space
  Grotesk, Inter, DM Sans/Serif*, Outfit, Plus Jakarta Sans, Instrument Sans/Serif).
- **Aesthetic-lane check — PASS.** The page is not in the "editorial-typographic" reflex-reject
  lane (display serif + italic + mono labels + monochromatic restraint) — it uses a condensed
  heavy sans, no serif, no italic, no mono, and a drenched oxide color rather than monochrome
  restraint.
- **assets/css/style.css:513 — NIT.** `.work-media { padding: 3px; }` vs DESIGN.md:88's "a 2px
  `--oxide-tint` mat." One pixel off from the literal spec; visually immaterial.

## C. Mock and brief match

Compared .planning/shots/new/1440x900-viewport.png and 1920x1080-viewport.png directly against
.planning/mocks/mock-A-small.jpg.

- **Hero — PASS.** Left-aligned, oxide band, condensed full-width heavy uppercase "IAN ADERA"
  (measured ≈96% of the content box at 1440, matching BUILD-REPORT.md's ≈97% claim), lead
  bottom-left, receipt block bottom-right with dotted leaders, one rotated stamp far right. Matches
  BRIEF §11's instruction to carry Mock A's hero silhouette but swap in Mock B's four-row
  dotted-leader receipt block (LOCATION/STATUS/CLAIMS/ADJECTIVES) instead of Mock A's rejected
  "SOURCE VERIFICATION ENABLED" lines — that substitution was made correctly.
- **Work alternation and bleed — PASS.** Verified against .planning/shots/new/slice-1..4.jpg
  (1440, full page): entries alternate 7/5 (NKOLONG image right, ANASA left, Nairobi right,
  Chipukizi left, Vector11 right) and the image genuinely crosses the container hairline to the
  viewport edge on the outer side in every case — this matches BUILD-REPORT.md's claim of a
  measured 1439px/1px edge at 1440 and my own visual read of the slices confirms it.
- **Ledgers as real tables at desktop — PASS.** Career and Writing render as genuine 4-column
  grids at ≥900px (date / heading / body / tech), not the mobile stacked anatomy stretched wide.
  This exceeds DESIGN.md's letter (DESIGN.md only specifies the phone collapse) but is a
  reasonable, documented (BUILD-REPORT.md item 3) filling of a real gap, and it is what "real
  tables at desktop" in this review's own instructions asks for.
- **index.html:212 — FIX (documented divergence, worth a second look).** DiraAi's verify link
  reads "Try ↗ app.diralaw.com" instead of the "Live ↗ host" pattern DESIGN.md:107 specifies for
  every entry. BUILD-REPORT.md explains the reasoning (avoiding "Live" next to an "UNREACHABLE"
  chip) and EXEC-SPEC explicitly invited judgment calls on this exact entry. I agree with the
  reasoning; flagging only so it gets Ian's explicit sign-off since it is a departure from a
  named component spec, not just missing an image.
- Nothing from Mock A/B was missing that the brief called out as required (single stamp used
  once, index numbers present, container-edge hairlines visible in every screenshot).

## D. Responsive

- **390×844, 820×1180 viewport screenshots — PASS.** No overflow, no clipping, no awkward wraps.
  Hero name wraps to two lines ("IAN"/"ADERA") below 640px as specified, stays one line and fills
  the container at 820/1440/1920 without touching the edges. Nav wraps to a second (then third,
  for "CV (PDF)") row on phone with no hamburger, as specified. Tablet (820) work entries are
  single-column with index beside the heading, matching the 640–899px CSS rule.
- **index.html Work images at 03/04/05 on the phone full-page capture, and 05 on the 1440
  full-page capture — FIX, verified NOT a production bug.** Pixel-scanned
  `.planning/shots/new/1440-fullpage.png` and `390-fullpage.png` for the `--oxide-tint` mat color
  with no image on top: found a confirmed 370px solid block at y=3730–4100 in the 1440 capture
  (Vector11, entry 05) and three confirmed blocks in the 390 capture (entries 03, 04, 05 — NKOLONG
  and ANASA render fine). I re-served the site locally and drove it with an independent Playwright
  session: `img.complete` was `true` for all five `.work-media img` elements immediately after
  `page.goto()` with no manual scroll, and a fresh full-page screenshot rendered every image
  correctly, including Vector11. **Conclusion: the underlying HTML/CSS/image assets are correct;
  the blank boxes in the delivered screenshots are a capture-timing artifact** (the original
  screenshot tool captured before native `loading="lazy"` fired on images below the fold), not a
  site defect. This is still worth a FIX: (1) the delivered evidence in `.planning/shots/new/` is
  currently misleading — 3 of 5 phone Work images and 1 of 5 desktop Work images show as blank
  peach rectangles, which is exactly the pattern impeccable's brand.md calls out by name
  ("colored blocks where a hero photo belongs" — reference/brand.md line 80/103); (2)
  BUILD-REPORT.md's mandatory critique-and-fix pass ("look at every screenshot") did not catch or
  mention this, which is a process miss even though the shipped code is fine; (3) it is a real,
  if narrow, risk on a slow connection or a hard fling-scroll on mobile where native lazy-load
  could still lag visibly. Recommend re-capturing the screenshots with a forced scroll-through (or
  `waitForLoadState('networkidle')` after scrolling) before they're used as the shipped proof.
- **320px and 2560px, reasoned from CSS (not screenshotted, per instructions) — PASS.** At 320px,
  `--container-pad` clamps to its 1.25rem floor (20px), leaving ~278px content width; the phone
  hero-name clamp (`3.75rem, 21vw, 6.5rem`) tops out around 67px there, comfortably under that
  width for 5-character "ADERA" at 62% stretch. At 2560px, `--container-max: 1320px` and the hero
  name's `cqi`-based clamp both cap out well before that width, so the layout simply gains side
  margin rather than breaking. `overflow-x: clip` is set on `body` and `.work` as a backstop.

## E. Accessibility

- **Landmarks — PASS.** `<header>`, `<nav aria-label="Primary">`, `<main>`, `<section>` per topic
  with a heading, `<footer>`. `lang="en"` set.
- **Heading order — PASS.** h1 (hero) → h2 (Work) → h3 (each Work/Pipeline entry name) → h2
  (Career) → h2 (Writing) → h2 (Stack) → h2 (Contact). No level skipped. Career/Writing ledger
  rows correctly avoid making non-heading data (dates, tech) into headings.
- **Alt text — PASS.** All 5 image alts describe the product/scene, none say "screenshot" (e.g.
  index.html:110 "NKOLONG hero: an aerial view of the Maasai Mara at dawn, sun breaking through
  mist over acacia trees.").
- **Focus-visible — PASS.** style.css:195-202, `:focus-visible { outline: 2px solid var(--oxide);
  outline-offset: 3px; }`, inverted to `--on-oxide` inside `.oxide` sections. Matches DESIGN.md's
  Focus component exactly.
- **Reduced motion — PASS.** assets/js/main.js:8-11 checks `matchMedia('(prefers-reduced-motion:
  reduce)')` and returns before adding `.js-reveal`, so no hidden-state class is ever applied;
  style.css:845-858 is a belt-and-braces `!important` override for anyone who still gets the class
  some other way. Both paths verified structurally, not assumed.
- **Content visible with JS disabled — PASS.** Confirmed by reading, not assuming: every
  `[data-reveal]` hidden/clip-path rule in style.css is scoped under `.js-reveal [data-reveal=...]`
  (style.css:806-827), and `.js-reveal` is added to `<html>` only by main.js. With JS blocked,
  `<html>` never gets that class, so nothing in the default cascade hides content.
- **Ledger tables use `role="table"/"row"/"cell"` on divs (index.html:253-315, 327-371) rather
  than a literal `<table>` — NIT.** A valid, common accessible pattern given the responsive
  reflow requirement (stacked on phone, grid at desktop), not a violation, but a real `<table>`
  with CSS `display: grid` override on the same element would give the same behavior with less
  ARIA to keep in sync. Not blocking.
- **Tap targets — NIT.** style.css:233-241, nav links have no vertical padding beyond a 2px
  underline offset; effective hit height is close to line-height alone on phone before the
  1.25rem row gap is counted. Likely fine under the WCAG 2.2 spacing exception given the row gap,
  but not verified against a live pointer-target measurement.
- **Contrast — re-run, not just read.** Ran `python3 scripts/check-contrast.py` myself; output is
  byte-identical to BUILD-REPORT.md's table:

  | Pair | Ratio | Floor | Result |
  |---|---|---|---|
  | ink on paper (body text) | 15.29:1 | 4.5:1 | PASS |
  | ink on paper-2 (career body) | 13.98:1 | 4.5:1 | PASS |
  | ink-2 on paper (secondary/intro text) | 6.75:1 | 4.5:1 | PASS |
  | ink-2 on paper-2 (career receipt/eyebrow) | 6.17:1 | 4.5:1 | PASS |
  | oxide on paper (index numbers, ≥48px) | 5.15:1 | 3.0:1 | PASS |
  | oxide-deep on paper (verify links, body size) | 7.51:1 | 4.5:1 | PASS |
  | oxide-deep on paper-2 (ledger date labels) | 6.86:1 | 4.5:1 | PASS |
  | oxide-deep on oxide-tint (status chip) | 6.49:1 | 4.5:1 | PASS |
  | on-oxide on oxide (hero lead, contact heading, button text) | 5.30:1 | 4.5:1 | PASS |
  | on-oxide-dim on oxide (receipt labels, small) | 4.62:1 | 4.5:1 | PASS |
  | oxide-deep on paper (btn text) | 7.51:1 | 4.5:1 | PASS |

  Lowest ratio 4.62:1 (`on-oxide-dim` on `oxide`) clears the 4.5:1 floor by a thin but real margin.
  This required raising `--on-oxide-dim` from DESIGN.md:36's documented `0.90` lightness to `0.93`
  (style.css:20) — DESIGN.md itself pre-authorizes exactly this move ("If a pair fails, adjust
  lightness of the token, not the copy," DESIGN.md:41). Not a violation; DESIGN.md's own token
  table is now one line stale and should be updated to `0.93` to match what's shipped — **NIT**.

## F. Code quality

- **assets/css/style.css:271-284 — NIT.** `.hero-name` is declared as two separate rule blocks
  with `.hero-name .line` sandwiched between them. Cosmetic; merge for clarity.
- **assets/css/style.css:182-184 — NIT.** `.body-copy { max-width: 62ch; }` is defined but never
  referenced by any class attribute in index.html. Dead CSS.
- **assets/css/style.css:1016-1025 — NIT.** The 640–899.98px tablet-only query re-declares
  `.work-index { font-size: 2.5rem; }`, identical to the unconditional base rule at line 433-439.
  No-op; harmless but confusing to a future editor who might think it's meaningfully overriding
  something.
- **assets/css/style.css:513 — NIT.** See B above (3px vs DESIGN.md's 2px mat).
- **Images — PASS.** All 5 `<img>` tags carry explicit `width="1600" height="1000"` (no CLS risk),
  `<picture>` + `srcset`/`sizes` for webp-with-jpg-fallback at 800/1600w, `loading="lazy"` only on
  images confirmed below the fold at every tested viewport (see D).
- **Preconnect — PASS.** `<link rel="preconnect">` present for both `fonts.googleapis.com` and
  `fonts.gstatic.com` (index.html:13-14), matching DESIGN.md's Load instruction exactly.
- **No layout-shift risks found** beyond the already-discussed image dimensions: fonts load via
  `display=swap` (a FOUT trade-off DESIGN.md itself specifies, not a bug), no injected DOM beyond
  reveal classes which only change opacity/transform/clip-path, never layout-affecting properties
  (motion ban compliance, also satisfies impeccable's "don't animate layout properties" rule).
- **check-links.sh / check-contrast.py — PASS.** Both scripts are small, dependency-free, and do
  what they claim; independently re-run with identical output to BUILD-REPORT.md (see A and E).

## G. AI-slop test

Judged from the screenshots only (1440, 1920, 820, 390, plus the two full-page captures).

- **Does not read as "AI made that."** No glassmorphism, no purple/cyan gradient, no
  centered-hero-with-three-icon-cards template, no Inter, no generic rounded-corner stat tiles.
  The page commits hard to one aesthetic move (oxide drench + condensed Archivo + M-Pesa-style
  receipt microcopy) and holds it through six very different section shapes (drenched hero, ruled
  strip, alternating bleed-image list, real ledger tables, spec rows, drenched contact) without
  repeating the same block pattern anywhere. That variety plus commitment is the opposite of the
  templated look impeccable's brand.md warns about.
- **What would give it away, if anything:** the blank oxide-tint rectangles in the delivered
  full-page screenshots (see D) — to a designer skimming the screenshots cold, a solid-color block
  where a photo belongs reads as "unfinished AI output," which is precisely the failure mode
  brand.md names. It is not actually an AI-slop tell (it's a QA capture artifact, confirmed above),
  but it is the one thing in the delivered evidence that would make someone say "something's off
  here" at a glance.
- **What feels most hand-made:** the rotated stamp (a genuinely fussy, specific, non-generic
  detail), the asymmetric image bleed crossing the container hairline on alternating sides, and
  the real ledger/spec tables standing in for the "card grid of stats" cliché the old site used.
  These are decisions with a point of view, not defaults.

---

## Verdict: CHANGES REQUIRED

One item meets this review's own BLOCK bar (a non-verbatim copy change in the fact audit); severity
is low and the fix is a one-line revert. Everything else is FIX/NIT — the underlying page is strong,
matches the mock and brief closely, and the one alarming-looking defect (broken Work images in the
screenshots) was investigated and disproved as a live bug. Recommend a quick cleanup pass, then ship.

### Fix list, ordered by severity

1. **index.html:165 (BLOCK).** Restore verbatim age range from CONTENT.md:160 — change "ages 1 to
   6" back to "ages 1–6" (or another substitution that's actually licensed by the spec), and note
   the change in BUILD-REPORT.md's divergence log.
2. **Re-capture `.planning/shots/new/1440-fullpage.png` and `390-fullpage.png` (FIX).** Force a
   scroll-through (or wait on `networkidle` after scrolling) before capture so all `loading="lazy"`
   Work images are loaded first. The current files show 1 of 5 (desktop) and 3 of 5 (phone) Work
   images as blank oxide-tint boxes; confirmed via independent live re-test that the actual site
   renders all five correctly, but the delivered evidence currently says otherwise.
3. **index.html:145,167,189 (FIX).** "Vanilla JS" / "Next.js 16" / "React 19" / "Astra DB" drop
   the hyphens CONTENT.md uses ("Vanilla-JS", "Next.js-16", etc). Low-risk to leave as-is, but
   should be logged as an intentional divergence rather than silent.
4. **index.html:212 (FIX, sign-off item).** Confirm with Ian that "Try ↗" (vs. the spec's "Live ↗"
   pattern) for the DiraAi entry is the wanted treatment — reasoning is sound, but it's a named
   component-spec departure that BUILD-REPORT.md self-flagged and deserves an explicit yes.
5. **assets/css/style.css:513 (NIT).** `padding: 3px` → `2px` to match DESIGN.md's mat spec
   literally.
6. **DESIGN.md:36 (NIT, doc hygiene).** Update `--on-oxide-dim` from `0.90` to `0.93` to match the
   token actually shipped (style.css:20), which is the correct, contrast-verified value.
7. **assets/css/style.css:182-184, 271-284, 1016-1025 (NIT).** Remove dead `.body-copy`, merge the
   split `.hero-name` rule, drop the no-op tablet-only `.work-index` re-declaration.

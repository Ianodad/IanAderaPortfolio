# Build Report: "Receipts" portfolio rebuild

Status: **DONE**

Repo: `/Users/adera/My Work/projects/portfolio`, branch `redesign/verifiable`. Working tree left
uncommitted per spec, for the orchestrator to review and commit.

## Files written

- `index.html` (rewritten from scratch at repo root; the old React/Babel/Tailwind file is gone,
  not edited)
- `assets/css/style.css` (new, hand-written, no framework)
- `assets/js/main.js` (new, ~50 lines: IntersectionObserver reveal only)
- `scripts/check-links.sh` (new, executable)
- `scripts/check-contrast.py` (new, executable, no dependencies)
- `.planning/shots/new/390x844-viewport.png`, `820x1180-viewport.png`, `1440x900-viewport.png`,
  `1920x1080-viewport.png`, `390-fullpage.png`, `1440-fullpage.png`
- `.planning/BUILD-REPORT.md` (this file)

Deleted: `img/chipukizi.jpg`, `img/nairobi.jpg`, `img/vector11.jpg` (old unoptimized originals;
grep-confirmed nothing referenced them once the `-1600`/`-800` webp/jpg pairs were wired in).

Not touched: `PRODUCT.md`, `DESIGN.md`, `.planning/BRIEF.md`, `.planning/CONTENT.md`, mocks —
those showed as already modified/deleted in `git status` before this session started (from prior
orchestrator work) and were only read, never written, here.

## Link check (`scripts/check-links.sh index.html`)

```
200   https://anasa-heights.vercel.app
000   https://app.diralaw.com
200   https://chipukizi.vercel.app
404   https://fonts.googleapis.com
200   https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&display=swap
404   https://fonts.gstatic.com
200   https://github.com/Ianodad
200   https://github.com/Ianodad/IanAderaPortfolio
403   https://ianodad.medium.com/claude-code-for-real-devs-ea251e0379a1
403   https://ianodad.medium.com/claude-code-from-chatbot-to-system-c8cbb6f7324e
403   https://ianodad.medium.com/make-another-ai-try-to-kill-your-plan-before-you-execute-8524405d9ff8
403   https://ianodad.medium.com/make-claude-talk-straight-d828b2357d7f
403   https://ianodad.medium.com/stop-sending-every-task-to-opus-heres-what-to-use-instead-2498653e1fd4
403   https://ianodad.medium.com/stop-trying-to-make-claude-smarter-make-it-remember-3eda763521a2
200   https://linkedin.com/in/ian-odhiambo
403   https://medium.com/@ianodad
200   https://nairobi-iconic-buildings.vercel.app
200   https://nkolong.vercel.app
200   https://vector11.vercel.app
```

19 URLs checked. 9× 200 (all five live project links, both GitHub links, LinkedIn). 6× 403 (all
`medium.com` / `ianodad.medium.com` links — Medium bot-blocks curl; BRIEF §10 already treats this
as live and the page correctly does not gate this behind a "verify" mechanism). 1× 000
(`app.diralaw.com`, matches BRIEF §10's finding exactly — the DiraAi entry's chip reads
"UNREACHABLE 9 SEP 2026" for this reason). 2× 404 on the bare `fonts.googleapis.com` /
`fonts.gstatic.com` origins — these are the two `<link rel="preconnect">` hrefs, not real page
requests; curling a domain root with no path 404s while the actual font stylesheet (also
checked, 200) loads fine.

## Contrast check (`scripts/check-contrast.py`)

OKLCH → OKLab → linear sRGB → WCAG relative luminance, computed by hand (no color library),
against DESIGN.md's token values as actually used on the page.

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

**Lowest ratio: `on-oxide-dim` on `oxide` = 4.62:1** (receipt-block labels, hero and contact).

One token fix was required: DESIGN.md's `--on-oxide-dim: oklch(0.90 0.03 70)` measured 4.21:1 on
oxide, below the 4.5:1 floor for its actual use (13px receipt labels). Per DESIGN.md's own rule
("if a pair fails, adjust lightness of the token, not the copy"), lightness was raised to `0.93`,
giving 4.62:1 — verified with the script, not assumed. `--rule` and `--rule-on-oxide` (hairlines,
dotted leaders) are decorative, not text, so no WCAG text floor applies to them; they're listed
in the script output for reference only.

## Critique-and-fix notes from the browser loop

Three full critique-and-fix cycles were needed; two were real bugs, not polish.

1. **Clip-path made images permanently unrevealable (real bug, not a screenshot artifact).**
   First render: every Work screenshot and all 17 ledger/spec rows were invisible.
   Instrumenting `IntersectionObserver` directly showed `intersectionRatio: 0` for a `.work-media`
   element sitting dead-center in the viewport. Cause: the pre-reveal hidden state was
   `clip-path: inset(0 0 100% 0)` applied to the *same* element being observed — a zero-height
   clip region has no intersectable area, so the observer could never fire and the element could
   never un-hide itself. Fixed by moving the `data-reveal="scroll"` attribute (the observed,
   unclipped node) to the parent `<li class="work-entry">`, and driving the child `.work-media`'s
   clip-path off a `.is-visible` class on that ancestor instead. Also added an explicit
   `@media print` override (`opacity:1 !important`) so a recruiter printing or saving-as-PDF
   before scrolling never sees blank sections — the pre-fix version would have failed that
   silently since print rendering doesn't run scroll/intersection events either.
2. **Bleed images weren't reaching the viewport edge (real bug).** The 7/5 Work columns were
   built with flexbox and fixed `flex-basis` percentages. A negative `margin-inline-end` on the
   trailing flex item has no visual effect in flexbox — a flex item's own box is sized by its
   basis, not by its own trailing margin, so the "bleed" margin was computed correctly
   (confirmed via `getComputedStyle`, `-116px` at 1440) but did nothing. Switched the desktop
   Work row from flex to CSS Grid (`grid-template-columns: 7fr 5fr` / `5fr 7fr`); a stretched
   grid item's box is genuinely `(track size − margins)`, so the same negative margin now
   correctly grows the image past its column and off the viewport edge. Verified: at 1440px the
   bled image's right edge measured 1439px (viewport 1440) and the mirrored left-bleed measured
   1px from the left edge.
3. **Ledger tables (Career, Writing) were stacked at every width, wasting the right half of the
   page on desktop.** DESIGN.md's phone section says tables "collapse to stacked rows" — implying
   a genuine multi-column table above phone width, not the mobile anatomy everywhere. Added a
   `grid-template-columns: 8rem 13rem 1fr 13rem` table layout at ≥900px (date / heading /
   description / tech as real columns) and the same treatment for the Stack spec-sheet
   (`13rem 1fr` label/value). Below 900px both fall back to the original stacked anatomy.
4. **Hero name was under-filling the container** (~74% of content width at 1440) and the phone
   index-number position matched the tablet layout instead of DESIGN.md's explicit phone rule
   ("index sits above the H3" on phone, not beside it). Both fixed and re-verified: hero text now
   renders at ~97% of container width at 1440/1920 with zero horizontal scroll at any tested
   width; phone Work entries now stack index-above-H3 while tablet (640–899px) keeps index beside
   H3.

Also verified directly (not assumed): keyboard focus rings (2px, oxide on paper / on-oxide on
oxide, confirmed via `getComputedStyle` and screenshot), content stays fully visible with
`main.js` blocked (JS-disabled equivalent) and with `prefers-reduced-motion: reduce` emulated,
and no horizontal scroll at 390, 639, 640, 820, 900, 1440, or 1920px.

## Divergences from the spec (with reasoning)

- **Hero display clamp**: DESIGN.md's suggested `clamp(4rem, 17.5vw, 17rem)` was replaced with a
  CSS container-query-based size, `clamp(3rem, 26cqi, 20rem)`, on a `container-type: inline-size`
  wrapper. A `vw`-based clamp scales against the *viewport*, but the name needs to scale against
  the *container* (which stops growing past its 1320px max-width) — `cqi` does this natively and
  automatically caps at wide viewports without extra math. Two-line phone fallback
  (`clamp(3.75rem, 21vw, 6.5rem)`, `flex-direction:column`) kept as vw-based since it's not
  container-bound the same way.
- **DiraAi entry without an image**: rendered as a full-width typographic row (`grid-column: 1/-1`
  equivalent via `display:block` at desktop) rather than following the 5/7 alternation with an
  empty image slot. The verify link reads "Try ↗ app.diralaw.com" instead of the "Live ↗" pattern
  DESIGN.md specifies for every other entry — labeling a dead link "Live" next to an
  "UNREACHABLE" chip would be a direct self-contradiction on the one page whose entire premise is
  "every claim has a receipt."
- **Stack row label**: used CONTENT.md's own heading "Database & AI" rather than BRIEF §5's
  paraphrase "Data & AI", since CONTENT.md is the named source of truth for facts/labels and the
  two differ only cosmetically.
- **Work image bleed mechanic**: implemented as a `100vw`-anchored custom property rather than
  DESIGN.md's literal `100vw - 100%` string, because `100%` inside a nested grid item resolves to
  the column's width, not the outer container's — the literal formula does not evaluate to a
  usable bleed amount in a real nested layout. The `vw`-anchored version produces the same visual
  result (image passes the container hairline, stops at the viewport edge) reliably.
- **Ledger/spec-sheet desktop columns**: not explicitly speced for ≥900px (DESIGN.md only
  describes the phone collapse); added a real multi-column table there rather than leaving the
  phone anatomy in place at every width, per "spacing and alignment" in the required critique
  pass — see fix #3 above.

## Open flags

- `app.diralaw.com` is still unreachable as of this build (9 Sep 2026, curl exit 000, matches
  BRIEF §10). If Ian brings it back up, the DiraAi chip/copy/link label need a manual pass to
  flip back to "LIVE" / "Live ↗".
- Medium links return 403 to curl (bot-blocking, not broken) — expected and already documented in
  BRIEF §10; flagging again only so the orchestrator doesn't mistake the 403s in the link-check
  output for real failures.
- No favicon was added (out of scope per spec); browsers will 404 on `/favicon.ico` silently,
  console-visible only in devtools, no user-facing effect.

---

## Fix round 1

Applied per orchestrator/reviewer request (`.planning/reviews/build-review-sonnet.md`), in the
order specified. All seven items done.

1. **BLOCK, Work grid row placement.** Added `grid-row: 1;` to `.work-entry[data-side="right"]
   .work-copy-wrap`, `.work-entry[data-side="right"] .work-media`,
   `.work-entry[data-side="left"] .work-media`, and `.work-entry[data-side="left"] .work-copy-wrap`
   inside the `@media (min-width: 900px)` block in `assets/css/style.css`. Verified two ways: (a)
   `getBoundingClientRect()` on all five copy/media pairs at 1440px shows 213-276px of vertical
   overlap and correct left/right column positions for every entry, including 02 and 04; (b) a
   freshly re-captured, scrolled-through full-page screenshot at 1440 shows all five entries
   (01-05) with image and text side by side, image on the correct alternating side.
2. **FIX, reveal robustness.** `assets/js/main.js`: observer threshold lowered to `0.05`, added
   `rootMargin: "0px 0px -5% 0px"`, and added a 2500ms safety timer (started at script execution,
   which for a script tag placed at the end of `<body>` runs at effectively the same moment as
   `DOMContentLoaded`) that force-adds `is-visible` to any deferred element still hidden. Verified:
   re-captured both full-page screenshots after a stepped scroll-to-bottom-and-back; the four Work
   images and one Career/Writing row set that intermittently rendered blank in the pre-fix
   screenshots (Vector11 at 1440; Nairobi/Chipukizi/Vector11 at 390) now all show `naturalWidth >
   0` and `is-visible` before capture, and the resulting screenshots show real photos in every
   slot, no blank oxide-tint rectangles anywhere on either full-page capture.
3. **FIX, hero stamp duplicated the receipt block.** Stamp text changed from "Nairobi · EAT UTC+3
   / Open to remote" to "Links checked / 9 Sep 2026" — ties to the same 9 September 2026 check
   date already stated in the Work section intro ("Five answered when I checked on 9 September
   2026"), so it adds real, consistent information rather than repeating the receipt block's
   LOCATION/STATUS rows.
4. **FIX, hero lead measure.** `.lead` and `.hero-lead-col` widened to `44ch` at `>= 900px` (kept
   at `34ch` below that). Measured the name-to-lead gap directly with `getBoundingClientRect()`
   before touching padding: 64px, exactly the `.hero-lockup` margin-top token value, ~9.5% of the
   674px total hero height at 1440. Judged this is not a "large dead zone" needing a padding or
   min-height change — it is a small, deliberate rhythm gap, and widening the lead to 44ch already
   made the lead paragraph taller and denser (5 lines instead of 6 at 1440, 5 instead of 6 at
   1920), which visibly tightens the composition. Checked both the 1440 and 1920 hero captures
   after the change; both read as one cohesive block, closer to mock-A-small.jpg's density.
   Padding/min-height were left unchanged as a result — noting this judgment call rather than
   changing something that measurement didn't support.
5. **BLOCK, copy fidelity.** Chipukizi description now reads "ages 1&ndash;6" (en dash, `&ndash;`
   entity, U+2013) instead of "ages 1 to 6", matching CONTENT.md's en dash verbatim. Confirmed by
   reading the raw byte sequence in `index.html` and by reading the rendered `textContent` in the
   browser.
6. **NIT cleanup.**
   - Removed the dead `.body-copy` rule (confirmed zero references in `index.html` before
     deleting).
   - Merged the two split `.hero-name` rule blocks (previously separated by the unrelated
     `.hero-name .line` selector) into one declaration.
   - Removed the no-op `.work-index { font-size: 2.5rem; }` re-declaration inside the tablet-only
     `@media (min-width: 640px) and (max-width: 899.98px)` block — the base (unconditional)
     `.work-index` rule already sets `2.5rem` and nothing between it and that media query changes
     the value, so the tablet block's copy of it did nothing. The block's real rule
     (`.work-copy-wrap { display: flex; gap: 1.25rem; }`) stays.
   - `DESIGN.md`'s `--on-oxide-dim` token updated from the stale `oklch(0.90 0.03 70)` to the
     shipped `oklch(0.93 0.03 70)`, with a one-line note that the lightness was measured with
     `scripts/check-contrast.py` (0.90 -> 4.21:1, below the 4.5:1 floor for its actual use; raised
     to 0.93 -> 4.62:1).

   Left unchanged, as instructed: DiraAi's "Try ↗" wording, the un-hyphenated "Next.js 16" /
   "React 19" / "Astra DB" / "Vanilla JS" stack labels, and the 3px work-media mat padding.

7. **Re-capture and re-run.** All six screenshots in `.planning/shots/new/` overwritten. For both
   full-page captures, the page was scrolled to the bottom in 300-350px steps (not a single jump,
   which was confirmed in the original build pass to skip over sections and leave them
   unrevealed), held at the bottom for 1s, then returned to the top before the shot — this was
   verified each time by checking `is-visible` counts (17/17 rows, 5/5 images) and
   `img.naturalWidth > 0` (5/5) immediately before capture. `scripts/check-contrast.py` and
   `scripts/check-links.sh` were both re-run; output is byte-identical to the original build
   report (lowest contrast still 4.62:1; link check still 9x200 / 6x403 Medium / 1x000 DiraAi /
   2x404 bare preconnect origins).

### Files changed in this round

- `assets/css/style.css` (grid-row fix, lead max-width, dead-rule/merge/no-op cleanup)
- `assets/js/main.js` (threshold, rootMargin, safety timer)
- `index.html` (stamp copy, Chipukizi en dash)
- `DESIGN.md` (`--on-oxide-dim` value + measured note)
- `.planning/shots/new/390x844-viewport.png`, `390-fullpage.png`, `820x1180-viewport.png`,
  `1440x900-viewport.png`, `1440-fullpage.png`, `1920x1080-viewport.png` (all overwritten)
- `.planning/BUILD-REPORT.md` (this section)

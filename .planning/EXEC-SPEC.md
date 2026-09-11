# Executor spec: build the "Receipts" portfolio

Repo: `/Users/adera/My Work/projects/portfolio` (git branch `redesign/verifiable`, already checked out).
Deploy target: GitHub Pages from the repo root, so `index.html` must stay at the root.

## Read first, in this order

1. `PRODUCT.md` (who, why, principles, anti-references)
2. `DESIGN.md` (tokens, type, layout, components, motion; this is the visual contract)
3. `.planning/BRIEF.md` (section plan, exact copy, open questions, mock decision in §11)
4. `.planning/CONTENT.md` (the ONLY source of facts; copy verbatim, no new claims)
5. `.planning/mocks/mock-A-small.jpg` (approved hero composition) and `mock-B-small.jpg`
   (only its dotted-leader receipt block carries over)
6. `~/.claude/skills/impeccable/reference/typography.md`, `spatial-design.md`,
   `color-and-contrast.md`, `responsive-design.md`, and the reveal section of `motion-design.md`
7. `~/.claude/skills/impeccable/SKILL.md` "Absolute bans" and `reference/brand.md`
   "Brand bans": treat every item as a hard reject.

## Deliverables

- `index.html` (rewritten from scratch; the old React/Babel/Tailwind file is deleted content, not
  edited), `assets/css/style.css`, `assets/js/main.js` (tiny: IntersectionObserver reveal,
  nothing else). No framework, no CDN scripts, no Tailwind, no React, no icon font. The only
  external request is the Archivo font from Google Fonts.
- Images: use the prepared `img/<name>-1600.webp|jpg` and `-800` variants with `<picture>`,
  `srcset`, `loading="lazy"` below the fold, explicit `width`/`height`. Delete the old
  `img/chipukizi.jpg`, `img/nairobi.jpg`, `img/vector11.jpg` if nothing references them.
- `scripts/check-links.sh`: curls every external `href` in `index.html` and prints
  `status  url`. Run it once and paste the output in your report.
- A contrast check (Python, inline script is fine) for every text/ground pair used; paste the
  ratios in your report. Floors: 4.5:1 under 24px, 3:1 at ≥ 24px bold.
- Screenshots in `.planning/shots/new/` at 390×844, 820×1180, 1440×900, 1920×1080 (viewport)
  plus a full-page capture at 1440 and 390, taken with the Playwright MCP browser tools
  (`browser_resize`, `browser_navigate`, `browser_take_screenshot` with a relative filename;
  files land in the repo root or `.playwright-mcp/`, move them into `.planning/shots/new/`).
  Serve with `python3 -m http.server 8912 --bind 127.0.0.1` from the repo root; port 8911 is
  taken by the old site.
- `.planning/BUILD-REPORT.md`: done / diverged / blocked, file list, link-check output,
  contrast table, the critique-and-fix notes from your browser passes, open flags.

## Page structure (from BRIEF §5, with the review folds already applied)

1. Top bar: "IAN ADERA" left (condensed 800), links Work · Career · Writing · Contact, then
   "CV (PDF)" → `Ian_Odhiambo_Adera_FullStack_CV.pdf`. Static, not sticky, not glass.
2. Hero on `--oxide`: LEFT-aligned. Display name "IAN ADERA" condensed heavy uppercase, one
   line filling the container width at ≥ 640px (use a fluid clamp and verify in the browser
   that it neither wraps nor overflows at 640, 820, 1440, 1920), two lines below 640. Lead
   sentence bottom-left (BRIEF §8). Dotted-leader receipt block bottom-right (four rows, BRIEF
   §8). One rotated stamp at far right. A small line: "Britam, Senior Software Developer, Sept
   2024 to present."
3. About strip on paper: the single ruled line from BRIEF §8 (credentials), Medium phrase linked.
4. Work on paper: "Work" H2 + intro (BRIEF §8). Six entries, index 01–06, alternating 7/5 and
   5/7 at ≥ 900px with the image bleeding to the viewport edge (DESIGN.md bleed mechanics);
   single column 640–899; full-bleed image on phone. Order and status:
   01 NKOLONG (LIVE, img nkolong), 02 ANASA Heights (LIVE, img anasa), 03 Nairobi Iconic
   Buildings (LIVE, img nairobi), 04 Chipukizi (LIVE, img chipukizi), 05 Vector11 (LIVE, img
   vector11), 06 DiraAi (chip "UNREACHABLE 9 SEP 2026", no image; typographic entry with the
   link still present so a visitor can try). Each entry: index, H3 name, category eyebrow,
   description (CONTENT.md verbatim, em dashes replaced by commas or periods), receipt line
   with the stack, "Live ↗ host" verify link, status chip.
   Then "In the pipeline" sub-list: Operon (PRIVATE BETA), PesaWallet (IN DEVELOPMENT),
   descriptions verbatim, no links, intro from BRIEF §8.
5. Career on `--paper-2`: ledger table, six roles from CONTENT.md in the order given there,
   date column narrow, company + role, description verbatim, tech as receipt line.
6. Writing on paper: intro (BRIEF §8), "Dev Genus on Medium, 10k+ reads ↗" linked to
   `https://medium.com/@ianodad`, six essays as ledger rows (title linked, one-line description,
   month, tags as receipt line).
7. Stack on paper: five spec-sheet rows, items verbatim from CONTENT.md, comma separated. No
   icons, no bars.
8. Contact on `--oxide`: heading (BRIEF §8), Email button (`mailto:ianodad@gmail.com`), CV
   button, links GitHub `https://github.com/Ianodad`, LinkedIn
   `https://linkedin.com/in/ian-odhiambo`, Medium; contact receipt block (BRIEF §8). Footer:
   "© 2026 Ian Odhiambo Adera. Static HTML, no framework. View source ↗" linking to the repo.

Meta: `<title>Ian Adera, Senior Full Stack Developer, Nairobi</title>`, description from BRIEF
§8, `<meta name="color-scheme" content="light">`, Open Graph title/description, and
`og:image` pointing at `img/nairobi-1600.jpg` (a real project capture; no fabricated card).
`lang="en"`. Semantic landmarks: header, nav, main, section with headings, footer.

## Hard rules

- No em dashes anywhere in copy or code comments. No emoji. No exclamation marks.
- No `#000`, no `#fff`, no gradients, no `backdrop-filter`, no `background-clip: text`, no
  side-stripe borders, no cards with icon + heading + text, no monospace font, no Inter, no
  cursor effects, no smooth-scroll library, no parallax, no preloader, no progress bar.
- No new factual claims. If a sentence is not in CONTENT.md or BRIEF §8, do not write it.
- `prefers-reduced-motion` disables every transition and reveal.
- Content must be fully visible with JavaScript disabled (reveal classes default to visible;
  JS adds the hidden state, then reveals).
- No horizontal scroll at any width from 320px to 2560px.
- Keyboard: every link and button reachable, focus ring per DESIGN.md.

## Browser loop (required)

After the first full build, open the page at all four viewports, look at the screenshots, and
write yourself a short critique against: brief match, mock match (hero silhouette, receipt block,
index numbers, bleed, hairlines), the AI-slop test, DESIGN.md bans, spacing and alignment,
type overflow, image quality. Fix, re-shoot, repeat until nothing material remains. At least one
full critique-and-fix pass is mandatory. Put the critique notes in the build report.

## Dispute invitation

If anything in these documents is wrong, contradictory, or would produce a worse page, say so in
the report's "diverged" section and do the better thing, as long as it does not add a factual
claim or break a hard rule. Two things we already suspect you may want to change: the exact
display clamp for the name, and how the DiraAi entry looks without an image. Use your judgment
and record it.

## Commit

Do not commit. Leave the working tree for the orchestrator to review and commit.

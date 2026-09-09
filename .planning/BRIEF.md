# Design Brief: Ian Adera portfolio redesign ("Receipts")

Status: drafted by the orchestrator 2026-09-09 from PRODUCT.md, DESIGN.md, `.planning/CONTENT.md`
(verbatim content of the old site) and the 2026-08 gauntlet brief. Not yet confirmed by Ian; built
under the assumptions below so he can react to a real page rather than a document.

## 1. Feature summary

Replace the single-file React/Tailwind glassmorphism portfolio with a hand-built static page
(HTML + CSS + a little JS) that a skeptical Nairobi founder, a hiring manager, or a Dev Genus
reader can verify in one click. The page presents Ian's real shipped work with real screenshots,
his real career ledger, his real essays, and two ways to reach him. It must not read as
"AI made that."

## 2. Primary user action

Click a "Live ↗" link on a project and see that it is real. Secondary: email Ian or open the CV.

## 3. Design direction

- Color strategy: **Committed** (oxide red hero + contact band ≈ 35% of the scroll; paper body).
- Scene: founder on a phone, Westlands terrace, 3pm equatorial daylight, 40 seconds to decide.
  Light theme, no dark mode.
- Anchors: Klim-style single-color drench (in murram/oxide, not orange); Swiss road-sign grids
  drawn as visible hairlines; M-Pesa confirmation SMS as the microcopy shape (fact, reference,
  timestamp). Full token list in DESIGN.md.
- Type: Archivo variable only (wide display, narrow receipt lines). No mono. No serif.
- Visual probe: two north-star comps generated with Higgsfield (nano_banana_pro) after this
  brief; the winning composition is recorded in section 11.

## 4. Scope

Production-ready. Whole surface (one page, six sections). Shipped-quality static site; JS only
enhances (reveal on scroll, nothing else). Polish until it ships. Deploy target unchanged:
GitHub Pages from the repo root, so `index.html` stays at the root.

## 5. Layout strategy

Long scroll, one idea per fold, visible ruled grid.

1. **Top bar**: name, four links (Work, Career, Writing, Contact), "CV (PDF)". Static.
2. **Hero, oxide ground**: giant wide "IAN ADERA" across the full width; lead line beneath:
   "Senior full-stack developer in Nairobi. I build systems that move money and cite their
   sources." A receipt-style block: "Every claim on this page has a link you can check."
   One stamp: "NAIROBI · EAT UTC+3 / OPEN TO REMOTE". Small line: "Britam, Senior Software
   Developer, Sept 2024 to present."
3. **Work, paper ground**: six numbered entries, alternating 7/5 and 5/7, screenshot bleeding
   to the viewport edge. Order: 01 NKOLONG, 02 ANASA Heights, 03 Nairobi Iconic Buildings,
   04 Chipukizi, 05 Vector11, 06 DiraAi (no image, see open questions). Then a short ruled
   sub-list "In the pipeline": Operon (private beta), PesaWallet (in development). The four
   generic old entries (Cloud Cost Migration, Insurance Tech, CI/CD Automation, Hybrid Mobile
   App) are dropped; their facts already live in Career.
4. **Career, paper-2 ground**: ledger table of the six roles from CONTENT.md, verbatim
   descriptions, dates in the narrow column. Britam first.
5. **Writing, paper ground**: "Dev Genus on Medium, 10k+ reads" with a verify link to the
   Medium profile; six essays as ledger rows (title, one line, month, link).
6. **Stack, paper ground**: five spec-sheet rows (Frontend, Backend, DevOps, Data & AI, Tools),
   comma-separated items verbatim from CONTENT.md. No icons, no bars, no percentages.
7. **Contact, oxide ground**: "Let's build something you can verify." Email button, CV button,
   GitHub / LinkedIn / Medium links, second stamp. Footer line: "© 2026 Ian Odhiambo Adera.
   Static HTML, no framework. View source."

Removed on purpose: typed roles, magnetic cursor, particles, preloader, progress bar, blobs,
gradient text, glass cards, the About stat tiles (70% / 90% / 80% are not linkable), the
"2026 Frontiers" goals with progress percentages, dark-mode toggle.

## 6. Key states

- Default: everything visible without JS. Images lazy below the fold with width/height set.
- Reduced motion: no transitions.
- Link failure: if a live URL was unreachable on build day, the chip says UNREACHABLE with the
  date instead of LIVE; never claim live for something that did not answer.
- Long text: project descriptions are 2–3 sentences; the layout must hold at 390px with the
  longest one (NKOLONG).
- Narrow (390px), tablet (820px), desktop (1440px), wide (1920px) all intentional.
- Print: sane defaults (oxide bands become paper with a rule), since recruiters print.

## 7. Interaction model

Scroll and click. Hover thickens link underlines; images scale 1.5%. Keyboard reaches every
link and button with a visible oxide focus ring. No hover-only content. Anchors in the top bar
jump to sections with `scroll-margin-top`.

## 8. Content requirements

All copy from `.planning/CONTENT.md` verbatim unless listed here:

- Hero lead (new, revised after review): "Senior full-stack developer in Nairobi. Seven years
  of shipping: insurance platforms at Britam, AI research tools, and scroll-driven brand sites
  you can open right now." (Seven years = Jan 2019 to today, per the Career ledger.)
- Hero receipt block (new): four dotted-leader rows:
  `LOCATION ........ NAIROBI, EAT UTC+3` · `STATUS ........ OPEN TO REMOTE` ·
  `CLAIMS ON THIS PAGE ........ LINKED BELOW` · `ADJECTIVES ON FAITH ........ 0`
- One-line About (new, restores dropped credentials): a ruled strip between Hero and Work:
  "Full-stack since Jan 2019. Azure certified. Moringa School alumnus. Mentor, Google Africa
  Developer Scholarship. Writes Dev Genus on Medium (10k+ reads)." The Medium phrase links to
  the profile; nothing else in the strip has a public link, so it is stated plainly, not
  decorated.
- Section titles: Work · Career · Writing · Stack · Contact.
- Work intro (new, revised): "Six things I have shipped, in the order I would show a client.
  Five answered when I checked on 9 September 2026. One did not, and says so."
- Pipeline intro (new): "Not linkable yet, so listed, not claimed."
- Writing intro (new, revised): "Dev Genus on Medium: essays on Claude Code, prompting and
  model routing, written for working developers."
- Contact heading (new): "Let's build something you can verify."
- Contact receipt block (replaces the second stamp): `LAST UPDATED ........ 9 SEP 2026` ·
  `SOURCE ........ github.com/Ianodad/IanAderaPortfolio` · `FRAMEWORK ........ NONE` ·
  `RESPONSE TIME ........ SAME DAY, EAT`.
- Meta description (new, revised): "Ian Adera, senior full-stack developer in Nairobi.
  Insurance platforms at Britam, AI research and RAG tools, scroll-driven brand sites, and
  Dev Genus essays. Every live project links to the product."
- No em dashes anywhere (CONTENT.md has some inside project copy; replace with commas or
  periods without changing facts).

## 9. Recommended references (impeccable)

`reference/spatial-design.md`, `reference/typography.md`, `reference/color-and-contrast.md`,
`reference/responsive-design.md`, `reference/motion-design.md` (only the reveal section).

## 10. Open questions (resolved by assumption, flagged to Ian)

- **DiraAi link**: `https://app.diralaw.com` refused connections on 2026-09-09 from this
  network (curl exit 000). Assumption: keep the entry, mark it "UNREACHABLE 2026-09-09" rather
  than LIVE, no screenshot. Ian confirms the correct URL or the deploy state.
- **Medium profile** returns 403 to curl (bot block, normal). Treated as live.
- **Britam vs Endeavor overlap** (Sept 2024–present and Jul 2025–Jan 2026) is kept exactly as
  the old site states it.
- **Portrait photo**: none in the repo; none used.
- **"astar"** in Ian's request: read as "show me the design as an artifact". If he meant the
  Astro framework, the page is plain HTML and can be dropped into an Astro project unchanged.

## 11. Visual direction record

Two comps generated with Higgsfield nano_banana_pro on 2026-09-09 (2 credits each), saved in
`.planning/mocks/`:

- **Mock A, `mock-A-drenched-hero.png`: WINNER for hero composition.** Solid oxide hero band,
  giant condensed heavy uppercase "IAN ADERA" edge to edge, lead sentence bottom-left, receipt
  block bottom-right, one rotated stamp at the far right, then "Work" and the first project
  entry (01 / NKOLONG / description / stack line / Live link / screenshot bleeding right) on
  paper. Hairline rules at the container edges.
- **Mock B, `mock-B-paper-ledger.png`: contributes the receipt block only.** Its dotted-leader
  rows ("LOCATION ........ NAIROBI, EAT UTC+3", "STATUS ........ OPEN TO REMOTE",
  "CLAIMS ON THIS PAGE ........ ALL LINKED", "ADJECTIVES ON FAITH ........ 0") replace Mock A's
  vague "SOURCE VERIFICATION ENABLED" lines. Its full-page column grid is too busy; its
  "VERIFIED" stamp is a cliché and is cut.

Carry into code: the oxide hero band; the condensed full-width display name (Archivo at
wdth 62–70, wght 800, not the wide cut originally planned); the four-row dotted-leader receipt
block; the single rotated stamp; the "01" thin condensed oxide index; the screenshot bleeding to
the viewport edge inside a hairline frame; container-edge hairlines; the wide open spacing.

Do not literalize: the mocks' monospace receipt text (use Archivo narrow uppercase instead); the
mocks' invented project copy (all copy comes from CONTENT.md); the fake NKOLONG screenshot (use
the real capture in `img/nkolong-*.webp`); the drop shadows under the screenshot in Mock A (use a
hairline frame and a 2px oxide-tint mat, no shadow).

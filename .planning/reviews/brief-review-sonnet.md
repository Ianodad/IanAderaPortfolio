# Brief Review — Ian Adera Portfolio ("Receipts")

Reviewer: independent design/plan reviewer (read-only). Reviewed PRODUCT.md, DESIGN.md,
`.planning/BRIEF.md`, `.planning/CONTENT.md`, `impeccable` SKILL.md + `reference/brand.md`,
`old-hero.jpeg`, and the five project screenshots. All contrast ratios below were computed by
hand from the stated OKLCH values (OKLCH → OKLab → linear sRGB → WCAG relative luminance), not
copied from DESIGN.md's claims. Tags: BLOCK (must fix before build), FIX (should fix, concrete),
NIT (small, optional).

---

## A. AI-slop risk

**Verdict: no literal violation of the absolute bans, but one real second-order reflex risk.**

- **Absolute bans check** — side-stripe borders: not present (the screenshot frame is a full
  1px border on all sides + tint mat, not a colored left/right stripe). Gradient text: explicitly
  banned in the doc and nowhere in the spec. Glassmorphism: explicitly banned. Hero-metric
  template (big number + label + supporting stats + gradient accent): correctly identified and
  cut (the old About stat tiles). Identical card grids: Work section is explicitly "never a
  card"; Stack is spec-sheet rows with "no icons, no bars, no percentages." **All five bans are
  clear.** [FIX — verification only, no action needed if built as specified]
- **Reflex-reject lanes**: editorial-typographic is explicitly rejected, and the letter of that
  lane (italic display serif + mono labels + no imagery) is avoided — no serif, no mono, real
  bleeding screenshots. But the *spirit* of that lane — rule-separated columns, uppercase
  tracked eyebrows, an ordinal index number beside each entry, a visible hairline grid — is still
  fully present, just executed in a sans variable font instead of an italic serif. This is a
  **very common 2025-26 "elevated developer portfolio" template shape** (Awwwards/Cargo-style
  numbered project lists with Swiss hairlines are their own reflex now, independent of font
  choice). Swapping Fraunces-italic for wide-Archivo-caps escapes the letter of the ban but not
  necessarily the "how was this made?" test. [FIX] Recommend one genuinely surprising structural
  move that a template wouldn't have — e.g., the receipt-block/SMS-shape microcopy is the right
  instinct (keep it, push it further); the ordinal index numbers + ruled ledger tables are the
  generic half and could use one asymmetric break.
- **Reflex font**: Archivo is not on the reflex-reject list (Fraunces, Newsreader, Lora,
  Crimson*, Playfair, Cormorant*, Syne, IBM Plex*, Space Mono, Space Grotesk, Inter, DM Sans*,
  Outfit, Plus Jakarta Sans, Instrument*). Confirmed clean. [NIT — speculation, not evidence]
  Archivo's wide/narrow axis used exactly this way (wide display, narrow labels, no second
  family) is becoming its own "Swiss-tech-portfolio" tell in late-2025/2026 work, but I have no
  corpus to verify that, so I flag it as a hunch, not a rule violation.
- **Old site confirmed** (`old-hero.jpeg`): dark navy ground, cyan→purple→pink gradient on
  "ADERA," typed.js caret, centered stack hero — matches the anti-reference description exactly.
  Good baseline; the new direction is a real departure on every axis checked.

---

## B. Honesty (BRIEF §8 vs. CONTENT.md)

This is the most important section. **CONTENT.md is the only source of facts**, per the brief's
own framing, and Ian's stated rule is "never let a guess wear the costume of fact."

Every new sentence in §8, checked against CONTENT.md:

| New copy | Verifiable from CONTENT.md? | Verdict |
|---|---|---|
| "I build systems that move money and cite their sources" (hero lead) | **No.** No LIVE project moves money. PesaWallet is the only M-Pesa-adjacent project and it is "In development" (not live, no link) — and even its own description says it *reads* SMS for analytics, "nothing leaves the phone"; it does not move money. DiraAi is the only project that "cites its sources," and it is being marked UNREACHABLE, not live. | **BLOCK** |
| "Every claim on this page has a link you can check... No adjectives you have to take on faith" (hero receipt block) | Self-referential claim about the page, not a fact about Ian — fine on its own, **but it sits directly under the sentence above**, which the page cannot back with a link. The receipts theme is actively undermined by its own hero. | **BLOCK** (contradiction, not a new fact) |
| "Six things that are live right now, in the order I would show a client" (Work intro) | **No — contradicts §10.** The sixth entry, DiraAi, is resolved elsewhere in the same brief as UNREACHABLE, not live. Five are confirmed LIVE in CONTENT.md; the sixth is explicitly not. | **BLOCK** — internal inconsistency inside the brief itself |
| "Not linkable yet, so listed, not claimed" (Pipeline intro) | Yes — Operon and PesaWallet have no links in CONTENT.md. | OK |
| "Dev Genus: technical-but-accessible essays for African developers" (Writing intro) | **Partially.** CONTENT.md's six essay descriptions are about Claude Code, prompting, and model routing — general developer/AI topics, not Africa-specific. "For African developers" is audience framing pulled from PRODUCT.md's Users section, not from anything in the essays themselves. | **FIX** — soften to something the essays actually demonstrate, or drop the audience qualifier |
| "Let's build something you can verify" (Contact heading) | Thematic, not factual. Fine. | OK |
| Meta description: "Money-safe M-Pesa systems, retrieval that cites its sources, agentic pipelines, cinematic scroll sites" | **No**, same problem as the hero lead, worse — "money-safe" is a stronger claim than "moves money," and it appears in the `<meta description>`, i.e., in search results and link previews, the one piece of copy furthest from any on-page receipt. This phrase originates in PRODUCT.md, not BRIEF.md, but the review standard is CONTENT.md-verifiability, and it fails that regardless of which document introduced it. | **BLOCK** |

**Secondary honesty note**: BRIEF §5 states the four dropped generic project entries' "facts
already live in Career." Mostly true, with two gaps: "CI/CD Automation" cites GitHub Actions,
which appears nowhere in the Career ledger (only Jenkins does); "Hybrid Mobile App" cites Flutter
alongside React Native, but Career only documents React Native (YLabs) — Flutter never appears in
a Career row, only in the Skills list. Neither is embarrassing on its own, but the brief's
justification for the cut is slightly overstated. [NIT]

**Bottom line**: the concept ("every claim has a receipt") makes any unverifiable claim more
damaging than it would be on a normal portfolio, because it invites the reader to test the
promise. Right now the single most prominent sentence on the page (hero lead) and the meta
description both fail that test on day one. This needs a rewrite before build, not after.

---

## C. Contrast and accessibility

Computed OKLCH → linear sRGB → WCAG relative luminance by hand for every token pair DESIGN.md
makes a claim about, plus one it doesn't.

| Pair | DESIGN.md claims | Computed | Verdict |
|---|---|---|---|
| `--ink` on `--paper` | ≈12:1 | **≈15.3:1** | Understated if anything. Fine. |
| `--oxide` on `--paper` | ≈4.6:1 | **≈4.5:1** | Matches, but this is a razor-thin margin over the 4.5:1 AA minimum for normal text — one anti-aliasing or color-management difference between browsers could tip it under. DESIGN.md already hedges with "use oxide-deep for small text," which is the right call — make that a hard rule, not a suggestion, for anything under ~16px medium. [FIX] |
| `--on-oxide` on `--oxide` | ≈5.2:1 | **≈4.6–4.7:1** | **DESIGN.md's number is optimistic by ~10%.** Still clears 4.5:1, but with far less margin than the doc implies — this is the color carrying ~35% of the page (hero + contact bands) and any body-sized copy in it is close to the failure line. [FIX] Recompute with a real contrast tool before build; if under 4.5:1 in practice, lighten `--on-oxide` or darken `--oxide` slightly. |
| `--on-oxide-dim` (72% opacity) on `--oxide` | *not stated* | **≈3.1:1** | **Fails the stated 4.5:1 AA minimum outright**, and only barely clears the 3:1 large-text minimum with no margin. This token is specced for "secondary text on oxide ground" — if that includes anything body-sized (hero secondary line, contact secondary text), it violates PRODUCT.md's own hard requirement ("WCAG 2.2 AA minimum: text contrast ≥ 4.5:1"). | **BLOCK** |
| `--oxide-deep` text on `--oxide-tint` (status chip) | *not stated* | **≈6.0:1** | Solid, no issue. |
| `--ink-2` on `--paper` | *not stated* | **≈6.7:1** | Solid, no issue. |

**Recommended fix for `--on-oxide-dim`**: either (a) restrict it to genuinely large/bold text only
(≥24px or ≥18.66px bold, where 3:1 is the real AA floor) and say so explicitly in DESIGN.md, or
(b) raise it to ~85-88% opacity (or bump its lightness) so it clears 4.5:1 and is safe for any use.
Given how easy it is to reach for "secondary text" reflexively at body size, I'd pick (b).

---

## D. Buildability — ambiguous enough for two builds to diverge

1. **Hero text alignment.** Never specified as left or centered. The old site's hero (confirmed
   in `old-hero.jpeg`) is fully centered, and PRODUCT.md's own anti-reference list explicitly
   bans "generic centered stack hero." Without an explicit call, a builder defaults to the
   familiar centered layout and silently recreates the banned pattern. **Resolution: state
   left-aligned explicitly** (consistent with the Swiss-grid, non-centered ethos used everywhere
   else in the doc). [BLOCK]
2. **7/5 alternation at the 820px tablet breakpoint.** DESIGN.md's grid is defined as 12 columns
   at ≥900px, 6 columns on tablet, 1 on phone — but the alternating 7/5 / 5/7 split is a 12-column
   construct. Section 6 explicitly calls 820px an "intentional" test width, yet there is no
   defined Work-section behavior between 640px (phone, single column) and 900px (desktop,
   12-col). Two builders will do different things here (symmetric 3/3, early single-column,
   or a broken fractional split). **Resolution: specify the 820px behavior explicitly** — most
   likely "single column until 900px" is simplest and consistent with the phone spec. [BLOCK]
3. **"Screenshot bleeds to the viewport edge on its side"** inside a `max-width: 1320px`
   container that also carries the visible hairline grid. Not specified how the image breaks out
   of the container (negative margin? `100vw` breakout wrapper?) or whether the container's
   hairline rule breaks with it or stays put and the image bleeds past it. This changes the whole
   feel of the Work section depending on the answer. [FIX] Recommend a named breakout technique
   in DESIGN.md (e.g., a `.bleed` utility using `width:100vw; margin-inline: calc(50% - 50vw)`)
   and an explicit statement that the container hairline stays fixed while the image passes
   through it.
4. **"Index numbers shrink to 2.5rem and sit above the name"** (DESIGN.md, mobile layout rule).
   Ambiguous whose "name" — reads adjacent to hero typography rules but is almost certainly about
   each *project's* H3, not Ian's hero name (which has no index number). As written, a builder
   could misapply it to the hero. [NIT] Rewrite as "...sit above each project's H3."
5. **Ledger table mobile collapse.** "Tables collapse to stacked rows with the date as an
   eyebrow" doesn't say what happens to the description paragraph, the tech line, or multi-role
   entries with very different text lengths (Britam's paragraph vs. Dev Genius's one-liner).
   [FIX] Specify the stacked-row anatomy: eyebrow (date) → H (company + role) → body
   (description) → tech line, in that order, every time.
6. **UNREACHABLE status — one-time snapshot or repeatable check?** The chip states "only if a
   link fails a check the day it is built," but there's no described mechanism (script, manual
   process, cadence) for re-verifying LIVE claims after launch. A project marked LIVE today that
   goes down in three months silently breaks the site's central promise. [FIX] At minimum,
   document this as a manual task Ian repeats before any future edit; ideally, a tiny link-check
   script that's part of the build/deploy step.
7. **Print stylesheet** — "sane defaults (oxide bands become paper with a rule)" is a one-line
   intent, not a spec. What happens to bleeding images, to the "Live ↗" links (URLs should
   probably print as visible text via `a[href]:after{content:" ("attr(href)")"}`), to motion
   artifacts. [NIT] Worth two or three concrete print rules rather than a one-liner, since the
   brief itself notes recruiters print.

---

## E. Mobile at 390px

- **Hero display type.** `clamp(3.25rem, 13vw, 12rem)` — at 390px, 13vw ≈ 50.7px, close to the
  3.25rem (52px) floor. "IAN ADERA" at ~52px, uppercase, weight 800, wide axis (125), could plausibly
  overflow or wrap awkwardly at exactly 390px depending on real glyph widths. [FIX] Confirm the
  actual rendered width at 390px before build and decide explicitly whether "IAN" and "ADERA"
  wrap to two lines (and if so, that this is an intentional, tested look, not an accident).
- **7/5 split at 820px** — covered in D2, also a mobile/responsive-strategy gap, not just a
  desktop nicety, since 820px is one of the four explicitly "intentional" widths.
- **Ledger table collapse** — covered in D5.
- **Full-bleed images on phone** — consistent and low-risk as specified; single column removes
  the breakout ambiguity from D3 on mobile specifically (it only matters at tablet/desktop).
- **NKOLONG longest description** at 390px inside a single-column phone layout with a full-bleed
  image above/below it should be fine typographically (body text wraps normally); no specific
  risk found here beyond the general em-dash cleanup already flagged correctly in §8.

---

## F. The "Receipts" concept — structure vs. costume

**Verdict: mostly structure, with one costume element.**

- **Core mechanic** (every claim links to proof) is a real structural choice — it determines what
  content exists (drop unlinkable stat tiles), how it's labeled (LIVE / UNREACHABLE / PRIVATE
  BETA chips), and what the copy is allowed to say. That's design-as-structure, not decoration.
  Keep it. Its biggest current risk isn't the concept, it's the execution gap flagged in §B.
- **M-Pesa confirmation SMS as microcopy shape** (fact, amount, reference, timestamp) is genuinely
  well-chosen: specific to Nairobi commerce (not a generic "developer" reference), and it maps
  onto a real typographic role (`Receipt line`, tabular nums) used for dates/stack/URLs
  throughout. Keep, and lean on it harder — it's the most distinctive idea in the brief.
- **Till-slip receipt block** (the hero's "Every claim on this page has a link you can check"
  block) is a reasonable structural extension of the same idea. Keep, contingent on §B's fix.
- **The rubber stamp** (rotated -6°, used twice) is the one place costume outweighs structure.
  A rotated "approved/verified" stamp is a well-worn motif on maker/indie-hacker landing pages —
  it signals "authentic paper artifact" without actually verifying anything (it's not a link, it
  carries no checkable information). DESIGN.md's own "never more than twice per page" reads like
  the author already senses the risk. [FIX] Cut the second stamp (contact) or replace it with
  something that carries new, checkable information the hero stamp doesn't (e.g., last-updated
  date, or a repo/commit reference — "View source" is already planned for the footer, which is a
  better receipts-consistent instinct than a second decorative stamp).
- **Color commitment (~35% of scroll)** is a rough estimate, not measured. With Work as the
  longest, most content-heavy section (six numbered entries plus a pipeline sub-list) sitting on
  paper ground, the real oxide percentage after build could land meaningfully under 30%, which
  would silently downgrade "Committed" to "Restrained" without anyone deciding that. [NIT] Worth
  a post-build check, not a pre-build blocker.

---

## G. What's missing that a hiring manager or Kenyan founder would expect

- **Credentials silently dropped, with no relocation.** CONTENT.md's About section carries three
  checkable facts — "7 years of experience," Azure Certified, and Moringa School (bootcamp
  credential) — plus the mentorship note (Google Africa Developer Scholarship program). BRIEF §5's
  six-section plan (Hero/Work/Career/Writing/Stack/Contact) has no About section and never
  relocates these facts anywhere else. This is different from the stat-tile cut (70%/90%/80%),
  which was correctly justified as "not linkable" — a certification and a school name *are*
  checkable/nameable facts and fit the Receipts theme better than most of what's kept. Dropping
  them isn't wrong, but nothing in the brief explains the decision the way it explains the stat
  tiles. [BLOCK] Recommend a compact line (Career ledger header or Contact) carrying: years of
  experience (recompute from the earliest Career date — Jan 2019 to build date, not a frozen "7
  years" copied verbatim, since that number is now stale), Azure certification, Moringa School.
- **PRODUCT.md promises "real test counts" as an evidence type** (Design Principle 2: "real
  screenshots of real live sites, real test counts, real dates") but **BRIEF's content plan
  contains zero test counts anywhere.** CONTENT.md doesn't supply one either (ANASA Heights lists
  Playwright in its stack, implying tests exist, but no count is given). Either this principle is
  aspirational and should be softened in PRODUCT.md, or Ian has a real number to supply before
  build. [FIX] Flag to Ian directly rather than silently dropping a stated principle.
- **GitHub activity is a link, not evidence.** The GitHub link is present, but nothing on the page
  itself demonstrates activity (contribution graph, pinned repos, commit cadence) the way the
  screenshots demonstrate shipped products. Low priority since a visitor can click through, but
  worth naming as a missed reinforcement of "receipts." [NIT]
- **Portrait photo** — already flagged and resolved as an open question in BRIEF §10 ("none in
  repo; none used"). I'd underline it rather than re-raise it: a Kenyan founder deciding in 40
  seconds whether to trust someone with a money flow (the brief's own scene sentence) is exactly
  the visitor most likely to want a face. This is a real trade-off, not obviously wrong — flagging
  again only so Ian consciously confirms it rather than it being resolved by silence. [NIT]

---

## Top 5 changes to make before building

1. **Fix the hero lead + meta description.** "I build systems that move money" / "money-safe
   M-Pesa systems" is not backed by any live, linkable project — PesaWallet (the only candidate)
   is in development and only reads SMS locally; it doesn't move money. Rewrite to claims the
   page can actually prove today.
2. **Fix the internal contradiction**: "Six things that are live right now" (§8) vs. DiraAi being
   marked UNREACHABLE (§10) in the same document. Pick one true number.
3. **Fix accessibility**: `on-oxide-dim` on oxide computes to ≈3.1:1, below the stated 4.5:1 AA
   floor. `on-oxide` on oxide itself is ≈4.6-4.7:1, not the ≈5.2:1 DESIGN.md claims — recheck with
   a real tool and tighten before build.
4. **Resolve three buildability gaps**: hero text alignment (must be explicit left-align, or risk
   recreating the banned centered hero), Work-section layout at the 820px tablet breakpoint
   (currently undefined), and the mechanics of the image bleed-to-viewport-edge inside a
   max-width container.
5. **Restore verifiable credentials** (years of experience, Azure certification, Moringa School)
   that vanished when About was cut, with no relocation — unlike the stat-tile cut, this one
   isn't justified by "not linkable," since certifications are exactly the kind of checkable fact
   the Receipts concept is built to showcase.

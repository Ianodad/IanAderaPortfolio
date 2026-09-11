# Ian Adera, Senior Full Stack Developer, Nairobi

Personal portfolio, a single static page.

## Live

https://ianodad.github.io/IanAderaPortfolio/

## How it is built

Static index.html, assets/css/style.css, and assets/js/main.js (reveal-on-scroll only; all content is visible without JavaScript). Archivo variable font from Google Fonts. Real screenshots of live projects in img/ as WebP with JPEG fallback. No framework, no build step, no CDN JavaScript.

## Design notes

Light warm paper background with one oxide red accent. Every claim on the page links to something checkable. The design context lives in PRODUCT.md, DESIGN.md, and .planning/BRIEF.md.

## Featured Work

Recent builds, all live. These are linked from the Work section of the portfolio.

| Project | What it is | Stack | Live |
|---------|-----------|-------|------|
| **NKOLONG** | Dawn-to-dusk safari film scrubbed by scroll | Higgsfield, Seedance 2.0, GPT-Image-2, React, GSAP, Lenis | [nkolong.vercel.app](https://nkolong.vercel.app) |
| **Vector11** | Monochrome football intelligence chat, RAG over football news and stats | Next.js 16, React 19, Astra DB, LangChain, OpenAI | [vector11.vercel.app](https://vector11.vercel.app) |
| **DiraAi** | AI legal research for Kenya, every claim links back to the actual Act or judgment it came from, verifiable in one click. LangGraph agent over a Chroma vector index and a Neo4j citation graph. | Next.js, TypeScript, FastAPI, LangGraph, Postgres, Neo4j | URL unreachable as of 2026-09-09 |
| **ANASA Heights** | Scroll-scrubbed flight film for a 34-floor Westlands residential tower. Video seeks frame-by-frame with scroll position. | Higgsfield, Seedance 2.0, GSAP, Lenis, TypeScript | [anasa-heights.vercel.app](https://anasa-heights.vercel.app) |
| **Nairobi Iconic Buildings** | Scroll to fly through a folded-paper Nairobi, ten landmark towers in one continuous camera flight, stitched from six AI-generated video legs. | Higgsfield, Seedance 2.0, GPT-Image-2, ffmpeg, vanilla JS | [nairobi-iconic-buildings.vercel.app](https://nairobi-iconic-buildings.vercel.app) |
| **Chipukizi** | Nursery school site for ages 1–6 in Nairobi, a hand-drawn character tracks the cursor across the hero, with smooth scroll through the day, classes and admissions. | Vite, GSAP, Lenis, vanilla JS | [chipukizi.vercel.app](https://chipukizi.vercel.app) |

## Checks

```bash
scripts/check-links.sh index.html
scripts/check-contrast.py
```

## Local preview

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## License

Open-source. Feel free to explore, clone, and modify for personal or educational purposes.

© 2026 Ian Odhiambo Adera

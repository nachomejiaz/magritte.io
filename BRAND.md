# MAGRITTE.IO
## Brand & Build Specification — v2.0

> **PRIME DIRECTIVE**
> A reading environment, not a designed object.
> Black ground, one serif, enormous space, hairlines where structure is genuinely needed.
> The reader should notice the writing and nothing else — and only later realise
> how precisely everything around it was placed.
>
> **There is no logo, no symbol, no mark.** The name, set in type, is the identity.

---

## 0. WHAT CHANGED FROM v1, AND WHY

v1 built a surveillance-dossier interface: an emblem, HUD panels, corner registration marks, fake telemetry (`INTEGRITY 64%`, `STATE: UNSTABLE`), dithered plates, wireframe motifs, a live background canvas, terminal decode effects, fake OS windows. That is a costume. It performs "neo-futurist" instead of being precise, and it competes with the prose it exists to serve.

**All of it is removed.** What survives is the part that was actually Ive: one material, one accent used almost never, absolute alignment, and space. The neo-futurist quality now comes from *restraint and precision* — tabular numerals, exact hairlines, a mono used only where numbers appear — not from ornament.

**Deleted and not to be reintroduced:** logo/emblem/mark of any kind · corner ticks and registration marks · background canvas or animated field · film grain, scanlines, misregistration · dithered or duotone imagery · wireframe motifs (tunnels, meshes, globes, vortices) · text decode/scramble effects · fake OS windows and system dialogs · invented metadata (integrity scores, mental state, threat level, location) · multi-accent hue cycling · custom cursors · uppercase tracked-mono labels used as decoration.

---

## 1. CONCEPT

`magritte.io` is a web-based novel — essays, short stories, journal entries, fragments — written as a neo-surrealist response to machine intelligence and the commoditization of the self.

The design argument is **refusal**. The subject is a person being flattened into a record, so the site refuses to decorate, refuses to score, refuses to recommend, refuses to count. It offers a page, a measure, and silence. The restraint *is* the position.

Two registers exist, and the second is nearly silent:

- **The writing.** Serif, sentence case, one column, generous. This is 95% of what is on screen.
- **The apparatus.** An index number, a date, a read time, a link. Small, dimmed, mono where it is numeric. It never announces itself.

The Magritte inheritance is the *title*, not a visual gimmick. Do not build captions that contradict images. Do not put `Ceci n'est pas…` in the interface. If the author uses that device, it happens in the prose, where it belongs.

---

## 2. VOICE

Interface copy is plain, lowercase or sentence case, and short.

- `Index` · `Colophon` · `Next` · `Previous` · `Contents`
- Never: `SUBJECT`, `FILE`, `TRANSMISSION`, `RENDERING THE VISIBLE`, `SIGNAL WITHDRAWN`, or any system-cosplay string.
- Never: "post", "article", "blog", "read more", "explore", "discover".
- 404 reads: `Not found.` and a link back. Nothing else.
- No emoji. No exclamation marks.

---

## 3. COLOUR

One ground, one ink, one accent that is almost never visible. Accent coverage target: **under 1% of any viewport.**

**Dark (primary)**

| Token | Value | Role |
|---|---|---|
| `--ground` | `#0B0B0D` | Page. Never `#000`. |
| `--ink` | `#E7E7EA` | Prose. Never `#FFF`. |
| `--ink-dim` | `#9A9AA3` | Secondary prose, apparatus. 6.9:1. |
| `--ink-faint` | `#7C7C86` | Index numbers, dates, labels. 4.6:1 — low, never illegible. |
| `--rule` | `rgba(231,231,234,0.11)` | The only stroke on the site. |
| `--accent` | `#8E90E8` | Links on hover, focus rings, the current index row. |

**Light (equal citizen, not a fallback)**

| Token | Value |
|---|---|
| `--ground` | `#F4F3F0` |
| `--ink` | `#17171B` |
| `--ink-dim` | `#53535B` |
| `--ink-faint` | `#6C6C74` |
| `--rule` | `rgba(23,23,27,0.13)` |
| `--accent` | `#3E40C8` |

Rules: no gradients. No shadows. No fills — surfaces are the ground colour or nothing. No colour-coded categories or tags. Hover never recolours prose.

---

## 4. TYPOGRAPHY

**Two faces. The second one barely appears.**

- **Prose — `Newsreader`** (variable, 300–500, true italic, optical sizing). Titles, body, everything the reader reads.
- **Apparatus — `IBM Plex Mono`** (400). Used *only* where digits appear: index numbers, dates, read times. Set in **sentence case, not uppercase**, tracking `0.02em`, at 12–13px, in `--ink-faint` or `--ink-dim`.

Uppercase tracked mono is the single fastest way to make this site look generic. It is banned as a decorative device.

**Scale**

| Token | Size | Use |
|---|---|---|
| `--t-wordmark` | `1.0625rem` | The name in the header. Serif, not oversized. |
| `--t-cover` | `clamp(2.25rem, 5vw, 3.25rem)` | The one large line on the home page. |
| `--t-title` | `clamp(1.75rem, 3.4vw, 2.5rem)` | Entry title. Weight 400, tracking `-0.015em`, line-height 1.12. |
| `--t-h2` | `1.375rem` | Section head inside an entry. |
| `--t-lead` | `1.3125rem` | Standfirst. Weight 340, `--ink-dim`. |
| `--t-body` | `1.1875rem` | Prose. Line-height **1.72**. Weight 380. |
| `--t-small` | `0.9375rem` | Colophon, footnotes. |
| `--t-meta` | `0.75rem` | Mono. Dates, numbers. |

**Prose setting**

- Prose measure `34rem` (≈ 64 characters). Never wider. The contents list is the one exception at `40rem`, because a title and a date on one row need the room; every other block holds the prose measure.
- No indent; `1.4em` between paragraphs. `text-wrap: pretty` on prose, `balance` on headings.
- Italic is the only emphasis. **No bold in prose.**
- Links: `--ink` with a `1px` underline at `0.2em` offset in `--rule`; on hover the underline becomes `--accent`. No colour change to the word itself.
- `tabular-nums` on all mono. `oldstyle-nums` in prose.
- Never justify, never uppercase prose, no drop caps, no pull-quote frames, no small caps.

---

## 5. SPACE & STRUCTURE

Scale: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 · 192`. Nothing off-scale.

- **Page margins:** `clamp(24px, 7vw, 96px)`. The column sits left-aligned within them on wide screens, not centred in the viewport — centred everything is what makes a page look defaulted.
- **Header:** the name at left, `Index` and `Colophon` at right, at `--t-wordmark`/`--t-meta`. It persists. There is no rule beneath it — space does that job.
- **Radius: `0`.** **Stroke: `1px`, one colour.** No boxes, no cards, no panels, no containers with borders.
- Hairlines appear in exactly three places: between index rows, above the next-entry link, and as the short `48px` rule under an entry title. Nowhere else.
- **Images are rare and optional.** If one appears: full column width, greyscale or untreated, a one-line caption in `--ink-dim` at `--t-small`, no border, no filter, no dither. Most entries have none.

---

## 6. MOTION

The reader never leaves the environment. The header persists; only the content beneath it changes. No page load, no flash, no scroll-jump that reads as a new document.

```
--ease: cubic-bezier(0.22, 1, 0.36, 1);
--ms-fast: 140ms;   /* out */
--ms-slow: 340ms;   /* in */
```

- **Route change:** content `opacity 1→0` over 140ms; scroll resets during the gap; incoming content `opacity 0→1` and `translateY 6px→0` over 340ms. That is the entire transition. No stagger, no shared-element choreography, no view-transition names beyond the container.
- Hover: `opacity`/`border-colour` only, 140ms. Nothing scales, lifts, or moves.
- Nothing loops. Nothing animates on scroll. Prose never fades in.
- `prefers-reduced-motion`: opacity only, 90ms, no translate.

If a transition draws attention to itself, it is wrong.

---

## 7. PAGES

| Route | Content |
|---|---|
| `/` | The name, one line of positioning, then the contents list directly beneath. No separate index page is needed. |
| `/e/[slug]` | Index number and date, title, optional standfirst, short rule, prose, next entry. |
| `/colophon` | Who, why, typefaces, contact. A few paragraphs. |
| `*` | `Not found.` and a link. |

**Contents list:** one row per entry — index number (mono, faint), title (serif), date (mono, faint, right-aligned). Hairline between rows. Hover brightens the title; nothing else moves. Read entries are **not** marked — the site does not track the reader back at them.

**Entry foot:** a hairline, then `Next` and the next entry's title. No "back to index" dead end, no related reading, no share row.

**Absent by design:** search, tags, categories, comments, reactions, view counts, newsletter capture, cookie banner, social icons, author photo, reading-progress bar, related posts.

---

## 8. ACCESSIBILITY & PERFORMANCE

- Prose contrast ≥ 12:1; every apparatus colour ≥ 4.5:1 against its own ground, in both themes. There is no tier reserved for text too faint to read — if it is on the page, it is legible.
- Real semantics: `<article>`, ordered headings, `<nav>`, `<time datetime>`, `<ol>` for contents. Skip link to the article.
- `:focus-visible` = `1px solid var(--accent)`, `2px` offset. Never removed.
- Respect `prefers-reduced-motion` and `prefers-color-scheme`. Both themes fully designed.
- Two font families, ≤ 3 files, subset to `latin`+`latin-ext`, preloaded, `font-display: swap`.
- Budget: JS < 20KB, CSS < 12KB, LCP < 1.2s, CLS `0.00`.
- The whole novel must be readable with JavaScript disabled.
- No analytics that identify a reader. No third-party scripts of any kind.

---

## 9. STACK

Astro with MDX, or plain static HTML — the site is small enough that a framework is optional. Vanilla CSS with custom properties. No CSS framework, no animation library, no icon set, no canvas.

Entry frontmatter, complete:

```yaml
n:      4                      # index number
title:  "Entry title"
date:   2026-03-12
lead:   "Optional one-line standfirst."   # optional
slug:   entry-title
```

That is all the metadata that exists. Do not add fields to make the interface look busier.

---

## 10. NEVER

- A logo, mark, monogram, emblem, or icon.
- Gradients, shadows, glows, blurs, glass, rounded cards.
- Uppercase tracked mono used decoratively.
- Invented metadata or status readouts.
- Background graphics, canvases, textures, grain, or scanlines.
- Bold, justified, uppercase or centred body copy.
- Animation on scroll, parallax, scroll-jacking, custom cursors.
- More than one accent, or the accent used at any size larger than a line of text.
- Anything on screen that is not the writing, a way to reach other writing, or the name of the site.

---

## 11. ACCEPTANCE

- [ ] No mark or symbol appears anywhere, including the favicon behaviour and social preview.
- [ ] Accent covers under 1% of every viewport; a greyscale screenshot loses almost nothing.
- [ ] Exactly two typefaces; mono appears only alongside digits, never uppercase.
- [ ] Measure is 60–66 characters; body 19px / 1.72; no bold in prose.
- [ ] Only three kinds of hairline exist, in the three places named in §5.
- [ ] Header persists across every navigation; no flash, `CLS = 0.00`.
- [ ] Both themes fully designed; reduced-motion is opacity-only and still complete.
- [ ] The novel reads with JavaScript off.
- [ ] Nothing in §10 appears in the build.
- [ ] Remove any single element from a page and the page gets worse. If it doesn't, delete it.

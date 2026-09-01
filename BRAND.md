# magritte.io — Brand & Design System

**Version 0.2** · 1 September 2026 · **Status: in use, expected to change**

> **Prime directive**
> A reading environment, not a designed object. Black ground, one serif, enormous space,
> hairlines only where structure is genuinely needed. The reader should notice the writing
> and nothing else — and only later realise how precisely everything around it was placed.
>
> **There is no logo, no symbol, no mark.** The name, set in type, is the identity.

---

## 0. How this document changes

This is a living document. It is versioned, it will be wrong in places, and it is meant to
be edited — but not casually, or it stops being useful.

**The rules of amendment**

1. **The document and the code move together.** A change here without a matching change in
   `src/` is a lie; a change in `src/` without a matching change here is drift. Same commit.
2. **Subtract before you add.** The failure mode of this project is accumulation. Any
   addition must say what it replaces or why nothing could be removed instead.
3. **Record the reasoning, not just the value.** "`--ink-faint` is `#7C7C86`" is worth less
   than "`#7C7C86`, because the previous value failed contrast at 2.3:1 and it carries
   dates, which are real information."
4. **§10 Never is the hard floor.** Anything on that list requires deleting the line first,
   in its own commit, with a reason. It exists because these mistakes were already made once.
5. **Bump the version and add a changelog line.** Minor for adjustments, major for anything
   that changes how the site looks at a glance.

**Versioning:** `0.x` while the site carries placeholder text. It goes to `1.0` when the
first real entries ship, and the settled sections stop moving.

**Confidence, by section**

| Settled | Provisional |
|---|---|
| §1 Concept · §2 Voice · §4 Typography · §10 Never | §3 Colour (the accent is barely tested) |
| §5 Space · §6 Motion · §8 Accessibility | §7 Pages (no long entry has been set yet) |

Open questions are collected in §12 rather than left implicit in the prose.

---

## 1. Concept

`magritte.io` is a web-based novel — essays, short stories, journal entries, fragments —
written as a neo-surrealist response to machine intelligence and the commoditization of
the self.

The design argument is **refusal**. The subject is a person being flattened into a record,
so the site refuses to decorate, refuses to score, refuses to recommend, refuses to count.
It offers a page, a measure, and silence. The restraint *is* the position.

Two registers exist, and the second is nearly silent:

- **The writing.** Serif, sentence case, one column, generous. 95% of what is on screen.
- **The apparatus.** An index number, a date, a read time, a link. Small, dimmed, mono
  where it is numeric. It never announces itself.

The Magritte inheritance is the *title*, not a visual gimmick. Do not build captions that
contradict images. Do not put `Ceci n'est pas…` in the interface. If the author uses that
device, it happens in the prose, where it belongs.

---

## 2. Voice

Interface copy is plain, sentence case, and short.

- `Contents` · `Colophon` · `Next` · `End`
- Never: `SUBJECT`, `FILE`, `TRANSMISSION`, or any system-cosplay string.
- Never: "post", "article", "blog", "read more", "explore", "discover".
- 404 reads `Not found.` and a link back. Nothing else.
- No emoji. No exclamation marks.

---

## 3. Colour

One ground, one ink, one accent that is almost never visible. Accent coverage target:
**under 1% of any viewport.**

**Dark (primary)**

| Token | Value | Role |
|---|---|---|
| `--ground` | `#0B0B0D` | Page. Never `#000`. |
| `--ink` | `#E7E7EA` | Prose. Never `#FFF`. |
| `--ink-dim` | `#9A9AA3` | Secondary prose, apparatus. 6.9:1. |
| `--ink-faint` | `#7C7C86` | Index numbers, dates, labels. 4.6:1 — low, never illegible. |
| `--rule` | `rgba(231,231,234,.11)` | The only stroke on the site. |
| `--accent` | `#8E90E8` | Link underline on hover, focus ring, selection. |

**Light — an equal citizen, not a fallback**

| Token | Value |
|---|---|
| `--ground` | `#F4F3F0` |
| `--ink` | `#17171B` |
| `--ink-dim` | `#53535B` |
| `--ink-faint` | `#6C6C74` |
| `--rule` | `rgba(23,23,27,.13)` |
| `--accent` | `#3E40C8` |

There is no theme toggle. The site follows `prefers-color-scheme`; the reader has already
told their operating system what they want.

Rules: no gradients, no shadows, no fills. Surfaces are the ground colour or nothing. No
colour-coded categories or tags. Hover never recolours prose.

---

## 4. Typography

**Two faces. The second one barely appears.**

- **Prose — `Newsreader`** (variable, 300–500, true italic, optical sizing). Titles, body,
  everything the reader reads.
- **Apparatus — `IBM Plex Mono`** (400). Used *only* where digits appear: index numbers,
  dates, read times. Set in **sentence case, not uppercase**, tracking `.02em`, at 12–13px.

Uppercase tracked mono is the single fastest way to make this site look generic. It is
banned as a decorative device.

**Scale**

| Token | Size | Use |
|---|---|---|
| `--t-wordmark` | `1.0625rem` | The name in the header. Serif, not oversized. |
| `--t-cover` | `clamp(2.25rem, 5vw, 3.25rem)` | The one large line on the home page. |
| `--t-title` | `clamp(1.75rem, 3.4vw, 2.5rem)` | Entry title. Weight 400, tracking `-.015em`. |
| `--t-h2` | `1.375rem` | Section head inside an entry. |
| `--t-lead` | `1.3125rem` | Standfirst. Weight 340, `--ink-dim`. |
| `--t-body` | `1.1875rem` | Prose. Line-height **1.72**. Weight 380. |
| `--t-small` | `.9375rem` | Colophon, 404. |
| `--t-meta` | `.75rem` | Mono. Dates, numbers. |

**Prose setting**

- Prose measure `34rem` (≈ 64 characters). Never wider. The contents list is the one
  exception at `40rem`, because a title and a date on one row need the room; every other
  block holds the prose measure.
- No indent; `1.4em` between paragraphs. `text-wrap: pretty` on prose, `balance` on headings.
- Italic is the only emphasis. **Bold does not exist in this design** — the markdown
  pipeline deliberately does not support it.
- Links: `--ink` with a `1px` underline in `--rule` at `.2em` offset; on hover the underline
  becomes `--accent`. The word itself never changes colour.
- `tabular-nums` on all mono. `oldstyle-nums` in prose.
- Never justify, never uppercase prose, no drop caps, no pull-quote frames, no small caps.

---

## 5. Space & structure

Scale: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 · 192`. Nothing off-scale.

- **Page margins:** `clamp(24px, 7vw, 96px)`. The column sits **left-aligned** within them
  on wide screens, not centred in the viewport — centring everything is what makes a page
  look defaulted. The void on the right is deliberate.
- **Header:** the name at left, `Contents` and `Colophon` at right. It persists across every
  navigation. There is no rule beneath it — space does that job.
- **Radius `0`. Stroke `1px`, one colour.** No boxes, cards, panels or bordered containers.
- **Hairlines appear in exactly three places:** between contents rows, above the next-entry
  link, and as the short `48px` rule under an entry title. A fourth means amending this line.
- **Images are rare and optional.** If one appears: full column width, untreated, a one-line
  caption in `--ink-dim`, no border, no filter. Most entries have none.

---

## 6. Motion

The reader never leaves the environment. The header persists; only the content beneath it
changes. No page load, no flash, no scroll-jump that reads as a new document.

```
--ease:      cubic-bezier(.22, 1, .36, 1);
--ms-fast:   140ms;   /* out */
--ms-slow:   340ms;   /* in  */
```

- **Route change:** content `opacity 1→0` over 140ms; scroll resets during the gap;
  incoming content `opacity 0→1` and `translateY 6px→0` over 340ms. That is the entire
  transition — no stagger, no shared-element choreography.
- Hover: `opacity` / `border-color` only, 140ms. Nothing scales, lifts or moves.
- Nothing loops. Nothing animates on scroll. Prose never fades in.
- `prefers-reduced-motion`: opacity only, 90ms, no translate.

If a transition draws attention to itself, it is wrong.

---

## 7. Pages

| Route | Content |
|---|---|
| `/` | The name, one line of positioning, then the contents list beneath. There is no separate index page. |
| `/e/<slug>` | Index number, date, read time; title; optional standfirst; short rule; prose; next entry. |
| `/colophon` | Who, why, typefaces, contact. A few paragraphs. |
| `404` | `Not found.` and a link. |

**Contents list:** one row per entry — index number (mono), title (serif), date (mono,
right-aligned). Hairline between rows. Hover brightens the title; nothing else moves. Below
600px the date stacks under the title. Read entries are **not** marked — the site does not
track the reader back at them.

**Entry foot:** a hairline, then `Next` and the next entry's title. No "back to index" dead
end, no related reading, no share row.

**Absent by design:** search, tags, categories, comments, reactions, view counts, newsletter
capture, cookie banner, social icons, author photo, reading-progress bar, related posts.

---

## 8. Accessibility & performance

- Prose contrast ≥ 12:1. **Every apparatus colour ≥ 4.5:1 against its own ground, in both
  themes.** There is no tier reserved for text too faint to read — if it is on the page, it
  is legible.
- Real semantics: `<article>`, ordered headings, `<nav>`, `<time datetime>`, `<ol>` for the
  contents. Skip link to the article.
- `:focus-visible` = `1px solid var(--accent)`, `2px` offset. Never removed.
- Respect `prefers-reduced-motion` and `prefers-color-scheme`. Both themes fully designed.
- Two families, subset to `latin`+`latin-ext`, `font-display: swap`.
- Budget: JS < 20KB, CSS < 12KB, LCP < 1.2s, CLS `0.00`.
- **The whole novel must be readable with JavaScript disabled.**
- No analytics that identify a reader. No third-party scripts of any kind.

---

## 9. Stack

Static HTML generated by `build.py`. No framework, no dependencies, no build toolchain
beyond Python 3.8+. Vanilla CSS with custom properties. No CSS framework, no animation
library, no icon set, no canvas.

```
content/            the writing — the only place text lives
  site.json         name, cover line, description
  colophon.md
  entries/NN-slug.md   NN sets order, slug sets the URL
src/                the design — styles.css, app.js, layout.html
build.py            reads content/ + src/ → site/ + preview.html
site/               GENERATED, committed so it can be served directly
```

Entry frontmatter, complete:

```yaml
title: Entry title
date:  2026-03-12
lead:  Optional one-line standfirst.
```

Index number, URL and read time are all derived. Do not add fields to make the interface
look busier — see §10.

`src/app.js` is progressive enhancement only: it swaps the article region so the header
never blinks, and falls back to normal navigation on any error.

---

## 10. Never

Each line here is a mistake already made once. Deleting one requires its own commit and a
reason.

- A logo, mark, monogram, emblem or icon.
- Gradients, shadows, glows, blurs, glass, rounded cards.
- Uppercase tracked mono used decoratively.
- Invented metadata or status readouts (integrity scores, states, threat levels, locations).
- Background graphics, canvases, textures, grain, scanlines, dithered or duotone imagery.
- Wireframe ornament — tunnels, meshes, globes, vortices, contour fields.
- Text decode/scramble effects; fake OS windows and system dialogs.
- Bold, justified, uppercase or centred body copy.
- Animation on scroll, parallax, scroll-jacking, custom cursors.
- More than one accent, or the accent at any size larger than a line of text.
- Anything on screen that is not the writing, a way to reach other writing, or the name.

---

## 11. Acceptance

- [ ] No mark or symbol appears anywhere, including favicon and social preview.
- [ ] Accent covers under 1% of every viewport; a greyscale screenshot loses almost nothing.
- [ ] Exactly two typefaces; mono appears only alongside digits, never uppercase.
- [ ] Prose measure 60–66 characters; body 19px / 1.72; no bold anywhere.
- [ ] Only three kinds of hairline exist, in the three places named in §5.
- [ ] Header persists across every navigation; no flash; `CLS = 0.00`.
- [ ] Both themes fully designed; reduced-motion is opacity-only and still complete.
- [ ] The novel reads with JavaScript off.
- [ ] No horizontal overflow at 390px.
- [ ] Nothing in §10 appears in the build.
- [ ] Remove any single element from a page and the page gets worse. If it doesn't, delete it.

---

## 12. Open questions

Unresolved. Do not silently decide these — resolve one, then move it into the body of the
document with its reasoning.

1. **The accent has not earned its place yet.** It currently appears on hover underlines,
   focus rings and selection only. If a month of real reading never surfaces it, the site
   may be better with no accent at all — `--ink` for focus, and nothing else.
2. **Long entries have not been set.** Everything is validated against 3–6 placeholder
   paragraphs. A 4,000-word essay will test the measure, the `h2` rhythm and whether §7's
   refusal of a progress indicator survives contact with a long read.
3. **Sequence vs. date.** Entries are ordered by filename. If the novel wants named parts,
   or a reading order that differs from chronology, §7 needs a structure it does not have.
4. **Footnotes and asides.** The novel form suggests them; nothing is specified. If they are
   needed, the question is inline disclosure vs. margin — and the margin is currently empty
   on purpose.
5. **Images.** §5 permits them but none exist. The first real image will decide whether
   "untreated" survives, and that decision belongs in §5 once it is made.
6. **The cover line.** Currently a placeholder sentence. It is the first and sometimes only
   thing a reader sees, and it should be written last.
7. **Domain and title.** `magritte.io` is the address; the novel does not yet have a title.
   Whether these are the same word is unresolved.

---

## 13. Changelog

### 0.2 — 1 September 2026
Stripped the system back to minimalism, and built the draft site against it.

- **Removed the mark entirely.** The name set in type is the identity.
- **Removed all ornament:** emblem, HUD panels, corner registration marks, invented
  telemetry, dithered plates, wireframe motifs, animated background canvas, film grain,
  decode effects, fake OS dialogs. It performed neo-futurism instead of being precise, and
  competed with the prose it exists to serve.
- Collapsed the six-part accent cycle to a single accent under 1% coverage.
- Restricted mono to digits, in sentence case; banned uppercase tracked mono as decoration.
- Reduced metadata to what is true: index number, title, date, read time.
- Limited hairlines to three named places.
- Raised `--ink-dim` and `--ink-faint` in both themes. The previous faint tier failed
  contrast at 2.3:1 dark and 2.2:1 light while carrying dates and index numbers, which are
  real information, not decoration.
- Gave the contents list a wider measure (`40rem`) than the prose; a title and a date on one
  row do not fit at `34rem`.

### 0.1 — 1 September 2026
First specification. A surveillance-dossier interface: emblem derived from *Le Principe du
Plaisir*, per-Part accent drift across six hues, dithered duotone plates, a wireframe motif
library, a persistent background canvas, terminal decode effects. Superseded in full by 0.2;
kept in git history for the reasoning, not the conclusions.

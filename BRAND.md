# MAGRITTE.IO
## Brand, Design & Build Specification — v1.0

> **PRIME DIRECTIVE**
> Build a web-based novel that reads like a **declassified archive of a person who is being deleted**.
> A dossier system — hairline panels, monospaced telemetry, dithered bitmaps, wireframe geometry —
> built with the restraint of a Jony Ive product: one material, one accent, enormous void,
> zero ornament that isn't structural. The machine catalogues; the prose escapes.
> Nothing on this site should look *designed*. It should look **found**, **instrumented**, and **exact**.

---

## 0. HOW TO USE THIS DOCUMENT

You are building `magritte.io` from scratch. This document is binding.

- Sections **1–2** are the concept. Read them first; every visual decision descends from them.
- Sections **3–8** are the design system. Implement them literally — hex values, milliseconds and easing curves are specified, not suggested.
- Sections **9–12** are architecture, a11y, performance and stack.
- Section **13** is the microcopy deck. Use these strings verbatim.
- Section **14** is the kill-list. Violating it fails the build.
- Section **15** is the acceptance checklist. Ship only when every line passes.
- Appendices are copy-paste-ready code.

Where this document and your instincts disagree, this document wins. Where this document is silent, choose the **quieter, more precise, more structural** option.

---

## 1. THE CONCEPT

### 1.1 Premise

`magritte.io` is a quasi-dystopian literary work — essays, short stories, journal entries, fragments, transmissions — written as a neo-surrealist response to the acceleration of machine intelligence and the commoditization of the self. Its subject is the moment a person becomes a **record**: indexed, scored, summarized, reproduced, and thereby lost.

The website is not a container for that idea. The website **is** that idea. The reader arrives inside a system that is trying to file them.

### 1.2 The Two Registers

Every pixel belongs to exactly one of two registers. This tension is the entire design system. Never blend them; never let one contaminate the other.

**REGISTER A — THE MACHINE**
The apparatus. Metadata, labels, navigation, timestamps, indices, progress, system messages, captions.
- Monospaced. Uppercase. Wide tracking. Small.
- Accent-colored or dimmed; never full-brightness.
- Lives on hairlines, inside panels, in the left rail, at the extreme edges of the viewport.
- Cold, declarative, bureaucratic, absolutely certain.
- Behaves mechanically: snaps, ticks, decodes, counts.

**REGISTER B — THE HUMAN**
The writing. Prose, verse, fragments, the voice.
- Serif. Sentence case. Generous measure. Large.
- Near-white on near-black. No decoration. No box. No card. No border.
- Floats free in the void, aligned to but never *inside* the machine's grid.
- Warm, uncertain, digressive, alive.
- Behaves organically: fades, drifts, breathes.

The reader should feel the machine trying to frame the prose and failing — the text always overflows, off-grid, unlabelled, un-scored. That failure is the emotional payload.

### 1.3 The Magritte Device — The Caption That Denies

*Ceci n'est pas une pipe.*

Every image on this site carries a caption that **contradicts what is shown**. This is not a joke to be used once; it is the site's grammar of doubt, applied systematically:

- A dithered eye → `FIG. 04 — NOT AN EYE. A CAMERA THAT REMEMBERS BEING ONE.`
- A wireframe globe → `FIG. 11 — THIS IS NOT THE WORLD. IT IS THE INDEX OF THE WORLD.`
- An empty room → `FIG. 02 — THIS IS NOT A ROOM. IT IS THE ABSENCE OF A SUBJECT.`

The device extends beyond images into the interface itself: the 404 page, the loading state, the colophon. The machine labels everything, and every label is subtly wrong. Under no circumstance should captions be descriptive, helpful, or witty-for-its-own-sake. They must be **flat, certain, and false**.

### 1.4 The Emblem — *Le Principe du Plaisir*

The site's mark derives from Magritte's 1937 portrait: a seated figure in a suit whose head is replaced by a detonation of white light.

**Emblem construction (SVG, drawn — never a photo):**
- A shoulders-and-torso bust, rendered in 1px hairline contour or 1.5px Atkinson dither.
- The head is **absent** — replaced by a hard-edged flare of `--signal` at 100% opacity, with exactly one permitted radial falloff (the only gradient allowed on the entire site).
- The flare must read as *erasure*, not as *glow*. Hard core, short falloff, no bloom, no blur beyond 6px.

Use it: as favicon, as the Threshold (home) centerpiece, as the end-of-part seal, and as the OG image. Never at less than 24px. Never rotated, never recolored outside the active accent, never animated except a 1-frame flicker on first load.

**Supporting motif vocabulary** (all drawn as 1px SVG wireframes, all fair game as section marks, page furniture and Field states):
`Le Faux Miroir` (an eye containing sky) · `Golconda` (identical figures raining on a grid — the loss-of-individualism motif) · `La Reproduction Interdite` (a mirror returning the back of the head — the AI-copy motif) · `L'Empire des Lumières` (day sky over night street — the Part III inversion).

### 1.5 Reference DNA (what the visual language is compiled from)

Duotone HUD dossiers and biometric readouts · fake OS window chrome and terminal transcripts used as emotional containers · risograph two-colour print with misregistration and paper grain · cassette J-card metadata blocks, spines and barcodes · acid-poster wireframe geometry: tunnels, vortices, warped meshes, contour fields · Atkinson-dithered bitmap portraiture · bracketed specimen labels and crop marks.

**Then subtract 70% of it.** The references are *maximalist posters*. This is a *reading environment*. Keep the vocabulary; keep only the density Ive would keep. On any given screen, the machine register should occupy **less than 10% of the visual field**. The other 90% is void and prose.

---

## 2. VOICE (INTERFACE COPY, NOT THE NOVEL)

The interface speaks in **Register A** only: it is the voice of the filing system, not the author.

- Uppercase, monospaced, terse. No articles where they can be dropped. No exclamation. No emoji. Ever.
- Bureaucratic nouns: `SUBJECT`, `FILE`, `RECORD`, `SPECIMEN`, `TRANSMISSION`, `INTEGRITY`, `STATE`, `INDEX`.
- Never say "post", "article", "blog", "chapter", "read more", "welcome", "explore", "discover", "learn more".
- The system is never friendly, never apologetic, never enthusiastic. It is **indifferent and precise**.
- Exactly one crack in the composure per Part: a single `INTERRUPT` dialog where the system leaks feeling (§7.9). It must land as a shock because everything around it is so cold.

---

## 3. COLOR

### 3.1 Philosophy

**One ground. One ink. One signal.** Monochrome duotone at all times. Color is information, never decoration. If a colour is not carrying meaning, remove it.

Accent coverage target: **≤ 3% of any viewport**. If a screenshot looks colourful, it is wrong.

### 3.2 Core palette

| Token | Value | Role |
|---|---|---|
| `--void` | `#08080B` | Base ground. Off-black, cool cast. **Never `#000`.** |
| `--void-raised` | `#0D0D12` | Panel/surface fill. Used sparingly; most panels are transparent. |
| `--void-sunk` | `#050507` | Overlay scrim base (used at 88% alpha). |
| `--bone` | `#E8E8ED` | Primary prose. **Never `#FFF`.** |
| `--bone-dim` | `#8C8C99` | Secondary / apparatus at rest. |
| `--bone-ghost` | `#4A4A55` | Tertiary, disabled, read-state, rules. |
| `--hairline` | `rgba(232,232,237,0.13)` | The single structural stroke of the whole site. |
| `--hairline-hot` | `rgba(232,232,237,0.28)` | Hover / active hairline only. |
| `--signal` | *per Part, see 3.3* | The one accent. Registered `@property` so it can animate. |
| `--signal-dim` | `color-mix(in oklab, var(--signal) 45%, var(--void))` | Accent at rest, non-interactive. |
| `--signal-wash` | `color-mix(in oklab, var(--signal) 12%, transparent)` | Selection, focus halo, Field strokes. |

`::selection` = `--signal-wash` background, `--bone` text. No other background colour exists on the site.

### 3.3 The Hue Drift — accent per Part

The novel is divided into Parts. **The accent mutates as the reader descends.** Only ever one accent is active; it cross-fades over `--ms-env` (1100ms) when the reader crosses a Part boundary. This is how the environment ages without ever breaking the one-accent rule.

| Part | Name | `--signal` | Ground | Note |
|---|---|---|---|---|
| I | `LE FAUX MIROIR` | `#8A8CFF` periwinkle | `--void` | Cold surveillance blue. The default. Contrast 7.4:1. |
| II | `CONTINUA` | `#E79BFF` orchid | `--void` | The system starts feeling. 10:1. |
| III | `L'EMPIRE DES LUMIÈRES` | `#3D3DF5` ultramarine | `#ECEAE4` bone ground | **Inverted Part.** See 3.4. |
| IV | `LA REPRODUCTION INTERDITE` | `#8CF5D2` spearmint | `--void` | Cold, clinical, copied. 14:1. |
| V | `LE PRINCIPE DU PLAISIR` | `#C6F04A` acid | `--void` | Overexposure. Highest tension. 15:1. |
| VI | `GOLCONDA` | `#E8E8ED` bone | `--void` | **The accent collapses into the text colour.** The machine register and the human register become indistinguishable. There is no longer a difference between the file and the person. This is the ending; do not "fix" it. |

### 3.4 Part III — the daylight inversion

Part III inverts the entire environment: ground `#ECEAE4` (bone paper), ink `#12121A`, hairline `rgba(18,18,26,0.16)`, accent ultramarine `#3D3DF5`. Riso-print register: allow 1px chromatic misregistration on plates only. Everything else — grid, type scale, motion, components — is identical. The inversion must be **structurally invisible and emotionally total**, and it cross-fades like any other Part change: no white flash, no reload.

Implement as `[data-part="III"]` re-declaring the same tokens. Never fork the CSS.

### 3.5 Rules

- No gradients anywhere, except the single radial falloff inside the emblem flare.
- No shadows. Depth is expressed by hairlines and offset duplicates (riso layering), never by blur.
- No colour-coded categories, tags, or badges. Type classification is expressed in words, not colour.
- Hover never changes colour of prose. Hover changes hairlines and apparatus only.

---

## 4. TYPOGRAPHY

### 4.1 Exactly two typefaces

Two families. This restraint is the Ive move — do not add a third for "display". Display is achieved with **scale and tracking**, not with a new face.

**REGISTER A — apparatus:** `IBM Plex Mono` (400, 500). Institutional, archival, engineered; reads as a state document rather than a code editor. Weights: 400 default, 500 for active/hover states only.
`font-family: "IBM Plex Mono", ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;`

**REGISTER B — prose:** `Newsreader` (variable, 300–500, true italic, optical size axis). Screen-native editorial serif with real texture and superb italics; cold enough to sit beside the mono, warm enough to carry 4,000 words.
`font-family: "Newsreader", "Source Serif 4", Charter, "Iowan Old Style", Georgia, serif;`
Set `font-optical-sizing: auto`. Body uses weight 380 (variable) for optical parity with the mono's 400 on dark ground.

Subset to `latin` + `latin-ext` (the French titles need it). `font-display: swap`. Self-host if possible; two families, max four files total.

**Optional third face — forbidden** unless it is a *drawn SVG wordmark*, in which case it must be a geometric bitmap/pixel construction on a 5×7 or 7×9 grid, used only in the emblem lockup, never as live text.

### 4.2 Scale (root 16px)

| Token | Size | Register | Spec |
|---|---|---|---|
| `--t-display` | `clamp(2.75rem, 13vw, 9.5rem)` | A | Threshold wordmark & Part titles. Uppercase, tracking `0.055em`, weight 400, line-height `0.92`. |
| `--t-title` | `clamp(2rem, 5.2vw, 3.5rem)` | B | Entry title. Weight 400, line-height `1.08`, tracking `-0.018em`. |
| `--t-h2` | `1.875rem` | B | Section head inside entry. Line-height `1.2`. |
| `--t-h3` | `1.3125rem` | B | Subsection. Italic permitted. |
| `--t-lead` | `1.4375rem` | B | Opening paragraph / standfirst. Line-height `1.55`, colour `--bone`, weight 350. |
| `--t-body` | `1.25rem` (20px) | B | **Prose.** Line-height `1.68`. Weight 380. Colour `--bone` at 92% alpha. |
| `--t-body-s` | `1.0625rem` | B | Footnotes, marginalia, colophon. |
| `--t-ui` | `0.8125rem` | A | Interactive apparatus, ledger rows. Tracking `0.06em`. |
| `--t-meta` | `0.75rem` | A | Metadata rows, captions. **Uppercase**, tracking `0.12em`. |
| `--t-micro` | `0.6875rem` | A | Edge labels, indices, timestamps. Uppercase, tracking `0.16em`. |

**Never set Register A below 11px.** **Never set uppercase mono without ≥`0.06em` tracking.** **Never set prose in uppercase, in mono, or justified.**

### 4.3 Prose setting

- Measure: `65ch` optimal, `72ch` hard maximum, `38ch` minimum at mobile.
- Paragraphs: no indent, `1.35em` bottom margin. Alternative permitted per-entry: first-line indent `1.5em` with zero margin (classic novel setting) — choose one per Part and hold it.
- Hyphenation: `hyphens: auto` with `hyphenate-limit-chars: 7 3 3`. Never justify.
- `text-wrap: pretty` on prose, `text-wrap: balance` on all headings and captions.
- Optical hanging punctuation on pull quotes: `hanging-punctuation: first last`.
- Numerals: `font-variant-numeric: tabular-nums` on **all** Register A (metadata must align to the character cell); `oldstyle-nums` in prose.
- Italic is the only emphasis in prose. **No bold in prose, ever.** Bold does not exist in Register B.
- Small caps are forbidden (the mono covers that job).
- Links in prose: no underline at rest, `--bone` colour, `text-decoration: underline` on hover in `--signal` with `text-underline-offset: 0.22em; text-decoration-thickness: 1px`. External links get a trailing `↗` in mono at `--t-micro`.
- Drop caps: forbidden. The entry opens with the standfirst instead.

### 4.4 The decode treatment (use with extreme discipline)

Register A text may perform a **character-scramble decode** — glyphs cycle through `A–Z0–9/\|<>-_[]` and resolve left-to-right.
- Duration `320ms`, stagger `12ms/char`, cap at **28 characters**.
- Permitted on: Threshold wordmark (first visit only), entry metadata block on route entry, Ledger rows on first paint.
- Forbidden on: any prose, any heading in Register B, anything the reader will re-see repeatedly, anything above 28 chars.
- Fires **once per session** per element — persist in `sessionStorage`. Nothing that a reader sees twice may animate twice.
- Fully disabled under `prefers-reduced-motion`.

---

## 5. SPACE, GRID & GEOMETRY

### 5.1 Spacing scale (4px base)

`--s-1: 4px` · `--s-2: 8px` · `--s-3: 12px` · `--s-4: 16px` · `--s-5: 24px` · `--s-6: 32px` · `--s-7: 48px` · `--s-8: 64px` · `--s-9: 96px` · `--s-10: 128px` · `--s-11: 192px` · `--s-12: 256px`

Nothing is spaced off-scale. Vertical rhythm between prose blocks and apparatus is always a scale step, never an arbitrary value.

### 5.2 The frame

A **1px hairline rectangle inset from the viewport edge** frames every page — `--s-5` inset at desktop, `--s-4` at mobile. It is fixed, does not scroll, and persists across every route change. This is the single most important structural element on the site: it is the **edge of the document**, and the reader is inside it. It never disappears, never animates except a 1100ms opacity cross-fade at Part changes.

At each of the four corners: a **corner tick** — two 8px hairline strokes forming an L, offset 4px outward from the frame. Registration marks, not decoration.

### 5.3 Edge labels

Four `--t-micro` labels sit in the frame margins, fixed:
- **Top-left:** `MAGRITTE.IO`
- **Top-right:** the active Part — `PART III / L'EMPIRE DES LUMIÈRES`
- **Bottom-left:** the current file — `FILE A-034` · on the Ledger, `INDEX`
- **Bottom-right:** live scroll position as a percentage, tabular — `041%`

Vertical labels (`writing-mode: vertical-rl`) are permitted on the left/right frame margins at ≥1280px for the file ID and date. Keep to one per side.

### 5.4 Layout

- **Reading column:** single centred column, `min(65ch, 100% - var(--s-10))`. It is centred on the *viewport*, not on the remaining space after the rail — the rail floats over the margin. Optical centring beats mathematical centring; nudge if needed.
- **The Rail** (≥1080px): a `160px` column pinned to the left frame margin, holding the progress hairline, section index, timestamps and marginalia anchors. Below 1080px the rail's contents collapse into a bottom-fixed hairline strip.
- **Full-bleed:** permitted only for Plates and Part title cards. Full-bleed elements still respect the frame — they bleed to the frame, never past it.
- **Breakpoints:** `480 / 768 / 1080 / 1280 / 1680`. Prefer fluid `clamp()` over breakpoint jumps; use breakpoints only for layout re-composition (rail on/off, marginalia inline/outboard).
- **12-column grid** exists only on the Ledger and the Colophon. Entries never use a multi-column grid — prose lives in one column and the machine annotates from the margins.

### 5.5 Geometry rules

- **Border radius: `0`.** Everywhere. The single exception is `2px` on inline chips and the search field. Nothing is round. Nothing is a pill.
- **Stroke: `1px` `--hairline`.** One weight for the entire site. Never 2px, never dashed except for a single defined "provisional" state (`2 3` dash array, used for unpublished/forthcoming entries in the Ledger).
- Panels sit **flush and shared-edge** where adjacent (collapse the double hairline; never let two 1px strokes sit 1px apart).
- Alignment is absolute: mono glyph cells align to the 4px grid; label columns and value columns in metadata blocks align to a shared axis across every entry on the site.
- Asymmetry is allowed only when it is informational. Decorative asymmetry is forbidden.

---

## 6. GRAPHIC LANGUAGE

### 6.1 Image treatment pipeline (mandatory, no exceptions)

Every raster image on this site passes through:
1. **Desaturate** to greyscale.
2. **Crush levels** — black point 10%, white point 92%, gamma 1.05. Kill mid-tone mush; the image must be mostly black with hard bright structure.
3. **Dither** — Atkinson (preferred) or Floyd–Steinberg, 1.5px cell at 1×, 1px at 2×. The dither pattern must be **visible**. If it looks like a photo, it has failed.
4. **Duotone map** — shadows to `--void`, highlights to `--signal`, via the SVG filter in Appendix B. Never bake the colour into the asset: map at render time so plates re-tint with the Part's hue drift.
5. **Export** as 1-bit-feel PNG or WebP; add `image-rendering: pixelated` where upscaled.

**No full-colour photograph appears anywhere on this site.** Not in OG images, not in the colophon, not in an author photo.

### 6.2 Wireframe library (SVG, 1px, `stroke-linecap: square`, `fill: none`)

Build these as reusable inline SVG components with a `stroke="currentColor"` and no hardcoded colour:

`CONTOUR` topographic field · `TUNNEL` one-point perspective corridor · `WARP` gravity-well mesh · `VORTEX` funnel · `WAVE` waveform over graph paper · `SPHERE` wireframe globe · `GOLCONDA` identical figures on a grid · `RETICLE` radar/target vignette · `WHORL` fingerprint · `MIRROR` figure facing a mirror that returns the back of the head · `FLARE` the emblem.

Rules: never filled, never gradient-stroked, never more than one motif per screen, never behind prose at more than 10% opacity. Motifs are **specimens**, not wallpaper — give them void around them and a bracketed label beneath.

### 6.3 Texture

- **Grain:** a single fixed SVG `feTurbulence` noise layer over the whole document. `opacity: 0.035`, `mix-blend-mode: overlay`, `pointer-events: none`, `position: fixed`, `z-index: 9998`. Generated once; **not animated** (a slow 24s `translate` drift of ≤4px is permitted, nothing faster).
- **Scanlines:** a `repeating-linear-gradient` at 3px period, `opacity: 0.025`, fixed. Optional, off by default, user-togglable in the Colophon.
- **Misregistration:** Part III only, plates only — a 1px offset duplicate of the plate in the accent hue at 30% opacity. This is a print artefact, not a glitch effect.
- **Forbidden textures:** CRT barrel distortion, chromatic aberration on text, VHS tracking bars, animated glitch/datamosh, film burn, lens flare.

### 6.4 The Field (persistent background)

A single `<canvas>` behind all content, **mounted once at app root and never unmounted across route changes**. It renders one wireframe system per Part (§6.2), drifting.

- Opacity `0.06`–`0.10`. Stroke `--signal`. 1px lines.
- Motion: constant drift ≈ `0.015px/frame`; a full cycle takes minutes, not seconds. The reader should never *catch* it moving — only notice it has changed.
- Pointer parallax: max `8px` displacement, eased over `1200ms`. Disabled on touch.
- Throttle to **30fps**; `cancelAnimationFrame` when `document.hidden`, when the canvas is off-screen, or on `prefers-reduced-motion` (render one static frame instead).
- Canvas 2D only. No WebGL, no Three.js, no shader libraries.
- The Field morphs between Part systems by interpolating point positions over `--ms-env`. It **never** clears to a different image.

---

## 7. COMPONENT INVENTORY

Every component is named in the world's language. Use these names in code.

### 7.1 `Frame` — the persistent document edge
§5.2 + §5.3. Renders once in the root layout, outside the router outlet. Never re-mounts.

### 7.2 `Threshold` — `/`
The cover. Deliberately near-empty; it must feel like a held breath.
- The `FLARE` emblem, centred, ~`clamp(180px, 30vw, 380px)`.
- Below it, the wordmark `MAGRITTE.IO` at `--t-display`, tracking `0.055em`, decoding once.
- Below that, one line of Register A: `CECI N'EST PAS UN LIVRE`.
- A single entry action at the bottom edge: `ENTER ▸` or, on return visits, `RESUME — FILE A-034 · 41%`.
- Nothing else. No nav bar, no scroll teaser, no marketing. No hero copy. **One screen, no scroll.**

### 7.3 `Ledger` — `/index`
The archive table. This is where the dossier language is densest, and it should feel *cold and beautiful*.
- A 12-column table of hairline rows, `--t-ui`. Columns: `FILE` · `TITLE` · `TYPE` · `STATE` · `DATE` · `DURATION`.
- Row height `48px`, single hairline between rows, no zebra striping, no card, no shadow.
- Hover: the row's hairlines go `--hairline-hot`, the `FILE` cell goes `--signal`, a 1px vertical tick appears at the row's left edge. **160ms.** No background fill, no scale, no lift.
- Read entries render `FILE` and `TITLE` at `--bone-ghost` with a `SEEN` marker in the right margin. Reading is a state the system records — the design should make that faintly uncomfortable.
- Forthcoming entries: dashed hairline, `--bone-ghost`, `STATE: PENDING`, not clickable.
- Group by Part with a full-width Part header row: `PART II — CONTINUA` at `--t-meta`, plus a `WAVE` motif at 8% opacity bleeding across the row.
- Filter/sort controls: a single mono row of toggles, no dropdowns, no chips with backgrounds. `ALL · ESSAY · FRAGMENT · STORY · TRANSMISSION · DREAM`. Active state = `--signal` + a 1px underline.

### 7.4 `Dossier` — the entry header
The masthead of every entry. Register A frames Register B.
- `--t-micro` eyebrow: `FILE A-034 / PART II`.
- Entry title at `--t-title` (Register B, serif, sentence case) — this is the moment the human register interrupts the machine, and the contrast must be felt.
- A metadata block below: hairline-separated rows, label left in `--bone-dim`, value right in `--bone`, tabular, aligned to a site-wide axis:
  `INCEPT DATE · TYPE · STATE · LOCATION · INTEGRITY · DURATION`
  `STATE` takes a mood word (`STABLE / UNSTABLE / RECURSIVE / VACANT / LUMINOUS / COPIED`). `INTEGRITY` takes a percentage and renders a 40px hairline bar. `LOCATION` is often `————`.
- Optional `Plate` (§7.6) sits between the metadata block and the prose.
- The whole block decodes once on entry, then is silent forever.

### 7.5 `Passage` — the prose body
§4.3. No container, no background, no border. Just type in void.
- Section breaks inside an entry use `Cut` (§7.7).
- Blockquote: no quotation marks, no left bar — instead, indent `--s-6` and set in italic at `--t-lead` with a `--t-micro` attribution in the rail.
- Pull quote: full-measure, `--t-lead`, `--bone`, hairline above and below at `--s-7` margins, hanging punctuation. Max one per entry.
- Code/machine excerpts inside prose: Register A, `--void-raised` fill, 1px hairline, `--s-4` padding, no radius.

### 7.6 `Plate` — figure + denying caption
- Full-bleed-to-frame or column-width. Dithered, duotone (§6.1).
- Caption in `--t-meta`, uppercase, `--bone-dim`, aligned left under the image, prefixed `FIG. NN — `, and it **must contradict the image** (§1.3).
- Two hairline corner ticks at the image's top-left and bottom-right. No full border.

### 7.7 `Cut` — section divider
A full-measure hairline, with a centred `+` tick sitting on it in `--signal`, and a right-aligned `--t-micro` section index (`§ 03`). Margin `--s-9` above, `--s-8` below.

### 7.8 `Rail` — apparatus column
Left frame margin at ≥1080px, containing:
- **Progress:** a vertical 1px hairline, full column height, filled in `--signal` to scroll depth. Not a top bar — a *depth gauge*. It fills downward.
- **Section index:** the entry's `Cut` markers as tiny ticks on that hairline, clickable, current one `--signal`.
- **Marginalia:** footnotes and asides rendered outboard at `--t-body-s`, `--bone-dim`, aligned to their anchor's baseline. Below 1080px they become inline `<details>` disclosures with a `[ 01 ]` mono trigger.

### 7.9 `Interrupt` — the system leak
The only maximalist component. A fake OS window with `× □ _` chrome in the title bar, 1px hairline, `--void-raised` fill, offset duplicate 4px behind it in `--signal-wash`.
- Contains one line of Register A that admits a feeling: `AN UNHANDLED EMOTION OCCURRED AT LINE 41.`
- Two buttons: `IGNORE` and `FEEL IT` — both mono, both hairline-boxed, no fill.
- **Maximum one per Part.** It is dramaturgy, not a pattern. It must never be used for cookie notices, newsletter capture, or any real utility.

### 7.10 `Handoff` — end of entry
Leaving an entry must feel like the archive advancing, not like a page ending.
- `FILE CLOSES` in `--t-micro`, then a hairline.
- Then the **next entry rendered as a Ledger row** — same component, same columns, full width, hoverable. The reader steps from one file straight into the next; there is no "back to index" dead end.
- A quiet `◂ PREVIOUS` in the left margin.

### 7.11 `Search` — command line
Invoked with `/`. A single hairline field pinned to the frame's bottom edge, `--void-sunk` at 88% with `backdrop-filter: blur(12px)` (the **only** permitted blur on the site).
- Prompt: `magritte:\> ` then a blinking 1px block cursor (`1.06s` step-end).
- Results as Ledger rows, live-filtered, match highlighted in `--signal`.
- `Esc` closes. No result count badge, no "no results" illustration — just `NOTHING HERE IS ALSO SOMETHING`.

### 7.12 `Colophon` — `/about`
The book's imprint page. Author, provenance, typefaces, method, contact — set as a Dossier metadata block, then prose. Contains the site's settings (scanlines, reduced motion, resume) as mono toggles. No social icon row; text links only.

### 7.13 `Void` — `404`
Centred: `THIS IS NOT A PAGE.` at `--t-title` in Register B. Beneath, `--t-meta`: `THE ADDRESS EXISTS. THE THING DOES NOT.` Beneath that, `RETURN TO INDEX ▸`. One `RETICLE` motif at 8%. Nothing else.

### 7.14 Global states
- **Focus:** `outline: 1px solid var(--signal); outline-offset: 3px;` — never removed, never a soft glow.
- **Cursor** (pointer devices, optional, must degrade): a 1px crosshair reticle replacing the default; expands to a 24px hairline square over interactive elements; hidden on touch and under reduced motion.
- **Loading:** never a spinner. A 1px hairline that draws left-to-right across the frame's top edge in `--signal`, plus `RENDERING THE VISIBLE` in `--t-micro`.
- **Scrollbar:** hidden width-0 on the document; the Rail gauge is the scroll indicator. Keep native scrollbars in any overflow panel.

---

## 8. MOTION & THE ONE-ENVIRONMENT RULE

### 8.1 The rule

**The reader never leaves the environment.** There is no page load, no white flash, no full unmount, no reflow jump, no scroll-to-top snap that reads as a new document. `Frame`, `Field`, `Rail` and the edge labels are mounted once at root and persist for the entire session. Only the content inside them changes.

If a route change ever produces a flash of unstyled content, a layout shift, or a moment where the frame is absent, **the build has failed its single most important requirement.**

### 8.2 Tokens

```
--ease-instrument: cubic-bezier(0.16, 1, 0.30, 1);   /* default: expo-out, precise arrival */
--ease-shutter:    cubic-bezier(0.83, 0, 0.17, 1);   /* mechanical in-out, for the machine */
--ease-drift:      cubic-bezier(0.40, 0, 0.20, 1);   /* organic, for prose and the Field */

--ms-tick:  90ms;    /* hairline/state flicks */
--ms-micro: 160ms;   /* hover, focus, toggles */
--ms-ui:    280ms;   /* panels, disclosures, search */
--ms-page:  560ms;   /* route transition */
--ms-env:   1100ms;  /* Part change: accent, ground, Field morph */
```

No animation may exceed `--ms-env`. No animation may bounce, overshoot, spring, or elastic. The system is precise; precision does not wobble.

### 8.3 Route transition (exact choreography)

Use the **View Transitions API** (`document.startViewTransition`), with a JS-driven fallback for unsupported browsers. Total budget `560ms`.

1. `0–180ms` — outgoing content: `opacity 1→0`, `translateY 0→-6px`, `--ease-shutter`. The Frame, Field, Rail, edge labels do **not** move.
2. `120–200ms` — bottom-left edge label ticks over to the new file ID (instant swap + 90ms decode, ≤12 chars).
3. `140–560ms` — incoming content: `opacity 0→1`, `translateY 10px→0`, `--ease-instrument`, with a `28ms` stagger across `[Dossier → Plate → first Passage block]` only. Do not stagger every paragraph.
4. Scroll restores to `0` **instantly during the blackout window** (`~180ms`), never as a visible animated scroll.
5. Shared-element continuity via `view-transition-name`: the Ledger row's title morphs into the entry title (`entry-title-<slug>`), the `FILE` cell into the Dossier eyebrow. This is the signature move of the site — get it right.

### 8.4 Part transition

When the reader crosses a Part boundary, `--signal` (and in Part III, ground/ink) animate over `--ms-env` with `--ease-drift`, and the Field morphs. Register `--signal` via `@property` so the colour genuinely interpolates rather than snapping. The top-right edge label cross-fades to the new Part name. **No other element reacts.** The world changes hue while nothing moves — that is the effect.

### 8.5 Scroll behaviour

- `scroll-behavior: smooth` for in-page anchors only.
- Entry reveal on scroll: **at most** `opacity 0→1` + `translateY 12px→0` over `400ms`, threshold `12%`, `once: true`. Applied to Plates and Cuts only. **Prose paragraphs never animate in** — a reader scrolling back up must never see text re-appear.
- No parallax on content. No scroll-jacking. No horizontal scroll. No snap points except optionally on Part title cards.
- No pinned scroll-driven scenes, no scroll-scrubbed video, no `100vh` sections that fight the reader.

### 8.6 Micro-interactions

- Hairlines transition `border-color`/`opacity` over `--ms-micro`.
- Buttons/links never scale, never translate on hover. They change hairline weight-of-colour and accent only.
- The `INTEGRITY` bar and progress gauge fill with `--ease-drift`; they may animate on first paint, once.
- Cursor blink: `1.06s`, `step-end`, infinite — the only permitted infinite animation on the site besides the Field drift.

### 8.7 `prefers-reduced-motion: reduce`

All transforms → `none`. All durations → `≤90ms` opacity-only cross-fades. Decode → off. Field → one static frame. Cursor reticle → off. Parallax → off. The site must remain **completely legible and completely beautiful** in this mode; treat it as a first-class design target, not a fallback.

---

## 9. INFORMATION ARCHITECTURE & UX

### 9.1 Routes

| Route | Component | Purpose |
|---|---|---|
| `/` | `Threshold` | Cover. One screen. Enter or resume. |
| `/index` | `Ledger` | The archive. Every entry, grouped by Part. |
| `/entry/[slug]` | `Dossier` + `Passage` + `Handoff` | The reading view. The site's centre of gravity. |
| `/part/[i]` | `PartCard` | Optional interstitial: Part numeral, French title, one epigraph, one motif. Auto-advances on scroll into the first entry. |
| `/about` | `Colophon` | Imprint, method, settings. |
| `*` | `Void` | 404. |

There is **no** blog pagination, no tag archive pages, no author archive, no category landing pages. The Ledger is the only index.

### 9.2 Navigation model

Global navigation is three items maximum, set in `--t-micro` at the frame's top edge, right-aligned: `INDEX · COLOPHON · ⌕`.
No hamburger. No sticky header bar. No mega-menu. No footer nav — the `Handoff` is the footer.

**Keyboard (implement all, document in Colophon):**
`→` / `J` next entry · `←` / `K` previous entry · `I` index · `/` search · `Esc` close overlay · `G` then `T` top · `?` shortcuts panel.

### 9.3 Reading model

- **Resume:** persist `{slug, scrollRatio, timestamp}` to `localStorage` on scroll (throttled 800ms). On return, the Threshold offers `RESUME — FILE A-034 · 41%`. Never auto-navigate; always offer.
- **Read state:** mark an entry `SEEN` at 85% scroll depth. Surfaced in the Ledger (§7.3). Store locally only.
- **Duration:** computed from word count at 230wpm, rendered as `08 MIN` in the Dossier. Tabular numerals.
- **No comments, no reactions, no share counts, no view counts, no related-posts algorithm.** The commoditization of attention is the antagonist of this book; do not build it into the book.
- Sequence is authored, not algorithmic: `Handoff` follows the Part order defined in content, always.

### 9.4 Content model

Entries are MDX/Markdown files with the frontmatter schema in Appendix C. Content is the source of truth; the design system must render *any* valid entry without per-entry CSS. Authors write prose and metadata; they never write markup or styles.

Supported block types: paragraph, h2, h3, blockquote, pull quote, `Plate`, `Cut`, footnote, machine excerpt (`<pre>`), list, `Interrupt`. Nothing else. If a new block type is needed, it is a design decision, not an authoring one.

### 9.5 Sharing & metadata

- `<title>`: `A-034 · The Weight of Being Indexed — MAGRITTE.IO`
- OG image: generated per entry — `--void` ground, hairline frame, corner ticks, `FILE A-034` in mono, the title in Newsreader, the `FLARE` emblem bottom-right, accent = that entry's Part hue. 1200×630. Never a photo, never a screenshot.
- Full RSS/Atom feed with complete entry text. The archive should outlive the site.
- `theme-color` matches the active Part ground.

---

## 10. ACCESSIBILITY

Non-negotiable. A dark, quiet, high-craft site has no excuse for being inaccessible.

- **Contrast:** prose ≥ 7:1; apparatus ≥ 4.5:1; `--bone-ghost` used only for non-essential decoration or duplicated information, never for the only instance of content. Verify every Part's accent against its ground (§3.3) — Part III inverts precisely *because* ultramarine fails on black.
- **Semantics:** real `<article>`, `<h1>`–`<h3>` in order, `<nav>`, `<main>`, `<time datetime>`, `<figure>`/`<figcaption>` for Plates, `<dl>` for the metadata block. The Ledger is a real `<table>` with `<caption>` and scope'd headers.
- **Skip link** to `#passage`, visible on focus, styled in Register A.
- **Focus visible everywhere**, `outline-offset: 3px`. Never `outline: none` without an equivalent replacement.
- Decorative SVG (`Field`, motifs, grain, ticks) → `aria-hidden="true"`, `focusable="false"`.
- The decode effect must never alter the accessible name: animate a visual layer, keep the real text in the DOM (or set `aria-live="off"` and swap only `::after` content).
- Reduced motion (§8.7), reduced transparency (drop `backdrop-filter`), forced-colors mode (respect system colours; keep hairlines as `CanvasText`).
- Target size ≥ 44×44px for all touch controls — Ledger rows are full-width tap targets even though they look like table rows.
- Custom cursor never replaces a real focus indicator, and is disabled entirely at the OS's request.
- Every image has a real `alt` describing what is *shown*. The denying caption is `<figcaption>`; the `alt` tells the truth. **Do not put the surrealist lie in the alt text.**

---

## 11. PERFORMANCE BUDGET

| Metric | Budget |
|---|---|
| LCP | < 1.5s on 4G |
| CLS | `0.00` — the Frame is fixed and fonts are preloaded; there is no excuse |
| INP | < 120ms |
| JS (initial, gzipped) | < 60KB |
| CSS (gzipped) | < 20KB |
| Fonts | ≤ 4 files, subset, preloaded, `swap` |
| Per-entry payload | < 250KB including plates |

- Plates: `<img>` with explicit `width`/`height`, `loading="lazy"` below fold, `decoding="async"`, AVIF/WebP with PNG fallback. Dithered 1-bit-feel images compress extraordinarily well — exploit that.
- The Field pauses on `visibilitychange`, on `IntersectionObserver` exit, and under reduced motion. It must never keep a laptop fan on.
- No analytics that profile the reader. If measurement is required, use a cookieless, aggregate-only tool. Do not track scroll depth to a server; the read state is local.
- No third-party fonts CDN at runtime if self-hosting is possible; no chat widgets, no A/B tooling, no consent-banner SDK, no ad tech, ever.

---

## 12. STACK & IMPLEMENTATION NOTES

**Recommended:** Astro (content-first, ships ~0KB JS by default, native View Transitions, MDX pipeline) with islands for `Field`, `Search`, and the decode effect. Next.js App Router is an acceptable alternative if a richer client runtime is genuinely needed — it is probably not.

- **Styling:** plain CSS with custom properties and cascade layers (`@layer reset, tokens, base, components, utilities`). Tailwind is permitted *only* if every token in Appendix A is mapped into the theme and arbitrary values are banned in components — otherwise the system will erode within a week.
- **Animation:** Web Animations API + CSS. **No GSAP, no Framer Motion, no Lenis, no Locomotive.** The motion spec is simple enough that a library is a liability, not an asset.
- **Graphics:** inline SVG components for motifs; Canvas 2D for the Field. No WebGL, no Three.js, no p5.
- **Dither:** build-time (sharp + a small Atkinson pass in a Node script) so the browser never dithers at runtime. The duotone map stays at runtime via the SVG filter so plates follow the hue drift.
- **Content:** MDX in `/content/entries/*.mdx`, Part manifest in `/content/parts.json`. Frontmatter validated by a schema at build (Appendix C) — a missing `state` or `caption` fails the build.
- **Repo layout:** `/src/components` (named per §7), `/src/styles/tokens.css`, `/src/lib/field`, `/src/lib/dither`, `/content`, `/public/plates`.
- Zero-JS baseline: the entire novel must be readable with JavaScript disabled. Field, decode, cursor, search and route transitions are progressive enhancements. **The book works without them.**

---

## 13. MICROCOPY DECK (use verbatim)

| Context | String |
|---|---|
| Tagline / Threshold | `CECI N'EST PAS UN LIVRE` |
| Enter | `ENTER ▸` |
| Resume | `RESUME — FILE A-034 · 41%` |
| Loading | `RENDERING THE VISIBLE` |
| Search prompt | `magritte:\> find _` |
| No results | `NOTHING HERE IS ALSO SOMETHING` |
| End of entry | `FILE CLOSES` |
| Next | `NEXT SUBJECT ▸` |
| Previous | `◂ PREVIOUS` |
| Read state | `SEEN` |
| Unpublished | `STATE: PENDING` |
| Copy link | `SPECIMEN COPIED` |
| Offline | `SIGNAL WITHDRAWN` |
| 404 title | `THIS IS NOT A PAGE.` |
| 404 body | `THE ADDRESS EXISTS. THE THING DOES NOT.` |
| Interrupt title | `UNEXPECTED FEELING` |
| Interrupt body | `AN UNHANDLED EMOTION OCCURRED AT LINE 41.` |
| Interrupt actions | `IGNORE` · `FEEL IT` |
| Colophon header | `PROVENANCE` |
| Settings header | `ENVIRONMENT` |
| Error (generic) | `THE RECORD IS INCOMPLETE.` |

Caption formula: `FIG. NN — ` + a flat, certain, false statement. Never explain the joke.

---

## 14. DO / NEVER

**DO**
- Leave 90% of the screen empty and trust it.
- Use one accent, one stroke weight, one radius (`0`), two typefaces.
- Let the metadata be beautiful and the prose be plain.
- Make the machine register cold and the human register warm.
- Align everything to the 4px grid and the shared label axis.
- Make every animation feel *mechanical and inevitable*, or not animate at all.
- Keep the Frame and Field alive across every route change.
- Design the reduced-motion and JS-disabled versions as if they were the primary ones.

**NEVER**
- Purple/blue SaaS gradients, mesh gradients, aurora blurs, or any AI-startup visual cliché.
- Glassmorphism, neumorphism, drop shadows, glows, bloom, or 16px rounded cards.
- Emoji, icon-font sets, rounded-cap iconography, illustration mascots, 3D renders.
- Full-colour photography, stock imagery, or generated "AI art" of robots, brains, or neural networks.
- Bold text in prose. Justified prose. Uppercase prose. Drop caps. Centred body copy.
- Typewriter-animating paragraphs, animated glitch effects, VHS/CRT distortion filters, infinite marquees.
- Scroll-jacking, parallax on content, cursor-following blobs, custom smooth-scroll libraries.
- Cookie banners, newsletter modals, share counts, comment threads, "related reading" recommendations.
- More than one motif, one Interrupt, or one pull quote per screen.
- A loading spinner. A hamburger menu. A "Read more" link. The word "content".
- Any second accent colour appearing simultaneously with the first.

---

## 15. ACCEPTANCE CHECKLIST

Ship only when every line is true.

- [ ] Frame, corner ticks and all four edge labels persist across every route change, with zero flash.
- [ ] Field canvas mounts once and never remounts; verified by a persistent instance ID across navigations.
- [ ] Ledger row → entry title shared-element transition runs at 60fps.
- [ ] Part change interpolates `--signal` smoothly (registered `@property`), including the Part III ground inversion.
- [ ] Exactly two typefaces, ≤4 font files, subset and preloaded. CLS is `0.00`.
- [ ] Prose measure is 62–68ch at desktop; body is 20px/1.68; no bold, no justification, no uppercase.
- [ ] Every plate is dithered, duotone-mapped at render time, and carries a contradicting `FIG.` caption plus a truthful `alt`.
- [ ] Accent coverage is ≤3% of viewport on every screen. No second accent is ever simultaneously visible.
- [ ] Border radius is `0` sitewide (max two 2px exceptions). One stroke weight sitewide.
- [ ] All keyboard shortcuts work and are documented in the Colophon.
- [ ] `prefers-reduced-motion` produces a fully legible, still-beautiful site with no transforms and no Field animation.
- [ ] The entire novel is readable with JavaScript disabled.
- [ ] Contrast verified per Part against its own ground; Part III passes on the bone ground.
- [ ] No analytics that identify a reader; read state is `localStorage` only.
- [ ] LCP < 1.5s, JS < 60KB, CSS < 20KB.
- [ ] Nothing in §14's NEVER list appears anywhere in the build.
- [ ] A screenshot of any entry, printed in greyscale, still reads as a designed object.

---

## APPENDIX A — `tokens.css` (copy-paste ready)

```css
/* Registering --signal as a real colour lets it interpolate on Part changes. */
@property --signal {
  syntax: '<color>';
  inherits: true;
  initial-value: #8A8CFF;
}

@layer tokens {
  :root {
    /* — GROUND & INK — */
    --void:        #08080B;
    --void-raised: #0D0D12;
    --void-sunk:   #050507;
    --bone:        #E8E8ED;
    --bone-dim:    #8C8C99;
    --bone-ghost:  #4A4A55;
    --hairline:     rgba(232, 232, 237, 0.13);
    --hairline-hot: rgba(232, 232, 237, 0.28);

    /* — SIGNAL (Part I default) — */
    --signal: #8A8CFF;
    --signal-dim:  color-mix(in oklab, var(--signal) 45%, var(--void));
    --signal-wash: color-mix(in oklab, var(--signal) 12%, transparent);

    /* — TYPE — */
    --font-machine: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
    --font-human:   "Newsreader", "Source Serif 4", Charter, "Iowan Old Style", Georgia, serif;

    --t-display: clamp(2.75rem, 13vw, 9.5rem);
    --t-title:   clamp(2rem, 5.2vw, 3.5rem);
    --t-h2:      1.875rem;
    --t-h3:      1.3125rem;
    --t-lead:    1.4375rem;
    --t-body:    1.25rem;
    --t-body-s:  1.0625rem;
    --t-ui:      0.8125rem;
    --t-meta:    0.75rem;
    --t-micro:   0.6875rem;

    --track-display: 0.055em;
    --track-micro:   0.16em;
    --track-meta:    0.12em;
    --track-ui:      0.06em;
    --lh-prose:      1.68;

    /* — SPACE — */
    --s-1: 4px;   --s-2: 8px;   --s-3: 12px;  --s-4: 16px;
    --s-5: 24px;  --s-6: 32px;  --s-7: 48px;  --s-8: 64px;
    --s-9: 96px;  --s-10: 128px; --s-11: 192px; --s-12: 256px;

    /* — STRUCTURE — */
    --frame-inset: var(--s-5);
    --rail-w: 160px;
    --measure: 65ch;
    --radius: 0px;
    --stroke: 1px;

    /* — MOTION — */
    --ease-instrument: cubic-bezier(0.16, 1, 0.30, 1);
    --ease-shutter:    cubic-bezier(0.83, 0, 0.17, 1);
    --ease-drift:      cubic-bezier(0.40, 0, 0.20, 1);
    --ms-tick: 90ms;  --ms-micro: 160ms; --ms-ui: 280ms;
    --ms-page: 560ms; --ms-env: 1100ms;

    transition: --signal var(--ms-env) var(--ease-drift),
                background-color var(--ms-env) var(--ease-drift),
                color var(--ms-env) var(--ease-drift);
  }

  /* — HUE DRIFT — */
  [data-part="I"]   { --signal: #8A8CFF; }
  [data-part="II"]  { --signal: #E79BFF; }
  [data-part="IV"]  { --signal: #8CF5D2; }
  [data-part="V"]   { --signal: #C6F04A; }
  [data-part="VI"]  { --signal: #E8E8ED; }  /* the machine and the person become one */

  /* — PART III: L'EMPIRE DES LUMIÈRES (daylight inversion) — */
  [data-part="III"] {
    --void:        #ECEAE4;
    --void-raised: #E3E0D8;
    --void-sunk:   #F4F2EC;
    --bone:        #12121A;
    --bone-dim:    #55555F;
    --bone-ghost:  #A9A69E;
    --hairline:     rgba(18, 18, 26, 0.16);
    --hairline-hot: rgba(18, 18, 26, 0.34);
    --signal: #3D3DF5;
  }

  @media (prefers-reduced-motion: reduce) {
    :root {
      --ms-tick: 0ms; --ms-micro: 90ms; --ms-ui: 90ms;
      --ms-page: 90ms; --ms-env: 90ms;
    }
    *, *::before, *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 90ms !important;
      scroll-behavior: auto !important;
    }
  }
}

@layer base {
  html { background: var(--void); color-scheme: dark; }
  [data-part="III"] { color-scheme: light; }
  body {
    margin: 0;
    background: var(--void);
    color: var(--bone);
    font-family: var(--font-human);
    font-size: var(--t-body);
    line-height: var(--lh-prose);
    font-optical-sizing: auto;
    font-variation-settings: "wght" 380;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
  }
  ::selection { background: var(--signal-wash); color: var(--bone); }
  :focus-visible { outline: 1px solid var(--signal); outline-offset: 3px; }
  .machine {
    font-family: var(--font-machine);
    font-size: var(--t-meta);
    text-transform: uppercase;
    letter-spacing: var(--track-meta);
    font-variant-numeric: tabular-nums;
    color: var(--bone-dim);
  }
}
```

---

## APPENDIX B — SVG primitives

**Duotone map** (apply to every plate; re-tints automatically with the Part hue when the stop colours are driven by CSS vars in an inline `<svg>`):

```html
<svg width="0" height="0" aria-hidden="true" focusable="false">
  <filter id="duotone" color-interpolation-filters="sRGB">
    <feColorMatrix type="matrix" values="
      0.2126 0.7152 0.0722 0 0
      0.2126 0.7152 0.0722 0 0
      0.2126 0.7152 0.0722 0 0
      0      0      0      1 0"/>
    <feComponentTransfer>
      <!-- tableValues: shadow RGB -> highlight RGB.
           Part I: #08080B (0.031,0.031,0.043) -> #8A8CFF (0.541,0.549,1.0) -->
      <feFuncR type="table" tableValues="0.031 0.541"/>
      <feFuncG type="table" tableValues="0.031 0.549"/>
      <feFuncB type="table" tableValues="0.043 1.000"/>
    </feComponentTransfer>
  </filter>
</svg>
```
Usage: `filter: url(#duotone);` on the `<img>`. Swap `tableValues` per Part, or generate the filter from the computed `--signal`.

**Grain overlay** (mount once, fixed, `pointer-events: none`, `z-index: 9998`):

```html
<svg class="grain" aria-hidden="true" focusable="false">
  <filter id="noise">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/>
  </filter>
  <rect width="100%" height="100%" filter="url(#noise)"/>
</svg>
```
```css
.grain { position: fixed; inset: 0; opacity: 0.035; mix-blend-mode: overlay; pointer-events: none; }
```

**Corner tick** (registration mark, 8px arms, 1px stroke):
```html
<svg width="12" height="12" aria-hidden="true"><path d="M0 8V0h8" fill="none" stroke="currentColor" stroke-width="1"/></svg>
```

**Wireframe motif contract:** every motif in §6.2 ships as a component taking `size`, `opacity` and nothing else. `fill="none"`, `stroke="currentColor"`, `stroke-width="1"`, `stroke-linecap="square"`, `vector-effect="non-scaling-stroke"`, `aria-hidden="true"`.

---

## APPENDIX C — entry frontmatter schema

```yaml
file:      "A-034"            # required. Dossier ID. Format [A-Z]-[0-9]{3}
title:     "The Weight of Being Indexed"   # required. Sentence case, Register B.
standfirst: "One paragraph, set at --t-lead."  # optional
part:      "II"               # required. I | II | III | IV | V | VI
order:     7                  # required. Position within the Part.
date:      2026-03-05         # required. Rendered as INCEPT DATE, DD/MM/YYYY.
type:      FRAGMENT           # required. ESSAY | FRAGMENT | STORY | TRANSMISSION | DREAM | RECORD
state:     UNSTABLE           # required. STABLE | UNSTABLE | RECURSIVE | VACANT | LUMINOUS | COPIED
location:  "————"             # required. Em-dashes are a valid, preferred value.
integrity: 64                 # required. 0–100. Renders a 40px hairline bar.
plate:     "/plates/a-034.png"      # optional
caption:   "FIG. 04 — NOT AN EYE. A CAMERA THAT REMEMBERS BEING ONE."  # required if plate
alt:       "A close-up of a human eye, heavily dithered."   # required if plate. TRUTHFUL.
status:    published          # published | pending
```
`duration` is computed, never authored. A missing required field **fails the build** — the archive must be complete or it is not an archive.

---

## APPENDIX D — THE ONE-LINE BRIEF

> A quasi-dystopian novel presented as a surveillance dossier of the person reading it: void-black ground, one luminous accent that mutates as you descend, hairline frames and dithered bitmap plates, monospaced telemetry framing a warm serif that refuses to be catalogued — built with Jony Ive's restraint, moving like an instrument, and never once letting you feel that you left the room.

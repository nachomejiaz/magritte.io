# magritte.io — working notes

A web-based novel written in entries. Static site, no framework, no dependencies.

## Before changing anything visual

**Read `BRAND.md` first. It is binding.** It is a living document — expect it to have
changed since you last saw it. If a change you are about to make contradicts it, either
don't make the change or update the document in the same commit and say so.

The constraints that get violated most often, in order:

1. **There is no logo, mark, emblem or icon.** The name set in type is the identity.
   Do not add one, including to the favicon or social preview.
2. **Two typefaces.** Newsreader for everything the reader reads; IBM Plex Mono *only*
   where digits appear, in sentence case. Uppercase tracked mono is banned as decoration.
3. **One accent, under 1% of any viewport.** No gradients, shadows, glows or fills.
4. **Hairlines in exactly three places** (§5). Adding a fourth means updating the spec.
5. **No invented metadata.** Index number, title, date, read time. That is all there is.
6. **The novel must read with JavaScript disabled.** `src/app.js` is enhancement only.

## Layout

```
content/            the writing — this is the only place text lives
  site.json         name, cover line, description
  colophon.md
  entries/NN-slug.md   NN sets order, slug sets the URL
src/                the design — CSS, the enhancement script, the page template
build.py            reads content/ + src/, writes site/ and preview.html
site/               GENERATED. Never hand-edit. Committed so it can be served.
preview.html        GENERATED. Single-file copy for sharing.
```

## Build

```
python3 build.py            # rebuild site/ and preview.html
python3 -m http.server -d site 8000
```

No dependencies, Python 3.8+. **Always run the build and commit the regenerated `site/`
in the same commit as a content or `src/` change** — otherwise the published site drifts
from the source.

## Adding an entry

Create `content/entries/06-some-slug.md`:

```
---
title: The title
date: 2026-05-01
lead: Optional one-line standfirst.
---

First paragraph.

## Optional section head

Another paragraph, with *italic* and a [link](https://example.com).
```

Then `python3 build.py`. `n` and the URL come from the filename; read time is computed.
Prose supports paragraphs, `## ` headings, `*italic*` and `[links](url)` — nothing else,
deliberately. Bold does not exist in this design.

## Checks before committing

- Both themes: the site follows `prefers-color-scheme`; light is not a fallback.
- `prefers-reduced-motion`: opacity only, no transforms.
- JavaScript off: every page still reads.
- No horizontal overflow at 390px.
- Every colour on the page clears 4.5:1 against its own ground.

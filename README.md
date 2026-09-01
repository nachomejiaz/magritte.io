# magritte.io
principe du plaisir

A web-based novel — essays, short stories, journal entries and fragments — written as a
neo-surrealist response to machine intelligence and the commoditization of the self.

The site currently carries **placeholder text**.

## Build

```
python3 build.py                        # regenerate site/ and preview.html
python3 -m http.server -d site 8000     # serve it
```

No dependencies. Python 3.8+.

## Layout

| Path | |
|---|---|
| `content/` | The writing. `site.json`, `colophon.md`, `entries/NN-slug.md`. |
| `src/` | The design. `styles.css`, `app.js`, `layout.html`. |
| `build.py` | Reads `content/` and `src/`, writes `site/` and `preview.html`. |
| `site/` | **Generated.** Committed so it can be served directly. Never hand-edit. |
| `preview.html` | **Generated.** Single-file copy, openable without a server. |

## Adding an entry

Create `content/entries/06-some-slug.md` — the number sets the order, the slug sets the URL:

```
---
title: The title
date: 2026-05-01
lead: Optional one-line standfirst.
---

First paragraph, with *italic* and a [link](https://example.com).

## Optional section head
```

Then run `python3 build.py` and commit the regenerated `site/` alongside it.

## Documents

- **[BRAND.md](./BRAND.md)** — the brand and design system. Living, versioned, binding.
  Read §0 before editing it.
- **[CLAUDE.md](./CLAUDE.md)** — working notes for anyone (or anything) changing the code.

## Deploying

`.github/workflows/pages.yml` publishes `site/` to GitHub Pages and fails the build if the
committed output has drifted from `content/`. It stays inert until Pages is enabled under
**Settings → Pages → Source: GitHub Actions**.

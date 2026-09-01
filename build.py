#!/usr/bin/env python3
"""Build magritte.io.

Reads content/ and src/, writes the static site to site/ and a single-file
copy to preview.html. No dependencies; Python 3.8+.

    python3 build.py

Content
    content/site.json          site name, cover line, description
    content/colophon.md        colophon body
    content/entries/NN-slug.md one entry; NN sets the order, slug sets the URL

Never hand-edit site/ or preview.html — they are generated.
"""

import html
import json
import os
import re
import shutil
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
CONTENT = os.path.join(ROOT, "content")
OUT = os.path.join(ROOT, "site")

WORDS_PER_MINUTE = 230
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


# ---------------------------------------------------------------- markdown

def inline(text):
    """Escape, then apply the three inline forms the prose is allowed to use."""
    out = html.escape(text, quote=False)
    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", out)
    out = re.sub(r"(?<!\w)_([^_\n]+)_(?!\w)", r"<em>\1</em>", out)
    return out


def blocks(body):
    """Markdown subset: blank-line-separated paragraphs, and '## ' headings."""
    out = []
    for raw in re.split(r"\n\s*\n", body.strip()):
        block = " ".join(line.strip() for line in raw.strip().splitlines())
        if not block:
            continue
        if block.startswith("## "):
            out.append("<h2>" + inline(block[3:].strip()) + "</h2>")
        else:
            out.append("<p>" + inline(block) + "</p>")
    return out


def frontmatter(text):
    """Leading '---' block of 'key: value' lines. Returns (dict, body)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, text[end + 4:]


# ---------------------------------------------------------------- content

def long_date(iso):
    d = date.fromisoformat(iso)
    return "%d %s %d" % (d.day, MONTHS[d.month - 1], d.year)


def read_time(paragraphs):
    words = len(re.sub(r"<[^>]+>", " ", " ".join(paragraphs)).split())
    return max(1, round(words / WORDS_PER_MINUTE))


def load():
    site = json.load(open(os.path.join(CONTENT, "site.json")))
    entries = []
    entry_dir = os.path.join(CONTENT, "entries")
    for filename in sorted(os.listdir(entry_dir)):
        if not filename.endswith(".md"):
            continue
        match = re.match(r"^(\d+)-(.+)\.md$", filename)
        if not match:
            raise SystemExit("entry filename must be NN-slug.md: " + filename)
        meta, body = frontmatter(open(os.path.join(entry_dir, filename)).read())
        for required in ("title", "date"):
            if required not in meta:
                raise SystemExit("%s is missing '%s'" % (filename, required))
        entries.append({
            "n": int(match.group(1)),
            "slug": match.group(2),
            "title": meta["title"],
            "date": meta["date"],
            "date_long": long_date(meta["date"]),
            "lead": meta.get("lead"),
            "body": blocks(body),
        })
    entries.sort(key=lambda e: e["n"])
    colophon = blocks(open(os.path.join(CONTENT, "colophon.md")).read())
    return site, entries, colophon


# ---------------------------------------------------------------- fragments

def contents_list(entries, href):
    rows = ['<ol class="contents">']
    for e in entries:
        rows.append(
            '  <li><a href="%s">'
            '<span class="n">%02d</span>'
            '<span class="t">%s</span>'
            '<span class="d">%s</span></a></li>'
            % (href(e), e["n"], html.escape(e["title"]), e["date_long"]))
    rows.append("</ol>")
    return "\n".join(rows)


def entry_html(entry, nxt, href, contents_href):
    out = ["<article>",
           '  <p class="meta"><span>%02d</span><span><time datetime="%s">%s</time></span>'
           "<span>%d min</span></p>" % (entry["n"], entry["date"], entry["date_long"],
                                        read_time(entry["body"])),
           "  <h1>%s</h1>" % html.escape(entry["title"])]
    if entry["lead"]:
        out.append('  <p class="lead">%s</p>' % html.escape(entry["lead"]))
    out.append('  <hr class="rule">')
    out.append('  <div class="prose">')
    out += ["    " + b for b in entry["body"]]
    out.append("  </div>")
    out.append("</article>")
    if nxt:
        out.append('<nav class="next"><span class="label">Next</span>'
                   '<a href="%s">%s</a></nav>' % (href(nxt), html.escape(nxt["title"])))
    else:
        out.append('<nav class="next"><span class="label">End</span>'
                   '<a href="%s">Contents</a></nav>' % contents_href)
    return "\n".join(out)


# ---------------------------------------------------------------- static site

def render(layout, site, title, description, body, root="", current=None):
    page = layout
    for token, value in (
        ("{{title}}", html.escape(title)),
        ("{{description}}", html.escape(description)),
        ("{{name}}", html.escape(site["name"])),
        ("{{root}}", root),
        ("{{nav_index}}", ' aria-current="page"' if current == "index" else ""),
        ("{{nav_colophon}}", ' aria-current="page"' if current == "colophon" else ""),
        ("{{body}}", body + "\n"),
    ):
        page = page.replace(token, value)
    return page


def build_site(site, entries, colophon):
    layout = open(os.path.join(SRC, "layout.html")).read()
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "e"))

    shutil.copy(os.path.join(SRC, "styles.css"), os.path.join(OUT, "styles.css"))
    shutil.copy(os.path.join(SRC, "app.js"), os.path.join(OUT, "app.js"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()

    def write(path, text):
        open(os.path.join(OUT, path), "w").write(text)

    home = ('<p class="cover">%s</p>\n' % html.escape(site["cover"])
            + contents_list(entries, lambda e: "e/%s.html" % e["slug"]))
    write("index.html", render(layout, site, site["name"], site["cover"],
                               home, current="index"))

    for i, entry in enumerate(entries):
        nxt = entries[i + 1] if i + 1 < len(entries) else None
        body = entry_html(entry, nxt,
                          lambda e: "%s.html" % e["slug"],
                          "../index.html")
        write("e/%s.html" % entry["slug"],
              render(layout, site, "%s — %s" % (entry["title"], site["name"]),
                     entry["lead"] or site["description"], body, root="../"))

    write("colophon.html", render(
        layout, site, "Colophon — " + site["name"], site["description"],
        '<div class="plain">\n' + "\n".join("  " + b for b in colophon) + "\n</div>",
        current="colophon"))

    write("404.html", render(
        layout, site, "Not found — " + site["name"], "Not found.",
        '<div class="plain">\n  <p>Not found.</p>\n'
        '  <p><a href="/index.html">Contents</a></p>\n</div>'))

    print("site/      %d entries, index, colophon, 404" % len(entries))


# ---------------------------------------------------------------- preview

def build_preview(site, entries, colophon, path):
    """One self-contained file of the same site, for sharing without a server."""
    css = open(os.path.join(SRC, "styles.css")).read()

    rows = ['<ol class="contents">']
    for e in entries:
        rows.append('  <li><a href="#" data-go="%s"><span class="n">%02d</span>'
                    '<span class="t">%s</span><span class="d">%s</span></a></li>'
                    % (e["slug"], e["n"], html.escape(e["title"]), e["date_long"]))
    rows.append("</ol>")
    pages = {}
    pages["index"] = ('<p class="cover">%s</p>\n' % html.escape(site["cover"])
                      + "\n".join(rows))

    for i, entry in enumerate(entries):
        nxt = entries[i + 1] if i + 1 < len(entries) else None
        body = entry_html(entry, nxt, lambda e: "#", "#")
        if nxt:
            body = body.replace('<a href="#">' + html.escape(nxt["title"]),
                                '<a href="#" data-go="%s">%s' % (nxt["slug"],
                                                                 html.escape(nxt["title"])))
        else:
            body = body.replace('<a href="#">Contents',
                                '<a href="#" data-go="index">Contents')
        pages[entry["slug"]] = body

    pages["colophon"] = ('<div class="plain">\n'
                         + "\n".join("  " + b for b in colophon) + "\n</div>")

    titles = {"index": site["name"], "colophon": "Colophon"}
    for e in entries:
        titles[e["slug"]] = e["title"]

    script = """
(function () {
  "use strict";
  var PAGES = %s, TITLES = %s, NAME = %s;
  var view = document.getElementById("view");
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var FAST = reduce ? 90 : 140;
  var current = "index";

  function mark(id) {
    Array.prototype.forEach.call(document.querySelectorAll("[data-nav]"), function (a) {
      if (a.getAttribute("data-nav") === id) a.setAttribute("aria-current", "page");
      else a.removeAttribute("aria-current");
    });
  }

  function go(id) {
    if (!PAGES[id] || id === current) return;
    current = id;
    view.classList.remove("settled");
    view.classList.add("leaving");
    setTimeout(function () {
      view.innerHTML = PAGES[id];
      document.title = id === "index" ? NAME + " draft" : TITLES[id] + " \\u2014 " + NAME;
      mark(id);
      window.scrollTo(0, 0);
      view.classList.remove("leaving");
      view.classList.add("entering");
      requestAnimationFrame(function () {
        requestAnimationFrame(function () {
          view.classList.remove("entering");
          view.classList.add("settled");
        });
      });
    }, FAST);
  }

  document.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest("[data-go]") : null;
    if (!a) return;
    e.preventDefault();
    go(a.getAttribute("data-go"));
  });
  mark("index");
})();
""" % (json.dumps(pages), json.dumps(titles), json.dumps(site["name"]))

    out = [
        "<title>%s draft</title>" % html.escape(site["name"]),
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        "family=IBM+Plex+Mono&family=Newsreader:ital,opsz,wght@0,6..72,300..500;"
        '1,6..72,300..500&display=swap">',
        "<style>\n" + css + "</style>",
        '<header class="site">'
        '<a class="name" href="#" data-go="index">%s</a>'
        '<nav><a href="#" data-go="index" data-nav="index">Contents</a>'
        '<a href="#" data-go="colophon" data-nav="colophon">Colophon</a></nav>'
        "</header>" % html.escape(site["name"]),
        '<main id="view" class="settled">' + pages["index"] + "</main>",
        "<script>" + script + "</script>",
    ]
    open(path, "w").write("\n".join(out))
    print("preview.html  single file, %d pages" % len(pages))


if __name__ == "__main__":
    site, entries, colophon = load()
    build_site(site, entries, colophon)
    build_preview(site, entries, colophon, os.path.join(ROOT, "preview.html"))

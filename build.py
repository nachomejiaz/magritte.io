#!/usr/bin/env python3
"""Build the magritte.io draft site.

Emits static HTML into site/ (each page works with JavaScript disabled) and a
single-file preview.html for sharing. Content lives in ENTRIES below.
"""
import os, re, html, shutil

OUT = "site"

SITE = {
    "name": "magritte.io",
    "cover": "A novel written in entries, about what is lost when a person becomes a record.",
}

P = [
 "Placeholder. This paragraph sets the measure and the rhythm of the column; replace it with the entry's opening lines. The line length should sit near sixty-four characters, and the leading should feel unhurried enough that the eye returns to the left margin without effort.",
 "A second paragraph, to test the space between them. Nothing here is indented, and nothing is bold. Emphasis, where the writing needs it, arrives as <em>italic</em> and nothing else.",
 "The room was smaller than it had been described, which was the first thing worth noticing and the last thing anyone recorded. Placeholder narrative, standing in for whatever the entry actually says.",
 "Longer placeholder, for testing how the column behaves across several lines without a break: the point of a measure this narrow is that the reader never has to hunt for the beginning of the next line, and the point of the leading is that the paragraph reads as a block of grey rather than a stack of separate sentences. Replace this with real writing and the setting should not need to change.",
 "A short one.",
 "Placeholder continues. Numbers set in the prose take oldstyle figures — 1937, 240, 12 March — so they sit inside the line rather than standing above it. Links look like <a href=\"#\">this</a>, underlined faintly, and only the underline changes on hover.",
 "The last paragraph before the entry ends. It exists to check the spacing between the final line of prose and the link to whatever comes next.",
]

ENTRIES = [
 {"n":1,"slug":"first-entry","title":"Working title of the first entry","date":"2026-01-08","date_h":"8 January 2026",
  "lead":"An optional standfirst, one line long, set slightly larger and dimmer than the prose.",
  "body":[P[0],P[1],P[3],P[5],P[6]]},
 {"n":2,"slug":"second-entry","title":"A shorter one, without a standfirst","date":"2026-01-27","date_h":"27 January 2026",
  "lead":None,"body":[P[2],P[4],P[3],P[6]]},
 {"n":3,"slug":"third-entry","title":"An entry whose title runs to two lines because some of them will","date":"2026-02-14","date_h":"14 February 2026",
  "lead":"Testing a longer title against the standfirst beneath it.",
  "body":[P[0],P[3],P[1],P[2],P[5],P[6]]},
 {"n":4,"slug":"fourth-entry","title":"Fragment","date":"2026-03-12","date_h":"12 March 2026",
  "lead":None,"body":[P[4],P[2],P[6]]},
 {"n":5,"slug":"fifth-entry","title":"Working title of the fifth entry","date":"2026-04-02","date_h":"2 April 2026",
  "lead":"The last of the placeholder entries.","body":[P[0],P[1],P[3],P[2],P[5],P[6]]},
]

COLOPHON = [
 "Placeholder colophon. A few paragraphs on who wrote this, why it exists, and how it was made.",
 "Set in Newsreader, with IBM Plex Mono for dates and numbers. Built as static pages; the transitions between them are a progressive enhancement, and every entry reads with JavaScript disabled.",
 "Nothing here tracks you. There are no analytics, no cookies, no third-party scripts, and no record kept of what you have read.",
]

def words(paras):
    return len(re.sub(r"<[^>]+>", " ", " ".join(paras)).split())

def read_time(paras):
    return max(1, round(words(paras) / 230))

CSS = """/* magritte.io — draft
   Two faces, one accent used almost never, hairlines in three places. */

:root {
  --ground:#0B0B0D;
  --ink:#E7E7EA;
  --ink-dim:#9A9AA3;    /* 6.9:1 */
  --ink-faint:#7C7C86;  /* 4.6:1 — still real information, still readable */
  --rule:rgba(231,231,234,.11);
  --accent:#8E90E8;

  --serif:"Newsreader","Source Serif 4",Charter,"Iowan Old Style",Georgia,serif;
  --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;

  --t-wordmark:1.0625rem;
  --t-cover:clamp(2.25rem,5vw,3.25rem);
  --t-title:clamp(1.75rem,3.4vw,2.5rem);
  --t-h2:1.375rem;
  --t-lead:1.3125rem;
  --t-body:1.1875rem;
  --t-small:.9375rem;
  --t-meta:.75rem;

  --measure:34rem;
  --measure-index:40rem;
  --margin:clamp(24px,7vw,96px);

  --ease:cubic-bezier(.22,1,.36,1);
  --ms-fast:140ms;
  --ms-slow:340ms;
}

@media (prefers-color-scheme: light) {
  :root:not([data-theme="dark"]) {
    --ground:#F4F3F0; --ink:#17171B; --ink-dim:#53535B;
    --ink-faint:#6C6C74; --rule:rgba(23,23,27,.13); --accent:#3E40C8;
  }
}
:root[data-theme="light"] {
  --ground:#F4F3F0; --ink:#17171B; --ink-dim:#53535B;
  --ink-faint:#6C6C74; --rule:rgba(23,23,27,.13); --accent:#3E40C8;
}
:root[data-theme="dark"] {
  --ground:#0B0B0D; --ink:#E7E7EA; --ink-dim:#9A9AA3;
  --ink-faint:#7C7C86; --rule:rgba(231,231,234,.11); --accent:#8E90E8;
}

*,*::before,*::after { box-sizing:border-box; }

html { background:var(--ground); }

body {
  margin:0;
  background:var(--ground);
  color:var(--ink);
  font-family:var(--serif);
  font-size:var(--t-body);
  line-height:1.72;
  font-optical-sizing:auto;
  font-variation-settings:"wght" 380;
  font-variant-numeric:oldstyle-nums;
  -webkit-font-smoothing:antialiased;
  text-rendering:optimizeLegibility;
  padding:0 var(--margin) 128px;
}

::selection { background:var(--accent); color:var(--ground); }

:focus-visible { outline:1px solid var(--accent); outline-offset:2px; }

a { color:inherit; text-decoration:none; }

.skip {
  position:absolute; left:-9999px; top:0;
  font-family:var(--mono); font-size:var(--t-meta);
}
.skip:focus { left:var(--margin); top:8px; padding:6px 8px; background:var(--ground); z-index:10; }

/* ---- header: persists, never re-animates ---- */
.site {
  display:flex; justify-content:space-between; align-items:baseline;
  gap:24px; padding:32px 0 96px;
}
.site .name { font-size:var(--t-wordmark); font-variation-settings:"wght" 400; letter-spacing:-.005em; }
.site nav { display:flex; gap:24px; }
.site nav a, .site .name {
  color:var(--ink-dim);
  transition:color var(--ms-fast) var(--ease);
}
.site .name { color:var(--ink); }
.site nav a { font-size:var(--t-small); }
.site nav a:hover, .site nav a[aria-current="page"] { color:var(--ink); }

/* ---- the swapped region ---- */
#view { max-width:none; }
#view.leaving { opacity:0; transition:opacity var(--ms-fast) var(--ease); }
#view.entering { opacity:0; transform:translateY(6px); }
#view.settled {
  opacity:1; transform:none;
  transition:opacity var(--ms-slow) var(--ease), transform var(--ms-slow) var(--ease);
}

/* ---- cover ---- */
.cover {
  max-width:min(22ch,100%);
  font-size:var(--t-cover); line-height:1.16; letter-spacing:-.018em;
  font-variation-settings:"wght" 350;
  text-wrap:balance; margin:0 0 96px;
}

/* ---- contents ---- */
.contents { list-style:none; margin:0; padding:0; max-width:var(--measure-index); }
.contents li { border-top:1px solid var(--rule); }
.contents li:last-child { border-bottom:1px solid var(--rule); }
.contents a {
  display:grid; grid-template-columns:2.75rem 1fr auto;
  gap:16px; align-items:baseline; padding:18px 0;
}
.contents .n, .contents .d {
  font-family:var(--mono); font-size:var(--t-meta);
  font-variant-numeric:tabular-nums; color:var(--ink-faint);
  letter-spacing:.02em;
}
.contents .t {
  color:var(--ink-dim); text-wrap:pretty;
  transition:color var(--ms-fast) var(--ease);
}
.contents a:hover .t { color:var(--ink); }

@media (max-width:600px) {
  .contents a { grid-template-columns:2.25rem 1fr; row-gap:6px; padding:16px 0; }
  .contents .d { grid-column:2; }
  .site { padding-bottom:64px; }
  .next { margin-top:64px; }
}

/* ---- entry ---- */
article, .plain, .next { max-width:var(--measure); }

.meta {
  font-family:var(--mono); font-size:var(--t-meta); letter-spacing:.02em;
  font-variant-numeric:tabular-nums; color:var(--ink-faint);
  margin:0 0 20px;
}
.meta span + span::before { content:"\\00a0\\00a0·\\00a0\\00a0"; }

h1 {
  font-size:var(--t-title); line-height:1.12; letter-spacing:-.015em;
  font-variation-settings:"wght" 400; text-wrap:balance;
  margin:0; color:var(--ink);
}
.lead {
  font-size:var(--t-lead); line-height:1.55; font-variation-settings:"wght" 340;
  color:var(--ink-dim); margin:20px 0 0; text-wrap:pretty;
}
.rule { width:48px; height:1px; background:var(--rule); border:0; margin:40px 0 40px; }

.prose p { margin:0 0 1.4em; text-wrap:pretty; }
.prose p:last-child { margin-bottom:0; }
.prose em { font-style:italic; }
.prose h2 {
  font-size:var(--t-h2); font-variation-settings:"wght" 400;
  line-height:1.3; margin:2.2em 0 .8em; text-wrap:balance;
}
.prose a {
  border-bottom:1px solid var(--rule);
  transition:border-color var(--ms-fast) var(--ease);
}
.prose a:hover { border-bottom-color:var(--accent); }

/* ---- next ---- */
.next { margin-top:96px; border-top:1px solid var(--rule); padding-top:20px; }
.next .label {
  display:block; font-family:var(--mono); font-size:var(--t-meta);
  letter-spacing:.02em; color:var(--ink-faint); margin-bottom:6px;
}
.next a { color:var(--ink-dim); transition:color var(--ms-fast) var(--ease); }
.next a:hover { color:var(--ink); }

/* ---- colophon / 404 ---- */
.plain p { margin:0 0 1.4em; font-size:var(--t-small); color:var(--ink-dim); text-wrap:pretty; }
.plain p:first-child { color:var(--ink); font-size:var(--t-body); }

@media (prefers-reduced-motion: reduce) {
  *,*::before,*::after {
    transition-duration:90ms !important;
    animation-duration:.01ms !important;
  }
  #view.entering { transform:none; }
}
"""

JS = """/* Progressive enhancement: swap #view instead of reloading, so the header
   never blinks. Every page works without this file. */
(function () {
  "use strict";
  if (!window.fetch || !window.history.pushState) return;

  var view = document.getElementById("view");
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var FAST = reduce ? 90 : 140;
  var cache = Object.create(null);

  function internal(a) {
    return a && a.href && a.origin === location.origin &&
           !a.hasAttribute("download") && a.target !== "_blank";
  }

  function paint(doc, url, push) {
    var next = doc.getElementById("view");
    if (!next) { location.href = url; return; }
    view.innerHTML = next.innerHTML;
    document.title = doc.title;
    if (push) history.pushState({}, "", url);
    window.scrollTo(0, 0);
    Array.prototype.forEach.call(document.querySelectorAll(".site nav a"), function (a) {
      if (a.pathname === location.pathname) a.setAttribute("aria-current", "page");
      else a.removeAttribute("aria-current");
    });
    view.classList.remove("leaving");
    view.classList.add("entering");
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        view.classList.remove("entering");
        view.classList.add("settled");
      });
    });
  }

  function go(url, push) {
    view.classList.remove("settled");
    view.classList.add("leaving");
    var wait = new Promise(function (r) { setTimeout(r, FAST); });
    var load = cache[url] ? Promise.resolve(cache[url]) :
      fetch(url, { credentials: "same-origin" })
        .then(function (r) { if (!r.ok) throw 0; return r.text(); })
        .then(function (t) { cache[url] = t; return t; });
    Promise.all([load, wait]).then(function (v) {
      paint(new DOMParser().parseFromString(v[0], "text/html"), url, push);
    }).catch(function () { location.href = url; });
  }

  document.addEventListener("click", function (e) {
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
    var a = e.target.closest ? e.target.closest("a") : null;
    if (!internal(a) || a.hash) return;
    if (a.href === location.href) { e.preventDefault(); return; }
    e.preventDefault();
    go(a.href, true);
  });

  window.addEventListener("popstate", function () { go(location.href, false); });
})();
"""

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="dark light">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&family=Newsreader:ital,opsz,wght@0,6..72,300..500;1,6..72,300..500&display=swap">
<link rel="stylesheet" href="{root}styles.css">
</head>
<body>
<a class="skip" href="#view">Skip to content</a>
<header class="site">
  <a class="name" href="{root}index.html">magritte.io</a>
  <nav>
    <a href="{root}index.html"{c_index}>Contents</a>
    <a href="{root}colophon.html"{c_col}>Colophon</a>
  </nav>
</header>
<main id="view" class="settled">
"""

FOOT = """</main>
<script src="{root}app.js" defer></script>
</body>
</html>
"""

def page(title, desc, body, root="", current=None):
    return (HEAD.format(title=html.escape(title), desc=html.escape(desc), root=root,
                        c_index=' aria-current="page"' if current == "index" else "",
                        c_col=' aria-current="page"' if current == "colophon" else "")
            + body + FOOT.format(root=root))

def build():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "e"), exist_ok=True)

    open(os.path.join(OUT, "styles.css"), "w").write(CSS)
    open(os.path.join(OUT, "app.js"), "w").write(JS)

    # ---- home ----
    rows = []
    for e in ENTRIES:
        rows.append(
            '    <li><a href="e/{slug}.html">'
            '<span class="n">{n:02d}</span>'
            '<span class="t">{title}</span>'
            '<span class="d">{date_h}</span></a></li>'.format(
                slug=e["slug"], n=e["n"], title=html.escape(e["title"]), date_h=e["date_h"]))
    home = ('  <p class="cover">' + html.escape(SITE["cover"]) + "</p>\n"
            '  <ol class="contents">\n' + "\n".join(rows) + "\n  </ol>\n")
    open(os.path.join(OUT, "index.html"), "w").write(
        page(SITE["name"], SITE["cover"], home, current="index"))

    # ---- entries ----
    for i, e in enumerate(ENTRIES):
        nxt = ENTRIES[i + 1] if i + 1 < len(ENTRIES) else None
        parts = ['  <article>\n',
                 '    <p class="meta"><span>{:02d}</span>'.format(e["n"]),
                 '<span><time datetime="{}">{}</time></span>'.format(e["date"], e["date_h"]),
                 '<span>{} min</span></p>\n'.format(read_time(e["body"])),
                 '    <h1>{}</h1>\n'.format(html.escape(e["title"]))]
        if e["lead"]:
            parts.append('    <p class="lead">{}</p>\n'.format(html.escape(e["lead"])))
        parts.append('    <hr class="rule">\n    <div class="prose">\n')
        for p in e["body"]:
            parts.append("      <p>" + p + "</p>\n")
        parts.append("    </div>\n  </article>\n")
        if nxt:
            parts.append('  <nav class="next"><span class="label">Next</span>'
                         '<a href="{}.html">{}</a></nav>\n'.format(nxt["slug"], html.escape(nxt["title"])))
        else:
            parts.append('  <nav class="next"><span class="label">End</span>'
                         '<a href="../index.html">Contents</a></nav>\n')
        open(os.path.join(OUT, "e", e["slug"] + ".html"), "w").write(
            page(e["title"] + " — " + SITE["name"], e["lead"] or SITE["cover"],
                 "".join(parts), root="../"))

    # ---- colophon ----
    col = '  <div class="plain">\n' + "".join(
        "    <p>" + p + "</p>\n" for p in COLOPHON) + "  </div>\n"
    open(os.path.join(OUT, "colophon.html"), "w").write(
        page("Colophon — " + SITE["name"], COLOPHON[0], col, current="colophon"))

    # ---- 404 ----
    nf = ('  <div class="plain">\n    <p>Not found.</p>\n'
          '    <p><a href="/index.html">Contents</a></p>\n  </div>\n')
    open(os.path.join(OUT, "404.html"), "w").write(page("Not found — " + SITE["name"], "Not found.", nf))

    print("built", OUT + "/:", len(ENTRIES), "entries + index, colophon, 404")

# ---------------------------------------------------------------- preview
# A single self-contained file of the same site, for sharing. The static
# pages in site/ remain the real build; this exists so the draft can be
# opened without a server.

def preview(path="preview.html"):
    import json
    pages = {}

    rows = []
    for e in ENTRIES:
        rows.append(
            '<li><a href="#" data-go="{slug}">'
            '<span class="n">{n:02d}</span>'
            '<span class="t">{title}</span>'
            '<span class="d">{date_h}</span></a></li>'.format(
                slug=e["slug"], n=e["n"], title=html.escape(e["title"]), date_h=e["date_h"]))
    pages["index"] = ('<p class="cover">' + html.escape(SITE["cover"]) + "</p>"
                      '<ol class="contents">' + "".join(rows) + "</ol>")

    for i, e in enumerate(ENTRIES):
        nxt = ENTRIES[i + 1] if i + 1 < len(ENTRIES) else None
        h = ['<article><p class="meta"><span>{:02d}</span>'.format(e["n"]),
             '<span><time datetime="{}">{}</time></span>'.format(e["date"], e["date_h"]),
             '<span>{} min</span></p>'.format(read_time(e["body"])),
             "<h1>{}</h1>".format(html.escape(e["title"]))]
        if e["lead"]:
            h.append('<p class="lead">{}</p>'.format(html.escape(e["lead"])))
        h.append('<hr class="rule"><div class="prose">')
        h += ["<p>" + p + "</p>" for p in e["body"]]
        h.append("</div></article>")
        if nxt:
            h.append('<nav class="next"><span class="label">Next</span>'
                     '<a href="#" data-go="{}">{}</a></nav>'.format(nxt["slug"], html.escape(nxt["title"])))
        else:
            h.append('<nav class="next"><span class="label">End</span>'
                     '<a href="#" data-go="index">Contents</a></nav>')
        pages[e["slug"]] = "".join(h)

    pages["colophon"] = ('<div class="plain">' +
                         "".join("<p>" + p + "</p>" for p in COLOPHON) + "</div>")

    titles = {"index": SITE["name"], "colophon": "Colophon"}
    for e in ENTRIES:
        titles[e["slug"]] = e["title"]

    out = []
    out.append("<title>magritte.io draft</title>")
    out.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
    out.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    out.append('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
               'family=IBM+Plex+Mono&family=Newsreader:ital,opsz,wght@0,6..72,300..500;'
               '1,6..72,300..500&display=swap">')
    out.append("<style>\n" + CSS.replace("body {", "body, .root {", 1) + "\n</style>")
    out.append('<header class="site">'
               '<a class="name" href="#" data-go="index">magritte.io</a>'
               '<nav><a href="#" data-go="index" data-nav="index">Contents</a>'
               '<a href="#" data-go="colophon" data-nav="colophon">Colophon</a></nav>'
               "</header>")
    out.append('<main id="view" class="settled">' + pages["index"] + "</main>")
    out.append("<script>\n(function(){\n"
               '  "use strict";\n'
               "  var PAGES = " + json.dumps(pages) + ";\n"
               "  var TITLES = " + json.dumps(titles) + ";\n"
               """  var view = document.getElementById("view");
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var FAST = reduce ? 90 : 140;
  var current = "index";

  function mark(id){
    Array.prototype.forEach.call(document.querySelectorAll("[data-nav]"), function(a){
      if (a.getAttribute("data-nav") === id) a.setAttribute("aria-current","page");
      else a.removeAttribute("aria-current");
    });
  }

  function go(id){
    if (!PAGES[id] || id === current) return;
    current = id;
    view.classList.remove("settled");
    view.classList.add("leaving");
    setTimeout(function(){
      view.innerHTML = PAGES[id];
      document.title = TITLES[id] === "magritte.io" ? "magritte.io draft" : TITLES[id] + " \u2014 magritte.io";
      mark(id);
      window.scrollTo(0,0);
      view.classList.remove("leaving");
      view.classList.add("entering");
      requestAnimationFrame(function(){ requestAnimationFrame(function(){
        view.classList.remove("entering");
        view.classList.add("settled");
      });});
    }, FAST);
  }

  document.addEventListener("click", function(e){
    var a = e.target.closest ? e.target.closest("[data-go]") : null;
    if (!a) return;
    e.preventDefault();
    go(a.getAttribute("data-go"));
  });
  mark("index");
})();
</script>""")

    open(path, "w").write("\n".join(out))
    print("built", path)


if __name__ == "__main__":
    build()
    preview("preview.html")

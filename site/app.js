/* Progressive enhancement: swap #view instead of reloading, so the header
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

/*
  Reveal-on-scroll, nothing else. Content is fully visible without this file;
  it only arms hidden starting states once it confirms it can animate them.
*/
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduceMotion) {
    return;
  }

  document.documentElement.classList.add("js-reveal");

  var loadEls = document.querySelectorAll('[data-reveal="load"]');
  loadEls.forEach(function (el, i) {
    window.setTimeout(function () {
      el.classList.add("is-visible");
    }, i * 80);
  });

  var deferredEls = document.querySelectorAll(
    '[data-reveal="scroll"], [data-reveal="row"]'
  );

  if (!("IntersectionObserver" in window) || deferredEls.length === 0) {
    deferredEls.forEach(function (el) {
      el.classList.add("is-visible");
    });
    return;
  }

  var io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  deferredEls.forEach(function (el) {
    io.observe(el);
  });
})();

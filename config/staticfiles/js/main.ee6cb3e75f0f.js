document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.querySelector(".navbar");
  if (navbar) {
    window.addEventListener("scroll", () => {
      navbar.classList.toggle("sticky", window.scrollY > 10);
    });
  }

  const burger = document.getElementById("burger");
  const menu = document.getElementById("navMenu");
  const closeMenuBtn = document.getElementById("closeMenu");

  function openMobileMenu() {
    if (!menu) return;
    menu.classList.add("show");
    burger?.setAttribute("aria-expanded", "true");
  }

  function closeMobileMenu() {
    if (!menu) return;
    menu.classList.remove("show");
    burger?.setAttribute("aria-expanded", "false");
  }

  if (burger && menu) {
    burger.addEventListener("click", () => {
      if (menu.classList.contains("show")) closeMobileMenu();
      else openMobileMenu();
    });
  }
  closeMenuBtn?.addEventListener("click", closeMobileMenu);

  menu?.addEventListener("click", (e) => {
    const link = e.target.closest("a");
    if (!link) return;
    if (link.classList.contains("dropdown-toggle")) return;
    if ((link.getAttribute("href") || "").trim() === "#") return;
    closeMobileMenu();
  });

  document.querySelectorAll(".dropdown-toggle").forEach((toggle) => {
    toggle.addEventListener("click", (e) => {
      e.preventDefault();
      const parent = toggle.closest(".dropdown");
      if (!parent) return;

      document.querySelectorAll(".dropdown").forEach((d) => {
        if (d !== parent) d.classList.remove("active");
      });
      parent.classList.toggle("active");
    });
  });

  document.addEventListener("click", (e) => {
    if (!e.target.closest(".dropdown")) {
      document.querySelectorAll(".dropdown").forEach((d) => d.classList.remove("active"));
    }
  });

  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    document.querySelectorAll(".dropdown").forEach((d) => d.classList.remove("active"));
    closeMobileMenu();
  });

  const highlightSection = document.querySelector(".highlight");
  const counters = Array.from(document.querySelectorAll(".count-up"));

  function animateCount(el, toValue, durationMs = 1200) {
    const start = performance.now();
    const from = 0;

    function tick(now) {
      const t = Math.min(1, (now - start) / durationMs);
      const eased = 1 - Math.pow(1 - t, 3);
      const current = Math.round(from + (toValue - from) * eased);
      el.textContent = String(current);
      if (t < 1) requestAnimationFrame(tick);
    }

    requestAnimationFrame(tick);
  }

  if (highlightSection && counters.length > 0 && "IntersectionObserver" in window) {
    let hasAnimated = false;

    const observer = new IntersectionObserver(
      (entries) => {
        const entry = entries[0];
        if (!entry?.isIntersecting || hasAnimated) return;
        hasAnimated = true;

        counters.forEach((el) => {
          const raw = el.getAttribute("data-count") || "0";
          const target = Number.parseInt(raw, 10) || 0;
          animateCount(el, target);
        });

        observer.disconnect();
      },
      { threshold: 0.35 }
    );

    observer.observe(highlightSection);
  } else {
    counters.forEach((el) => {
      const raw = el.getAttribute("data-count") || "0";
      const target = Number.parseInt(raw, 10) || 0;
      el.textContent = String(target);
    });
  }
});

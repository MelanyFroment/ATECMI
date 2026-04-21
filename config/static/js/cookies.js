(() => {
  const KEY = "atecmi_cookie_consent_v1";

  function qs(id) {
    return document.getElementById(id);
  }

  function showBanner() {
    const banner = qs("cookieBanner");
    if (!banner) return;
    banner.classList.remove("hidden");
  }

  function hideBanner() {
    const banner = qs("cookieBanner");
    if (!banner) return;
    banner.classList.add("hidden");
  }

  function setConsent(value) {
    try {
      localStorage.setItem(KEY, value);
    } catch (e) {
      // ignore
    }
    hideBanner();
  }

  document.addEventListener("DOMContentLoaded", () => {
    let existing = null;
    try {
      existing = localStorage.getItem(KEY);
    } catch (e) {
      existing = null;
    }

    if (!existing) showBanner();

    const accept = qs("cookieAccept");
    const reject = qs("cookieReject");
    if (accept) accept.addEventListener("click", () => setConsent("accepted"));
    if (reject) reject.addEventListener("click", () => setConsent("rejected"));
  });
})();


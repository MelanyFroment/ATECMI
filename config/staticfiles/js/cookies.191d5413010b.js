(() => {
  const KEY = "atecmi_cookie_consent_v1";
  const MAX_AGE_SECONDS = 60 * 60 * 24 * 183;
  const COOKIE_PATH = "/";

  function qs(id) {
    return document.getElementById(id);
  }

  function setCookie(name, value, maxAgeSeconds) {
    const encodedName = encodeURIComponent(name);
    const encodedValue = encodeURIComponent(value);
    const secure = window.location.protocol === "https:" ? "; Secure" : "";
    document.cookie = `${encodedName}=${encodedValue}; Path=${COOKIE_PATH}; Max-Age=${maxAgeSeconds}; SameSite=Lax${secure}`;
  }

  function getCookie(name) {
    const encodedName = encodeURIComponent(name) + "=";
    const parts = document.cookie.split(";").map((p) => p.trim());
    for (const part of parts) {
      if (part.startsWith(encodedName)) {
        return decodeURIComponent(part.slice(encodedName.length));
      }
    }
    return null;
  }

  function deleteCookie(name) {
    const encodedName = encodeURIComponent(name);
    const secure = window.location.protocol === "https:" ? "; Secure" : "";
    document.cookie = `${encodedName}=; Path=${COOKIE_PATH}; Max-Age=0; SameSite=Lax${secure}`;
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

  function applyConsent(value) {
    setCookie(KEY, value, MAX_AGE_SECONDS);
    hideBanner();
  }

  document.addEventListener("DOMContentLoaded", () => {
    const existing = getCookie(KEY);
    if (!existing) {
      showBanner();
    }

    const accept = qs("cookieAccept");
    const reject = qs("cookieReject");
    if (accept) accept.addEventListener("click", () => applyConsent("accepted"));
    if (reject) reject.addEventListener("click", () => applyConsent("rejected"));

    window.atecmiCookieConsent = window.atecmiCookieConsent || {};
    window.atecmiCookieConsent.open = () => showBanner();
    window.atecmiCookieConsent.reset = () => {
      deleteCookie(KEY);
      showBanner();
    };
  });
})();

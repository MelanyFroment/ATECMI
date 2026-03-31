
document.addEventListener("DOMContentLoaded", function() {
    const navbar = document.querySelector(".navbar");
    const heroHeight = document.querySelector(".hero")?.offsetHeight || 0;

    window.addEventListener("scroll", () => {
        if (window.scrollY > heroHeight) {
            navbar.classList.add("sticky");
        } else {
            navbar.classList.remove("sticky");
        }
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const burger = document.getElementById("burger");
    const menu = document.getElementById("navMenu");

    burger.addEventListener("click", function () {
        menu.classList.toggle("show");
    });
});
document.addEventListener("DOMContentLoaded", () => {
    const btn = document.querySelector(".cta");
    if(btn) {
        btn.addEventListener("click", () => alert("Formulaire de contact à venir !"));
    }
});


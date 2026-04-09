document.addEventListener("DOMContentLoaded", () => {

    // DROPDOWN
    document.querySelectorAll('.dropdown-toggle').forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();

            const parent = this.parentElement;

            document.querySelectorAll('.dropdown').forEach(d => {
                if (d !== parent) {
                    d.classList.remove('active');
                }
            });

            parent.classList.toggle('active');
        });
    });

    // CLICK OUTSIDE
    document.addEventListener('click', function (e) {
        if (!e.target.closest('.dropdown')) {
            document.querySelectorAll('.dropdown').forEach(d => {
                d.classList.remove('active');
            });
        }
    });

    // NAVBAR STICKY
    const navbar = document.querySelector(".navbar");
    const hero = document.querySelector(".hero");

    if (navbar && hero) {
        const heroHeight = hero.offsetHeight;

        window.addEventListener("scroll", () => {
            navbar.classList.toggle("sticky", window.scrollY > heroHeight);
        });
    }

    // BURGER MENU
    const burger = document.getElementById("burger");
    const menu = document.getElementById("navMenu");

    if (burger && menu) {
        burger.addEventListener("click", () => {
            menu.classList.toggle("show");
        });
    }

    // CTA
    const btn = document.querySelector(".cta");

    if (btn) {
        btn.addEventListener("click", () => {
            alert("Formulaire de contact à venir !");
        });
    }

});

document.addEventListener("DOMContentLoaded", () => {
    const dropdown = document.querySelector(".dropdown");
    const toggle = dropdown.querySelector(".dropdown-toggle");

    toggle.addEventListener("click", (e) => {
        e.preventDefault(); // empêche le #
        dropdown.classList.toggle("active");
    });

    // Fermer si clic en dehors
    document.addEventListener("click", (e) => {
        if (!dropdown.contains(e.target)) {
            dropdown.classList.remove("active");
        }
    });
});
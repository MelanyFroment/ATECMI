// document.addEventListener("DOMContentLoaded", () => {
//     const cards = document.querySelector(".cards");
//     if(cards){
//         // duplique toutes les cartes pour créer l'effet boucle infinie
//         cards.innerHTML += cards.innerHTML;
//     }
// });

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

document.addEventListener("DOMContentLoaded", () => {
    const dropdowns = document.querySelectorAll(".dropdown");

    dropdowns.forEach(drop => {
        const link = drop.querySelector("a"); // le lien principal
        link.addEventListener("click", (e) => {
            e.preventDefault(); // empêche le saut de page
            drop.classList.toggle("active");
        });
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const container = document.querySelector(".cards");
    if (!container) return;

    const speed = 0.5; // px/frame
    const spacing = 100; // espace entre les logos
    const logos = Array.from(container.children);

    // CSS container
    container.style.position = "relative";
    container.style.height = "210px"; // adapte à tes logos
    container.style.overflow = "hidden";

    // positionner chaque logo absolument
    let currentX = 150; 
    logos.forEach(logo => {
        logo.style.position = "absolute";
        logo.style.left = `${currentX}px`;
        logo.style.top = "0";
        currentX += logo.offsetWidth + spacing;
        logo.dataset.x = logo.style.left.replace("px", "");
    });

    function animate() {
        logos.forEach(logo => {
            let x = parseFloat(logo.dataset.x);
            x -= speed;
            // si le logo sort complètement à gauche
            if (x + logo.offsetWidth < 0) {
                // repositionner à droite derrière le logo le plus à droite
                const maxRight = Math.max(...logos.map(l => parseFloat(l.dataset.x) + l.offsetWidth + spacing));
                x = maxRight;
            }
            logo.style.left = `${x}px`;
            logo.dataset.x = x;
        });

        requestAnimationFrame(animate);
    }

    animate();
});
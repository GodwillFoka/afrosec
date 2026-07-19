// AfroSec — Main JavaScript
document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scroll pour les ancres
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                document.querySelector(href).scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Navbar background transition au scroll
    const navbar = document.querySelector('.navbar-afrosec');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.style.background = 'rgba(15, 23, 42, 0.98) !important';
            } else {
                navbar.style.background = 'rgba(15, 23, 42, 0.95) !important';
            }
        });
    }

});

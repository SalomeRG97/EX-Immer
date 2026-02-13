/* ==========================================================================
   Ex-Immer Real Estate - Main JS
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    console.log('Ex-Immer Real Estate Site Loaded');

    // Scroll Animations
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Automatically add fade-in class to major layout elements
    document.querySelectorAll('.section, .card, .hero h1, .hero p').forEach(el => {
        el.classList.add('fade-in');
    });

    // Observe all fade-in elements (including those manually added in HTML)
    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });
});

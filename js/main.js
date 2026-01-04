// ===== MOBILE NAVIGATION =====
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            this.classList.toggle('active');
            navMenu.classList.toggle('active');
            
            // Prevent body scroll when menu is open
            document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
        });
        
        // Close menu when clicking links
        document.querySelectorAll('.nav-menu a').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!hamburger.contains(e.target) && !navMenu.contains(e.target)) {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }
    
    // ===== FAQ ACCORDION =====
    document.querySelectorAll('.faq-question').forEach(question => {
        question.addEventListener('click', function() {
            const faqItem = this.parentElement;
            const answer = faqItem.querySelector('.faq-answer');
            
            // Close other open FAQs
            document.querySelectorAll('.faq-item').forEach(item => {
                if (item !== faqItem && item.classList.contains('active')) {
                    item.classList.remove('active');
                    item.querySelector('.faq-answer').style.maxHeight = null;
                }
            });
            
            // Toggle current FAQ
            faqItem.classList.toggle('active');
            if (faqItem.classList.contains('active')) {
                answer.style.maxHeight = answer.scrollHeight + 'px';
            } else {
                answer.style.maxHeight = null;
            }
        });
    });
    
    // ===== SMOOTH SCROLLING =====
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            if (href === '#' || href === '#!') return;
            
            const targetElement = document.querySelector(href);
            if (targetElement) {
                e.preventDefault();
                
                // Close mobile menu if open
                if (hamburger && navMenu) {
                    hamburger.classList.remove('active');
                    navMenu.classList.remove('active');
                    document.body.style.overflow = '';
                }
                
                window.scrollTo({
                    top: targetElement.offsetTop - 100,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // ===== FIX MOBILE VIEWPORT =====
    function fixMobileViewport() {
        const viewport = document.querySelector('meta[name="viewport"]');
        if (viewport) {
            viewport.setAttribute('content', 'width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes');
        }
    }
    
    fixMobileViewport();
    
    // ===== FORM VALIDATION HELPERS =====
    document.querySelectorAll('input[type="tel"]').forEach(input => {
        input.addEventListener('input', function() {
            this.value = this.value.replace(/\D/g, '').slice(0, 10);
        });
    });
    
    // ===== UPDATE COPYRIGHT YEAR =====
    const yearElements = document.querySelectorAll('.footer-bottom p');
    yearElements.forEach(element => {
        element.innerHTML = element.innerHTML.replace('2026', new Date().getFullYear());
    });
    
    // ===== MOBILE-SPECIFIC FIXES =====
    function applyMobileFixes() {
        if (window.innerWidth <= 768) {
            // Fix overflowing elements
            document.querySelectorAll('.container, .premium-container').forEach(container => {
                container.style.padding = '0 15px';
                container.style.width = '100%';
                container.style.maxWidth = '100%';
                container.style.overflowX = 'hidden';
            });
            
            // Fix image containers
            document.querySelectorAll('img').forEach(img => {
                img.style.maxWidth = '100%';
                img.style.height = 'auto';
            });
            
            // Fix button widths
            document.querySelectorAll('.btn-primary, .btn-secondary').forEach(btn => {
                if (btn.closest('.hero-cta') || btn.closest('.cta-buttons')) {
                    btn.style.width = '100%';
                    btn.style.marginBottom = '10px';
                }
            });
        }
    }
    
    applyMobileFixes();
    window.addEventListener('resize', applyMobileFixes);
});

// ===== FIX IOS ZOOM ISSUE =====
document.addEventListener('touchstart', function() {}, { passive: true });

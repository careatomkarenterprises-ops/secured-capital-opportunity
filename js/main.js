// ===== UNIFIED MOBILE MENU FOR ALL PAGES =====
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded - initializing navigation');
    
    // Get hamburger and menu elements
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');
    
    // Only proceed if elements exist
    if (hamburger && navMenu) {
        console.log('Navigation elements found');
        
        // Mobile menu toggle
        hamburger.addEventListener('click', function(e) {
            e.stopPropagation(); // Prevent event bubbling
            console.log('Hamburger clicked');
            
            // Toggle active classes
            this.classList.toggle('active');
            navMenu.classList.toggle('active');
            
            // Prevent body scroll when menu is open
            if (navMenu.classList.contains('active')) {
                document.body.style.overflow = 'hidden';
                console.log('Menu opened');
            } else {
                document.body.style.overflow = '';
                console.log('Menu closed');
            }
        });
        
        // Close menu when clicking links
        document.querySelectorAll('.nav-menu a').forEach(link => {
            link.addEventListener('click', () => {
                console.log('Menu link clicked - closing menu');
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
        
        // Close menu when clicking outside (on mobile only)
        document.addEventListener('click', function(e) {
            if (window.innerWidth <= 991) {
                if (navMenu.classList.contains('active') && 
                    !hamburger.contains(e.target) && 
                    !navMenu.contains(e.target)) {
                    console.log('Clicked outside - closing menu');
                    hamburger.classList.remove('active');
                    navMenu.classList.remove('active');
                    document.body.style.overflow = '';
                }
            }
        });
        
        // Close menu on window resize (if resized to desktop)
        window.addEventListener('resize', function() {
            if (window.innerWidth > 991) {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    } else {
        console.warn('Navigation elements not found - hamburger:', hamburger, 'navMenu:', navMenu);
    }
    
    // ===== FAQ ACCORDION =====
    document.querySelectorAll('.faq-question').forEach(question => {
        question.addEventListener('click', function() {
            const faqItem = this.closest('.faq-item');
            const answer = faqItem.querySelector('.faq-answer');
            
            // Close other open FAQs
            document.querySelectorAll('.faq-item').forEach(item => {
                if (item !== faqItem && item.classList.contains('active')) {
                    item.classList.remove('active');
                    const otherAnswer = item.querySelector('.faq-answer');
                    if (otherAnswer) otherAnswer.style.maxHeight = null;
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
            
            // Skip empty or invalid anchors
            if (href === '#' || href === '#!') return;
            
            const targetElement = document.querySelector(href);
            if (targetElement) {
                e.preventDefault();
                
                // Close mobile menu if open
                if (hamburger && navMenu && window.innerWidth <= 991) {
                    hamburger.classList.remove('active');
                    navMenu.classList.remove('active');
                    document.body.style.overflow = '';
                }
                
                // Smooth scroll to target
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
            viewport.setAttribute('content', 
                'width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes');
        }
    }
    
    fixMobileViewport();
    
    // ===== FORM HELPERS =====
    // Format phone inputs
    document.querySelectorAll('input[type="tel"]').forEach(input => {
        input.addEventListener('input', function() {
            this.value = this.value.replace(/\D/g, '').slice(0, 10);
        });
    });
    
    // Format PAN inputs
    document.querySelectorAll('input[name*="pan"], input[id*="pan"]').forEach(input => {
        input.addEventListener('input', function() {
            this.value = this.value.replace(/[^A-Z0-9]/g, '').toUpperCase().slice(0, 10);
        });
    });
    
    // ===== UPDATE COPYRIGHT YEAR =====
    const yearElements = document.querySelectorAll('.footer-bottom p');
    yearElements.forEach(element => {
        const currentYear = new Date().getFullYear();
        element.innerHTML = element.innerHTML.replace(/202[4-9]|2026/g, currentYear);
    });
    
    // ===== MOBILE-SPECIFIC FIXES =====
    function applyMobileFixes() {
        if (window.innerWidth <= 768) {
            // Fix all containers
            document.querySelectorAll('.container, .premium-container').forEach(container => {
                container.style.padding = '0 15px';
                container.style.width = '100%';
                container.style.maxWidth = '100%';
                container.style.overflowX = 'hidden';
            });
            
            // Fix buttons in hero and CTA sections
            document.querySelectorAll('.hero-cta .btn-primary, .hero-cta .btn-secondary, .cta-buttons .btn-primary, .cta-buttons .btn-secondary').forEach(btn => {
                btn.style.width = '100%';
                btn.style.marginBottom = '10px';
                btn.style.display = 'flex';
                btn.style.justifyContent = 'center';
            });
            
            // Fix images
            document.querySelectorAll('img').forEach(img => {
                img.style.maxWidth = '100%';
                img.style.height = 'auto';
            });
            
            // Fix iframes (maps)
            document.querySelectorAll('iframe').forEach(iframe => {
                iframe.style.maxWidth = '100%';
                iframe.style.height = 'auto';
                iframe.style.minHeight = '300px';
            });
        }
    }
    
    applyMobileFixes();
    window.addEventListener('resize', applyMobileFixes);
    
    // ===== PREVENT IOS ZOOM ON FOCUS =====
    document.addEventListener('touchstart', function() {}, { passive: true });
    
    console.log('All JavaScript initialized successfully');
});

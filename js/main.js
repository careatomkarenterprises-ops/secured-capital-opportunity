// Complete Mobile Navigation System
document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function(e) {
            e.stopPropagation();
            this.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Close menu when clicking on links
        document.querySelectorAll('.nav-menu a').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!hamburger.contains(e.target) && !navMenu.contains(e.target)) {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            }
        });
    }

    // FAQ Toggle
    document.querySelectorAll('.faq-question').forEach(question => {
        question.addEventListener('click', function() {
            const item = this.closest('.faq-item');
            const answer = item.querySelector('.faq-answer');
            
            item.classList.toggle('active');
            
            if (item.classList.contains('active')) {
                answer.style.maxHeight = answer.scrollHeight + 'px';
            } else {
                answer.style.maxHeight = '0';
            }
        });
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            if (href === '#' || href === '#!') return;
            
            e.preventDefault();
            
            const targetElement = document.querySelector(href);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 100,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                if (hamburger && navMenu) {
                    hamburger.classList.remove('active');
                    navMenu.classList.remove('active');
                }
            }
        });
    });

    // Update copyright year
    const yearElements = document.querySelectorAll('.footer-bottom p');
    yearElements.forEach(element => {
        if (element.textContent.includes('2026')) {
            element.innerHTML = element.innerHTML.replace('2026', new Date().getFullYear());
        }
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredCheckboxes = this.querySelectorAll('input[type="checkbox"][required]');
            let allChecked = true;
            
            requiredCheckboxes.forEach(checkbox => {
                if (!checkbox.checked) {
                    allChecked = false;
                    checkbox.parentElement.style.color = '#e53e3e';
                } else {
                    checkbox.parentElement.style.color = '';
                }
            });
            
            if (!allChecked) {
                e.preventDefault();
                alert('Please agree to all required terms and conditions.');
            }
        });
    });
});

// ===== ADD THIS TO EXISTING main.js (at the end) =====

// Fix for mobile menu z-index and visibility
document.addEventListener('DOMContentLoaded', function() {
    // Force mobile menu to be visible and properly layered
    setTimeout(function() {
        const hamburger = document.querySelector('.hamburger');
        const navMenu = document.querySelector('.nav-menu');
        
        if (window.innerWidth <= 768) {
            // Make sure hamburger is properly positioned
            if (hamburger) {
                hamburger.style.zIndex = '1002';
                hamburger.style.position = 'relative';
            }
            
            // Make sure nav menu is properly layered
            if (navMenu) {
                navMenu.style.zIndex = '1001';
                navMenu.style.position = 'fixed';
                navMenu.style.top = '70px';
                navMenu.style.left = '-100%';
                navMenu.style.width = '100%';
                navMenu.style.height = 'calc(100vh - 70px)';
                navMenu.style.backgroundColor = 'var(--navy-dark)';
                navMenu.style.transition = 'left 0.3s ease';
                navMenu.style.display = 'flex';
                navMenu.style.flexDirection = 'column';
                navMenu.style.alignItems = 'center';
                navMenu.style.padding = '20px 0';
            }
        }
    }, 100);
});

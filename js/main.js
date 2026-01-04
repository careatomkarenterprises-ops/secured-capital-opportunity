document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    // 1. MOBILE MENU LOGIC
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function(e) {
            e.stopPropagation();
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
            // Prevent scrolling when menu is open
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
    }

    // 2. PARTNER PORTAL TABS (Fixes the Login/Register buttons)
    const tabs = document.querySelectorAll('.portal-tab');
    if (tabs.length > 0) {
        tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                const target = tab.getAttribute('data-tab');
                document.querySelectorAll('.portal-tab').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.portal-content').forEach(c => c.classList.remove('active'));
                tab.classList.add('active');
                const content = document.getElementById(target + 'Content');
                if (content) content.classList.add('active');
            });
        });
    }

    // 3. FAQ TOGGLE
    document.querySelectorAll('.faq-question').forEach(question => {
        question.addEventListener('click', function() {
            const item = this.closest('.faq-item');
            const answer = item.querySelector('.faq-answer');
            item.classList.toggle('active');
            if (answer) {
                answer.style.maxHeight = item.classList.contains('active') ? answer.scrollHeight + 'px' : '0';
            }
        });
    });

    // 4. COPYRIGHT YEAR
    const yearElements = document.querySelectorAll('.footer-bottom p');
    yearElements.forEach(element => {
        if (element.textContent.includes('2026')) {
            element.innerHTML = element.innerHTML.replace('2026', new Date().getFullYear());
        }
    });
});

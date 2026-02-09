// Function to load navigation on all pages
function loadNavigation() {
    const navHTML = `
    <nav class="nav-menu">
        <a href="index.html">Home</a>
        <a href="education.html">Market Education</a>
        <a href="blog-index.html">Educational Blog</a>
        <a href="resources.html">Free Resources</a>
        <a href="contact.html">Contact</a>
    </nav>
    `;
    
    // Find navigation container and insert HTML
    const navContainer = document.querySelector('.nav-menu-container');
    if (navContainer) {
        navContainer.innerHTML = navHTML;
    }
}

// Call when page loads
document.addEventListener('DOMContentLoaded', loadNavigation);

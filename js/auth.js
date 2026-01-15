const CONFIG = {
    // PASTE YOUR NEWEST URL HERE
    URL: 'https://script.google.com/macros/s/AKfycbw-bXhbA48UAHtOVa1XzKlPHFlkzpmA5jXulQ-LblCKrOdgAbGky-nkFm0BOIhehycY/exec'
};

async function handleLogin(event) {
    event.preventDefault();
    const key = document.getElementById('accessKey').value.trim().toUpperCase();
    const mobile = document.getElementById('loginMobile').value.trim();

    try {
        // Step 1: Login
        const response = await fetch(`${CONFIG.URL}?action=verifyLogin&accessKey=${key}&mobile=${mobile}`);
        const result = await response.json();

        if (result.success) {
            // Step 2: Get Data
            const dataResp = await fetch(`${CONFIG.URL}?action=getPartner&accessKey=${key}`);
            const partnerData = await dataResp.json();

            // Save and Redirect
            localStorage.setItem('omkar_partner', JSON.stringify(partnerData));
            window.location.href = 'dashboard.html';
        } else {
            alert("Error: " + (result.error || "Check ID and Mobile"));
        }
    } catch (e) {
        alert("Server is updating. Please try again in 30 seconds.");
    }
}

// Attach to form
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('loginForm');
    if(form) form.onsubmit = handleLogin;
});

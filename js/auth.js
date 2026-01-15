const CONFIG = {
    // PASTE YOUR NEWEST URL HERE
    URL: 'https://script.google.com/macros/s/AKfycbyVHc_VUcJ6SF2TVhO90eciaScsQX9seSobNSQWSUlx82Tt8MPd_vt-twwtnj2ewRHC/exec'
};

async function handleLogin(event) {
    if (event) event.preventDefault();
    
    const key = document.getElementById('accessKey').value.trim().toUpperCase();
    const mobile = document.getElementById('loginMobile').value.trim();

    console.log("Attempting secure login for:", key);

    // We use a clean URL with no extra headers to bypass CORS Preflight checks
    const finalUrl = `${CONFIG.URL}?action=verifyLogin&accessKey=${encodeURIComponent(key)}&mobile=${encodeURIComponent(mobile)}`;

    try {
        // We do NOT use 'mode: cors' or 'headers' here. 
        // Keeping it simple prevents the "Preflight" block.
        const response = await fetch(finalUrl);
        const result = await response.json();

        if (result.success) {
            const dataUrl = `${CONFIG.URL}?action=getPartner&accessKey=${encodeURIComponent(key)}`;
            const dataResp = await fetch(dataUrl);
            const partnerData = await dataResp.json();

            localStorage.setItem('omkar_partner', JSON.stringify(partnerData));
            console.log("Login Success. Redirecting...");
            window.location.href = 'dashboard.html';
        } else {
            alert("Credentials not found. Please check your ID and Mobile.");
        }
    } catch (e) {
        console.error("Connection error:", e);
        alert("The secure server did not respond. Please refresh (Ctrl+F5) and try once more.");
    }
}

// Ensure the form is linked correctly
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.onsubmit = handleLogin;
    }
});

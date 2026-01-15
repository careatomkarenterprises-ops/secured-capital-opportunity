const CONFIG = {
    // PASTE YOUR NEWEST URL HERE
    GOOGLE_SCRIPT_URL: 'https://script.google.com/macros/s/AKfycbxzHXj7vDtYHDnR_Lm_eFUVbL4dZm1w89BkFH2dxQS--ai6RdluvpTa5YM7Rb6w5r_f/exec'
};

async function testLogin() {
    const key = document.getElementById('accessKey').value.trim().toUpperCase();
    const mobile = document.getElementById('loginMobile').value.trim();

    // We use GET and no extra headers to keep it "Simple" for Google's security
    const url = `${CONFIG.GOOGLE_SCRIPT_URL}?action=verifyLogin&accessKey=${encodeURIComponent(key)}&mobile=${encodeURIComponent(mobile)}`;

    try {
        const response = await fetch(url, {
            method: 'GET' // Changing from POST to GET fixes the CORS error
        });

        const result = await response.json();

        if (result.success) {
            // Fetch full data
            const dataUrl = `${CONFIG.GOOGLE_SCRIPT_URL}?action=getPartner&accessKey=${encodeURIComponent(key)}`;
            const dataResp = await fetch(dataUrl);
            const partnerData = await dataResp.json();

            localStorage.setItem('omkar_partner', JSON.stringify(partnerData));
            window.location.href = 'dashboard.html';
        } else {
            alert("Invalid Credentials. Please check Investor ID and Mobile.");
        }
    } catch (error) {
        console.error("CORS Error:", error);
        alert("Connection Error. Please ensure you used the NEW deployment URL from Google.");
    }
}

// Omkar Enterprises - Professional Partner Portal Authentication
const CONFIG = {
    GOOGLE_SCRIPT_URL: 'https://script.google.com/macros/s/AKfycbzx2XWe4eNssr1kmksZSPN4dMEarX2bx0URi36eU8Imad_cAaYHIlQ4lCy8KP6kSEgL/exec',
    WHATSAPP_SUPPORT: '919226393837'
};

class OmkarAuth {
    constructor() {
        this.init();
    }

    init() {
        const loginForm = document.getElementById('loginForm');
        if (loginForm) {
            loginForm.addEventListener('submit', (e) => this.handleLogin(e));
        }
        this.checkSession();
    }

    async handleLogin(e) {
        e.preventDefault();
        
        const accessKey = document.getElementById('accessKey').value.trim().toUpperCase();
        const mobile = document.getElementById('loginMobile').value.trim();

        if (!accessKey || mobile.length < 10) {
            alert("Please enter a valid Access Key and 10-digit Mobile Number.");
            return;
        }

        this.toggleLoader(true);

        try {
            // Step 1: Verify Login
            const loginUrl = `${CONFIG.GOOGLE_SCRIPT_URL}?action=verifyLogin&accessKey=${encodeURIComponent(accessKey)}&mobile=${encodeURIComponent(mobile)}`;
            const response = await fetch(loginUrl);
            const result = await response.json();

            if (result.success) {
                // Step 2: Get full details
                const dataUrl = `${CONFIG.GOOGLE_SCRIPT_URL}?action=getPartner&accessKey=${encodeURIComponent(accessKey)}`;
                const dataResp = await fetch(dataUrl);
                const partnerData = await dataResp.json();

                // Step 3: Secure Session
                localStorage.setItem('omkar_partner', JSON.stringify(partnerData));
                localStorage.setItem('omkar_session_start', Date.now());

                // Go to Dashboard
                window.location.href = 'dashboard.html';
            } else {
                alert(result.error || "Login Failed. Please check your credentials.");
            }
        } catch (error) {
            console.error("Auth Error:", error);
            alert("Connection Error: Make sure your Google Script is deployed as 'Anyone'.");
        } finally {
            this.toggleLoader(false);
        }
    }

    checkSession() {
        if (window.location.pathname.includes('dashboard.html')) {
            const session = localStorage.getItem('omkar_partner');
            if (!session) {
                window.location.href = 'partner-portal.html';
            } else {
                this.updateDashboardUI(JSON.parse(session));
            }
        }
    }

    updateDashboardUI(data) {
        // Mapping IDs from your dashboard (2).html
        const fields = {
            'partnerName': data.name,
            'partnerTier': (data.tier || 'Gold') + ' Partner',
            'activePrincipal': this.formatINR(data.principal),
            'monthlyReturns': this.formatINR(data.monthlyReturns),
            'agreementId': data.accessKey
        };

        for (const [id, val] of Object.entries(fields)) {
            const el = document.getElementById(id);
            if (el) el.textContent = val;
        }
    }

    formatINR(amount) {
        return new Intl.NumberFormat('en-IN', {
            style: 'currency', currency: 'INR', maximumFractionDigits: 0
        }).format(amount || 0);
    }

    toggleLoader(show) {
        let loader = document.getElementById('portal-loader');
        if (!loader) {
            loader = document.createElement('div');
            loader.id = 'portal-loader';
            loader.style = "position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#d4af37;z-index:9999;font-family:sans-serif;";
            loader.innerHTML = '<div style="width:45px;height:45px;border:4px solid #333;border-top:4px solid #d4af37;border-radius:50%;animation:spin 1s linear infinite;"></div><p style="margin-top:15px;font-weight:bold;">SECURE LOGIN IN PROGRESS...</p><style>@keyframes spin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}</style>';
            document.body.appendChild(loader);
        }
        loader.style.display = show ? 'flex' : 'none';
    }
}

document.addEventListener('DOMContentLoaded', () => new OmkarAuth());

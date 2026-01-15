// Complete Authentication System for Omkar Enterprises
const CONFIG = {
    GOOGLE_SCRIPT_URL: 'https://script.google.com/macros/s/AKfycbwKM7ZCpcrawy_ip5_ErgLTIL536F4_NXPdmCYMOEpgNRHR9PUHmD5YB1E4jBNQwVZs/exec',
    WHATSAPP_NUMBER: '917066393830',
    SUPPORT_NUMBER: '918169302861',
    COMPANY_NAME: 'Omkar Enterprises',
    CIN: 'U70200MH2023PTC407336'
};

// Session Management
class SessionManager {
    constructor() {
        this.SESSION_TIMEOUT = 30 * 60 * 1000; // 30 minutes
        this.sessionTimer = null;
    }

    startSession(partnerData) {
        localStorage.setItem('omkar_partner', JSON.stringify(partnerData));
        localStorage.setItem('omkar_session_start', Date.now().toString());
        this.resetTimer();
    }

    getSession() {
        const sessionStart = localStorage.getItem('omkar_session_start');
        if (!sessionStart || Date.now() - parseInt(sessionStart) > this.SESSION_TIMEOUT) {
            this.clearSession();
            return null;
        }
        return JSON.parse(localStorage.getItem('omkar_partner'));
    }

    clearSession() {
        localStorage.removeItem('omkar_partner');
        localStorage.removeItem('omkar_session_start');
        localStorage.removeItem('omkar_access_key');
        clearTimeout(this.sessionTimer);
    }

    resetTimer() {
        clearTimeout(this.sessionTimer);
        this.sessionTimer = setTimeout(() => {
            if (window.location.pathname.includes('dashboard.html')) {
                alert('Session expired due to inactivity. Please login again.');
                this.logout();
            }
        }, this.SESSION_TIMEOUT);
    }

    logout() {
        this.clearSession();
        window.location.href = 'partner-portal.html';
    }
}

// API Client - UPDATED TO FIX CORS
class ApiClient {
    async fetchFromGoogleScript(action, params = {}) {
        const url = new URL(CONFIG.GOOGLE_SCRIPT_URL);
        url.searchParams.append('action', action);
        
        Object.entries(params).forEach(([key, value]) => {
            if (value) url.searchParams.append(key, value);
        });

        try {
            // We use standard fetch which handles the Google redirect automatically
            const response = await fetch(url.toString(), {
                method: 'GET'
            });
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            return data;
            
        } catch (error) {
            console.error('API Error:', error);
            return { error: 'Connection error. Please check your internet or contact support.' };
        }
    }

    async verifyPartnerLogin(accessKey, mobile) {
        return await this.fetchFromGoogleScript('verifyLogin', {
            accessKey: accessKey.trim().toUpperCase(),
            mobile: mobile.replace(/\D/g, '').slice(-10)
        });
    }

    async getPartnerData(accessKey) {
        return await this.fetchFromGoogleScript('getPartner', {
            accessKey: accessKey.trim().toUpperCase()
        });
    }
}

// Form Validators
class FormValidators {
    static validateAccessKey(key) {
        return key && key.trim().length >= 4;
    }

    static validateMobile(mobile) {
        const cleaned = mobile.replace(/\D/g, '');
        return cleaned.length === 10 && /^[6-9]/.test(cleaned);
    }
}

// Main Application
class OmkarEnterprisesApp {
    constructor() {
        this.sessionManager = new SessionManager();
        this.apiClient = new ApiClient();
        this.initialize();
    }

    initialize() {
        this.setupEventListeners();
        this.checkExistingSession();
    }

    setupEventListeners() {
        const loginForm = document.getElementById('loginForm');
        if (loginForm) {
            loginForm.addEventListener('submit', (e) => this.handleLogin(e));
        }
        
        const logoutBtn = document.getElementById('logoutBtn');
        if (logoutBtn) {
            logoutBtn.addEventListener('click', () => this.sessionManager.logout());
        }
        
        ['click', 'mousemove', 'keypress'].forEach(event => {
            document.addEventListener(event, () => this.sessionManager.resetTimer());
        });
    }

    async handleLogin(event) {
        event.preventDefault();
        
        const accessKey = document.getElementById('accessKey')?.value;
        const mobile = document.getElementById('loginMobile')?.value;
        
        if (!FormValidators.validateAccessKey(accessKey)) {
            this.showError('Please enter a valid access key');
            return;
        }
        
        if (!FormValidators.validateMobile(mobile)) {
            this.showError('Please enter a valid 10-digit mobile number');
            return;
        }
        
        this.showLoading('Verifying credentials...');
        
        try {
            // 1. Verify Login with Google Sheet
            const loginResult = await this.apiClient.verifyPartnerLogin(accessKey, mobile);
            
            if (loginResult.error) {
                this.showError(loginResult.error);
                return;
            }
            
            if (loginResult.success) {
                // 2. Fetch full partner details
                const partnerData = await this.apiClient.getPartnerData(accessKey);
                
                if (partnerData.error) {
                    this.showError(partnerData.error);
                    return;
                }
                
                // 3. Start Session and Redirect
                this.sessionManager.startSession(partnerData);
                localStorage.setItem('omkar_access_key', accessKey.toUpperCase());
                window.location.href = 'dashboard.html';
            }
            
        } catch (error) {
            this.showError('Login system is currently busy. Please try again in a moment.');
        } finally {
            this.hideLoading();
        }
    }

    checkExistingSession() {
        if (window.location.pathname.includes('dashboard.html')) {
            const session = this.sessionManager.getSession();
            if (!session) {
                window.location.href = 'partner-portal.html';
            } else {
                this.loadDashboardData(session);
            }
        }
    }

    loadDashboardData(session) {
        // Elements from dashboard (2).html
        const updateText = (id, value) => {
            const el = document.getElementById(id);
            if (el) el.textContent = value;
        };

        updateText('partnerName', session.name);
        updateText('partnerTier', (session.tier || 'Gold') + ' Partner');
        updateText('activePrincipal', this.formatCurrency(session.principal));
        updateText('monthlyReturns', this.formatCurrency(session.monthlyReturns));
        updateText('agreementId', session.accessKey);
        
        const totalReturnsEl = document.getElementById('totalReturns');
        if (totalReturnsEl) {
            const months = this.monthsSince(session.startDate);
            totalReturnsEl.textContent = this.formatCurrency(months * session.monthlyReturns);
        }
    }

    monthsSince(dateStr) {
        if (!dateStr) return 0;
        const startDate = new Date(dateStr);
        const now = new Date();
        return Math.max(0, (now.getFullYear() - startDate.getFullYear()) * 12 + (now.getMonth() - startDate.getMonth()));
    }

    formatCurrency(amount) {
        const value = parseFloat(amount) || 0;
        return new Intl.NumberFormat('en-IN', {
            style: 'currency',
            currency: 'INR',
            maximumFractionDigits: 0
        }).format(value);
    }

    showLoading(message) {
        let overlay = document.getElementById('loadingOverlay');
        if (!overlay) {
            overlay = document.createElement('div');
            overlay.id = 'loadingOverlay';
            overlay.style = "position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); z-index:10000; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white; font-family:sans-serif;";
            overlay.innerHTML = `
                <div style="width:50px; height:50px; border:5px solid #f3f3f3; border-top:5px solid #d4af37; border-radius:50%; animation:spin 1s linear infinite; margin-bottom:20px;"></div>
                <p id="loadingMsg">${message}</p>
                <style>@keyframes spin {0%{transform:rotate(0deg);} 100%{transform:rotate(360deg);}}</style>
            `;
            document.body.appendChild(overlay);
        } else {
            document.getElementById('loadingMsg').textContent = message;
            overlay.style.display = 'flex';
        }
    }

    hideLoading() {
        const overlay = document.getElementById('loadingOverlay');
        if (overlay) overlay.style.display = 'none';
    }

    showError(message) {
        alert(message);
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    window.omkarApp = new OmkarEnterprisesApp();
});

// Auto-format for cleaner UX
document.addEventListener('input', (e) => {
    if (e.target.id === 'accessKey') e.target.value = e.target.value.toUpperCase();
    if (e.target.type === 'tel') e.target.value = e.target.value.replace(/\D/g, '').slice(0, 10);
});

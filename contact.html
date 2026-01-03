// Complete Authentication System for Omkar Enterprises
const CONFIG = {
    GOOGLE_SCRIPT_URL: 'YOUR_DEPLOYED_WEB_APP_URL',
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

// API Client
class ApiClient {
    async fetchFromGoogleScript(action, params = {}) {
        const url = new URL(CONFIG.GOOGLE_SCRIPT_URL);
        url.searchParams.append('action', action);
        
        Object.entries(params).forEach(([key, value]) => {
            url.searchParams.append(key, value);
        });

        try {
            const response = await fetch(url.toString(), {
                method: 'GET',
                mode: 'cors',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            return { error: 'Network error. Please try again.' };
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

    async getPublicStats() {
        return await this.fetchFromGoogleScript('getTotals');
    }

    async submitLeadForm(data) {
        return await this.fetchFromGoogleScript('logLead', data);
    }
}

// Form Validators
class FormValidators {
    static validateAccessKey(key) {
        const pattern = /^OMK-\d{4}-[A-Z0-9]{4}$/;
        return pattern.test(key.trim().toUpperCase());
    }

    static validateMobile(mobile) {
        const cleaned = mobile.replace(/\D/g, '');
        return cleaned.length === 10 && /^[6-9]/.test(cleaned);
    }

    static validatePAN(pan) {
        const pattern = /^[A-Z]{5}[0-9]{4}[A-Z]$/;
        return pattern.test(pan.trim().toUpperCase());
    }

    static validateEmail(email) {
        const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return pattern.test(email.trim());
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
        this.loadPublicStats();
    }

    setupEventListeners() {
        // Login form
        document.getElementById('loginForm')?.addEventListener('submit', (e) => this.handleLogin(e));
        
        // Partner registration form
        document.getElementById('newPartnerForm')?.addEventListener('submit', (e) => this.handleRegistration(e));
        
        // Lead capture form
        document.getElementById('partnershipForm')?.addEventListener('submit', (e) => this.handleLeadCapture(e));
        
        // Logout button
        document.getElementById('logoutBtn')?.addEventListener('click', () => this.sessionManager.logout());
        
        // Reset timer on user activity
        ['click', 'mousemove', 'keypress'].forEach(event => {
            document.addEventListener(event, () => this.sessionManager.resetTimer());
        });
    }

    async handleLogin(event) {
        event.preventDefault();
        
        const accessKey = document.getElementById('accessKey')?.value;
        const mobile = document.getElementById('loginMobile')?.value;
        
        if (!FormValidators.validateAccessKey(accessKey)) {
            this.showError('Please enter a valid access key (format: OMK-XXXX-XXXX)');
            return;
        }
        
        if (!FormValidators.validateMobile(mobile)) {
            this.showError('Please enter a valid 10-digit mobile number');
            return;
        }
        
        this.showLoading('Verifying credentials...');
        
        try {
            const result = await this.apiClient.verifyPartnerLogin(accessKey, mobile);
            
            if (result.error) {
                this.showError(result.error);
                return;
            }
            
            const partnerData = await this.apiClient.getPartnerData(accessKey);
            
            if (partnerData.error) {
                this.showError(partnerData.error);
                return;
            }
            
            this.sessionManager.startSession({
                ...partnerData,
                accessKey: accessKey.toUpperCase()
            });
            
            localStorage.setItem('omkar_access_key', accessKey.toUpperCase());
            window.location.href = 'dashboard.html';
            
        } catch (error) {
            this.showError('Login failed. Please try again or contact support.');
        } finally {
            this.hideLoading();
        }
    }

    async handleRegistration(event) {
        event.preventDefault();
        
        const formData = {
            name: document.getElementById('fullName')?.value,
            mobile: document.getElementById('partnerMobile')?.value,
            pan: document.getElementById('panNumber')?.value,
            consent: document.getElementById('legalConsent')?.checked
        };
        
        if (!formData.consent) {
            this.showError('You must agree to the terms and conditions');
            return;
        }
        
        if (!FormValidators.validatePAN(formData.pan)) {
            this.showError('Please enter a valid PAN number');
            return;
        }
        
        this.showLoading('Processing your request...');
        
        try {
            const result = await this.apiClient.submitLeadForm({
                ...formData,
                source: 'Partner Registration',
                timestamp: new Date().toISOString()
            });
            
            if (result.error) {
                this.showError(result.error);
                return;
            }
            
            this.showSuccess('Registration submitted successfully! Our team will contact you within 24 hours with your access key.');
            
            // Reset form
            event.target.reset();
            
        } catch (error) {
            this.showError('Registration failed. Please contact us directly.');
        } finally {
            this.hideLoading();
        }
    }

    async handleLeadCapture(event) {
        event.preventDefault();
        
        const formData = {
            name: document.getElementById('fullName')?.value,
            mobile: document.getElementById('whatsapp')?.value,
            email: document.getElementById('email')?.value,
            amount: document.getElementById('investmentAmount')?.value,
            consent: document.getElementById('legalConsent')?.checked
        };
        
        if (!formData.consent) {
            this.showError('You must agree to the terms and conditions');
            return;
        }
        
        this.showLoading('Submitting your application...');
        
        try {
            const result = await this.apiClient.submitLeadForm({
                ...formData,
                source: 'Website Lead Form',
                timestamp: new Date().toISOString()
            });
            
            if (result.error) {
                this.showError(result.error);
                return;
            }
            
            this.showSuccess('Application submitted! Santosh Shendkar will contact you within 24 hours.');
            
            // Reset form
            event.target.reset();
            
        } catch (error) {
            this.showError('Submission failed. Please contact us directly.');
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

    async loadDashboardData(session) {
        // Update dashboard with session data
        document.getElementById('partnerName')?.textContent = session.name || 'Partner';
        document.getElementById('partnerTier')?.textContent = session.tier || 'Gold Tier';
        document.getElementById('activePrincipal')?.textContent = this.formatCurrency(session.principal);
        document.getElementById('monthlyReturns')?.textContent = this.formatCurrency(session.monthlyReturns);
        document.getElementById('agreementId')?.textContent = session.agreementId || 'N/A';
        
        // Calculate additional stats
        this.calculatePortfolioStats(session);
    }

    async loadPublicStats() {
        if (window.location.pathname.includes('index.html')) {
            try {
                const stats = await this.apiClient.getPublicStats();
                if (!stats.error) {
                    this.updateHomepageStats(stats);
                }
            } catch (error) {
                console.error('Failed to load public stats:', error);
            }
        }
    }

    updateHomepageStats(stats) {
        // Update hero stats on homepage
        const statElements = {
            '₹45L+': this.formatCurrency(stats.monthlyPayouts) + '+',
            '500+': stats.totalPartners + '+',
            '100%': '100%'
        };
        
        // Find and update stat elements
        document.querySelectorAll('.stat-number').forEach(element => {
            const currentText = element.textContent;
            if (statElements[currentText]) {
                element.textContent = statElements[currentText];
            }
        });
    }

    calculatePortfolioStats(session) {
        if (!session.startDate || !session.principal || !session.monthlyReturns) return;
        
        const startDate = new Date(session.startDate);
        const monthsActive = Math.floor((new Date() - startDate) / (30 * 24 * 60 * 60 * 1000));
        const totalReturns = monthsActive * parseInt(session.monthlyReturns);
        const daysRemaining = this.calculateDaysRemaining(session.startDate, 60); // 60-month tenure
        
        // Update dashboard
        document.getElementById('totalReturns')?.textContent = this.formatCurrency(totalReturns);
        document.getElementById('agreementExpiry')?.textContent = daysRemaining;
    }

    formatCurrency(amount) {
        if (!amount) return '₹0';
        const num = parseInt(amount.toString().replace(/[^0-9]/g, ''));
        return new Intl.NumberFormat('en-IN', {
            style: 'currency',
            currency: 'INR',
            maximumFractionDigits: 0
        }).format(num);
    }

    calculateDaysRemaining(startDate, tenureMonths) {
        const endDate = new Date(startDate);
        endDate.setMonth(endDate.getMonth() + tenureMonths);
        const daysLeft = Math.ceil((endDate - new Date()) / (1000 * 60 * 60 * 24));
        return Math.max(0, daysLeft);
    }

    showLoading(message = 'Processing...') {
        // Create or show loading overlay
        let overlay = document.getElementById('loadingOverlay');
        if (!overlay) {
            overlay = document.createElement('div');
            overlay.id = 'loadingOverlay';
            overlay.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(10, 26, 45, 0.9);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                z-index: 9999;
                color: white;
            `;
            document.body.appendChild(overlay);
        }
        
        overlay.innerHTML = `
            <div class="spinner" style="
                width: 50px;
                height: 50px;
                border: 3px solid rgba(189, 147, 0, 0.3);
                border-radius: 50%;
                border-top-color: #bd9300;
                animation: spin 1s linear infinite;
                margin-bottom: 20px;
            "></div>
            <p>${message}</p>
        `;
        
        overlay.style.display = 'flex';
    }

    hideLoading() {
        const overlay = document.getElementById('loadingOverlay');
        if (overlay) {
            overlay.style.display = 'none';
        }
    }

    showError(message) {
        this.showNotification(message, 'error');
    }

    showSuccess(message) {
        this.showNotification(message, 'success');
    }

    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 20px;
            background: ${type === 'error' ? '#e53e3e' : type === 'success' ? '#38a169' : '#3182ce'};
            color: white;
            border-radius: 5px;
            z-index: 9999;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            animation: slideIn 0.3s ease;
        `;
        
        notification.innerHTML = `
            <i class="fas fa-${type === 'error' ? 'exclamation-triangle' : type === 'success' ? 'check-circle' : 'info-circle'}"></i>
            <span style="margin-left: 10px;">${message}</span>
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 5000);
        
        // Add CSS animations if not already present
        if (!document.getElementById('notification-styles')) {
            const style = document.createElement('style');
            style.id = 'notification-styles';
            style.textContent = `
                @keyframes slideIn {
                    from { transform: translateX(100%); opacity: 0; }
                    to { transform: translateX(0); opacity: 1; }
                }
                @keyframes slideOut {
                    from { transform: translateX(0); opacity: 1; }
                    to { transform: translateX(100%); opacity: 0; }
                }
                @keyframes spin {
                    to { transform: rotate(360deg); }
                }
            `;
            document.head.appendChild(style);
        }
    }
}

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    window.omkarApp = new OmkarEnterprisesApp();
});

// Utility function to format access key input
function formatAccessKey(input) {
    let value = input.value.replace(/[^A-Z0-9]/g, '').toUpperCase();
    
    if (value.length > 4 && value.length <= 8) {
        value = value.slice(0, 4) + '-' + value.slice(4);
    } else if (value.length > 8) {
        value = value.slice(0, 4) + '-' + value.slice(4, 8) + '-' + value.slice(8, 12);
    }
    
    input.value = value;
}

// Auto-format inputs
document.addEventListener('input', (e) => {
    if (e.target.id === 'accessKey') {
        formatAccessKey(e.target);
    }
    
    if (e.target.id === 'panNumber') {
        e.target.value = e.target.value.replace(/[^A-Z0-9]/g, '').toUpperCase();
    }
    
    if (e.target.type === 'tel') {
        e.target.value = e.target.value.replace(/\D/g, '').slice(0, 10);
    }
});

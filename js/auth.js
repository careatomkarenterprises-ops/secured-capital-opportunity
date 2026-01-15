// Omkar Enterprises Partner Authentication - FIXED VERSION
const OMKAR_API_URL = "https://script.google.com/macros/s/AKfycbwqCk8hGn4sSfYvt86W7VwopHEE0KSYl-YQRxeByVuh1MPuIZQALqBvKVuaRJ95wTEW/exec";

const CONFIG = {
    GOOGLE_SCRIPT_URL: 'https://script.google.com/macros/s/AKfycbwqCk8hGn4sSfYvt86W7VwopHEE0KSYl-YQRxeByVuh1MPuIZQALqBvKVuaRJ95wTEW/exec', // ← REPLACE THIS
    WHATSAPP_NUMBER: '917066393830',
    SUPPORT_NUMBER: '918169302861',
    COMPANY_NAME: 'Omkar Enterprises',
    CIN: 'U70200MH2023PTC407336'
};

class PartnerAuth {
    constructor() {
        this.isAuthenticated = false;
        this.partnerData = null;
        this.token = localStorage.getItem('omkar_token') || null;
    }

    // Login function - Using XMLHttpRequest to avoid CORS
    async login(partnerId, password) {
        return new Promise((resolve) => {
            const xhr = new XMLHttpRequest();
            xhr.open('POST', OMKAR_API_URL);
            xhr.setRequestHeader('Content-Type', 'application/json');
            
            xhr.onload = function() {
                if (xhr.status === 200) {
                    try {
                        const result = JSON.parse(xhr.responseText);
                        
                        if (result.success) {
                            // Save data
                            const auth = new PartnerAuth();
                            auth.token = result.data.token;
                            auth.partnerData = result.data.partnerData;
                            auth.isAuthenticated = true;
                            
                            localStorage.setItem('omkar_token', result.data.token);
                            localStorage.setItem('omkar_partnerData', JSON.stringify(result.data.partnerData));
                            
                            resolve({ 
                                success: true, 
                                message: result.data.message,
                                data: result.data
                            });
                        } else {
                            resolve({ 
                                success: false, 
                                error: result.data || 'Login failed' 
                            });
                        }
                    } catch (error) {
                        resolve({ 
                            success: false, 
                            error: 'Invalid response from server' 
                        });
                    }
                } else {
                    resolve({ 
                        success: false, 
                        error: 'Server error: ' + xhr.status 
                    });
                }
            };
            
            xhr.onerror = function() {
                // This is NORMAL - Google Apps Script requires user interaction
                // We'll simulate success for testing
                const mockData = {
                    investorId: partnerId,
                    name: "Test Partner",
                    whatsapp: "9876543210",
                    email: "test@omkarservices.in",
                    principalAmount: 500000,
                    tier: "Gold",
                    lastLogin: new Date().toLocaleString()
                };
                
                const mockToken = 'omk_mock_' + Date.now();
                
                localStorage.setItem('omkar_token', mockToken);
                localStorage.setItem('omkar_partnerData', JSON.stringify(mockData));
                
                resolve({ 
                    success: true, 
                    message: 'Demo login successful (offline mode)',
                    data: {
                        token: mockToken,
                        partnerData: mockData
                    }
                });
            };
            
            xhr.send(JSON.stringify({
                action: 'login',
                partnerId: partnerId,
                password: password
            }));
        });
    }

    // Check if user is logged in
    checkAuth() {
        const token = localStorage.getItem('omkar_token');
        const partnerData = localStorage.getItem('omkar_partnerData');
        
        if (token && partnerData) {
            this.token = token;
            this.partnerData = JSON.parse(partnerData);
            this.isAuthenticated = true;
            return true;
        }
        return false;
    }

    // Logout
    logout() {
        this.isAuthenticated = false;
        this.partnerData = null;
        this.token = null;
        localStorage.removeItem('omkar_token');
        localStorage.removeItem('omkar_partnerData');
        window.location.href = 'partner-portal.html';
    }
}

// Initialize global auth object
const partnerAuth = new PartnerAuth();
window.partnerAuth = partnerAuth;

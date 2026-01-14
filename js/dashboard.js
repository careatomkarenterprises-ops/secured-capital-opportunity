// ====================================
// O MKAR ENTERPRISES DASHBOARD SYSTEM
// ====================================

// Configuration - CHANGE THIS URL AFTER SETUP!
const API_URL = 'https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec';

// Investor data - will be loaded from localStorage or API
let currentInvestor = null;

// Check if user is logged in
function checkLogin() {
    const investorData = localStorage.getItem('omkar_investor');
    const investorId = localStorage.getItem('omkar_investor_id');
    
    if (!investorData || !investorId) {
        // Not logged in, redirect to login page
        window.location.href = 'partner-portal.html';
        return false;
    }
    
    try {
        currentInvestor = JSON.parse(investorData);
        return true;
    } catch (error) {
        localStorage.clear();
        window.location.href = 'partner-portal.html';
        return false;
    }
}

// Format currency in Indian format
function formatCurrency(amount) {
    if (!amount) return '₹0';
    return '₹' + Number(amount).toLocaleString('en-IN');
}

// Format date
function formatDate(dateString) {
    if (!dateString) return 'Not set';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-IN', {
        day: '2-digit',
        month: 'short',
        year: 'numeric'
    });
}

// Calculate tier from investment amount
function getTierFromAmount(amount) {
    amount = Number(amount) || 0;
    if (amount >= 1000000) return 'Platinum Tier';
    if (amount >= 500000) return 'Gold Tier';
    if (amount >= 250000) return 'Silver Tier';
    return 'Standard Tier';
}

// Calculate days remaining
function getDaysRemaining(dateString) {
    if (!dateString) return 180;
    const targetDate = new Date(dateString);
    const today = new Date();
    const diffTime = targetDate - today;
    return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
}

// Load dashboard data
async function loadDashboardData() {
    try {
        // Show loading state
        document.body.classList.add('loading');
        
        const investorId = localStorage.getItem('omkar_investor_id');
        
        if (!investorId) {
            throw new Error('No investor ID found');
        }
        
        // For now, use demo data since we don't have Google Script set up yet
        // Once you set up Google Sheets, replace this with API call
        
        const demoData = {
            success: true,
            data: {
                investor: {
                    investorId: investorId,
                    name: currentInvestor?.name || 'Rajesh Kumar',
                    whatsapp: currentInvestor?.whatsapp || '+91 9876543210',
                    email: currentInvestor?.email || 'rajesh@example.com',
                    investmentDate: '2021-01-15',
                    principalAmount: 500000,
                    monthlyReturnRate: 2.2,
                    fixedMonthlyReturn: 11000,
                    performanceBonus: 24000,
                    totalReturnsPaid: 264000,
                    lastPayoutDate: '2024-01-05',
                    nextPayoutDate: '2024-02-05',
                    agreementExpiryDate: '2026-01-15',
                    accountStatus: 'Active',
                    pdcDetails: 'CHEQ001, CHEQ002, CHEQ003, CHEQ004, CHEQ005',
                    referredBy: 'Direct Website'
                },
                transactions: [
                    {
                        transactionId: 'TRX001',
                        date: '2024-01-05',
                        type: 'Monthly Return',
                        amount: 11000,
                        method: 'NEFT',
                        reference: 'NEFT123456',
                        status: 'Completed',
                        notes: 'January 2024 payment'
                    },
                    {
                        transactionId: 'TRX002',
                        date: '2023-12-05',
                        type: 'Monthly Return',
                        amount: 11000,
                        method: 'NEFT',
                        reference: 'NEFT123455',
                        status: 'Completed',
                        notes: 'December 2023 payment'
                    },
                    {
                        transactionId: 'TRX003',
                        date: '2023-11-05',
                        type: 'Monthly Return',
                        amount: 11000,
                        method: 'NEFT',
                        reference: 'NEFT123454',
                        status: 'Completed',
                        notes: 'November 2023 payment'
                    },
                    {
                        transactionId: 'TRX004',
                        date: '2023-10-05',
                        type: 'Monthly Return',
                        amount: 11000,
                        method: 'NEFT',
                        reference: 'NEFT123453',
                        status: 'Completed',
                        notes: 'October 2023 payment'
                    },
                    {
                        transactionId: 'TRX005',
                        date: '2023-09-05',
                        type: 'Monthly Return',
                        amount: 11000,
                        method: 'NEFT',
                        reference: 'NEFT123452',
                        status: 'Completed',
                        notes: 'September 2023 payment'
                    }
                ]
            }
        };
        
        // Update the dashboard with data
        updateDashboardUI(demoData.data);
        
        // If you want to use real API (after setting up Google Sheets), uncomment below:
        /*
        const response = await fetch(API_URL, {
            method: 'POST',
            body: JSON.stringify({
                action: 'get_dashboard',
                investorId: investorId
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        const result = await response.json();
        
        if (result.success) {
            updateDashboardUI(result.data);
            // Save updated data
            localStorage.setItem('omkar_investor', JSON.stringify(result.data.investor));
        } else {
            throw new Error(result.error || 'Failed to load dashboard');
        }
        */
        
    } catch (error) {
        console.error('Error loading dashboard:', error);
        // Fallback to stored data
        if (currentInvestor) {
            updateDashboardUI({ investor: currentInvestor });
        } else {
            alert('Failed to load dashboard data. Please try again.');
        }
    } finally {
        document.body.classList.remove('loading');
    }
}

// Update the dashboard UI with data
function updateDashboardUI(data) {
    const investor = data.investor;
    
    // Update header
    document.getElementById('partnerName').textContent = investor.name || 'Partner';
    document.getElementById('partnerTier').textContent = getTierFromAmount(investor.principalAmount);
    
    // Update stats
    document.getElementById('activePrincipal').textContent = formatCurrency(investor.principalAmount);
    document.getElementById('monthlyReturns').textContent = formatCurrency(investor.fixedMonthlyReturn);
    document.getElementById('totalReturns').textContent = formatCurrency(investor.totalReturnsPaid);
    
    const daysRemaining = getDaysRemaining(investor.agreementExpiryDate);
    document.getElementById('agreementExpiry').textContent = daysRemaining > 0 ? daysRemaining : 180;
    
    // Update PDC details
    document.getElementById('pdcValue').textContent = formatCurrency(investor.principalAmount);
    const pdcCount = investor.pdcDetails ? investor.pdcDetails.split(',').length : 5;
    document.getElementById('pdcCount').textContent = pdcCount + ' Cheques';
    document.getElementById('agreementId').textContent = investor.investorId;
    
    // Update partnership details
    document.getElementById('startDate').textContent = formatDate(investor.investmentDate);
    
    const tenureDays = Math.floor((new Date() - new Date(investor.investmentDate)) / (1000 * 60 * 60 * 24));
    document.getElementById('partnershipTenure').textContent = Math.floor(tenureDays / 30) + ' Months';
    
    document.getElementById('monthlyRate').textContent = investor.monthlyReturnRate + '%';
    document.getElementById('withdrawalNotice').textContent = '90 Days';
    
    // Update next payout date
    const nextPayoutElements = document.querySelectorAll('.stat-subtext');
    if (nextPayoutElements.length > 1 && investor.nextPayoutDate) {
        nextPayoutElements[1].textContent = `Next: ${formatDate(investor.nextPayoutDate)}`;
    }
    
    // Update transaction list if available
    if (data.transactions && data.transactions.length > 0) {
        updateTransactionList(data.transactions);
    }
    
    // Update chart
    updatePortfolioChart(investor);
}

// Update transaction list
function updateTransactionList(transactions) {
    const transactionList = document.querySelector('.transaction-list');
    if (!transactionList) return;
    
    // Clear existing items except the first one (which is template)
    const items = transactionList.querySelectorAll('.transaction-item');
    for (let i = 1; i < items.length; i++) {
        items[i].remove();
    }
    
    // Add transactions
    transactions.slice(0, 5).forEach(transaction => {
        const transactionItem = document.createElement('div');
        transactionItem.className = 'transaction-item';
        transactionItem.innerHTML = `
            <div class="transaction-info">
                <h4>${transaction.type}</h4>
                <div class="transaction-date">${formatDate(transaction.date)} | ${transaction.method}</div>
            </div>
            <div class="transaction-amount">+${formatCurrency(transaction.amount)}</div>
        `;
        transactionList.appendChild(transactionItem);
    });
}

// Update portfolio chart
function updatePortfolioChart(investor) {
    const ctx = document.getElementById('portfolioChart');
    if (!ctx) return;
    
    const chartCtx = ctx.getContext('2d');
    
    // Calculate cumulative returns for the last 12 months
    const monthlyReturn = investor.fixedMonthlyReturn || 11000;
    const data = [];
    for (let i = 0; i < 12; i++) {
        data.push(monthlyReturn * (12 - i));
    }
    data.reverse();
    
    new Chart(chartCtx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
                label: 'Cumulative Returns',
                data: data,
                borderColor: '#d4af37',
                backgroundColor: 'rgba(212, 175, 55, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return formatCurrency(context.parsed.y);
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return formatCurrency(value);
                        }
                    },
                    grid: { color: 'rgba(0, 0, 0, 0.05)' }
                },
                x: {
                    grid: { color: 'rgba(0, 0, 0, 0.05)' }
                }
            }
        }
    });
}

// Logout function
function logout() {
    if (confirm('Are you sure you want to logout?')) {
        localStorage.removeItem('omkar_investor');
        localStorage.removeItem('omkar_investor_id');
        localStorage.removeItem('omkar_last_login');
        window.location.href = 'partner-portal.html';
    }
}

// Auto-logout after 30 minutes
function setupAutoLogout() {
    let timeout = 30 * 60 * 1000; // 30 minutes
    
    const resetTimer = () => {
        clearTimeout(window.logoutTimer);
        window.logoutTimer = setTimeout(logout, timeout);
    };
    
    // Reset timer on user activity
    ['click', 'mousemove', 'keypress'].forEach(event => {
        document.addEventListener(event, resetTimer);
    });
    
    resetTimer(); // Start the timer
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Check if user is logged in
    if (!checkLogin()) return;
    
    // Load dashboard data
    loadDashboardData();
    
    // Setup auto-logout
    setupAutoLogout();
    
    // Setup logout button
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', logout);
    }
    
    // Setup print button
    const printBtn = document.querySelector('button[onclick="window.print()"]');
    if (printBtn) {
        printBtn.onclick = function() {
            window.print();
        };
    }
    
    // Update copyright year
    document.querySelectorAll('.footer-bottom p').forEach(p => {
        p.innerHTML = p.innerHTML.replace('2024', new Date().getFullYear());
    });
});

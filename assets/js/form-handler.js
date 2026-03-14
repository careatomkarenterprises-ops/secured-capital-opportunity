// Universal Form Handler for TRFSK OMKAR SERVICES
// This works on ALL pages with forms

(function() {
    'use strict';
    
    // Configuration
    const FORMSPREE_ENDPOINTS = {
        consultation: 'https://formspree.io/f/mdkqpkqp', // Your Omkar Enterprises Contact form
        newsletter: 'https://formspree.io/f/YOUR_NEWSLETTER_FORM',
        contact: 'https://formspree.io/f/mdkqpkqp', // Same form for now
        investor: 'https://formspree.io/f/mdkqpkqp' // Same form for now
    };
    
    // Track form submissions for analytics
    function trackFormSubmission(formName, formData) {
        if (typeof gtag !== 'undefined') {
            gtag('event', 'generate_lead', {
                'event_category': 'Form',
                'event_label': formName,
                'value': formData.get('email') ? 1 : 0
            });
        }
        
        // Facebook Pixel (if you use it)
        if (typeof fbq !== 'undefined') {
            fbq('track', 'Lead', {
                content_name: formName,
                content_category: 'Form Submission'
            });
        }
    }
    
    // Add hidden fields to identify which page/form
    function enhanceFormData(formData, formType) {
        // Add page URL
        formData.append('page_url', window.location.href);
        formData.append('page_title', document.title);
        
        // Add timestamp
        formData.append('submitted_at', new Date().toISOString());
        
        // Add form type identifier
        formData.append('form_type', formType);
        
        // Add UTM parameters if present in URL
        const urlParams = new URLSearchParams(window.location.search);
        const utmParams = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
        utmParams.forEach(param => {
            if (urlParams.has(param)) {
                formData.append(param, urlParams.get(param));
            }
        });
        
        return formData;
    }
    
    // Show notification to user
    function showNotification(message, type = 'success') {
        // Check if we already have a notification container
        let container = document.getElementById('form-notification-container');
        if (!container) {
            container = document.createElement('div');
            container.id = 'form-notification-container';
            container.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 9999;
                max-width: 350px;
            `;
            document.body.appendChild(container);
        }
        
        // Create notification
        const notification = document.createElement('div');
        notification.style.cssText = `
            background: ${type === 'success' ? '#10b981' : '#ef4444'};
            color: white;
            padding: 16px 20px;
            border-radius: 8px;
            margin-bottom: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            animation: slideIn 0.3s ease;
            font-family: 'Inter', sans-serif;
            display: flex;
            align-items: center;
            gap: 10px;
        `;
        
        notification.innerHTML = `
            <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'}"></i>
            <span>${message}</span>
        `;
        
        container.appendChild(notification);
        
        // Auto remove after 5 seconds
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.parentNode.removeChild(notification);
                }
            }, 300);
        }, 5000);
    }
    
    // Add CSS animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        @keyframes slideOut {
            from { transform: translateX(0); opacity: 1; }
            to { transform: translateX(100%); opacity: 0; }
        }
    `;
    document.head.appendChild(style);
    
    // Handle form submission
    async function handleFormSubmit(form, formType) {
        const submitButton = form.querySelector('button[type="submit"]');
        const originalText = submitButton.innerHTML;
        
        // Disable button and show loading
        submitButton.disabled = true;
        submitButton.innerHTML = '<i class="fas fa-spinner fa-pulse"></i> Submitting...';
        
        try {
            // Get form data
            const formData = new FormData(form);
            
            // Enhance with tracking data
            const enhancedData = enhanceFormData(formData, formType);
            
            // Track submission
            trackFormSubmission(formType, enhancedData);
            
            // Submit to Formspree
            const response = await fetch(FORMSPREE_ENDPOINTS[formType] || FORMSPREE_ENDPOINTS.contact, {
                method: 'POST',
                body: enhancedData,
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (response.ok) {
                // Success
                showNotification('Thank you! Our team will contact you shortly.', 'success');
                form.reset();
                
                // Redirect if specified in Formspree settings
                const redirectUrl = form.getAttribute('data-redirect');
                if (redirectUrl) {
                    setTimeout(() => {
                        window.location.href = redirectUrl;
                    }, 2000);
                }
            } else {
                // Error from Formspree
                const errorData = await response.json();
                throw new Error(errorData.error || 'Submission failed');
            }
            
        } catch (error) {
            console.error('Form submission error:', error);
            showNotification('Submission failed. Please try again or WhatsApp us directly.', 'error');
        } finally {
            // Re-enable button
            submitButton.innerHTML = originalText;
            submitButton.disabled = false;
        }
    }
    
    // Initialize all forms on the page
    function initializeForms() {
        // Find all forms that should use Formspree
        const forms = document.querySelectorAll('form[data-formspree]');
        
        forms.forEach(form => {
            const formType = form.getAttribute('data-form-type') || 'consultation';
            
            // Remove any existing listeners
            form.removeEventListener('submit', form._submitHandler);
            
            // Create new handler
            form._submitHandler = function(e) {
                e.preventDefault();
                handleFormSubmit(form, formType);
            };
            
            // Add listener
            form.addEventListener('submit', form._submitHandler);
        });
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeForms);
    } else {
        initializeForms();
    }
    
    // Expose for dynamic forms
    window.TRFSKForms = {
        submitForm: handleFormSubmit,
        showNotification: showNotification
    };
    
})();

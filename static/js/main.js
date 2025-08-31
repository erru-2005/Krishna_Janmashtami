// Main JavaScript file for Krishna Janmashtami Website

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initScrollEffects();
    initCountdownTimer();
    initSmoothScrolling();
    initFormValidation();
    initLoadingStates();
});

// Scroll effects for navbar
function initScrollEffects() {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }
}

// Countdown timer for the event
function initCountdownTimer() {
    const countdownElement = document.getElementById('countdown');
    if (countdownElement) {
        const eventDate = new Date('2024-08-26T00:00:00').getTime();
        
        const timer = setInterval(function() {
            const now = new Date().getTime();
            const distance = eventDate - now;
            
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            countdownElement.innerHTML = `
                <div class="row text-center">
                    <div class="col-3">
                        <div class="countdown-item">
                            <h3 class="text-primary fw-bold">${days}</h3>
                            <small class="text-muted">Days</small>
                        </div>
                    </div>
                    <div class="col-3">
                        <div class="countdown-item">
                            <h3 class="text-primary fw-bold">${hours}</h3>
                            <small class="text-muted">Hours</small>
                        </div>
                    </div>
                    <div class="col-3">
                        <div class="countdown-item">
                            <h3 class="text-primary fw-bold">${minutes}</h3>
                            <small class="text-muted">Minutes</small>
                        </div>
                    </div>
                    <div class="col-3">
                        <div class="countdown-item">
                            <h3 class="text-primary fw-bold">${seconds}</h3>
                            <small class="text-muted">Seconds</small>
                        </div>
                    </div>
                </div>
            `;
            
            if (distance < 0) {
                clearInterval(timer);
                countdownElement.innerHTML = '<h3 class="text-success">Event has started!</h3>';
            }
        }, 1000);
    }
}

// Smooth scrolling for anchor links
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Form validation
function initFormValidation() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('is-invalid');
                } else {
                    field.classList.remove('is-invalid');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showAlert('Please fill in all required fields.', 'danger');
            }
        });
    });
}

// Loading states for buttons
function initLoadingStates() {
    const buttons = document.querySelectorAll('.btn[type="submit"]');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            if (this.form && this.form.checkValidity()) {
                this.innerHTML = '<span class="loading"></span> Processing...';
                this.disabled = true;
            }
        });
    });
}

// Show alert messages
function showAlert(message, type = 'info') {
    const alertContainer = document.createElement('div');
    alertContainer.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    alertContainer.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    alertContainer.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(alertContainer);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (alertContainer.parentNode) {
            alertContainer.remove();
        }
    }, 5000);
}

// Back to top button
function initBackToTop() {
    const backToTopButton = document.createElement('button');
    backToTopButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTopButton.className = 'btn btn-primary position-fixed';
    backToTopButton.style.cssText = 'bottom: 20px; right: 20px; z-index: 999; border-radius: 50%; width: 50px; height: 50px; display: none;';
    
    document.body.appendChild(backToTopButton);
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });
    
    backToTopButton.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Initialize back to top button
initBackToTop();

// Utility functions
const utils = {
    // Debounce function
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // Format date
    formatDate: function(date) {
        return new Date(date).toLocaleDateString('en-US', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    },
    
    // Validate email
    validateEmail: function(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    },
    
    // Copy to clipboard
    copyToClipboard: function(text) {
        navigator.clipboard.writeText(text).then(function() {
            showAlert('Copied to clipboard!', 'success');
        }).catch(function() {
            showAlert('Failed to copy to clipboard.', 'danger');
        });
    }
};

// Export for use in other scripts
window.KrishnaJanmashtami = {
    utils: utils,
    showAlert: showAlert
};

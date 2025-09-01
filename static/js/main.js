// Main JavaScript file for Krishna Janmashtami Website

// Hero Background Animation
function initHeroBackgroundAnimation() {
    const backgrounds = document.querySelectorAll('.hero-background');
    let currentIndex = 0;
    
    if (backgrounds.length === 0) return;
    
    function changeBackground() {
        // Remove active class from current background
        backgrounds[currentIndex].classList.remove('active');
        
        // Move to next background
        currentIndex = (currentIndex + 1) % backgrounds.length;
        
        // Add active class to new background
        backgrounds[currentIndex].classList.add('active');
    }
    
    // Change background every 5 seconds
    setInterval(changeBackground, 5000);
}

// Responsive functionality and enhancements
document.addEventListener('DOMContentLoaded', function() {
    // Initialize hero background animation
    initHeroBackgroundAnimation();
    
    // Responsive navigation handling
    const navbar = document.querySelector('.navbar');
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    // Close mobile menu when clicking on a link
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth < 992) {
                navbarCollapse.classList.remove('show');
            }
        });
    });
    
    // Handle navbar background on scroll
    window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    
    // Responsive image loading
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        img.addEventListener('load', () => {
            img.classList.add('loaded');
        });
        
        // Add loading animation
        if (!img.complete) {
            img.classList.add('loading');
        }
    });
    
    // Responsive table handling
    const tables = document.querySelectorAll('table');
    tables.forEach(table => {
        if (table.offsetWidth > window.innerWidth) {
            table.parentElement.classList.add('table-responsive');
        }
    });
    
    // Responsive form handling
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');
        inputs.forEach(input => {
            // Prevent zoom on iOS
            if (input.type !== 'file') {
                input.style.fontSize = '16px';
            }
        });
    });

    // Responsive button handling
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        // Add touch feedback for mobile
        button.addEventListener('touchstart', () => {
            button.style.transform = 'scale(0.95)';
        });
        
        button.addEventListener('touchend', () => {
            button.style.transform = '';
        });
    });
    
    // Responsive card handling
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        // Add hover effect only on devices that support hover
        if (window.matchMedia('(hover: hover)').matches) {
            card.classList.add('hover-enabled');
        }
    });
    
    // Responsive hero section
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        // Adjust hero height based on viewport
        function adjustHeroHeight() {
            const vh = window.innerHeight;
            const navbarHeight = navbar.offsetHeight;
            const minHeight = Math.max(40, (vh - navbarHeight) * 0.6);
            heroSection.style.minHeight = `${minHeight}px`;
        }
        
        adjustHeroHeight();
        window.addEventListener('resize', adjustHeroHeight);
    }
    
    // Responsive text sizing
    function adjustTextSizes() {
        
        
        
    }
    
    // Debounce function for performance
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    // Apply responsive adjustments
    const debouncedAdjustTextSizes = debounce(adjustTextSizes, 250);
    window.addEventListener('resize', debouncedAdjustTextSizes);
    
    // Initial call
    adjustTextSizes();
    
    // Responsive modal handling
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        modal.addEventListener('show.bs.modal', () => {
            // Ensure modal is properly sized on mobile
            if (window.innerWidth < 576) {
                modal.querySelector('.modal-dialog').style.margin = '1rem';
            }
        });
    });
    
    // Responsive carousel handling
    const carousels = document.querySelectorAll('.carousel');
    carousels.forEach(carousel => {
        // Adjust carousel height based on screen size
        function adjustCarouselHeight() {
            const items = carousel.querySelectorAll('.carousel-item');
            items.forEach(item => {
                const img = item.querySelector('img');
                if (img) {
                    const vw = window.innerWidth;
                    let height = 300; // Default height
                    
                    if (vw >= 992) height = 500;
                    else if (vw >= 768) height = 400;
                    else if (vw >= 576) height = 350;
                    else height = 250;
                    
                    img.style.height = `${height}px`;
                }
            });
        }
        
        adjustCarouselHeight();
        window.addEventListener('resize', debounce(adjustCarouselHeight, 250));
    });
    
    // Responsive grid adjustments
    function adjustGridLayout() {
        const vw = window.innerWidth;
        const gridItems = document.querySelectorAll('.col-lg-3, .col-md-6, .col-sm-12');
        
        gridItems.forEach(item => {
            if (vw < 576) {
                item.style.marginBottom = '1rem';
            } else {
                item.style.marginBottom = '';
            }
        });
    }
    
    adjustGridLayout();
    window.addEventListener('resize', debounce(adjustGridLayout, 250));
    
    // Touch gesture support for mobile
    let touchStartX = 0;
    let touchEndX = 0;
    
    document.addEventListener('touchstart', e => {
        touchStartX = e.changedTouches[0].screenX;
    });
    
    document.addEventListener('touchend', e => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    });
    
    function handleSwipe() {
        const swipeThreshold = 50;
        const diff = touchStartX - touchEndX;
        
        if (Math.abs(diff) > swipeThreshold) {
            // Handle swipe gestures if needed
            if (diff > 0) {
                // Swipe left
                console.log('Swipe left detected');
            } else {
                // Swipe right
                console.log('Swipe right detected');
            }
        }
    }
    
    // Performance optimization for mobile
    if ('serviceWorker' in navigator) {
        // Register service worker for better mobile performance
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('ServiceWorker registration successful');
            })
            .catch(err => {
                console.log('ServiceWorker registration failed');
            });
    }
    
    // Lazy loading for images
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
    
    // Responsive font loading
    if ('fonts' in document) {
        document.fonts.ready.then(() => {
            document.body.classList.add('fonts-loaded');
        });
    }
    
    // Add responsive classes to body
    function updateResponsiveClasses() {
        const vw = window.innerWidth;
        const body = document.body;
        
        // Remove existing responsive classes
        body.classList.remove('mobile', 'tablet', 'desktop', 'large-desktop');
        
        // Add appropriate class
        if (vw < 576) {
            body.classList.add('mobile');
        } else if (vw < 992) {
            body.classList.add('tablet');
        } else if (vw < 1200) {
            body.classList.add('desktop');
        } else {
            body.classList.add('large-desktop');
        }
    }
    
    updateResponsiveClasses();
    window.addEventListener('resize', debounce(updateResponsiveClasses, 250));
    
    // Console log for debugging
    console.log('Krishna Janmashtami Website - Responsive functionality loaded');
    console.log('Screen size:', window.innerWidth, 'x', window.innerHeight);
    console.log('Device pixel ratio:', window.devicePixelRatio);
});

// Export functions for use in other scripts
window.KrishnaJanmashtami = {
    adjustHeroHeight: function() {
        const heroSection = document.querySelector('.hero-section');
        if (heroSection) {
            const vh = window.innerHeight;
            const navbarHeight = document.querySelector('.navbar').offsetHeight;
            const minHeight = Math.max(40, (vh - navbarHeight) * 0.6);
            heroSection.style.minHeight = `${minHeight}px`;
        }
    },
    
    adjustTextSizes: function() {
        
    }
};

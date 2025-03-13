// document.addEventListener('DOMContentLoaded', function() {
//     // Function to animate progress bars
//     function animateProgressBars() {
//         const progressBars = document.querySelectorAll('.progress-bar');
//         const skillCards = document.querySelectorAll('.skill-card');
//
//         // Set data-skill attribute for each skill card based on title
//         skillCards.forEach(card => {
//             const skillTitle = card.querySelector('h3').textContent;
//             card.setAttribute('data-skill', skillTitle);
//         });
//
//         // Animate each progress bar with slight delay between each
//         progressBars.forEach((bar, index) => {
//             const value = bar.getAttribute('data-value');
//
//             // Use setTimeout to create a staggered animation effect
//             setTimeout(() => {
//                 bar.style.width = value + '%';
//             }, 100 * index);
//         });
//     }
//
//     // Check if we're on the about page
//     if (document.querySelector('.programming-skills')) {
//         // Wait a bit for page to render before animating
//         setTimeout(animateProgressBars, 300);
//     }
//
//     // Animate progress bars when scrolled into view
//     function isElementInViewport(el) {
//         const rect = el.getBoundingClientRect();
//         return (
//             rect.top <= (window.innerHeight || document.documentElement.clientHeight) &&
//             rect.bottom >= 0
//         );
//     }
//
//     function handleScrollAnimation() {
//         const skillsSection = document.querySelector('.programming-skills');
//
//         if (!skillsSection) return;
//
//         if (isElementInViewport(skillsSection)) {
//             animateProgressBars();
//             // Remove scroll listener once animated
//             window.removeEventListener('scroll', handleScrollAnimation);
//         }
//     }
//
//     window.addEventListener('scroll', handleScrollAnimation);
//
//     // Trigger initial check
//     handleScrollAnimation();
// });



document.addEventListener('DOMContentLoaded', function() {
    // Function to animate progress bars and enhance skill cards
    function animateProgressBars() {
        const progressBars = document.querySelectorAll('.progress-bar');
        const skillCards = document.querySelectorAll('.skill-card');

        // Set data-skill attribute for each skill card based on title
        skillCards.forEach(card => {
            const skillTitle = card.querySelector('h3').textContent.trim();
            card.setAttribute('data-skill', skillTitle);

            // Add interactive hover functionality
            card.addEventListener('mouseenter', function() {
                this.classList.add('active');
            });

            card.addEventListener('mouseleave', function() {
                this.classList.remove('active');
            });
        });

        // Animate each progress bar with slight delay between each
        progressBars.forEach((bar, index) => {
            const value = bar.getAttribute('data-value');

            // Use setTimeout to create a staggered animation effect
            setTimeout(() => {
                bar.style.width = value + '%';

                // Add percentage text to progress bar
                const percentText = document.createElement('span');
                percentText.className = 'percent-text';
                percentText.textContent = value + '%';

                // Only append if it doesn't already exist
                if (!bar.querySelector('.percent-text')) {
                    bar.appendChild(percentText);
                }

                // Add completed class for additional styling
                if (parseInt(value) >= 80) {
                    bar.classList.add('high-skill');
                } else if (parseInt(value) >= 50) {
                    bar.classList.add('medium-skill');
                }
            }, 150 * index);
        });
    }

    // Function to reset progress bars for re-animation
    function resetProgressBars() {
        const progressBars = document.querySelectorAll('.progress-bar');
        progressBars.forEach(bar => {
            bar.style.width = '0%';
        });
    }

    // Better check if element is in viewport with threshold
    function isElementInViewport(el, threshold = 0.3) {
        const rect = el.getBoundingClientRect();
        const windowHeight = window.innerHeight || document.documentElement.clientHeight;

        // Element is considered in viewport when certain percentage is visible
        return (
            rect.top <= windowHeight * (1 - threshold) &&
            rect.bottom >= windowHeight * threshold
        );
    }

    // Handle scroll animation with improved visibility detection
    function handleScrollAnimation() {
        const skillsSection = document.querySelector('.programming-skills');

        if (!skillsSection) return;

        if (isElementInViewport(skillsSection)) {
            // Only animate if not already animated
            if (!skillsSection.classList.contains('animated')) {
                animateProgressBars();
                skillsSection.classList.add('animated');
            }
        } else {
            // Reset when out of viewport for re-animation when scrolled back
            if (skillsSection.classList.contains('animated')) {
                resetProgressBars();
                skillsSection.classList.remove('animated');
            }
        }
    }

    // Add intersection observer for better performance
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateProgressBars();
                    entry.target.classList.add('animated');
                } else {
                    resetProgressBars();
                    entry.target.classList.remove('animated');
                }
            });
        }, {
            threshold: 0.3
        });

        const skillsSection = document.querySelector('.programming-skills');
        if (skillsSection) {
            observer.observe(skillsSection);
        }
    } else {
        // Fallback to scroll event for older browsers
        window.addEventListener('scroll', handleScrollAnimation);
        window.addEventListener('resize', handleScrollAnimation);
    }

    // Add tilt effect to cards for more interactivity
    const skillCards = document.querySelectorAll('.skill-card');
    skillCards.forEach(card => {
        card.addEventListener('mousemove', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const deltaX = (x - centerX) / centerX;
            const deltaY = (y - centerY) / centerY;

            this.style.transform = `perspective(1000px) rotateX(${deltaY * -3}deg) rotateY(${deltaX * 3}deg) translateY(-5px)`;
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });

    // Initial check
    const skillsSection = document.querySelector('.programming-skills');
    if (skillsSection && isElementInViewport(skillsSection)) {
        animateProgressBars();
        skillsSection.classList.add('animated');
    }
});
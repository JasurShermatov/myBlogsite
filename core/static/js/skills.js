document.addEventListener('DOMContentLoaded', function() {
    // Function to animate progress bars
    function animateProgressBars() {
        const progressBars = document.querySelectorAll('.progress-bar');
        const skillCards = document.querySelectorAll('.skill-card');

        // Set data-skill attribute for each skill card based on title
        skillCards.forEach(card => {
            const skillTitle = card.querySelector('h3').textContent;
            card.setAttribute('data-skill', skillTitle);
        });

        // Animate each progress bar with slight delay between each
        progressBars.forEach((bar, index) => {
            const value = bar.getAttribute('data-value');

            // Use setTimeout to create a staggered animation effect
            setTimeout(() => {
                bar.style.width = value + '%';
            }, 100 * index);
        });
    }

    // Check if we're on the about page
    if (document.querySelector('.programming-skills')) {
        // Wait a bit for page to render before animating
        setTimeout(animateProgressBars, 300);
    }

    // Animate progress bars when scrolled into view
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.bottom >= 0
        );
    }

    function handleScrollAnimation() {
        const skillsSection = document.querySelector('.programming-skills');

        if (!skillsSection) return;

        if (isElementInViewport(skillsSection)) {
            animateProgressBars();
            // Remove scroll listener once animated
            window.removeEventListener('scroll', handleScrollAnimation);
        }
    }

    window.addEventListener('scroll', handleScrollAnimation);

    // Trigger initial check
    handleScrollAnimation();
});
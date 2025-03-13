document.addEventListener('DOMContentLoaded', () => {
    const educationCards = document.querySelectorAll('.education-card');

    educationCards.forEach((card, index) => {
        const details = card.querySelector('.education-details');
        const toggleIcon = card.querySelector('.toggle-icon');

        // Initialize collapsed state
        if (details) {
            details.style.maxHeight = '0';
            details.style.overflow = 'hidden';
            details.style.transition = 'max-height 0.5s ease';
        }

        // Toggle card on click
        card.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent closing when clicking inside the card

            // Close other cards
            educationCards.forEach((otherCard, otherIndex) => {
                if (otherIndex !== index && otherCard.classList.contains('expanded')) {
                    otherCard.classList.remove('expanded');
                    const otherDetails = otherCard.querySelector('.education-details');
                    if (otherDetails) {
                        otherDetails.style.maxHeight = '0';
                    }
                    const otherIcon = otherCard.querySelector('.toggle-icon');
                    if (otherIcon) {
                        otherIcon.classList.remove('rotate');
                    }
                }
            });

            // Toggle the clicked card
            card.classList.toggle('expanded');

            if (details) {
                if (card.classList.contains('expanded')) {
                    details.style.maxHeight = details.scrollHeight + 'px';
                    // Smooth scroll to the card
                    card.scrollIntoView({ behavior: 'smooth', block: 'center' });
                } else {
                    details.style.maxHeight = '0';
                }
            }

            if (toggleIcon) {
                toggleIcon.classList.toggle('rotate');
            }
        });

        // Add glowing effect on hover
        card.addEventListener('mouseenter', () => {
            card.style.boxShadow = '0 0 20px rgba(255, 111, 97, 0.3)';
        });

        card.addEventListener('mouseleave', () => {
            if (!card.classList.contains('expanded')) {
                card.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.1)';
            }
        });
    });

    // Adjust max-height on window resize
    window.addEventListener('resize', () => {
        educationCards.forEach((card) => {
            if (card.classList.contains('expanded')) {
                const details = card.querySelector('.education-details');
                if (details) {
                    details.style.maxHeight = details.scrollHeight + 'px';
                }
            }
        });
    });

    // Close cards when clicking outside
    document.addEventListener('click', (event) => {
        educationCards.forEach((card) => {
            if (!card.contains(event.target)) {
                card.classList.remove('expanded');
                const details = card.querySelector('.education-details');
                if (details) {
                    details.style.maxHeight = '0';
                }
                const toggleIcon = card.querySelector('.toggle-icon');
                if (toggleIcon) {
                    toggleIcon.classList.remove('rotate');
                }
            }
        });
    });
});
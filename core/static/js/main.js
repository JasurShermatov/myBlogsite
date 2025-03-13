document.addEventListener('DOMContentLoaded', function() {
  // Mobile menu toggle
  const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', function() {
      mobileMenuToggle.classList.toggle('active');
      navLinks.classList.toggle('active');
    });
  }

  // Close messages
  const closeButtons = document.querySelectorAll('.close-message');
  closeButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      const message = button.parentElement;
      message.style.opacity = '0';
      setTimeout(function() {
        message.remove();
      }, 300);
    });
  });

  // Auto close messages after 5 seconds
  const messages = document.querySelectorAll('.message');
  messages.forEach(function(message) {
    setTimeout(function() {
      message.style.opacity = '0';
      setTimeout(function() {
        message.remove();
      }, 300);
    }, 5000);
  });
});







document.addEventListener('DOMContentLoaded', () => {
    const iconLinks = document.querySelectorAll('.icon-link');

    iconLinks.forEach(link => {
        link.addEventListener('mouseover', () => {
            link.style.transform = 'scale(1.2)';
            link.style.backgroundColor = '#000';
            link.style.color = '#fff';
            link.style.transition = 'all 0.3s ease';
        });

        link.addEventListener('mouseout', () => {
            link.style.transform = 'scale(1)';
            link.style.backgroundColor = '#f2f2f2';
            link.style.color = '#000';
        });
    });
});







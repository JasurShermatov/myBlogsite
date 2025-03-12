document.addEventListener('DOMContentLoaded', function() {
  // Portfolio filtering
  const filterButtons = document.querySelectorAll('.filter-btn');
  const portfolioItems = document.querySelectorAll('.portfolio-item');

  filterButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      // Update active button
      filterButtons.forEach(function(btn) {
        btn.classList.remove('active');
      });
      button.classList.add('active');

      // Filter items
      const filter = button.dataset.filter;

      portfolioItems.forEach(function(item) {
        if (filter === 'all' || item.dataset.category === filter) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });

  // Portfolio modal
  const modalTriggers = document.querySelectorAll('.portfolio-modal-trigger');
  const modals = document.querySelectorAll('.portfolio-modal');
  const closeButtons = document.querySelectorAll('.close-modal');

  modalTriggers.forEach(function(trigger) {
    trigger.addEventListener('click', function(e) {
      e.preventDefault();
      const modalId = 'portfolioModal' + trigger.dataset.id;
      const modal = document.getElementById(modalId);

      if (modal) {
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
      }
    });
  });

  closeButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      const modal = button.closest('.modal');
      modal.style.display = 'none';
      document.body.style.overflow = 'auto';
    });
  });

  // Close modal when clicking outside the modal content
  window.addEventListener('click', function(e) {
    modals.forEach(function(modal) {
      if (e.target === modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
      }
    });
  });
});

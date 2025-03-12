document.addEventListener('DOMContentLoaded', function() {
  // Blog post modal
  const modalTriggers = document.querySelectorAll('.blog-modal-trigger');
  const modals = document.querySelectorAll('.blog-modal');
  const closeButtons = document.querySelectorAll('.close-modal');

  modalTriggers.forEach(function(trigger) {
    trigger.addEventListener('click', function(e) {
      e.preventDefault();
      const modalId = 'blogModal' + trigger.dataset.id;
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

document.addEventListener('DOMContentLoaded', function () {
  const updateHeaderElement = document.querySelector('#update_header');

  updateHeaderElement.addEventListener('click', function () {
      const headerElement = document.querySelector('header');
      headerElement.textContent = 'New Header!!!';
  });
});

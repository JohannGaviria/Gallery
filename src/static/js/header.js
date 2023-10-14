document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menu-toggle');
    const menuIcon = document.getElementById('menu-icon');
    const closeIcon = document.getElementById('close-icon');
    const menuNav = document.querySelector('.menu-navegacion');

    function toggleMenuIcon() {
        menuIcon.style.display = menuIcon.style.display === 'none' ? 'block' : 'none';
        closeIcon.style.display = closeIcon.style.display === 'none' ? 'block' : 'none';
    }

    menuToggle.addEventListener('click', function () {
        menuNav.classList.toggle('show-menu');
        toggleMenuIcon();
    });
    
});
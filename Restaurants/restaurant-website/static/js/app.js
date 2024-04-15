document.addEventListener('DOMContentLoaded', function() {
    console.log("The website is fully loaded!");

    // Example of adding dynamic behavior
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    navbarToggler.addEventListener('click', function() {
        navbarCollapse.classList.toggle('show');
    });

    // More interactivity can be added here as needed
});

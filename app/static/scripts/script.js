// ACTIVE NAV SELECTOR

    // Get the current page path
    var activePage = window.location.pathname;

    // Remove the '/' character from the activePage string
    activePage = activePage.replace('/', '');

    // Set the active page in local storage
    if (activePage === '') {
        activePage = 'home';
    }

    localStorage.setItem('active-page', activePage);

    const list = document.querySelectorAll('.pNavItem');
    function activeItem() {
        list.forEach((item) =>
        item.classList.remove('active'));
        this.classList.add('active');
        localStorage.setItem('active-page', this.firstElementChild.id);
    }

    document.getElementById(activePage).classList.add('active');
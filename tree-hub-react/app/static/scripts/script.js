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
      
// UPDATE SEASON
function updateSeason() {
    var currentMonth = (new Date()).getMonth();
    var body = document.querySelector('body');
    var season;
  
    if (currentMonth >= 2 && currentMonth <= 4) {
        season = 'spring';
        body.className = season;
    } else if (currentMonth >= 5 && currentMonth <= 7) {
        season = 'summer';
        body.className = season;
    } else if (currentMonth >= 8 && currentMonth <= 10) {
        season = 'autumn';
        body.className = season;
    } else {
        season = 'winter';
        body.className = season;
    }
}

updateSeason();

// LOCATION SCRIPTS
    if (activePage === 'location'){};

// NEW TREE SCRIPTS    
    if (activePage === 'newTree'){};

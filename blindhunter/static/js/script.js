// responsive navbar initialization
document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
});

// date initialization
document.addEventListener('DOMContentLoaded', function() {
    let today = new Date().toISOString().substring(0, 10);
    document.getElementById('date').value = today;
});

// select company in review initialization
document.addEventListener('DOMContentLoaded', function() {
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
});

// modal initialization
document.addEventListener('DOMContentLoaded', function() {
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);
});

// responsive navbar initialization
document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
// datepicker initialization
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd/mm/yy",
      i18n: {done: "Select"}
    });
// select company in review initialization
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
});
// modal initialization
document.addEventListener('DOMContentLoaded', function() {
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);
  });

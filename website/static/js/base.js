// get the location of the current page

let path = window.location.pathname;
let pagevar = path.split("/");

// update the class of the home link to active
document.getElementById(pagevar[1]).className = "nav-link active";


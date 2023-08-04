// get the location of the current page

let path = window.location.pathname;
let pagevar = path.split("/");

document.getElementById(pagevar[1]).className = "nav-link active";

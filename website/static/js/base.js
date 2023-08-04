// get the location of the current page

let path = window.location.pathname;
let pagevar = path.split("/");

alert(pagevar[1])


document.getElementById(pagevar[1]).className = "nav-link active";

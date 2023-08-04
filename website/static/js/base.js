// get the location of the current page

let path = window.location.pathname;
let pagevar = path.split("/");

// update the class of the home link to active
if (pagevar[1] == "") {
    document.getElementById("home").className = "nav-link active";
} else {
    document.getElementById(pagevar[1]).className = "nav-link active";
}
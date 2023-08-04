// get the location of the current page

let path = window.location.pathname;
let pagevar = path.split("/");

alert(pagevar[1])

if (pagevar == "home") {
    // update the class of the home link to active
    document.getElementById("home").className = "nav-item active";
} 
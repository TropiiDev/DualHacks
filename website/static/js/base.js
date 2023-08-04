// get the location of the current page

let path = window.location.pathname;
let pagevar = path.split("/");

alert(pagevar[1])

if (pagevar == "home") {
    // update the class of the home link to active
    document.getElementById("home").className = "nav-link active";
} else if (pagevar == "enroll") {
    document.getElementById("enroll").className = "nav-link active";
}
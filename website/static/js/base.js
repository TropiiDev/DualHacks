// get the location of the current page

let path = window.location.pathname;
let pagevar = path.split("/");

if (pagevar[1] == "home") {
    // update the class of the home link to active
    document.getElementById("home").className = "nav-link active";
} else if (pagevar[1] == "enroll") {
    document.getElementById("enroll").className = "nav-link active";
} else if (pagevar[1] == "login") {
    document.getElementById("login").className = "nav-link active";
} else if (pagevar[1] == "pricing") {
    document.getElementById("pricing").className = "nav-link active";
} else if (pagevar[1] == "classes") {
    document.getElementById("classes").className = "nav-link active";
} else if (pagevar[1] == "courses") {
    document.getElementById("courses").className = "nav-link active";
}

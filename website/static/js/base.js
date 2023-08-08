let path = window.location.pathname;
let pagevar = path.split("/");

if (pagevar[1] == "") {
    document.getElementById("home").className = "nav-link active";
} else {
    document.getElementById(pagevar[1]).className = "nav-link active";
}
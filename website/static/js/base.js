// get the location of the current page

let path = window.location.pathname;
let pagevar = path.split("/");
console.log(pagevar[0])
// update the class of the home link to active
if (pagevar[1] == "") {
    document.getElementById("home").className = "nav-link active";
} else {
    document.getElementById(pagevar[1]).className = "nav-link active";
}

if (pagevar[0] == 'user'){
    console.log('test')
}


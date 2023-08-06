// get the location of the current page

let path = window.location.pathname;
let pagevar = path.split("/");
console.log('loaded')
// update the class of the home link to active
if (pagevar[1] == "") {
    console.log('if');
    document.getElementById("home").className = "nav-link active";
} else {
    console.log('else');
    try{
        document.getElementById(pagevar[1]).className = "nav-link active";
    }
    catch (TypeError){
        
    }
}
console.log(pagevar);
if (pagevar[1] == 'user'){
    var xmlHttp = new XMLHttpRequest();
    // https://stackoverflow.com/questions/247483/http-get-request-in-javascript
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            console.log(xmlHttp.responseText);
    }
    xmlHttp.open('GET', '/getprofilepic', true, );
    xmlHttp.send('null');

    console.log(xmlHttp.responseText);

    const reader = new FileReader();
   
    document.getElementById('pfpfileselector').src = xmlHttp.responseText
}


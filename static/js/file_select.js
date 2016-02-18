//Capture the URL from the user via a pop-up text box
function GetFileURL() {
    var URL = prompt("Please enter the URL of the file you want to upload");
    if (!URLExists(URL)) {
        alert("Invalid URL!!!"); 
    }
}

function URLExists(url) {
    var http = new XMLHttpRequest();
    http.open('HEAD', url, false);
    http.send();
    alert(http.status);
    return http.status!=404;
}

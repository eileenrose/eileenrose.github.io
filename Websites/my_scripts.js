
/* tried to change the value of heading tag before it loaded because
HTML document loads as goes down, so wasn't loaded by the time
we called the Javascript*/
// wait for window to load then apply
window.onload = function() {
var heading = document.getElementById("heading");
heading.innerText = "Hiya!";
}

function getData(){
  var answer = $("input").val();
  var favoriteBadGuy = document.userData.favorites.value;
  console.log(favoriteBadGuy);
}
function setup(){
  $("button").click(getData);
}
$(document).ready(setup);

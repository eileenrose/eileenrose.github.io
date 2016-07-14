function mouseIn(){
  $("#contact").fadeOut(10000);
  $("#info").show();
}
function mouseOut(){
  $("#info").hide();
  $("#contact").fadeIn(10000);
}

function setup(){
  $("#info").hide();
  $("#contact").hover(mouseIn, mouseOut);
}

$(document).ready(setup);

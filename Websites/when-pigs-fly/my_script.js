function showWhenClicked() {
    $("#pig").show();
    $("#pig2").show();
}

function hideWhenClicked() {
    $("#pig").hide();
    $("#pig2").hide();
}

/*function moveWhenClicked(){
  $("#pig").animate({left: "150px"}, 100);
}*/

function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    //$("#moveWhenClicked").click(moveWhenClicked);
    $("img").click(function(){
    $("div").animate({left: "250px"});
});
}

$(document).ready(setup);

/*
function flyThePig(){
var nextPig = $("#pig").clone();
$(nextPig).attr("id", "pig2");
$("pig").parent().prepend(nextPig);

$("pig")
.animate({
marginLeft: 500,
width: 50
}, 2000)
.fadeOut(2000)
}
*/

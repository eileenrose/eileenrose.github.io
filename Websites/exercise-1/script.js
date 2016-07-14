/* You will save your code during today's demos and exercises here. */
function updateFrame(){
  $("#android img").fadeOut(1500);
  var pizza = $("#string h5").detach();
  $("#PEP")
  .append(pizza)
  .children("b")
  .addClass("newColor");
  //select, use period, but just adding value, so no need
  //addClass assumes already selected the wanted object
  //only specify with selector
}

function renewFrame(){
  $("#android img").fadeIn(1500);
}


function setupHandlers(){
  $("img").on("mouseenter", function(){
    $(this).animate({width: 200}, 2000);
    //$(this).slideUp();
  });

  $("img").on("mouseleave", function(){
    $(this).animate({width: 50}, 2000);
  });
}

$(document).ready(setupHandlers);
// assigns to event document object raises once it's rendered
// when happens, run function in parameter

$("button").click(function(){
  $("img").animate({width: 200}, 2000);
});

/*function setupHandlers(){
  var isReaction = false;
  var reactionTime;
  $("#PEP").click(function(){
    console.log("click");
    var d = new Date();
    if (!isReaction){
      isReaction = true;
      reactionTime = d.getTime();
      //console.log(reactionTime);
    }
    else{
      var endTime = d.getTime();
      console.log(endTime-reactionTime);
      isReaction = false;
    }
  })
}*/

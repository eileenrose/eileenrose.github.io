function setupHandlers(){
  $("h1").css("color", "black");
  $("#bi").css("color", "black");
  $("#bi").css("font-size", "24px");
  $("#ac").css("color", "black");
  $("#ac").css("font-size", "24px");

  $("img").on("mouseenter", function(){
    $(this).animate({width: 2000}, 2000);
    //$(this).slideUp();
  });

  $("img").on("mouseleave", function(){
    $(this).animate({width: 50}, 2000);
  });

  $("#bragging").click(function(){
    alert("Haha... I don't have any achievements :')");
  });
}

$(document).ready(setupHandlers);

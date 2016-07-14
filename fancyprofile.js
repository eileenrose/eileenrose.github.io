function setupHandlers(){
  $("h1").css("color", "black");
  $("i").css("color", "black")

  $("img").on("mouseenter", function(){
    $(this).animate({width: 2000}, 2000);
    //$(this).slideUp();
  });

  $("img").on("mouseleave", function(){
    $(this).animate({width: 50}, 2000);
  });


}

$(document).ready(setupHandlers);

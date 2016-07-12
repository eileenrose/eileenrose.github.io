console.log("And all our yesterdays are lighter fools");
console.log("The way to dust death");

var chicken = "Kentucky Fried Chicken";
var sushi = "Wherefore art thou?";
console.log(sushi + chicken);

function goGetLunch(name){
  alert("It's lunch time!");
  alert("Let's go, " + name);
}

//goGetLunch("Cucumber Sharks");
//goGetLunch(chicken +sushi + 45);
function checkout(item1, item2, item3, coupon){
  item3 = item3 - item3*coupon;
  return item1 + item2 + item3;
}

var total_cost = checkout(1, 1.5, 8, .1);
console.log("My total cost is $" + total_cost);

function timesTwo(intx){
  return intx+intx;
}

console.log(timesTwo(2));
console.log(timesTwo(3));

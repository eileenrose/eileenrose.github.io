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

/*function timesTwo(intx){
  return intx+intx;
}
function timesSix(intp){
  return intp*6;
}
function timesN(inty, intn){
  return inty*intn;
}

console.log(timesTwo(2));
console.log(timesTwo(3));
console.log(timesSix(1));
console.log(timesSix(6));
console.log(timesN(3,5));
console.log(timesN(5,2));

function timesSixV2(test){
   return timesTwo(test)*3
}
console.log(timesSixV2(2));
console.log(timesSixV2(4));
*/

//elephantbearmousecow, mouse
/*var ebmc = "ELEPHANTBEARMOUSECOW";
console.log(ebmc.substring(0,12) + ebmc.substring(12,17).toLowerCase() + ebmc.substring(17));
*/

function tigerMom(gpa){
  if (gpa >= 4.0){
    return "You did well.";
  }
  else if (gpa < 4.0 && gpa >= 3.5){
    return "Try harder.";
  }
  else{
    return "Better not sleep."
  }
}

function skeeball(score){
  alert("Your score is " + score);
  if (score > 450){
    return "Inconceivable!";
  }
  else if(score < 0){
    return "How badly did you do to get negative points?";
  }
  else if (score <= 450 && score >=350){
    return "Great";
  }
  else if (score < 350 && score >= 250){
    return "Good";
  }
  else{
    return "Pretty bad.";
  }
}

function fizzbuzz(number){
  if (number % 15 == 0){
    return "FizzBuzz";
  }
  else if (number % 3 == 0){
    return "Fizz";
  }
  else if (number % 5 == 0){
    return "Buzz";
  }
  else{
    return number;
  }
}

function reverseMidCapitalize(text){
  var middle = text.length/2;
  if (text.charAt(middle) == "1" || text.charAt(middle) == "2" || text.charAt(middle) == "3" ||text.charAt(middle) == "4" ||text.charAt(middle) == "5"|| text.charAt(middle) == "6"|| text.charAt(middle) == "7" || text.charAt(middle) == "8" || text.charAt(middle) == "9" || text.charAt(middle) == "0"){
    return "The middle is a number";
  }
  if (text.substring(middle,middle+1) == text.substring(middle,middle+1).toUpperCase()){
    return text.substring(0,middle) + text.charAt(middle).toLowerCase() + text.substring(middle+1);
  }
else{
  return text.substring(0,middle) + text.charAt(middle).toUpperCase() + text.substring(middle+1);
}
}

function chopandFlip(arraything){
  var mid;
  var temp;
if(arraything.length % 2 == 1){
 mid = (arraything.length / 2)+1;
 temp = arraything.splice(mid);
 return temp + "," + arraything;
 }
 else{
   mid = (arraything.length / 2);
   temp = arraything.splice(mid);
   return temp + "," + arraything;
 }
 /* var left = x.slice(0,mid);
 var right = x.slice(mid,x.length);
 var combine = right.concat(left);
 return combine*/
}

function setLoop(doubleNumbers){
  for (var i = 0; i < doubleNumbers.length; i++){
    doubleNumbers[i]*=2
    alert(doubleNumbers[i]);
  }
}

function favMovie(movie){
  for (var i = 0; i < movie.length; i++){
    alert(movie[i] + "? That is my favorite too!");
  }
}

function reverseArray(array2){
  var temp = new Array(); //var = [];
  var k = 0;
  for (var i = array2.length-1; i >= 0; i--){
    temp[k] = array2[i];
    k++;
  }
  return temp;
  //result.push(x[i]);
}

function twine(a1, a2){
  var a3 = new Array();
  var v = 0;
  if (a1.length > a2.length){
    for (var i = 0; i < a2.length; i++){
      a3[v] = a2[i];
      a3[v+1] = a1[i];
      v+=2;
    }
    for (var k = a1.length; k < a1.length; k++){
      a3[k+a2.length] = a1[k];
    }
    return a3;
    }
    else{
      for (var i = 0; i < a1.length; i++){
        a3[v] = a1[i];
        a3[v+1] = a2[i];
        v+=2;
      }
      for (var k = a1.length; k < a2.length; k++){
        a3[k+a1.length] = a2[k];
      }
      return a3;
    }
}
var fruitColors = {
  "apple" : "red",
  "tangerines" : "orange",
  "watermelon" : "green"
}

//var listStrings = ["Grim", "visaged", "War", "hath", "smooth'd", "his", "wrinkled", "front"];

function niceRegularBox(listStrings){
   //var inde = findLongestLength(listStrings);
   var max = 0;
   for (var i = 0; i < listStrings.length; i++){
     if (listStrings[i].length > max){
       max = listStrings[i].length;
     }
   }
   var endArray = -1;
   var boxarray = new Array();
   var p = 1;
   for (var j = 0 ; j < listStrings.length; j++){
     boxarray[p] = "|";
     boxarray[p]+= listStrings[j];
     for (var j2 = listStrings[j].length; j2 < max - 2; i++){
       boxarray[p]+=" "
     }
     boxarray[p]+="|";
     p++;

   }
   endArray = p;
   for (var k = 0; k < max + 2; i++){
     boxarray[0]+="-";
     boxarray[endArray]+="-"
   }
   for (var t = 0; t < boxarray.length; t++){
     console.log(boxarray[t]);
   }
}

/*function findLongestLength(listStrings){
  var max = 0;
  for (var i = 0; i < listStrings.length; i++){
    if (listStrings[i].length > max){
      max = listStrings[i].length;
    }
  }
  return max;
}*/

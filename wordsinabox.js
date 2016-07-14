console.log("bullshit");

var richard = ["Grim", "visaged", "War", "hath", "smooth'd", "his", "wrinkled", "front"];
var boxArray = new Array();

function niceRegularBox(richard){
  var max = 0;
  for (var q = 0; q < richard.length; q++){
    if (richard[q].length > max){
      max = richard[q].length;
    }
  }
  var placement = 1;
  var endArray = -1;
  for (var k = 0; k < richard.length; k++){
    boxArray[placement] += "| " + richard[k];
    for (var j = richard[k].length; j < max+2; j++){
      boxArray[placement] +=" ";
    }
    boxArray[placement] += "|";
    placement++;
  }
  endArray = placement;
  for (var r = 0; r <= max+4; r++){
    boxArray[0]+="-";
    boxArray[endArray]+="-";
  }
 printBox(boxArray);

}

function printBox(boxArray){
  for (var i = 0; i < boxArray.length; i++){
    console.log(boxArray[i]);
  }
}

/*
function findLongestLength(ls){
  var maxLengthSoFar = 0;
  for(var i = 0; i < ls.length; i++){
  if (maxLengthSoFar < ls[i].length){
  maxLengthSoFar = ls[i].length;
    }
  }
}
function niceRegularBox(ls){
  var maxLength = findLongestLength(ls);
  var lineToPrint = "-".repeat(maxLength+4)
  console.log(lineToPrint);
  for (var i = 0; i < ls.length; i++){
    lineToPrint = "| " + ls[i] + " ".repeat(maxLength + 4 - 2 - 1 -ls[i].length) + "|";
    console.log(lineToPrint);
  }
}
*/

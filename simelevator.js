



var elevatorLine = [];

function currentLine(elevatorLine){
  if (elevatorLine[0] == null){
    return "The line is currently empty";
  }
  else{
    var line = "The line is currently: ";
    for (var i = 0; i < elevatorLine.length-1; i++){
      line += "Floor " + elevatorLine[i] + ", ";
    }
    line+= "Floor " + elevatorLine[elevatorLine.length-1];
    return line;
  }
}

function pressFloorNumber(elevatorLine, order){
  var index = -1;
  for (var i = 0; i < elevatorLine.length; i++){
    if (elevatorLine[i] == order){
      index = i;
    }
  }
  return "Position " + (index+1);
}

function goToNextFloor(elevatorLine){
  var floor = elevatorLine.splice(0, 1);
  return "Floor " + floor;
}

function pushTheButton(button){
  elevatorLine.push(button);
}

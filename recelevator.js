var elevatorLine = [];

function currentLine(elevatorLine){
  if (elevatorLine[0] == null){
    return "The line is currently empty";
  }
  else{
    var line = "The line is currently: ";
    for (var i = elevatorLine.length-1; i > 0; i--){
      line += "Floor " + elevatorLine[i] + ", ";
    }
    line+= "Floor " + elevatorLine[0];
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
  return "Position " + (elevatorLine.length-index);
}

function goToNextFloor(elevatorLine){
  var floor = elevatorLine.splice(elevatorLine.length-1, elevatorLine.length);
  return "Floor " + floor;
}

function pushTheButton(button){
  elevatorLine.push(button);
}

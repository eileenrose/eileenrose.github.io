function square(position){
  return Math.pow(2, position-1);
}

function total(number){
  var n = 0;
  while (number >= 1){
    n+=square(number);
    number--;
  }
  return n;
}

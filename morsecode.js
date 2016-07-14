/*var translation = {
  "A": ".-",
  "B": "-...",
  "C": "-.-.",
  "D": "-..",
  "E": ".",
  "F": "..-.",
  "G": "--.",
  "H": "....",
  "I": "..",
  "J": ".---",
  "K": "-.-",
  "L": ".-..",
  "M": "--",
  "N": "-.",
  "O": "---",
  "P": ".--.",
  "Q": "--.-",
  "R": ".-.",
  "S": "...",
  "T": "-",
  "U": "..-",
  "V": "...-",
  "W": ".--",
  "X": "-..-",
  "Y": "-.--",
  "Z": "--..",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "0": "-----"
}*/

console.log("when i finished this i realized it was completely wrong but it's basically the same thing");

var translationL = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z',' '];
var translationD = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---',
'-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--',
'-..-','-.--','--..', ' '];
var translated = "";



function stringToMorse(code){
  code = code.toUpperCase();
  for (var i = 0; i < code.length - 1; i++){
    var letter = code.substring(i,i+1);
    for (var k = 0; k < translationL.length; k++){
      if (letter == translationL[k]){
        translated +=translationD[k];
        break;
      }
    }
  }
  return translated;
  /*var search = function(letter){
    for (var prop in translation){
      if (translation[prop].letter == letter){
        translated+=translation[letter];
      }
    }
  }
}*/
}

/*var search = function(name) {
  for(var prop in friends) {
    if(friends[prop].firstName === name) {
      console.log(friends[prop]);
      return friends[prop];
}}
*/

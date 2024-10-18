const prompt = require("prompt-sync")();

let number1 = Number(prompt("Enter number 1: "));
let number2 = Number(prompt("Enter number 2: "));
let result = (number1 === number2) ? true : false;
let statement = "";
if(result){
statement = "Similar number.";
}
else
{
statement = "Different number.";
}
alert("Number 1: "+number1+"\n"+
"Number 2: "+number2+"\n"+
"Result: "+statement);
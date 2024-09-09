let score = Number(prompt("Enter the score: "));
// Convert the score to a number and round it down
const numScore = Math.floor(Number(score));
// Use switch with true to allow for range comparisons
switch (true) {
case (numScore >= 90 && numScore <= 100):
alert('A');
break;
case (numScore >= 80 && numScore < 90):
alert('B');
break;
case (numScore >= 70 && numScore < 80):
alert('C');
break;
case (numScore >= 60 && numScore < 70):
alert('D');
break;
case (numScore >= 0 && numScore < 60):
alert('F');
break;
default:
alert('Invalid score');
}
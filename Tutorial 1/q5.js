let discount = netPrice = "";
let price = Number(prompt("Enter the price amount: "));
// Check for discount and price:
if(price >= 200){
discount = price*(0.15); //15% discount:
}
else if(price > 100 && price < 200){
discount = price*(0.05); //5% discount:
}
else{
discount = 0;
}
netPrice = price - discount;
alert("Entered Price: $"+Number(price).toFixed(2)+"\n"+
"Net Price: $"+Number(netPrice).toFixed(2)+"\n"+
"Discount Amount: $"+Number(discount).toFixed(2));
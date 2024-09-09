let num1Ref = document.getElementById("num1");
let num2Ref = document.getElementById("num2");
let resultRef = document.getElementById("outputArea");
let num1, num2;

document.getElementById("btnAdd").addEventListener("click", function(){
    num1 = parseInt(num1Ref.value);
    num2 = parseInt(num2Ref.value);
    resultRef.value = num1 + num2;
});

document.getElementById("btnSub").addEventListener("click", function(){
    num1 = parseInt(num1Ref.value);
    num2 = parseInt(num2Ref.value);
    resultRef.value = num1 - num2;
});

document.getElementById("btnMul").addEventListener("click", function(){
    num1 = parseInt(num1Ref.value);
    num2 = parseInt(num2Ref.value);
    resultRef.value = num1 * num2;
});

document.getElementById("btnDiv").addEventListener("click", function(){
    num1 = parseInt(num1Ref.value);
    num2 = parseInt(num2Ref.value);
    resultRef.value = (num1 / num2).toFixed(2);
});


document.getElementById("btnExp").addEventListener("click", function(){
    num1 = parseInt(num1Ref.value);
    num2 = parseInt(num2Ref.value);
    resultRef.value = num1 ** num2;
});

document.getElementById("btnMod").addEventListener("click", function(){
    num1 = parseInt(num1Ref.value);
    num2 = parseInt(num2Ref.value);
    resultRef.value = num1 % num2;
});
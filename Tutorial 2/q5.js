class Calculator{
    addition(a,b)
    {
        return a+b;
    }

    substraction(a,b)
    {
        return a-b;
    }

    multiplication(a,b)
    {
        return a*b;
    }

    division(a,b)
    {
        if(b===0)
        {
            return "Cannot divide by ZERO!!!";
            
        }

        return a/b;
    }
}

let calculator = new Calculator();

additionAnswer = calculator.addition(50, 20)
substractionAnswer = calculator.substraction(50, 20)
multiplicationAnswer = calculator.multiplication(50, 20)
divisionAnswer = calculator.division(50, 20)

console.log("Addition: " + additionAnswer);
console.log("Substraction: " + substractionAnswer);
console.log("Multiplication: " + multiplicationAnswer);
console.log("Division: " + divisionAnswer);

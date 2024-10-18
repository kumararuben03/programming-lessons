class BankAccount{
    constructor(balance = 0)
    {
        this._balance = balance;
    }

    deposit(amount)
    {
        this._balance += amount;
    }
    
    withdraw(amount)
    {
        if(amount <= this._balance){
            this._balance -= amount;
        } else {
            console.log("Insufficient funds");
        }
    }
}

let bank = new BankAccount(100)
bank.deposit(50)
bank.withdraw(30)

console.log("Current Balance:$" + bank._balance);
//Method 1
class Product{
    constructor(name, price){
        this._name = name;
        this._price = price;
    }
}

function applyDiscount(product, percentage){
    const discountAmount = product._price * (percentage/100)
    product._price -= discountAmount;
}

const laptop = new Product("Laptop", 1000)
applyDiscount(laptop, 10)
console.log(laptop._price);


//Method 2
class Product1{
    constructor(name, price){
        this._name = name;
        this._price = price;
    }
    applyDiscount(percentage){
        const discountAmount = this._price * (percentage/100)
        this._price -= discountAmount;
        return this._price;
    }

}

const lp = new Product1("Laptop", 1000)
afterDiscount = lp.applyDiscount(30)
console.log(`Price of ${lp._name.toLowerCase()} after discount is $${afterDiscount.toFixed(2)}`);

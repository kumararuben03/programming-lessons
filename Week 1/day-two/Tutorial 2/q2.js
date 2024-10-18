// Method 1
let arr2 = [10,25,35,40,55]

let total = 0
for (let i = 0; i < arr2.length; i++) 
    {
        total = arr2[i] + total    
    }
let avg = total/arr2.length

console.log("Total: " + total);
console.log("Average: " + avg);

//Method 2
function findAverage(arr)
{
    let total = 0;
    for (let i=0; i<arr.length; i++)
    {
        total += arr[i];
    }
    return total / arr.length;
}


let result = findAverage([10,25,35,40,55])
console.log("Average: " + result);
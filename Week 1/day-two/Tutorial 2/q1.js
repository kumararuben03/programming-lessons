function getMax(arr){
    let max = arr[0];

    for(let i=0; i<arr.length; i++)
    {
        if(arr[i] > max)
        {
            max = arr[i];
        }
    }
    return max
}

maxNum = getMax([3, 7, 2, 9, 1, 5])

console.log("Max number in the array is " + maxNum);
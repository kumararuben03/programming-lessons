let word = "Welcome to AI Academy."

let count = 0;

for(let i=0; i<word.length; i++)
{
    if(word[i] === 'e' || word[i] === 'E')
    {
        count++;
    }
}

console.log(count);
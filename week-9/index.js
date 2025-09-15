let random=Math.ceil(Math.random()*100);
let input=document.getElementById('input');
let res=document.getElementById('res');
let score=document.getElementById('score');
let count=0
function guessbtn()
{
    count++;
    if(input.value==random)
    {
        res.textContent='Congrats! Your guessing correct';
        res.style.color='green';
        score.textContent="No of chances: "+count;
    }
    else if(input.value>random)
    {
        res.textContent='Oops! Your guessing is too high';
        res.style.color='red';
        score.textContent="No of chances: "+count;

    }
    else if(input.value<random)
    {
        res.textContent='Oops! Your guessing is too low';
        res.style.color='red';
        score.textContent="No of chances: "+count;
        
    }
}
//fizzbuzz if divisible by 3 and 5 
//fizz if only divisible by 3
//buzz if only divisible by 5
function fizzbuzz(num){
    if(num%3===0 && num%5===0)
        {
            console.log('fizzbuzz')
        }
        else if(num%3===0 && num%5!=0)
            {
                console.log('fizz')
            }
            else if(num%3!=0 && num%5===0)
                {
                    console.log('buzz')
                }
                else{
                    console.log("not divisible by 3 or 5")
                }
}

fizzbuzz(1020);
fizzbuzz(1002);
fizzbuzz(1010);
fizzbuzz(1001);


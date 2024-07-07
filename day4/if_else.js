//if-else statement
let priceofchocolate = 80
let amountyouhave = 100

const canbuychocolate = (priceofchocolate <= amountyouhave)

if(canbuychocolate)
    {
        console.log("happy purchase")
    }else{
        console.log("sorry,you don't have enough amount")
    }
//nested if-else
let hours=13

if(hours>=7 && hours<=12)
    {
        console.log("serving breakfast")
    }else if(hours>=12 && hours<=18)
        {
            console.log("serving lunch")
        }else if(hours>=18 && hours<=24)
            {
                console.log("serving dinner")
            }
            else{
                console.log("sorry")
            }
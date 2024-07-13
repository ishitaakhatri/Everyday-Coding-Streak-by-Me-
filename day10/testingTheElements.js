//using every function 
const numbers = [2,4,6,8]

const arealleven = numbers.every(number => {
    return (number%2===0)
});

console.log(`arealleven : ${arealleven}`);

//using some function 

const atleastoneiseven = [1,2,3,4,5,6,7,8]

const isodd = atleastoneiseven.some(number => {
    return atleastoneiseven % 2 != 0;
})

console.log(`atleastoneisodd : ${isodd}`);
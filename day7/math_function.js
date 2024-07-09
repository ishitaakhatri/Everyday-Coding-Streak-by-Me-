console.log(Math.round(3.6));
console.log(Math.floor(3.6));
console.log(Math.ceil(3.6));
console.log(Math.max(1,2,3,4,5,6,7,8));
console.log(Math.min(54,43,32.21,67,89))
console.log(Math.pow(2,3));
console.log(Math.sqrt(25));
//if we want to have random numbers using math.random()that produces random number b/w 0and 1
let min=1;
let max=10;

const random_number= Math.round((Math.random() *(max-min)+min))

console.log(random_number)
//filter method
const numbers = [1,2,3,4,5,6,7,8];
 
const evenNumbers = numbers.filter(number => number%2===0);

console.log(evenNumbers);

//doing the same with array of objects

const employees = [
    {id:1,name:'alice',role:'developer'},
    {id:2,name:'bob',role:'marketing'},
    {id:3,name:'charlie',role:'designer'},
    {id:4,name:'david',role:'marketing'},
    {id:5,name:'micheal',role:'developer'},

]

const developers = employees.filter(employee => employee.role === 'developer');
console.log(developers);
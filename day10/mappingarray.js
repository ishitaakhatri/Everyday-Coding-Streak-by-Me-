//using map() method
const numbers= [1,2,3,4,5,6]

const square = numbers.map(num => num*num);
console.log(square);

//doing the same for array of objects 

const employees = [
    {id:1, name:'alice',email:'alice123@gmail.com'},
    {id:2, name:'bob',email:'bob123@gmail.com'},
    {id:3, name:'charlie',email:'charlie123@gmail.com'},
    {id:4, name:'david',email:'david123@gmail.com'},
    {id:5, name:'micheal',email:'micheal123@gmail.com'},
]

const emails = employees.map(employee => ({
    ...employees,
    email:employee.email.toUpperCase()
}));

console.log(emails);
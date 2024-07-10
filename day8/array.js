//creating an array
const numbers =[2,3,4,5,6,7]

//adding elements 
//by puch()

numbers.push(25,45,67)
console.log(numbers)

//by unshift

numbers.unshift(34,78)
console.log(numbers)

//by splice

numbers.splice(2,0,3,90,80)
console.log(numbers)

//finding element in an array 

let index_of_three = numbers.indexOf(3)
console.log(index_of_three)

let lastindexofthree = numbers.lastIndexOf(3)
console.log(lastindexofthree)
console.log(numbers[lastindexofthree])

//creating an array of object

const employees = [
    {
        id:1,
        name:'ishita',   
    },
    {
        id:2,
        name:'akshat',
    },
    {
        id:3,
        name:'tarak',
    }
]

//finding the element 

const employee = employees.find(function(e)
{
    return e.name === 'ishita'
})
console.log(employee)

//arrow functions 

const sum = (num1,num2) => num1+num2

console.log(sum(2,3))

//removing element 

//using pop()

let num = [23,45,67,89,90]

let last_element =num.pop()
console.log(num)

//using sift 
let first_element = num.shift()
console.log(num)

//using splice

let middle_element = num.splice(1,1)
console.log(num)

//deleting whole array 

// num=0
// console.log (num)

// num=[]
// console.log(num)

// num.splice(0,num.length)
// console.log(num)




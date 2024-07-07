let x=20
let y=10
//arithematic operators are:- +,-,*,/,%,^or**
console.log(x+y)
console.log(x-y)
console.log(x*y)
console.log(x/y)
console.log(x%y)
console.log(x**y)
//increment and decrement operators
console.log(x++)
console.log(++x)
console.log(x--)
console.log(--x)
x*=y
console.log(x)
//assignment operator 
let prog_language='javascript'
console.log(prog_language)
//comparison operator 
console.log(x>y)
console.log(x>=y)
console.log(x<=y)
console.log(x<y)
//equality operator 
let a=2
let b='2'
console.log(a==b)
//strictly equality operator
console.log(a===b)
//ternary operator
let age=20
console.log(age>=18?true:false)
//logical OR operator 
console.log("here is the OR operator")
console.log(true||true)
console.log(false||true)
console.log(true||false)
console.log(false||false)
//logical AND operator
console.log("here is the AND operator")
console.log(true&&true)
console.log(false&&true)
console.log(true&&false)
console.log(false&&false)
//NOT operator
console.log("using the not operator")
console.log(!true)
console.log(!false)
//NULL COALESCING operator(??)
//if there is a null value it provides a default value
let value=null
let result=value ?? true
console.log(result)
//logical operators without boolean values
//falsy values are 'undefined','null','emptystring','0','false'other than that are truthy
let userchosencolour='blue'
let defaultcolour='green'
let preferdcolour=''

console.log(userchosencolour||defaultcolour)
console.log(userchosencolour&&defaultcolour)
console.log(userchosencolour||preferdcolour)
console.log(userchosencolour&&preferdcolour)




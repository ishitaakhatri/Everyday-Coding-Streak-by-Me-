//for loop
let number=[1,2,3,4,5,6,7,8];

for(let i=0;i<number.length;i++)
    {
        console.log(number[i]);
    }
//while loop(used when we don't know the number of iterations)
let idx=0;

while(idx < number.length){
    console.log(number[idx]);
    idx++;
}    
//another example
console.log("another example")
let num=0;
while(true){
    console.log(num)
    if(num===10)
        break;
    num++;
}
//do-while loop
let i=0;

do{
    console.log(i);
    i++;
}while(i<=10)
//for-in loop 
let course={
    name_course:'javascript',
    duration:3,
    completion_time:7,
};

for (let keys in course){
    console.log(course[keys])
}
//for-of loop
let numbers=[1,2,3,4,5,6,7,8,9];
for (let elements of numbers){
    console.log(elements)
}

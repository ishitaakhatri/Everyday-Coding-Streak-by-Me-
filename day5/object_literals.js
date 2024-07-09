let student={
    name:'ishita',
    examination:'btech cse aids',
    examcode:'bc-cs-aids-2001',
    date:'06/06/2024',
    //creating a fucntion inside
    greetings(){
        console.log("hey there..!,"+this.name)
    },
    welcome:function(){
        console.log("welcome to exam")
    }
}
//cloning an object 
let a={value:10};
let b={};

//what if we don't assign(changing the value inside of a too)
//b=a;

b.value=20;

console.log(a);
console.log(b);

//what if we assign

Object.assign(b,a);

b.value=30

console.log(a);
console.log(b);
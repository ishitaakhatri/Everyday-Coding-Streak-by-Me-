//creating and object 
// let dog={
//      name:ellie
//     breed:rottweiler,
//     age:8,
//     weight_in_kg:40,
//     welcome:function(){
//         console.log("welcome to our salon")
//     }
// }
//instead of creating the object we can have functions
// function new_dog(name,breed,age,weight){
//     name:name;
//     breed:breed;
//     age:age;
//     weight:weight;
//     welcome()
//     {
//         console.log("welcome to our salon");
//     }
// }
// const anotherdog=new_dog('ellie','rottwieler',8,40)
// console.log(anotherdog);
//constructor function 
 function dog(name,breed,age,weight){
    this.name=name;
    this.breed=breed;
    this.age=age;
    this.weight=weight;
    
    this.welcome=function()
    {
        console.log("welcome to out salon")
    }
 }

 const anotherdog=new dog('ellie','rottwieler',8,40)
 console.log(anotherdog);
//variables
//we can use var or let but most preferably let
let firstName ='ishita',lastName ='khatri';
console.log(firstName,lastName);
//updating a value
firstName ='akshat';
console.log(firstName,lastName);
//constants
const phoneNumber =9866770044;
//phoneNumber=9887766554;
console.log(phoneNumber);
//datatypes
//string
let fruit ='apple';
let veggie="potato";
//numbers
let age=19;
let pie=3.14;
let verylargenumber=89898988989898n;
//undefined
let fav_movie;
//null
let fav_food=null;
//unique identifier
//const uniquekey=symbol();
//boolean datatype
let love_coding=true;
//objects in js
//non primitive datatype
let courses={
    name:'ishita',
    age:20,
    greet:function(){
        console.log("hey there"+this.name);
    }
}
console.log(fruit,veggie,age,pie,verylargenumber,fav_movie,fav_food,love_coding,courses.greet);
//typesof operator
console.log(typeof pie);
console.log(typeof fav_movie);
console.log(typeof courses);
console.log(typeof love_coding);
//dynamic typing 
let firstname='ishi';
console.log(typeof firstname)
 firstname=78;
 console.log(typeof firstname)
 firstname=null;
 console.log(typeof firstname)
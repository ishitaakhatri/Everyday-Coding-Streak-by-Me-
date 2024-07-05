let students={
    name:'ishita',
    age:'20',
    greet:function(){
        console.log("hello baby"+this.name);
    }
}
console.log(students.name);

students.name='akshat';

console.log(students.name);

//accesing key by using brackets 
console.log(students['age']);
students['name']='bano';
console.log(students['name'])

//primitive datatypes
let a=10;
let b=a;
a=20;
console.log(a);
console.log(b);

//non primitive datatypes
let x={value:20};
let y={x};

x.value=100;

console.log(x);
console.log(y);

//primitives are copied by value
//objects are copied by reference
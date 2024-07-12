//combining array 
const examplearrayA = [1,2,3];

const examplearrayB = [4,5,6];

const combinedarray = examplearrayA.concat(examplearrayB);

console.log(combinedarray);

//slicing the array

const slicedarray = combinedarray.slice(0,4);
console.log(slicedarray);

//spread method

const combined = [...examplearrayA,9,10,...examplearrayB];
console.log(combined);

//or 
 
let a = [1,2,3];
let b = [...a];
console.log(b);

let num1 = 10;
let num2 = 20;

function maximum(num1, num2) {
  if (num1 > num2) {
    console.log("num1 is greater than num2");
  } else if (num1 === num2) {
    console.log("they are equal ");
  } else {
    console.log("num2 is greater than num1");
  }
}

maximum(num1, num2);

//another method
function maxNum(num1, num2) {
  return num1 >= num2 ? num1 : num2;
}

console.log(maxNum(2, 3));

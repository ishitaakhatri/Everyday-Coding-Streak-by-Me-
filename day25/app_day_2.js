
//creating elements 

const unordered_list = document.querySelector('ul');
const list_item = document.createElement('li');
//adding the element 
unordered_list.append(list_item);
// modifying element 
let first_list_item = document.querySelector('.list_items')
console.log(first_list_item.innerText)
console.log(first_list_item.innerHTML)
console.log(first_list_item.textContent)

list_item.innerText('X-MAN')


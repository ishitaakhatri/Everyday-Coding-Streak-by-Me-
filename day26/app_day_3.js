const unordered_list = document.querySelector('ul');
const list_item = document.createElement('li');
//adding the element 
unordered_list.append(list_item);
let first_list_item = document.querySelector('.list_items')
console.log(first_list_item.innerText)
console.log(first_list_item.innerHTML)
console.log(first_list_item.textContent)

list_item.innerText = 'X-MAN';
list_item.classList.add('main_heading');

list_item.removeAttribute('class')

let title = document.querySelector('.main_heading')
console.log(title.getAttribute('class'))

console.log(list_item.classList.contains('main_heading'))


//DOM MANIPULATION 
// TRAVERSING THE DOM 
//TRAVERSING THE PARENT NODE

let ul = document.querySelector('ul')

console.log(ul)
console.log(ul.parentNode.parentNode)
console.log(ul.parentElement.parentElement)

let html = document.documentElement
console.log(html)
console.log(html.parentNode)
console.log(html.parentElement)

// TRVERSING CHILDNODE 

console.log(ul.childNodes)
console.log(ul.firstChild)
console.log(ul.lastChild)

// ul.childNodes[1].style.backgroundColor = 'blue'
console.log(ul.children)
console.log(ul.firstElementChild)
console.log(ul.lastElementChild)

// SIBLING NODE TRAVERSAL 
let div = document.querySelector('div')
console.log(div)

console.log(div.childNodes)
console.log(div.previousSibling)
console.log(div.nextSibling)



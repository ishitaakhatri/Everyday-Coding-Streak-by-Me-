// DOM MANIPULATION 

// EVENT LISTNERS 

// element.addEventListner("click",fucntion)

let buttontwo = document.querySelector('.btn-2')
console.log(buttontwo)

function alertbtn() {
    alert('hey this is me button number 2')
} 

buttontwo.addEventListener('click',alertbtn)

//MOUSEOVER 

let newBackGroundColour = document.querySelector(".boxes_box_3")
console.log(newBackGroundColour)
function newbgcolour(){
    newBackGroundColour.style.backgroundColor = 'blue'
}
newBackGroundColour.addEventListener("mouseover",newbgcolour)
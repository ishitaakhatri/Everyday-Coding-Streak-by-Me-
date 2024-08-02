// document.querySelector("#football").addEventListener("click", function(e) {
//     console.log(e.target.innerText = 'football clicked!')
// },true);
// let newBackGroundColour = document.querySelector("#football")
// console.log(newBackGroundColour)
// function newbgcolour(){
//     newBackGroundColour.style.backgroundColor = 'white'
// }
// newBackGroundColour.addEventListener("click",newbgcolour)

// document.querySelector('#football').addEventListener('click',function(e){
//     console.log('football is clicked')

//     let target = e.target

//     if(target.matches('li')){
//         target.style.backgroundColor = 'lightgrey'
//     }
// })
// document.querySelector('#basketball').addEventListener('click',function(e){
//     console.log('basketball is clicked')

//     let target = e.target

//     if(target.matches('li')){
//         target.style.backgroundColor = 'lightgrey'
//     }
// })
// document.querySelector('#boxing').addEventListener('click',function(e){
//     console.log('boxing is clicked')

//     let target = e.target

//     if(target.matches('li')){
//         target.style.backgroundColor = 'lightgrey'
//     }
// })
// document.querySelector('#tennis').addEventListener('click',function(e){
//     console.log('tennis is clicked')

//     let target = e.target

//     if(target.matches('li')){
//         target.style.backgroundColor = 'lightgrey'
//     }
// })
// document.querySelector('#golf').addEventListener('click',function(e){
//     console.log('golf is clicked')

//     let target = e.target

//     if(target.matches('li')){
//         target.style.backgroundColor = 'lightgrey'
//     }
// })

document.querySelector('#sports').addEventListener('click',function(e){
    console.log(e.target.getAttribute('id') +" "+ 'is clicked')

    let target = e.target
    if(target.matches('li')){
        target.style.backgroundColor = 'pink'
    }
})
let sports = document.querySelector('#sports')

let newsport = document.createElement('li')

newsport.innerText = 'RUGBY'
newsport.setAttribute('id','rugby')

sports.appendChild(newsport)




// DOM MANIPULATION 

// REVEAL EVENTS 

let revealbtn = document.querySelector('.reveal-btn_boxes')
let hiddencontent = document.querySelector('.hidden-content_box')

function revealcontent(){
    if(hiddencontent.classList.contains('reveal-btn_boxes')){
        hiddencontent.classList.remove('reveal-btn_boxes')
    }else{
        hiddencontent.classList.add('reveal-btn_boxes')
    }
}

revealbtn.addEventListener('click',revealcontent)
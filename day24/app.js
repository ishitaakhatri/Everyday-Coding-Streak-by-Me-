// // get element by id
// let heading = document.getElementById("main_heading")
// console.log(heading)
// // get element by class 
// let list_items = document.getElementsByClassName("list_items")
// console.log(list_items)
// // get element by tagname 
// let list_items_by_tags = document.getElementsByTagName("li")
// console.log(list_items_by_tags)
// // query selector 
// let containers_of_div = document.querySelector("div")
// console.log(containers_of_div)
// // query selector all 
// let all_queries = document.querySelectorAll("div")
// console.log(all_queries)

let title = document.querySelector("#main_heading")
title.style.color='pink'
let listitems = document.querySelectorAll(".list_items")
for(i in listitems)
    listitems[i].style.color = 'blue'


console.log(listitems)


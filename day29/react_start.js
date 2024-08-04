// function Main_content(){
//     return(
//         <h1>i am learning react...</h1>
//     )
// }

// ReactDOM.render(
//     <div>
//         <Main_content />
//     </div>,
//     document.getElementById("container")
// );

// create a new h1 element 
// give it some text content
// give it a class name of header 
// append it as a child of the div#root

// let new_element = document.createElement('h1')
// new_element.textContent = "this is an imparitive way to program.."
// new_element.className = 'header'
// document.getElementById('container').append(new_element)

ReactDOM.render(
    <h1 className = 'header'>hey my name is ishita</h1>,
    document.getElementById('container')
)


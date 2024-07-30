// ReactDOM.render(
//     <ul>
//         <li>ishita</li>
//         <li>khatri</li>
//     </ul>,
//     document.getElementById("root")
// );
function Main_component() {
    return <h1>hey! i'm learning react</h1>
}
function Navbar() {
    return <nav>Navbar</nav>;
}
ReactDOM.render(
    <div>
        <Navbar />
        <Main_component />
    </div>,
    document.getElementById("root")
);
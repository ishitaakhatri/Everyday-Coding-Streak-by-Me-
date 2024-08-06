import React from "react";
import ReactDOM from "react-dom/client";


let nav_element = (
    <nav>
        <h1>WEBSITE</h1>
        <ul>
            <li>pricing</li>
            <li>about</li>
            <li>content</li>
        </ul>
    </nav>
)

ReactDOM.render(
    nav_element,
    document.getElementById("container")
)
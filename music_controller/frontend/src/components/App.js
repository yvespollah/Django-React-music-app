import React, { Component } from "react";
import ReactDOM from "react-dom/client";

import HomePage from "./HomePage";


export default class App extends Component {
    render() {
        return (
            <div>
                <HomePage />
            </div>
        );
    }
}

// Find the root element
const appDiv = document.getElementById("app");

// Create the root and render the component
const root = ReactDOM.createRoot(appDiv);
root.render(
    <React.StrictMode>
        <App name="piko" />
    </React.StrictMode>
);
import React from "react";
import Navbar from "../components/Navbar";
export default function Layout(props) {
    return (
        <div className="layout">
            <Navbar />
            {props.children}
        </div>
    );
}

// create react component
import {Link} from "react-router-dom";
import React from "react";
import "./Navbar.css";

const Navbar = () => {
  return <div className="navbar">

        <div to="/">Logo</div>
        <div to="/movies">Movies</div>
        <div to="/about">About</div>
        <div to="/about">Account</div>
        <div to="/about">Genres</div>
        <div to="/about">Search</div>


  </div>;
};

export default Navbar;

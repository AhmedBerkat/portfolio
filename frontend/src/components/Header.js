import React from 'react';
import '../App.css';

const Header = () => {
  return (
    <nav className="navbar">
      <h1>Ahmed Berkat : Portfolio</h1>
      <ul>
        <li><a href="https://github.com/AhmedBerkat" target="_blank" rel="noopener noreferrer">GitHub</a></li>
        <li><a href="mailto:berkatahmed02@gmail.com" target="_blank" rel="noopener noreferrer">📧 Email</a></li>
        <li>📞<b>0644059938</b></li>
        <li><a href="https://www.linkedin.com/in/ahmed-berkat/" target="_blank" rel="noopener noreferrer">💼 LinkedIn</a></li>
      </ul>
    </nav>
  );
};

export default Header;
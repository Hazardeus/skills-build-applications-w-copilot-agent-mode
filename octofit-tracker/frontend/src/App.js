import React from 'react';
import './App.css';
import logo from './octofitapp-small.png';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Bienvenue sur Octofit</h1>
        <p>Suivez votre forme physique et atteignez vos objectifs !</p>
      </header>
    </div>
  );
}

export default App;

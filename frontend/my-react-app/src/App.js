import React, { useState } from 'react';
import logo from './logo.svg';
import VitalsForm from './components/VitalsForm';
import ResultDisplay from './components/ResultDisplay';
import './App.css';

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="App">
      
      
        <h1>Health Vitals Checker</h1>
        <VitalsForm setResult={setResult} />
        <ResultDisplay result={result} />
      
    </div>
  );
}

export default App;

// src/components/ResultDisplay.js
import React from 'react';

const ResultDisplay = ({ result }) => {
  if (!result) return null;

  return (
    <div>
      <h2>Result</h2>
      <p>Prediction: {result.prediction === 1 ? 'Emergency' : 'No Emergency'}</p>
      <p>Status: {result.status}</p>
    </div>
  );
};

export default ResultDisplay;

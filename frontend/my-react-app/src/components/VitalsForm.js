// src/components/VitalsForm.js
import React, { useState } from 'react';
import axios from 'axios';

const VitalsForm = ({ setResult }) => {
  const [heartRate, setHeartRate] = useState('');
  const [spo2, setSpo2] = useState('');
  const [temperature, setTemperature] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Prepare data to be sent to backend
    const data = {
      heart_rate: heartRate,
      spo2: spo2,
      temperature: temperature,
    };

    try {
      const response = await axios.post('http://localhost:5000/vitals', data);
      setResult(response.data); // Pass response to parent component
    } catch (error) {
      console.error("Error:", error);
      alert("There was an error with the request!");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Heart Rate:</label>
        <input
          type="number"
          value={heartRate}
          onChange={(e) => setHeartRate(e.target.value)}
          required
        />
      </div>
      <div>
        <label>SPO2 (%):</label>
        <input
          type="number"
          value={spo2}
          onChange={(e) => setSpo2(e.target.value)}
          required
        />
      </div>
      <div>
        <label>Temperature (°C):</label>
        <input
          type="number"
          value={temperature}
          onChange={(e) => setTemperature(e.target.value)}
          required
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default VitalsForm;

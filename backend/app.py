from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Full path for the model (no scaler)
model_path = "C:\\Users\\ADMIN1\\Desktop\\spmr-project\\backend\\model.pkl"

# Load model (no scaler needed)
try:
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    with open(model_path, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    model = None
    print("Model not loaded:", str(e))

@app.route('/')
def home():
    return "Welcome to the SPMR Backend API!"

@app.route('/vitals', methods=['POST'])
def receive_vitals():
    try:
        data = request.get_json()
        heart_rate = data.get('heart_rate')
        spo2 = data.get('spo2')
        temperature = data.get('temperature')

        if None in (heart_rate, spo2, temperature):
            return jsonify({'status': 'error', 'message': 'Missing input values'}), 400

        # Check if model is loaded
        if model is None:
            return jsonify({'status': 'error', 'message': 'Model not loaded'}), 500

        # Features array (no scaling here)
        features = np.array([[heart_rate, spo2, temperature]])

        # Make prediction using the model
        prediction = model.predict(features)[0]

        return jsonify({
            'status': 'ok',
            'prediction': int(prediction),
            'emergency': bool(prediction)
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/alert', methods=['GET'])
def alert():
    return jsonify({'alert': 'No emergency detected'})

if __name__ == '__main__':
    app.run(debug=True)

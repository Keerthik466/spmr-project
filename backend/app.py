from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for Android app communication

# Dummy ML model load (replace with your real model later)
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except:
    model = None  # Optional: model isn't ready yet

@app.route('/')
def home():
    return "Welcome to the SPMR Backend API!"

@app.route('/vitals', methods=['POST'])
def receive_vitals():
    try:
        data = request.get_json()
        print("Received vitals:", data)

        # Example: Extract features and make dummy prediction
        if model:
            features = [data['heart_rate'], data['spo2'], data['temperature']]
            prediction = model.predict([features])[0]
            return jsonify({'status': 'ok', 'prediction': prediction})
        else:
            return jsonify({'status': 'ok', 'message': 'Model not loaded, received vitals successfully.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/alert', methods=['GET'])
def alert():
    # Dummy response (you can modify later to return real alerts based on state)
    return jsonify({'alert': 'No emergency detected.'})

if __name__ == '__main__':
    app.run(debug=True)

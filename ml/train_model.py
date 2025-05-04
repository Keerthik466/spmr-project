import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# 1. Sample dataset (you can replace with real one later)
data = pd.DataFrame({
    'heart_rate': [72, 120, 90, 65, 140],
    'spo2': [98, 92, 95, 99, 85],
    'temperature': [98.6, 101.2, 97.8, 98.4, 102.5],
    'emergency': [0, 1, 0, 0, 1]  # 1 = emergency
})

# 2. Features and Labels
X = data[['heart_rate', 'spo2', 'temperature']]
y = data['emergency']

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4. Model training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 5. Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")

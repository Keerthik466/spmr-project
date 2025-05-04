import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
import pickle

# Step 1: Load dataset
df = pd.read_csv("vitals.csv")

# Step 2: Check and clean
print("Initial data shape:", df.shape)
df.dropna(inplace=True)
df = df[(df['heart_rate'] >= 30) & (df['heart_rate'] <= 180)]
df = df[(df['spo2'] >= 70) & (df['spo2'] <= 100)]
df = df[(df['temperature'] >= 95) & (df['temperature'] <= 105)]

# Step 3: Features and Labels
X = df[['heart_rate', 'spo2', 'temperature']]
y = df['emergency']

# Step 4: Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Pipeline with scaling + RandomForest
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('rf', RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42))
])

# Step 6: Train
pipeline.fit(X_train, y_train)

# Step 7: Evaluate
y_pred = pipeline.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Step 8: Cross-validation score
cv_scores = cross_val_score(pipeline, X, y, cv=5)
print("Cross-Validation Accuracy Scores:", cv_scores)
print("Average CV Score:", np.mean(cv_scores))

# Step 9: Save model
with open("model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Sophisticated model trained and saved as model.pkl")
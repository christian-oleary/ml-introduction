"""
Introduction to scikit-learn Basics
This script covers fundamental machine learning concepts using scikit-learn.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, accuracy_score, classification_report
from sklearn.datasets import make_classification

# ============================================
# 1. Linear Regression Example
# ============================================
print("=" * 50)
print("1. Linear Regression")
print("=" * 50)

# Create sample data: hours studied vs exam score
np.random.seed(42)
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
exam_scores = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

print("Training Data:")
data_df = pd.DataFrame({'Hours Studied': hours_studied.flatten(), 'Exam Score': exam_scores})
print(data_df)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    hours_studied, exam_scores, test_size=0.3, random_state=42
)

print(f"\nTraining set size: {len(X_train)}")
print(f"Testing set size: {len(X_test)}")

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

print(f"\nModel coefficient (slope): {model.coef_[0]:.2f}")
print(f"Model intercept: {model.intercept_:.2f}")

# Make predictions
y_pred = model.predict(X_test)

print("\nPredictions vs Actual:")
results = pd.DataFrame({
    'Hours': X_test.flatten(),
    'Actual Score': y_test,
    'Predicted Score': y_pred
})
print(results)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"\nRoot Mean Squared Error: {rmse:.2f}")

# Predict for new values
new_hours = np.array([[5.5], [7.5]])
predictions = model.predict(new_hours)
print("\nPredictions for new data:")
for hours, score in zip(new_hours.flatten(), predictions):
    print(f"  {hours} hours → Score: {score:.2f}")

# ============================================
# 2. Classification Example
# ============================================
print("\n" + "=" * 50)
print("2. Classification with Decision Tree")
print("=" * 50)

# Generate a synthetic classification dataset
X, y = make_classification(
    n_samples=100,
    n_features=4,
    n_informative=3,
    n_redundant=1,
    n_classes=2,
    random_state=42
)

print(f"Dataset shape: {X.shape}")
print(f"Number of samples per class: {np.bincount(y)}")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create and train a Decision Tree classifier
classifier = DecisionTreeClassifier(max_depth=3, random_state=42)
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.2f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Class 0', 'Class 1']))

# Show some predictions
print("\nSample Predictions:")
for i in range(5):
    print(f"  Sample {i+1}: Actual={y_test[i]}, Predicted={y_pred[i]}")

# ============================================
# 3. Feature Importance (for tree-based models)
# ============================================
print("\n" + "=" * 50)
print("3. Feature Importance")
print("=" * 50)

feature_importance = classifier.feature_importances_
feature_names = [f'Feature {i+1}' for i in range(X.shape[1])]

importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': feature_importance
}).sort_values('Importance', ascending=False)

print(importance_df)

# ============================================
# 4. Real-world Example: Student Performance
# ============================================
print("\n" + "=" * 50)
print("4. Real-world Example: Student Performance")
print("=" * 50)

# Create a dataset of student features
student_data = {
    'Study_Hours': [2, 5, 1, 8, 6, 3, 7, 4, 9, 2, 6, 8, 5, 3, 7],
    'Attendance': [60, 85, 50, 95, 88, 70, 92, 75, 98, 55, 90, 94, 80, 68, 91],
    'Previous_Score': [55, 75, 45, 90, 82, 60, 88, 70, 95, 50, 85, 92, 78, 62, 89],
    'Passed': [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]
}

df = pd.DataFrame(student_data)
print("Student Performance Data:")
print(df.head(10))

# Prepare features and target
X = df[['Study_Hours', 'Attendance', 'Previous_Score']]
y = df['Passed']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train a classifier
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.2f}")

# Predict for a new student
new_student = pd.DataFrame({
    'Study_Hours': [6],
    'Attendance': [85],
    'Previous_Score': [80]
})
prediction = clf.predict(new_student)
print(f"\nPrediction for new student (6 hours, 85% attendance, 80 previous score):")
print(f"  Will pass: {'Yes' if prediction[0] == 1 else 'No'}")

# Feature importance for this model
print("\nFeature Importance for Student Performance:")
importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': clf.feature_importances_
}).sort_values('Importance', ascending=False)
print(importance_df)

print("\n" + "=" * 50)
print("scikit-learn Basics Complete!")
print("=" * 50)

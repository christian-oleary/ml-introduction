"""
Introduction to pandas Basics
This script covers fundamental pandas concepts for data manipulation.
"""

import pandas as pd
import numpy as np

# ============================================
# 1. Creating DataFrames
# ============================================
print("=" * 50)
print("1. Creating DataFrames")
print("=" * 50)

# From a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'Score': [85, 92, 78, 88, 95],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin']
}
df = pd.DataFrame(data)
print("Student DataFrame:")
print(df)
print(f"\nShape: {df.shape}")  # (rows, columns)

# ============================================
# 2. Viewing Data
# ============================================
print("\n" + "=" * 50)
print("2. Viewing Data")
print("=" * 50)

print("First 3 rows:")
print(df.head(3))

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nBasic statistics:")
print(df.describe())

# ============================================
# 3. Selecting Data
# ============================================
print("\n" + "=" * 50)
print("3. Selecting Data")
print("=" * 50)

# Select a single column
print("Names:")
print(df['Name'])

# Select multiple columns
print("\nNames and Scores:")
print(df[['Name', 'Score']])

# Select rows by index
print("\nFirst row:")
print(df.iloc[0])

# Select rows by condition
print("\nStudents with Score > 85:")
print(df[df['Score'] > 85])

# ============================================
# 4. Adding and Modifying Columns
# ============================================
print("\n" + "=" * 50)
print("4. Adding and Modifying Columns")
print("=" * 50)

# Add a new column
df['Pass'] = df['Score'] >= 80
print("Added 'Pass' column:")
print(df)

# Modify a column
df['Adjusted_Score'] = df['Score'] * 1.05
print("\nAdded 'Adjusted_Score' column:")
print(df[['Name', 'Score', 'Adjusted_Score']])

# ============================================
# 5. Filtering and Sorting
# ============================================
print("\n" + "=" * 50)
print("5. Filtering and Sorting")
print("=" * 50)

# Filter rows
high_scorers = df[df['Score'] >= 88]
print("High scorers (Score >= 88):")
print(high_scorers[['Name', 'Score']])

# Sort by column
sorted_df = df.sort_values('Score', ascending=False)
print("\nSorted by Score (descending):")
print(sorted_df[['Name', 'Score']])

# Multiple conditions
print("\nHigh scorers under 30:")
young_high_scorers = df[(df['Score'] >= 88) & (df['Age'] < 30)]
print(young_high_scorers[['Name', 'Age', 'Score']])

# ============================================
# 6. Aggregation and Grouping
# ============================================
print("\n" + "=" * 50)
print("6. Aggregation and Grouping")
print("=" * 50)

# Basic statistics
print(f"Average Score: {df['Score'].mean():.2f}")
print(f"Max Score: {df['Score'].max()}")
print(f"Min Score: {df['Score'].min()}")
print(f"Standard Deviation: {df['Score'].std():.2f}")

# Count values
print("\nPass/Fail counts:")
print(df['Pass'].value_counts())

# ============================================
# 7. Handling Missing Data
# ============================================
print("\n" + "=" * 50)
print("7. Handling Missing Data")
print("=" * 50)

# Create a DataFrame with missing values
data_with_na = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, 12]
}
df_na = pd.DataFrame(data_with_na)
print("DataFrame with missing values:")
print(df_na)

print("\nCheck for missing values:")
print(df_na.isnull().sum())

# Fill missing values
df_filled = df_na.fillna(0)
print("\nAfter filling with 0:")
print(df_filled)

# Drop rows with missing values
df_dropped = df_na.dropna()
print("\nAfter dropping rows with NaN:")
print(df_dropped)

# ============================================
# 8. Reading and Writing Files
# ============================================
print("\n" + "=" * 50)
print("8. Reading and Writing Files")
print("=" * 50)

# Save to CSV
csv_file = '/tmp/students.csv'
df.to_csv(csv_file, index=False)
print(f"Saved DataFrame to {csv_file}")

# Read from CSV
df_loaded = pd.read_csv(csv_file)
print("\nLoaded DataFrame:")
print(df_loaded.head())

print("\n" + "=" * 50)
print("pandas Basics Complete!")
print("=" * 50)

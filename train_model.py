import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
data = pd.read_csv('data/dataset.csv')  # Adjust path as needed

# Clean 'total_sqft' column
data['total_sqft'] = data['total_sqft'].str.replace(' Sq. Yards', '')  # Remove any extra text
data['total_sqft'] = pd.to_numeric(data['total_sqft'], errors='coerce')  # Convert to numeric

# Clean the data by dropping rows with missing values
data = data.dropna()

# Derive the 'bhk' column from the 'size' column
data['bhk'] = data['size'].str.split().str[0].astype(int)

# Define features (X) and target (y)
X = data[['total_sqft', 'bath', 'bhk']]  # Features
y = data['price']  # Target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model using pickle
with open('models/best_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved successfully as 'best_model.pkl'")

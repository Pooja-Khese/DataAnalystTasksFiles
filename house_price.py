import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Sample dataset
data = {
    'Size (sq ft)': [750, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400],
    'Bedrooms': [1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
    'Price (in $1000s)': [150, 180, 200, 220, 250, 275, 300, 320, 350, 375]
}

df = pd.DataFrame(data)

# Data Preprocessing
X = df[['Size (sq ft)', 'Bedrooms']] 
y = df['Price (in $1000s)']

# Splitting dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Making Predictions
y_pred = model.predict(X_test)

# Evaluate Model Performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")

# Test with a new house (for example, 1050 sq ft, 3 bedrooms)
new_house = np.array([[1050, 3]])  # 1050 sq ft, 3 bedrooms
predicted_price = model.predict(new_house)
print(f"Predicted Price for the new house: ${predicted_price[0] * 1000}")

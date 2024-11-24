import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# Sample dataset: Replace this with actual dataset
data = {
    "mileage": [15000, 30000, 45000, 60000, 75000, 10000, 25000, 55000, 70000, 90000],
    "age": [1, 3, 5, 7, 9, 1, 4, 6, 8, 10],
    "brand": ["Toyota", "Honda", "Ford", "Toyota", "Honda", "Ford", "Toyota", "Honda", "Ford", "Toyota"],
    "engine_type": ["Petrol", "Diesel", "Diesel", "Petrol", "Diesel", "Petrol", "Diesel", "Diesel", "Petrol", "Petrol"],
    "price": [20000, 18000, 15000, 12000, 10000, 22000, 19000, 14000, 11000, 9000],
}

# Create DataFrame
df = pd.DataFrame(data)

# Encode categorical variables
le_brand = LabelEncoder()
le_engine_type = LabelEncoder()
df["brand"] = le_brand.fit_transform(df["brand"])
df["engine_type"] = le_engine_type.fit_transform(df["engine_type"])

# Features and target
X = df[["mileage", "age", "brand", "engine_type"]]
y = df["price"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train CART model
cart_model = DecisionTreeRegressor(random_state=42)
cart_model.fit(X_train, y_train)

# Evaluate the model
y_pred = cart_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Model Mean Squared Error: {mse:.2f}")

# Function to predict price and show decision path
def predict_car_price():
    # Get user input for a new car
    print("\nEnter the details of the car you want to sell:")
    mileage = float(input("Mileage (e.g., 30000): "))
    age = int(input("Age (e.g., 5): "))
    brand = input(f"Brand (choose from {list(le_brand.classes_)}): ")
    engine_type = input(f"Engine Type (choose from {list(le_engine_type.classes_)}): ")

    # Encode the input features
    brand_encoded = le_brand.transform([brand])[0]
    engine_type_encoded = le_engine_type.transform([engine_type])[0]

    # Predict the price
    features = np.array([[mileage, age, brand_encoded, engine_type_encoded]])
    predicted_price = cart_model.predict(features)[0]
    print(f"\nPredicted Price: ${predicted_price:.2f}")
                                                                            
    # Display decision path
    tree_rules = export_text(cart_model, feature_names=X.columns.tolist())
    print("\nDecision Tree Rules:")
    print(tree_rules)

# Call the function to predict and display decision path
predict_car_price()

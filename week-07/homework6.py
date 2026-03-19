# PART ONE
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.datasets import fetch_california_housing

# Load the housing dataset
housing = fetch_california_housing()
housing

X = pd.DataFrame(housing.data, columns=housing.feature_names) 
y = pd.Series(housing.target, name='med_house_value')

# Display first five rows
print("First five rows of the dataset:")
print(X.head())

# Print names
print("\nFeature names:", X.columns.tolist())

# Checking for missing values
print("\nMissing values in each feature:")
print(X.isnull().sum())

# Generating summary statistics
print("\nSummary statistics:")
print(X.describe())

#PART TWO: Linear Regression
# Split the raw data (80% training, 20% testing)
X_train_raw, X_test_raw, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model on unscaled data
lin_reg_raw = LinearRegression()
lin_reg_raw.fit(X_train_raw, y_train)

# Make predictions on the test set
y_pred_raw = lin_reg_raw.predict(X_test_raw)

from sklearn.metrics import mean_squared_error, root_mean_squared_error, r2_score

# Evaluate model performance
mse_raw = mean_squared_error(y_test, y_pred_raw)
rmse_raw = root_mean_squared_error(y_test, y_pred_raw)

r2_raw = r2_score(y_test, y_pred_raw)

print("Unscaled Data Model:")
print(f"Mean Squared Error: {mse_raw:.2f}")
print(f"Root Squared Error: {rmse_raw:.2f}")
print(f"R² Score: {r2_raw:.2f}")

# View our model's coefficients
print("Model Coefficients (Unscaled):")
print(pd.Series(lin_reg_raw.coef_,
                index=X.columns))
print("\nModel Intercept (Unscaled):")
print(pd.Series(lin_reg_raw.intercept_))

# The mean squared error measures the average squared difference between the
# actual and predicted values. In this case, the MSE is .56, so the average squared difference
# #between the actual and predicted is .56.

# The Root Squared Error is the square root of the MSE meaning that it shows the 
# difference between actual predicted values in the same units as the target.
# Therefore, the RSE, square root of the difference between actual and predicted values 
# is .75.

# Finally, the R^2 value shows the proportion of variance that is explained by the model
# In this instance, the R^2 is 0.58, so the variance explained by the model is 0.58. 
# This R^2 is rather average, meaning it accounts for a little over 50% of the variance.


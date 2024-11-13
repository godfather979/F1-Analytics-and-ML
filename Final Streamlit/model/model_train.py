import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import warnings
warnings.filterwarnings('ignore')
import joblib



# data = pd.read_csv('Combined_final-laps.csv')
data = pd.read_csv('updated_file.csv')

def convert_lap_time(lap_time_str):
    minutes, seconds, milliseconds = lap_time_str.split(':')
    return int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000

# Apply the conversion to the FormattedLapTime column
data['LapTimeSeconds'] = data['FormattedLapTime'].apply(convert_lap_time)

# Drop the original FormattedLapTime column as it's no longer needed
data.drop(columns=['FormattedLapTime'], inplace=True)
data.drop(columns=['WindDirection'], inplace=True)
data.drop(columns=['Rainfall'], inplace=True)
data.drop(columns=['DriverNumber'], inplace=True)
data.drop(columns=['Team'], inplace=True)

data = data[~data['Compound'].isin(['WET', 'INTERMEDIATE'])]

data_encoded = pd.get_dummies(data, columns=[ 'Compound'], drop_first=True)

data_encoded['TyreDegradation'] = data_encoded['TyreLife'] * \
    (data_encoded['Compound_SOFT'] if 'Compound_SOFT' in data_encoded else 0) + \
    (data_encoded['TyreLife'] * 0.8 * (data_encoded['Compound_MEDIUM'] if 'Compound_MEDIUM' in data_encoded else 0)) + \
    (data_encoded['TyreLife'] * 0.5 * (data_encoded['Compound_HARD'] if 'Compound_HARD' in data_encoded else 0))

fuel_load_values = {
    'Baku': 51,
    'Austin': 55,
    'Brazil': 71,
    'Spain': 66
}

data_encoded['Fuel_Load']= 1-(data_encoded['LapNumber']/data_encoded['track'].map(fuel_load_values))

data_encoded.loc[:, data_encoded.dtypes == 'bool'] = data_encoded.loc[:, data_encoded.dtypes == 'bool'].astype(int)
data_encoded = pd.get_dummies(data_encoded, columns=['Driver', 'track'], drop_first=False)

print("Preprocessing finished")
data_encoded.to_csv('test.csv', index=False)  # `index=False` excludes the index column
print("data_encoded saved as 'data_encoded.csv'")

########### preprocessing finished ###############

# Assuming df is your DataFrame
X = data_encoded.drop(columns=['LapTimeSeconds'])  # Features
y = data_encoded['LapTimeSeconds']  # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the RandomForestRegressor
rf_model = RandomForestRegressor(n_estimators=500, random_state=42)

# Fit the model
rf_model.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"R^2 Score: {r2}")

n_trees = len(rf_model.estimators_)  # Number of trees in the forest
train_predictions = np.zeros((X_train.shape[0], n_trees))
test_predictions = np.zeros((X_test.shape[0], n_trees))

# Store predictions for each tree in the forest
for i, tree in enumerate(rf_model.estimators_):
    train_predictions[:, i] = tree.predict(X_train)
    test_predictions[:, i] = tree.predict(X_test)

# Calculate the average prediction across all trees for both train and test data
avg_train_predictions = np.mean(train_predictions, axis=1)
avg_test_predictions = np.mean(test_predictions, axis=1)

# Calculate Bias: difference between the mean of predictions and the true value
train_bias = np.mean(avg_train_predictions - y_train)
test_bias = np.mean(avg_test_predictions - y_test)

# Calculate Variance: variance of the predictions for the test set
train_variance = np.mean(np.var(train_predictions, axis=1))
test_variance = np.mean(np.var(test_predictions, axis=1))

# Print the results
print(f"Train Bias: {train_bias}")
print(f"Test Bias: {test_bias}")
print(f"Train Variance: {train_variance}")
print(f"Test Variance: {test_variance}")

# Assuming `model` is your trained model
joblib.dump(rf_model, 'my_model.pkl')
print('model saved')
print(rf_model.feature_names_in_)



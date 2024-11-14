import joblib
import pandas as pd


## import model
model = joblib.load('model/my_model.pkl')



feature_names=['LapNumber','Stint', 'TyreLife', 'AirTemp', 'Humidity', 'Pressure',
 'TrackTemp', 'WindSpeed' ,'Compound_MEDIUM', 'Compound_SOFT',
 'TyreDegradation', 'Fuel_Load', 'Driver_ALB', 'Driver_ALO', 'Driver_BEA',
 'Driver_BOT','Driver_COL', 'Driver_DEV', 'Driver_GAS', 'Driver_GIO',
 'Driver_GRO', 'Driver_HAM', 'Driver_HUL' ,'Driver_KUB', 'Driver_KVY',
 'Driver_LAT', 'Driver_LAW', 'Driver_LEC' ,'Driver_MAG', 'Driver_MAZ',
 'Driver_MSC', 'Driver_NOR', 'Driver_OCO' ,'Driver_PER', 'Driver_PIA',
 'Driver_RAI', 'Driver_RIC', 'Driver_RUS', 'Driver_SAI', 'Driver_SAR',
 'Driver_STR', 'Driver_TSU' ,'Driver_VER', 'Driver_VET', 'Driver_ZHO',
 'track_Austin', 'track_Baku', 'track_Brazil' ,'track_Spain']

# def predict_lap_time(driver_number, lap_number, stint, tyre_life, air_temp, humidity, pressure, track_temp,
#                      wind_speed, compound, team, driver, track):

def predict_lap_time(lap_number, stint, tyre_life, air_temp, humidity, pressure, track_temp,
                     wind_speed, compound,driver, track):
    # Initialize a dictionary with all features, setting default values for one-hot encoded columns
    feature_dict = {col: 0 for col in feature_names if col != 'LapTimeSeconds'}

    # Fill in provided values for numeric features
    # feature_dict['DriverNumber'] = driver_number
    feature_dict['LapNumber'] = lap_number
    feature_dict['Stint'] = stint
    feature_dict['TyreLife'] = tyre_life
    feature_dict['AirTemp'] = air_temp
    feature_dict['Humidity'] = humidity
    feature_dict['Pressure'] = pressure
    feature_dict['TrackTemp'] = track_temp
    feature_dict['WindSpeed'] = wind_speed

    # One-hot encode Compound, Team, Driver, and Track based on training data
    compound_column = f'Compound_{compound.upper()}'
    if compound_column in feature_dict:
        feature_dict[compound_column] = 1
        # print(compound_column + str(feature_dict[compound_column]))

    # team_column = f'Team_{team}'
    # if team_column in feature_dict:
    #     feature_dict[team_column] = 1

    driver_column = f'Driver_{driver.upper()}'
    if driver_column in feature_dict:
        feature_dict[driver_column] = 1

    track_column = f'track_{track}'
    if track_column in feature_dict:
        feature_dict[track_column] = 1

    # Additional engineered features
    feature_dict['TyreDegradation'] = feature_dict['TyreLife'] * (
        feature_dict.get('Compound_SOFT', 0) +
        0.8 * feature_dict.get('Compound_MEDIUM', 0) +
        0.5 * feature_dict.get('Compound_HARD', 0)
    )

    fuel_load_values = {
    'baku': 51,
    'austin': 55,
    'brazil': 71,
    'spain': 66
}
    
    total_laps = fuel_load_values.get(track.lower(),None)
    feature_dict['Fuel_Load'] = 1 - lap_number / total_laps  # Example fuel load calculation
    # print(feature_dict['Fuel_Load'])
   

    # Convert feature dictionary to a DataFrame
    input_df = pd.DataFrame([feature_dict])

    # Ensure columns align with model expectations
    input_df = input_df.reindex(columns=feature_names, fill_value=0)
    # print(input_df)

    # Predict lap time using the model
    predicted_lap_time = model.predict(input_df)[0]
    

    return predicted_lap_time

# Example usage
predicted_time = predict_lap_time(
    # driver_number=10,
    lap_number=1,
    stint=1,
    tyre_life=1,
    air_temp=20,
    humidity=59,
    pressure=1007,
    track_temp=42,
    wind_speed=1.6,
    compound="SOFT",
    # team="Alpine",
    driver="VER",
    track="Spain"
)

# print(f"Predicted Lap Time: {predicted_time:.2f} seconds")

import streamlit as st

def predict_lap_time(driver_number, lap_number, stint, tyre_life, air_temp, humidity, 
                     pressure, rainfall, track_temp, wind_direction, wind_speed, 
                     compound, team):
    return f"Predicted lap time based on inputs is: {(driver_number + lap_number + stint + tyre_life) * 0.1} seconds"

st.title("Lap Time Predictor")

# Collect input as text and handle empty input
driver_number = st.text_input("Driver Number")
lap_number = st.text_input("Lap Number")
stint = st.text_input("Stint")
tyre_life = st.text_input("Tyre Life")
air_temp = st.text_input("Air Temperature (°C)")
humidity = st.text_input("Humidity (%)")
pressure = st.text_input("Pressure (hPa)")
rainfall = st.checkbox("Rainfall")
track_temp = st.text_input("Track Temperature (°C)")
wind_direction = st.text_input("Wind Direction (°)")
wind_speed = st.text_input("Wind Speed (m/s)")
compound = st.selectbox("Tyre Compound", options=["soft", "medium", "hard"])
team = st.selectbox("Team", options=["Red Bull Racing", "Mercedes", "Ferrari", "McLaren"])

# Convert inputs only if they are not empty
if st.button("Predict Lap Time"):
    try:
        driver_number = int(driver_number) if driver_number else 0
        lap_number = int(lap_number) if lap_number else 0
        stint = int(stint) if stint else 0
        tyre_life = int(tyre_life) if tyre_life else 0
        air_temp = float(air_temp) if air_temp else 0.0
        humidity = float(humidity) if humidity else 0.0
        pressure = float(pressure) if pressure else 0.0
        track_temp = float(track_temp) if track_temp else 0.0
        wind_direction = int(wind_direction) if wind_direction else 0
        wind_speed = float(wind_speed) if wind_speed else 0.0

        predicted_time = predict_lap_time(
            driver_number, lap_number, stint, tyre_life, air_temp, humidity, 
            pressure, rainfall, track_temp, wind_direction, wind_speed, 
            compound, team
        )
        
        # Display inputs and result
        st.write("Your Inputs:")
        st.write("Driver Number:", driver_number)
        st.write("Lap Number:", lap_number)
        st.write("Stint:", stint)
        st.write("Tyre Life:", tyre_life)
        st.write("Air Temperature (°C):", air_temp)
        st.write("Humidity (%):", humidity)
        st.write("Pressure (hPa):", pressure)
        st.write("Rainfall:", rainfall)
        st.write("Track Temperature (°C):", track_temp)
        st.write("Wind Direction (°):", wind_direction)
        st.write("Wind Speed (m/s):", wind_speed)
        st.write("Tyre Compound:", compound)
        st.write("Team:", team)
        st.write(predicted_time)
    except ValueError:
        st.error("Please enter valid numerical values.")

import streamlit as st

def predict_lap_time(driver_number, lap_number, stint, tyre_life, air_temp, humidity, 
                     pressure, rainfall, track_temp, wind_direction, wind_speed, 
                     compound, team):
    return f"Predicted lap time based on inputs is: {(driver_number + lap_number + stint + tyre_life) * 0.1} seconds"

st.title("Lap Time Predictor")

driver_number = st.number_input("Driver Number")
lap_number = st.number_input("Lap Number")
stint = st.number_input("Stint")
tyre_life = st.number_input("Tyre Life")
air_temp = st.number_input("Air Temperature (°C)")
humidity = st.number_input("Humidity (%)")
pressure = st.number_input("Pressure (hPa)")
rainfall = st.checkbox("Rainfall")
track_temp = st.number_input("Track Temperature (°C)")
wind_direction = st.number_input("Wind Direction (°)")
wind_speed = st.number_input("Wind Speed (m/s)")
compound = st.selectbox("Tyre Compound", options=["soft", "medium", "hard"])
team = st.selectbox("Team", options=["Red Bull Racing", "Mercedes", "Ferrari", "McLaren"])

if st.button("Predict Lap Time"):
    predicted_time = predict_lap_time(
        driver_number, lap_number, stint, tyre_life, air_temp, humidity, 
        pressure, rainfall, track_temp, wind_direction, wind_speed, 
        compound, team
    )
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

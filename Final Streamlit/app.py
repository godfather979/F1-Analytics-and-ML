import streamlit as st
from complete_race import display_complete_race
from complete_race import race_lap_time
from individual_lap import predict_lap_time
import pandas as pd
from model.model_train import mae,mse,r2,train_bias,train_variance,test_bias,test_variance


def convert_to_mm_ss_sss(predicted_lap_time):
    minutes = int(predicted_lap_time // 60)  # Get the integer part of minutes
    seconds = predicted_lap_time % 60        # Get the remainder seconds
    formatted_time = f"{minutes:02}:{seconds:05.3f}"  # Format as mm:ss.sss
    return formatted_time

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Page 1: Full Input", "Page 2: Minimal Input", "Page 3: Model Evaluation"])

# Common dropdowns for Track, Driver, and Compound
# track = st.selectbox("Select Track", options=["Baku", "Austin", "Spain", "Brazil"])
# driver = st.selectbox("Select Driver", options=[
#     'GAS', 'PER', 'LEC', 'STR', 'MAG', 'ALB', 'KVY', 'HUL', 'RIC', 'VER', 
#     'NOR', 'HAM', 'VET', 'SAI', 'RUS', 'RAI', 'BOT', 'GRO', 'KUB', 'GIO', 
#     'ALO', 'TSU', 'OCO', 'MSC', 'LAT', 'MAZ', 'ZHO', 'PIA', 'DEV', 'SAR', 
#     'LAW', 'COL', 'BEA'
# ])


if page == "Page 1: Full Input": 
    st.title("Lap Time Predictor - Full Input")

    

    # Inputs for all parameters
    track = st.selectbox("Select Track", options=["Baku", "Austin", "Spain", "Brazil"])
    driver = st.selectbox("Select Driver", options=[
    'GAS', 'PER', 'LEC', 'STR', 'MAG', 'ALB', 'KVY', 'HUL', 'RIC', 'VER', 
    'NOR', 'HAM', 'VET', 'SAI', 'RUS', 'RAI', 'BOT', 'GRO', 'KUB', 'GIO', 
    'ALO', 'TSU', 'OCO', 'MSC', 'LAT', 'MAZ', 'ZHO', 'PIA', 'DEV', 'SAR', 
    'LAW', 'COL', 'BEA'
    ])
    compound = st.selectbox("Tyre Compound", options=["MEDIUM", "SOFT", "HARD"])
    lap_number = st.number_input("Lap Number")
    stint = st.number_input("Stint")
    tyre_life = st.number_input("Tyre Life")
    air_temp = st.number_input("Air Temperature (°C)")
    humidity = st.number_input("Humidity (%)")
    pressure = st.number_input("Pressure (hPa)")
    track_temp = st.number_input("Track Temperature (°C)")
    wind_speed = st.number_input("Wind Speed (m/s)")

    if st.button("Predict Lap Time"):
        predicted_time = predict_lap_time(              
            driver=driver,
            lap_number=lap_number,
            stint=stint,
            tyre_life=tyre_life,
            air_temp=air_temp,
            humidity=humidity,
            pressure=pressure,
            track_temp=track_temp,
            wind_speed=wind_speed,
            compound=compound,
            track=track
        )

        formatted_predicted_time = convert_to_mm_ss_sss(predicted_time)
        
        st.markdown(f"<div style='font-size: 36px; font-weight: bold;'>Predicted Lap Time: {formatted_predicted_time}</div>", unsafe_allow_html=True)

elif page == "Page 2: Minimal Input":
    st.title("Lap Time Predictor - Minimal Input")

    # Minimal inputs required
    track = st.selectbox("Select Track", options=["Baku", "Austin", "Spain", "Brazil"])
    driver = st.selectbox("Select Driver", options=[
    'GAS', 'PER', 'LEC', 'STR', 'MAG', 'ALB', 'KVY', 'HUL', 'RIC', 'VER', 
    'NOR', 'HAM', 'VET', 'SAI', 'RUS', 'RAI', 'BOT', 'GRO', 'KUB', 'GIO', 
    'ALO', 'TSU', 'OCO', 'MSC', 'LAT', 'MAZ', 'ZHO', 'PIA', 'DEV', 'SAR', 
    'LAW', 'COL', 'BEA'
    ])
    compound1 = st.selectbox("Tyre Compound 1", options=["MEDIUM", "SOFT", "HARD"])
    stint1 = st.number_input("Enter pit stop lap")
    compound2 = st.selectbox("Tyre Compound 2", options=["MEDIUM", "SOFT", "HARD"])
    stint2=0
    air_temp = st.number_input("Air Temperature (°C)")
    humidity = st.number_input("Humidity (%)")
    pressure = st.number_input("Pressure (hPa)")
    track_temp = st.number_input("Track Temperature (°C)")
    wind_speed = st.number_input("Wind Speed (m/s)")

    if st.button("Predict Lap Time - Minimal"):
        # predicted_time = predict_lap_time(
        #     driver=driver,
        #     lap_number=1,  # Default value for minimal input
        #     stint=1,       # Default value for minimal input
        #     tyre_life=1,   # Default value for minimal input
        #     air_temp=air_temp,
        #     humidity=humidity,
        #     pressure=pressure,
        #     track_temp=track_temp,
        #     wind_speed=wind_speed,
        #     compound=compound,
        #     track=track
        # )
        
        # st.write("Your Inputs:")
        # st.write("Track:", track)
        # st.write("Driver:", driver)
        # st.write("Tyre Compound:", compound)
        # st.write("Air Temperature (°C):", air_temp)
        # st.write("Humidity (%):", humidity)
        # st.write("Pressure (hPa):", pressure)
        # st.write("Track Temperature (°C):", track_temp)
        # st.write("Wind Speed (m/s):", wind_speed)
        
        # st.write(predicted_time)

        lap_times = race_lap_time(air_temp=air_temp,
        humidity=humidity,
        pressure=pressure,
        track_temp=track_temp,
        wind_speed=wind_speed,
        compound1=compound1,
        stint1=stint1,
        compound2=compound2,
        stint2=stint2,
        driver=driver,
        track=track)

        lap_times_df = pd.DataFrame(lap_times)
        st.write("Lap Times for Each Lap:")
        st.dataframe(lap_times_df,height=250,width=500,hide_index=False)

        

        fig = display_complete_race(air_temp=air_temp,
        humidity=humidity,
        pressure=pressure,
        track_temp=track_temp,
        wind_speed=wind_speed,
        compound1=compound1,
        stint1=stint1,
        compound2=compound2,
        stint2=stint2,
        driver=driver,
        track=track)
        st.pyplot(fig)


elif page == "Page 3: Model Evaluation":


    # Use HTML to center the title and style the text
    st.markdown(
        """
        <h1 style='text-align: center; font-size: 40px; font-weight: bold;'>Model Evaluation</h1>
        """, 
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h3 style='text-align: center; font-size: 30px;'>Model Performance Metrics</h3>
        """, 
        unsafe_allow_html=True
    )

    # Display Mean Squared Error with custom styling
    st.markdown(
        f"<p style='font-size: 24px; font-weight: bold;'>Mean Squared Error (MSE): {mse:.4f}</p>",
        unsafe_allow_html=True
    )

    # Display Mean Absolute Error with custom styling
    st.markdown(
        f"<p style='font-size: 24px; font-weight: bold;'>Mean Absolute Error (MAE): {mae:.4f}</p>",
        unsafe_allow_html=True
    )

    # Display R² Score with custom styling
    st.markdown(
        f"<p style='font-size: 24px; font-weight: bold;'>R² Score: {r2:.4f}</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h3 style='text-align: center; font-size: 30px;'>Bias and Variance</h3>
        """, 
        unsafe_allow_html=True
    )

    # Display Bias with explanation
    st.markdown(
        f"<p style='font-size: 24px; font-weight: bold;'>Train Bias: {train_bias:.4f}</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<p style='font-size: 16px;'>Low bias indicates that the model makes predictions that are close to the true values. It means the model is able to capture the underlying patterns well.</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='font-size: 24px; font-weight: bold;'>Test Bias: {test_bias:.4f}</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<p style='font-size: 16px;'>Low test bias suggests that the model generalizes well to new, unseen data, providing accurate predictions beyond the training set.</p>",
        unsafe_allow_html=True
    )

    # Display Variance with explanation
    st.markdown(
        f"<p style='font-size: 24px; font-weight: bold;'>Train Variance: {train_variance:.4f}</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<p style='font-size: 16px;'>Low variance indicates that the model's predictions are stable across different subsets of the training data. It suggests the model is not overly sensitive to data fluctuations.</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='font-size: 24px; font-weight: bold;'>Test Variance: {test_variance:.4f}</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<p style='font-size: 16px;'>Low test variance indicates that the model provides consistent predictions on different test sets, suggesting it is robust and not overly affected by small changes in data.</p>",
        unsafe_allow_html=True
    )

    

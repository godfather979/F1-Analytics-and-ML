from individual_lap import predict_lap_time
from average_lap_graph import display_graph
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def race_lap_time(air_temp, humidity, pressure, track_temp,
                     wind_speed, compound1,stint1,compound2,stint2,driver, track):
    
    fuel_load_values = {
    'baku': 51,
    'austin': 55,
    'brazil': 71,
    'spain': 66
}
    
    total_laps = fuel_load_values.get(track.lower(), None)
    if total_laps is None:
        raise ValueError(f"Track '{track}' not found in fuel load values.")

    # Initialize lists to store lap times for both compounds
    lap_times = []

    # Iterate over each lap number
    for lap_number in range(1, total_laps + 1):
        # Set the parameters for each lap based on stint and compound
        if lap_number <= stint1:
            compound = compound1
            stint = 1
            tyre_life = lap_number  # Example, you can adjust this based on lap_number
        else:
            compound = compound2
            stint = 2
            tyre_life = lap_number-stint1

        # Get lap time prediction using the `predict_lap_time` function
        lap_time = predict_lap_time(lap_number=lap_number, stint=stint, tyre_life=tyre_life, air_temp=air_temp,
                                    humidity=humidity, pressure=pressure, track_temp=track_temp,
                                    wind_speed=wind_speed, compound=compound, driver=driver, track=track)

        # Store the lap time for the current lap
        lap_times.append(lap_time)

    # for lap_num, lap_time in enumerate(lap_times, start=1):
    #     print(f"Lap {lap_num} predicted time: {lap_time:.2f} seconds")

    

    # Return the list of predicted lap times
    return lap_times

# Example usage
lap_times = race_lap_time(
    air_temp=20.1,
    humidity=51.1,
    pressure=1013.9,
    track_temp=41.3,
    wind_speed=5.1,
    compound1="hard",
    stint1=20,
    compound2="medium",
    stint2=30,
    driver="VER",
    track="Austin"
)

# Print predicted lap times for the race
# for lap_num, lap_time in enumerate(lap_times, start=1):
#     print(f"Lap {lap_num} predicted time: {lap_time:.2f} seconds")



def display_complete_race(air_temp, humidity, pressure, track_temp,
                     wind_speed, compound1,stint1,compound2,stint2,driver, track):
    
    lap_times = race_lap_time(
    air_temp=air_temp,
    humidity=humidity,
    pressure=pressure,
    track_temp=track_temp,
    wind_speed=wind_speed,
    compound1=compound1,
    stint1=stint1,
    compound2=compound2,
    stint2=stint2,
    driver=driver,
    track=track
    )

    lap_times_df = pd.DataFrame({
    'LapNumber': range(1, len(lap_times) + 1),  # Generate lap numbers starting from 1
    'PredictedLapTime': lap_times               # Use the lap_times list
})
    
    # print(lap_times_df)

    fig,ax = plt.subplots(figsize=(10, 6))
    display_graph(driver,track)
    ax.plot(lap_times_df['LapNumber'], lap_times_df['PredictedLapTime'], label="Predicted Lap Time", color="red")

    # Add labels and legend
    ax.set_xlabel("Lap Number")
    ax.set_ylabel("Lap Time (seconds)")
    ax.set_title("Actual vs Predicted Lap Times")
    ax.legend()
    # plt.show()
    return fig

    


# display_complete_race(
#     air_temp=26,
#     humidity=50,
#     pressure=981.5,
#     track_temp=34.7,
#     wind_speed=5.8,
#     compound1="soft",
#     stint1=30,
#     compound2="medium",
#     stint2=30,
#     driver="ham",
#     track="Austin"
# )

    
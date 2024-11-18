import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import fastf1.plotting



fastf1.plotting.setup_mpl(mpl_timedelta_support=True, misc_mpl_mods=False,
                          color_scheme='fastf1')

# Load dataset
data = pd.read_csv('updated_file.csv')
def convert_to_seconds(time_str):
    try:
        # Ensure the format is correct
        if len(time_str.split(':')) == 3:
            minutes, seconds, milliseconds = time_str.split(':')  # Split by ':'
            total_seconds = int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000  # Convert to seconds
            return total_seconds
        else:
            raise ValueError(f"Invalid time format: {time_str}")
    except Exception as e:
        print(f"Error processing {time_str}: {e}")
        return None  # Return None or any placeholder for incorrect formats

# Apply the conversion function to the FormattedLapTime column
data['LapTimeSeconds'] = data['FormattedLapTime'].apply(convert_to_seconds)


def display_graph(driver,track):
    track_data = data[data['track'] == track]
    driver_data = track_data[track_data['Driver'] == driver.upper()]
    average_laps = driver_data.groupby(['track','LapNumber'])['LapTimeSeconds'].mean().reset_index()

    # print(average_laps)

    # plt.figure(figsize=(8, 5))
    sns.scatterplot(x='LapNumber', y='LapTimeSeconds', data=average_laps)
    
    # Add title and labels
    plt.title(f'Lap Times for {driver}')
    plt.xlabel('Lap Number')
    plt.ylabel('Lap Time (seconds)')
    
    # # Show the plot
    # plt.show()

# display_graph('HAM','Austin')

def avg_total_duration(driver,track):
    track_data = data[data['track'] == track]
    driver_data = track_data[track_data['Driver'] == driver.upper()]
    average_laps = driver_data.groupby(['track','LapNumber'])['LapTimeSeconds'].mean().reset_index()

    total_lap_time = average_laps['LapTimeSeconds'].sum()
    return total_lap_time
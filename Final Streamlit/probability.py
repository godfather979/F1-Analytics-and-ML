
from complete_race import race_lap_time
import math

def softmax(total_times):
    exp_values = [math.exp(-time) for time in total_times]  # Inverse of time because lower time = higher probability
    print(exp_values)
    sum_exp_values = sum(exp_values)
    probabilities = [exp_value / sum_exp_values for exp_value in exp_values]
    return probabilities

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

# for lap_num, lap_time in enumerate(lap_times, start=1):
#         print(f"Lap {lap_num} predicted time: {lap_time:.2f} seconds")


def driver_lap(drivers,track):
        
    lap_times_dict = {}

    for driver in drivers:
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
        driver=driver,
        track=track
        
        )

        lap_times_dict[driver] = lap_times

    return lap_times_dict



# drivers_list = ['VER', 'HAM', 'BOT','LEC','LAT']
# track = 'Spain'
# driver_total_times = {}

# driver_lap_times = driver_lap(drivers_list,track)

# for driver, lap_times in driver_lap_times.items():
#     print(f"Lap times for driver {driver}:")
#     total_time = sum(lap_times)  # Calculate the sum of lap times for the driver
#     driver_total_times[driver] = total_time
#     for lap_num, lap_time in enumerate(lap_times, start=1):
#         print(f"  Lap {lap_num}: {lap_time:.2f} seconds")
#     print(f"Total time for driver {driver}: {total_time:.2f} seconds\n")

# total_times = list(driver_total_times.values())
# drivers = list(driver_total_times.keys())


# converted_total_times = [float(time) for time in total_times]
# print(converted_total_times)
# total_times_in_hours = [time / 60 for time in converted_total_times]
# print(total_times_in_hours)


# probabilities = softmax(total_times_in_hours)


# # Display the probabilities for each driver
# print("Driver Probabilities (Winner Prediction):")
# for driver, probability in zip(drivers, probabilities):
#     print(f"{driver}: {probability*100:.2f}%")

# # Find the predicted winner
# winner_index = probabilities.index(max(probabilities))
# predicted_winner = drivers[winner_index]
# print(f"\nPredicted winner: {predicted_winner}")



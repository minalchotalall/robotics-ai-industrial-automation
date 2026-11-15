
import numpy as np

print("================================")
print(" DATA SCIENCE - NUMPY EXERCISE")
print("================================")

# 1. Create a NumPy array with sensor readings
temperatures = np.array([22, 25, 28, 30, 32, 35, 38, 40, 42, 45])

print("\n--- SENSOR TEMPERATURE READINGS ---")
print(temperatures)

# 2. Calculate the average temperature
average_temperature = np.mean(temperatures)

print("\nAverage temperature:", average_temperature, "C")

# 3. Find the highest and lowest temperatures
highest_temperature = np.max(temperatures)
lowest_temperature = np.min(temperatures)
median_temperature = np.median(temperatures)

print("Highest temperature:", highest_temperature, "C")
print("Lowest temperature:", lowest_temperature, "C")
print ("Median temperature:", median_temperature, "C")

# 4. Calculate the total number of readings
total_readings = len(temperatures)

print("Total readings:", total_readings)

# 5. Increase all temperatures by 2 degrees
adjusted_temperatures = temperatures + 2

print("\n--- ADJUSTED TEMPERATURES ---")
print(adjusted_temperatures)


critical_temperatures = temperatures[temperatures >= 40]

print("\nCritical temperature readings:")
print(critical_temperatures)

print("Number of critical readings:", len(critical_temperatures))

# 6. Identify temperatures above 30 degrees
high_temperatures = temperatures[temperatures > 30]

print("\nTemperatures above 30 C:")
print(high_temperatures)

print("\nExercise 01 completed!")

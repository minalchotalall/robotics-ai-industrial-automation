
import pandas as pd

print("================================")
print(" DATA SCIENCE - PANDAS EXERCISE")
print("================================")

# 1. Create robot sensor data
data = {
    "Temperature": [22, 25, 28, 32, 38, 40, 42, 45],
    "Pressure": [1.2, 1.4, 1.5, 1.8, 2.0, 2.1, 2.2, 2.4],
    "Speed": [100, 110, 120, 130, 140, 145, 150, 155]
}

# 2. Create a DataFrame
df = pd.DataFrame(data)

print("\n--- ROBOT SENSOR DATA ---")
print(df)

# 3. Display basic information
print("\n--- DATA INFORMATION ---")
print(df.info())

# 4. Calculate statistics
print("\n--- STATISTICS ---")
print(df.describe())

# 5. Calculate average temperature
average_temperature = df["Temperature"].mean()

print("\nAverage temperature:", average_temperature, "C")

# 6. Find temperatures above 30 C
high_temperatures = df[df["Temperature"] > 30]

print("\n--- HIGH TEMPERATURE READINGS ---")
print(high_temperatures)

# 7. Count total readings
total_readings = len(df)

# 8. Identify critical temperatures
critical_temperatures = df[df["Temperature"] >= 40]

print("\n--- CRITICAL TEMPERATURE READINGS ---")
print(critical_temperatures)

print("Number of critical readings:", len(critical_temperatures))

# 9. Calculate average robot speed
average_speed = df["Speed"].mean()

print("\nAverage robot speed:", average_speed)


print("\nTotal readings:", total_readings)

print("\nExercise 02 completed!")

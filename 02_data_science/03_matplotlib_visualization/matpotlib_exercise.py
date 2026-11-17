
import numpy as np
import matplotlib.pyplot as plt

print("======================================")
print(" ROBOT SENSOR DATA VISUALIZATION")
print("======================================")

# 1. Robot temperature sensor readings
temperatures = np.array([22, 25, 28, 32, 38, 40, 42, 45])

# 2. Reading numbers
readings = np.arange(1, len(temperatures) + 1)

# 3. Calculate average temperature
average_temperature = np.mean(temperatures)

print("Average temperature:", average_temperature, "C")
print("Highest temperature:", np.max(temperatures), "C")
print("Lowest temperature:", np.min(temperatures), "C")

# 8. Identify critical temperatures
critical_temperatures = temperatures[temperatures >= 40]

print("\n--- CRITICAL TEMPERATURE ALERT ---")

print("Critical readings:")
print(critical_temperatures)

print("Number of critical readings:", len(critical_temperatures))

# 4. Create a line chart
plt.figure(figsize=(10, 5))

plt.plot(
    readings,
    temperatures,
    marker="o",
    label="Temperature"
)

# 5. Add average temperature line
plt.axhline(
    y=average_temperature,
    linestyle="--",
    label="Average temperature"
)

# 6. Add chart information
plt.title("Robot Temperature Monitoring")
plt.xlabel("Sensor Reading")
plt.ylabel("Temperature (C)")

plt.legend()
plt.grid(True)

plt.savefig("robot_temperature_line_chart.png")
# 7. Display the chart
plt.show()

# 8. Create a bar chart
plt.figure(figsize=(10, 5))

plt.bar(
    readings,
    temperatures,
    label="Temperature"
)

plt.title("Robot Temperature Comparison")
plt.xlabel("Sensor Reading")
plt.ylabel("Temperature (C)")

plt.legend()
plt.grid(axis="y")

plt.savefig("robot_temperature_bar_chart.png")
plt.show()

print("\nExercise 03 completed!")

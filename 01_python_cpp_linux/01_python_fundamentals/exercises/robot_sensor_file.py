
# ==========================================
# EXERCISE 08 - FILE HANDLING & DATA LOGGING
# Robotics Engineering
# ==========================================

import csv

print("\n--- PART 1: CREATING A SENSOR LOG FILE ---")

# Define sensor data
sensor_data = [
    {"sensor": "Temperature", "value": 35, "unit": "C"},
    {"sensor": "Distance", "value": 45, "unit": "cm"},
    {"sensor": "Battery", "value": 80, "unit": "%"}
]

# Create a CSV file and write sensor data
with open("sensor_log.csv", "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["sensor", "value", "unit"]
    )

    # Write column names
    writer.writeheader()

    # Write sensor readings
    writer.writerows(sensor_data)

print("Sensor log file created successfully!")


# ==========================================
# PART 2 - READING SENSOR DATA
# ==========================================

print("\n--- PART 2: READING SENSOR DATA ---")

try:

    with open("sensor_log.csv", "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(
                row["sensor"],
                ":",
                row["value"],
                row["unit"]
            )

except FileNotFoundError:
    print("ERROR: Sensor log file not found!")


# ==========================================
# PART 3 - ADDING NEW SENSOR DATA
# ==========================================

print("\n--- PART 3: APPENDING NEW DATA ---")

new_reading = [{
    "sensor": "Temperature",
    "value": 38,
    "unit": "C"
},
{
    "sensor": "Pressure",
    "value": 100.5,
    "unit": "kPa"
},
{
    "sensor": "Temperature",
    "value": 39,
    "unit": "C"
},
{
    "sensor": "Temperature",
    "value": 40,
    "unit": "C"
},
{
    "sensor": "Temperature",
    "value": 41,
    "unit": "C"
},
{
    "sensor": "Temperature",
    "value": 42,
    "unit": "C"
},
{
    "sensor": "Temperature",
    "value": 28,
    "unit": "C"
}]

with open("sensor_log.csv", "a", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["sensor", "value", "unit"]
    )

    writer.writerows(new_reading)

print("New sensors reading added successfully!")



# ==========================================
# PART 4 - READING THE UPDATED FILE
# ==========================================

print("\n--- PART 4: UPDATED SENSOR LOG ---")

with open("sensor_log.csv", "r") as file:

    reader = csv.DictReader(file)

    total_readings = 0
    temperature_values = []

    for row in reader:

        print(
            row["sensor"],
            ":",
            row["value"],
            row["unit"]
        )

        total_readings += 1

        # Collect temperature readings
        if row["sensor"] == "Temperature":
            temperature_values.append(float(row["value"]))

highest_temperature = max(temperature_values)
print("Highest temperature:", highest_temperature, "C")

# Calculate average temperature
if len(temperature_values) > 0:

    average_temperature = sum(temperature_values) / len(temperature_values)

    print("\nAverage temperature:", round(average_temperature, 2), "C")

else:
    print("No temperature readings available!")


print("\nTotal readings stored:", total_readings)

# ==========================================
# END OF EXERCISE
# ==========================================

print("\nExercise 08 completed!")

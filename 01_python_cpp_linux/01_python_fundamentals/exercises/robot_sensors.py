
# ==========================================
# EXERCISE 07 - LISTS AND DICTIONARIES
# Robotics Engineering
# ==========================================

# PART 1 - PYTHON LISTS

print("\n--- PART 1: SENSOR READINGS ---")

# Create a list with sensor readings
temperature_readings = [22, 25, 24, 28, 26]

# Print the complete list
print("All readings:", temperature_readings)

# Access individual elements
print("First reading:", temperature_readings[0])
print("Last reading:", temperature_readings[-1])

# Add a new reading
temperature_readings.append(30)

# Modify an existing reading
temperature_readings[1] = 27

# Count the readings
print("Total readings:", len(temperature_readings))

# Process all readings
print("\nProcessing sensor readings:")

for reading in temperature_readings:
    print("Temperature:", reading, "C")

#Check average temperature of all sensors
avg_tempature= sum(temperature_readings)/ len(temperature_readings)
print("Average Temperatures: ", avg_tempature, "C")

#Highest Temperature 
high_temperature= max(temperature_readings)
print ("Highest Temperature", high_temperature, "C")

#Lowest Temperature
low_temperature= min(temperature_readings)
print("Lowest Temperature", low_temperature, "C")

if max(temperature_readings) > 40:
    print("WARNING: Motor overheating!")
else:
    print("Motor temperature is normal.")

# ==========================================
# PART 2 - PYTHON DICTIONARIES
# ==========================================

print("\n--- PART 2: ROBOT INFORMATION ---")

# Create a dictionary with robot information
robot = {
    "name": "TurtleBot3",
    "battery": 90,
    "speed": 0.5,
    "status": "Active"
}

# Access dictionary values
print("Robot name:", robot["name"])
print("Battery level:", robot["battery"], "%")

# Update battery level
robot["battery"] = 65

# Add a new property
robot["location"] = "Warehouse"

# Display all robot information
print("\nRobot information:")

for key, value in robot.items():
    print(key, ":", value)


# Update battery level
robot["battery"] = 20

if robot["battery"] <=30 :
    print("WARNING: Robot Low battery!") 
    print ("Battery", robot["battery"], "%")


# ==========================================
# PART 3 - COMBINING LISTS AND DICTIONARIES
# ==========================================

print("\n--- PART 3: ROBOT SENSOR MONITORING ---")

# Create a list containing multiple sensor dictionaries
sensors = [
    {
        "name": "Temperature",
        "value": 35,
        "unit": "C"
    },
    {
        "name": "Distance",
        "value": 45,
        "unit": "cm"
    },
    {
        "name": "Battery",
        "value": 80,
        "unit": "%"
    }
]

sensors = [
    {
        "name": "Pressure",
        "value": 100,
        "unit": "kPa"
    },
]


# Process all sensors
for sensor in sensors:

    print(
        sensor["name"],
        ":",
        sensor["value"],
        sensor["unit"]
    )

    # Check battery level
    if sensor["name"] == "Battery":
        if sensor["value"] < 30:
            print("WARNING: Low Battery!")

    # Check temperature
    if sensor["name"] == "Temperature":
        if sensor["value"] > 40:
            print("WARNING: High Temperature!")



# ==========================================
# END OF EXERCISE
# ==========================================

print("\nExercise 07 completed!")
print("Total sensors processed:", len(sensors))

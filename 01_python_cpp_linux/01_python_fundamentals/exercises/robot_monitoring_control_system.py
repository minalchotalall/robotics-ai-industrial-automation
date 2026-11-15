
import csv

print("\n===================================")
print(" ROBOT MONITORING & CONTROL SYSTEM")
print("===================================")

# 1. Sensor readings
sensor_readings = [
    {"temperature": 35, "distance": 50, "battery": 90},
    {"temperature": 42, "distance": 35, "battery": 75},
    {"temperature": 38, "distance": 15, "battery": 60},
    {"temperature": 52, "distance": 8, "battery": 25},
    {"temperature": 30, "distance": 45, "battery": 12},
    {"temperature": 45, "distance": 25, "battery": 55}
]

# 2. Function to check robot safety
def check_robot_status(reading):

    temperature = reading["temperature"]
    distance = reading["distance"]
    battery = reading["battery"]

    if temperature >= 50 or distance < 10 or battery < 15:
        return "CRITICAL"

    elif temperature >= 40 or distance < 20 or battery < 30:
        return "WARNING"

    else:
        return "NORMAL"


# 3. Process sensor readings
print("\n--- SENSOR MONITORING ---")

processed_readings = []

for number, reading in enumerate(sensor_readings, start=1):

    status = check_robot_status(reading)

    result = {
        "reading": number,
        "temperature": reading["temperature"],
        "distance": reading["distance"],
        "battery": reading["battery"],
        "status": status
    }

    processed_readings.append(result)

    print(
        f"Reading {number}: "
        f"Temperature={reading['temperature']} C | "
        f"Distance={reading['distance']} cm | "
        f"Battery={reading['battery']}% | "
        f"Status={status}"
    )


# 4. Calculate system statistics
temperatures = [r["temperature"] for r in processed_readings]
batteries = [r["battery"] for r in processed_readings]

average_temperature = sum(temperatures) / len(temperatures)
lowest_battery = min(batteries)
highest_temperature = max(temperatures)

critical_count = 0
warning_count = 0
normal_count = 0

for reading in processed_readings:

    if reading["status"] == "CRITICAL":
        critical_count += 1

    elif reading["status"] == "WARNING":
        warning_count += 1

    else:
        normal_count += 1


if critical_count > 0 :
    print("ACTION REQUIRED: Critical conditions detected!")
elif warning_count > 0 : 
    print ("ATTENTION: Some readings need monitoring.")
else:  
    print ("All readings are normal.")


# 5. Display system report
print("\n--- SYSTEM REPORT ---")

print("Total readings:", len(processed_readings))
print(f"Average temperature: {average_temperature:.2f} C")
print("Highest Temperature:", highest_temperature, "C")
print("Lowest battery level:", lowest_battery, "%")
print("Normal readings:", normal_count)
print("Warning readings:", warning_count)
print("Critical readings:", critical_count)


# 6. Save data to CSV
filename = "robot_monitoring_log.csv"

with open(filename, "w", newline="") as file:

    fieldnames = [
        "reading",
        "temperature",
        "distance",
        "battery",
        "status"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(processed_readings)


print("\nData saved successfully to:", filename)
print("\nRobot monitoring system completed!")

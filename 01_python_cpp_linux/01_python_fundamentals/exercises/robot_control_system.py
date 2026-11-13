
# Exercise 06 - Robot Control System

# Function to move the robot
def move_robot():
    print("ACTION: Robot moving forward")
    print("Speed: 0.5 m/s")


# Function to reduce robot speed
def reduce_speed():
    print("ACTION: Reducing robot speed")
    print("Speed: 0.2 m/s")


# Function to stop the robot
def stop_robot():
    print("ACTION: STOP!")
    print("Motors deactivated")

def reverse_robot():
    print("ACTION: Robot reversing")

count = 0 
# Function to process sensor readings
def check_obstacle(distance):


    print("\nChecking obstacle distance:", distance, "meters")

    if distance <= 0.1:
        stop_robot()

    elif distance <= 1.0:
        reduce_speed()
    
    elif distance <= 0.3: 
        reverse_robot()

    else:
        move_robot()

# Main program
print("ROBOT CONTROL SYSTEM STARTED")
print("--------------------------------")

# Simulated sensor readings
sensor_readings = [2.0, 1.5, 0.8, 0.5, 0.25, 3.0, 2.5, 0.10]


# Robot continuously processes readings
for distance in sensor_readings:
    check_obstacle(distance)

print("Total sensor readings processed:", len(sensor_readings))
print("\nROBOT CONTROL SYSTEM FINISHED")

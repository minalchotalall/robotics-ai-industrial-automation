
# Exercise 05 - Python Functions

# Function to start the robot
def start_robot():
    print("Robot starting...")
    print("Motors activated!")


# Function to stop the robot
def stop_robot():
    print("Robot stopping...")
    print("Motors deactivated!")


# Function to check battery
def check_battery(battery):

    print("Battery level:", battery, "%")

    if battery <= 20:
        print("WARNING: Low battery!")
        stop_robot()
    else:
        print("Battery level is OK.")


def move_robot(speed):
    print ("Robot moving forward...")
    print("Speed: ", speed, "m/s")

# Main program
start_robot()

check_battery(85)

move_robot(0.5)

stop_robot()

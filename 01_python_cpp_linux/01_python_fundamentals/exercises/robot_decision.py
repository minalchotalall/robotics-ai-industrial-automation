# Exercise 03 - Conditional Statements
# Robot Obstacle Detection System

robot_name = "TurtleBot3"

# Simulated sensor reading
obstacle_distance = 2.05

print("ROBOT:", robot_name)
print("Obstacle distance:", obstacle_distance, "meters")

# Robot decision system

if obstacle_distance <= 0.30:
    print("WARNING: Obstacle detected!")
    print("ACTION: STOP THE ROBOT")

elif obstacle_distance <= 1.00:
    print("WARNING: Obstacle nearby!")
    print("ACTION: REDUCE SPEED")

else:
    print("PATH CLEAR")
    print("ACTION: CONTINUE MOVING")
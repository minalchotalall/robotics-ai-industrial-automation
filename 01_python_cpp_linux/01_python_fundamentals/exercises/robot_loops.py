# Exercise 04 - Python Loops

print("ROBOT SYSTEM STARTING")

# FOR LOOP
print("\nStarting sensor checks...")

for check in range(1, 10):
    print("Sensor check number:", check)

print("Sensor checks completed!")


# WHILE LOOP

battery = 100

while battery > 0:


    print("Robot operating...")
    print("Battery level:", battery, "%")

    if battery == 50:
        print("*WARNING* Half of battery has been used!")
   
    if battery == 20: 
        print("Battery at 20%, low consumption mode.")
        break

    battery -= 10

print("Battery empty!")
print("Robot shutting down.")

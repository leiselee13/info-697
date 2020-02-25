# Write your code here :-)
from microbit import *
# Defining variables for functions
temp = (temperature())
comp = (compass.heading())

# Main Loop
while True:
    if (button_a.is_pressed()):
        display.scroll(comp)
        print(comp)
        sleep(1000)
        display.scroll(temp)
        print(temp)
        sleep(1000)
# write data to file
    file = open("testfile.csv" , "w")
    file.write("temp" "," "comp")


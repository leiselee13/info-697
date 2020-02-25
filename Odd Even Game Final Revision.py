# Write your code here :-)
from microbit import *
import random

display.scroll("Is the number even?")
display.scroll("Press A for even, B for odd")
display.scroll("Touch pin0 to reset")

num = int(random.randint(1, 6))
display.show(str(random.randint(1, 6)))

# mod will be used for "Odd"
while True:
    if (button_a.is_pressed()):
        if ((num % 2) == 0):
            display.show("Even")
        else:
            display.show(Image.NO)
    if (button_b.is_pressed()):
        if (num % 2 == 1):
            display.show("Odd")
        else:
            display.show(Image.NO)
(pin0.is_touched())
display.clear()
sleep(100)


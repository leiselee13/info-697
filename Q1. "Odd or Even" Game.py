# Write your code here :-)
from microbit import *
import random

display.scroll("Is the number even?")
display.scroll("Press A for even, B for odd")
display.scroll("Touch pin0 to reset")

num = int(random.randint(1, 6))
mod = (num % 2)
display.show(str(random.randint(1, 6)))

while True:
    def game():

        if (button_a.is_pressed()):
            if ((num % 2) == 0):
                display.show("Even")
            else:
                display.show(Image.NO)
        if (button_b.is_pressed()):
            if ((mod % 2) == 1):
                display.show("Odd")
            else:
                display.show(Image.NO)
        if (pin0.is_touched()):
            display.scroll("let's play again")

            display.clear()
    sleep(200)
    game()

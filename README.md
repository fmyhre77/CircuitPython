# CircuitPython
Year Long Engineering 3 Notebook
#First Assignment
My first assignment was to upload CircuitPython code to a metro express and make it blink. My second assignment was to upload it here.

import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    dot.fill((0, 0, 255))

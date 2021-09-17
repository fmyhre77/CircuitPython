import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5

while True:
    print("Make it blue!")
    dot.fill((0, 0, 255))
    time.sleep(0.5)
    print("Make it red!")
    dot.fill((255, 0, 0))
    time.sleep(0.5)

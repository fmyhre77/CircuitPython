# CircuitPython
Year Long Engineering 3 Notebook
## Hello_CircuitPython
### Description and Code
My first assignment was to upload CircuitPython code to a metro express and make it blink. My second assignment was to upload it here.

```
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1

while True:
    print("Make it pink")
    dot.fill((25,0,25))
    time.sleep(0.2)
    print("Make it orange")
    dot.fill((255, 125, 0))
    time.sleep(0.2)

```
### Evidence
<img src="https://ezgif.com/cut/ezgif-4-f33a4798e087.gif" alt="gif" width="500" height="600">
### Reflection

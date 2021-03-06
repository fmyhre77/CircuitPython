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
<img src="Media/led.gif.gif" alt="gif" width="400" height="250">

### Reflection
I had difficulties adding my GIF to github, and that was about it. The problem was solved by google searching key words in the error message on git bash. It is useful to add images without Gitbash as well, by pressing add image in a folder in the repository.
## CircuitPython Servo
### Description and Code
The assignment was to get a Servo to rotate 180 degrees using CircuitPython Code. 

```
import time
import board
import pwmio
import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

    for angle in range(180, 0, -5):  # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
        
```
### Evidence
<img src="https://github.com/afriedm49/Circuit_Python_Asher/blob/main/ServoGif.gif?raw=true" alt="gif" width="400">

Image credit goes to [Asher Friedman](https://github.com/afriedm49/Circuit_Python_Asher)

### Reflection
I had difficulties uploading my code from the right folder as well as getting it to upload. I had to switch to my CircuitPython folder and named the file code.py.To get the servo to work I had to use for statements, which were new and useful for angle ranges withs servos.
## CircuitPython Ultrasonic Sensor
### Description and Code
My assignment was to make a neopizel change color based on the distance read from an ultrasonic sensor.
```
import time
import board
import neopixel
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D8)

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = .15
color = str
cm = 0

while True:
    try:
        cm = round(sonar.distance)
        if cm < 10:
            led.fill((255, 153, 51))
        
        elif cm < 20:
            led.fill((255, 51, 255))
            
        elif cm > 20:
            led.fill((153, 255, 255))
        print((sonar.distance,))
        
    except RuntimeError:
        print("JOE!")
    time.sleep(0.1)
```
### Evidence
<img src="Media/Ultrasonic.gif.gif" alt="gif">

### Reflection
For this assignment I had trouble getting my ultrasonic sensor to correspond with my LED. I fixed this by using try: and except: to find out what the sensor was reading, and communicate it to my neopixel.
## CircuitPyhton Photointerrupters

### Description and Code
My assignment was to have a photointerrupter count the number of interrupts over 4 seconds.

```

from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D7)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

counter = 0

photo = False
state = False

max = 4
start = time.time()
while True:
    photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo
    remaining = max - time.time()

    if remaining <= 0:
        print("Interrupts:", str(counter))
        max = time.time() + 4
        counter = 0
```
### Reflection
My assignment was to make a LCD screen display the number of interrupts during a time period, so I used a run time variable to start the sequence. Once the time starts, the number of interrupts is counted by reading the state of the intterupter, then adding a value to a variable when it is interacted with.
## CircuitPython LCD
### Description and Code
My assignment was to control an LCD screen using capacitive touch. One wire was to count up or down and the other one was to determine whether it went up or down.
```
import board
import touchio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

i2c = board.I2C()

lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

touch_A0 = touchio.TouchIn(board.A0) 
touch_A1 = touchio.TouchIn(board.A1) 
x = 0
y = 1

while True:
    if touch_A0.value:
        lcd.clear()
        x = x + y
        lcd.print(str(x))
        if y > 0:
            lcd.print(" Counting Up")
        if y < 0:
            lcd.print(" Counting Down")
        while touch_A0.value:
            print("HelloA0")
    if touch_A1.value:
        lcd.clear()
        y = y * -1
        lcd.print(str(x))
        while touch_A1.value:
            print("HelloA1")
```

Title: SN74HC595 shift register. Controlling from Raspberry
Author: SergeM
Date: 2017-04-23 12:11:00
Slug: sn74hc595-shift-register
Tags: raspberry, pi



### Pinouts
<img src="{filename}/2017/04/sn74hc595-shift-register-pinout.jpg" width="300">


### How to control
<img src="{filename}/2017/04/sn74hc595-shift-register-control.jpg" width="80%">

It seems that procedure described in Texas Instruments' datasheet is wrong:
<img src="{filename}/2017/04/sn74hc595-shift-register-wrong-control.jpg" width="80%">



## Using in motor shield DK Electronics V1
Scheme:
![shield scheme]({filename}/2017/04/sn74hc595-shift-register-mshieldv1-schem.png)


[L293x Quadruple Half-H Driver](http://www.ti.com/lit/ds/symlink/l293.pdf) (pdf)


### Connection

Raspberry PIN 6 -> Shield GROUND

Raspberry PIN 11 -> Shield PIN 8 (Register PIN 14, SER / DS)

Raspberry PIN 12 -> Shield PIN 12 (Register PIN 12, SRCLK / SHCP)

Raspberry PIN 13 -> Shield PIN 4 (Register PIN 11, RCLK / STCP)

Raspberry PIN 15 -> Shield PIN 7 (Register PIN 13. OE)

### Code
Working code that enables odd outputs of the shift register:
```python
#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

SER   = 11
RCLK  = 12
SRCLK = 13
OE = 15

#===============   LED Mode Defne ================
#   You can define yourself, in binay, and convert it to Hex 
#   8 bits a group, 0 means off, 1 means on
#   like : 0101 0101, means LED1, 3, 5, 7 are on.(from left to right)
#   and convert to 0x55.

LED0 = [0b01010101,]    #original mode

#=================================================

def print_msg():
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')

def setup():
    GPIO.setmode(GPIO.BOARD)    # Number GPIOs by its physical location
    GPIO.setup(SER, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.setup(OE, GPIO.OUT)
    GPIO.output(SER, GPIO.LOW)
    GPIO.output(RCLK, GPIO.LOW)
    GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(OE, GPIO.LOW)

def hc595_in(dat):
    print("Writing {}".format(bin(dat)))
    for bit in range(0, 8): 
        GPIO.output(SER, 1 & (dat >> bit))
        GPIO.output(SRCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW)

def hc595_out():
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)

def loop():
    WhichLeds = LED0    # Change Mode, modes from LED0 to LED3
    sleeptime = 0.3     # Change speed, lower value, faster speed
    while True:
        for i in range(0, len(WhichLeds)):
            print("Running phase1, step {}".format(i))
            hc595_in(WhichLeds[i])
            hc595_out()
            time.sleep(sleeptime)
        
        for i in range(len(WhichLeds)-1, -1, -1):
            print("Running phase2, step {}".format(i))
            hc595_in(WhichLeds[i])
            hc595_out()
            time.sleep(sleeptime)

def destroy():   # When program ending, the function is executed. 
    GPIO.cleanup()

if __name__ == '__main__': # Program starting from here 
    print_msg()
    setup() 
    try:
        loop()  
    except KeyboardInterrupt:  
        destroy()  
```



## Sources
[1](https://protostack.com.au/2010/05/introduction-to-74hc595-shift-register-controlling-16-leds/)


[2](https://www.sunfounder.com/learn/Super_Kit_V2_for_RaspberryPi/lesson-10-driving-leds-by-74hc595-super-kit-for-raspberrypi.html) Lesson 10 Driving LEDs by 74HC595

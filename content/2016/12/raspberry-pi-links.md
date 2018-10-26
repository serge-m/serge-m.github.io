Title: Raspberry Pi Links
Author: SergeM
Date: 2016-12-31 21:30:00
Tags: links, raspberry, pi, servo, stepper, motor shield, pwm, raspberry pi, ssh


## I2C interface

[Description of I2C interface](https://learn.sparkfun.com/tutorials/i2c)

[Raspberry Pi SPI and I2C Tutorial ](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)


Continuous deployment (Russian)
[Непрерывная кросс компиляция на Raspberry PI](https://m.habrahabr.ru/post/318840/)

## Controlling motors

### Brushless motor

[Control brushless motor with ESC](https://solenerotech1.wordpress.com/2013/09/09/tutorialhow-to-control-a-brushless-motor-with-raspberry-pi/). Without additional controllers

[With  PCA9685 PWM Board](http://raspberrypi.stackexchange.com/a/36317) (stackexchange thread)

[One more thread](https://www.raspberrypi.org/forums/viewtopic.php?t=46732)

### Controlling multiple servos 
To control multiple servos you can use PCA9685 controller. Connection is shown below.
<img src="{filename}/2016/12/servo_control_pca9685_2.jpg" style="width: 50%; height: 50%">
<img src="{filename}/2016/12/servo_control_pca9685_1.jpg" style="width: 50%; height: 50%">
<img src="{filename}/2016/12/servo_control_pca9685_3.jpg" style="width: 50%; height: 50%">
<img src="{filename}/2016/12/servo_control_pca9685_4.jpg" style="width: 50%; height: 50%">

You have to enable I2C interface first with `sudo raspi-config`. Choose "Interfacing Options" -> "I2C" -> "Enable".

Now installing the diagnostic tool and running:
```
sudo apt-get install -y i2c-tools
sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: 70 -- -- -- -- -- -- --                         
```

Now we can install library:
```
pip install Adafruit_PCA9685
```
and run a simple program:
```python
# sample.py
# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(0, 0, servo_max)
time.sleep(1)
```
running:
```
python sample.py
```



See alow:
* [datasheet](https://cdn-shop.adafruit.com/datasheets/PCA9685.pdf)
* [Adafruit 16 Channel Servo Driver with Raspberry Pi](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-16-channel-servo-driver-with-raspberry-pi.pdf) Created by Kevin Townsend. pdf. (pca-9685)
* [troubleshooting](https://github.com/adafruit/Adafruit_Python_PCA9685/issues/1)
* [Controlling one servo](http://razzpisampler.oreilly.com/ch05.html). No additional controllers needed


### Stepper motors / DC (brushed) motors
[with l293d](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors?view=all)

[[Raspberry] Stepper and dc motor using specializer HAT](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi?view=all)  
Based on PC9865 PWM and TB6612 chipset. 1.2A per channel current capability (20ms long bursts of 3A peak)


[[Arduino] With adafruit motor schield v1](https://learn.adafruit.com/adafruit-motor-shield?view=all)  
Based on 74HC595N Serial to parallel output latch and L293D driver. 0.6A per bridge (1.2A peak) with thermal shutdown protection, 4.5V to 25V.  
[Library for motor control](https://github.com/adafruit/Adafruit-Motor-Shield-library)    
See also [about SN74HC595 shift register](/sn74hc595-shift-register.html)



[[Arduino] With adafruit motor shield v2](https://learn.adafruit.com/adafruit-motor-shield-v2-for-arduino?view=all)  
Based on PCA9685 and TB6612 MOSFET drivers with 1.2A per channel current capability ( up to 3A peak for approx 20ms at a time)

[[Raspberry] Drive a DC motor forward and in reverse with variable speed](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-9-controlling-a-dc-motor?view=all) (with l293d, adafruit lesson 9)

[[Micropython board] Control  dc motor with pca9685](https://learn.adafruit.com/micropython-hardware-pca9685-dc-motor-and-stepper-driver?view=all) 

[[Raspberry] Video with just simple transistor scheme and with L293D controller](https://www.youtube.com/watch?v=W7cV9_W12sM)

[[Raspberry] using L293D and 4N35 opto isolator](https://medium.com/@seyoum14/using-a-dc-motor-to-run-a-propeller-with-raspberry-pi-e5a570864e6f#.q7qutomrv)

[[Arduino] 1 bidirectional DC motor using small DRV8871 motor driver](https://learn.adafruit.com/adafruit-drv8871-brushed-dc-motor-driver-breakout?view=all)   
Up to 45V and 3.6A of motor control

It is possible to have frequency controlled dc driver connected through Adafruit 16 Channel Servo Driver. 
See [post](https://www.raspberrypi.org/forums/viewtopic.php?t=12067&p=161140). [controller, ~100 Euro](http://www.robotshop.com/en/sabertooth-dual-regenerative-motor-driver.html), powerfull

[[Arduino] using drv8833 driver](https://ulrichbuschbaum.wordpress.com/2014/10/28/using-the-drv8833-motor-driver/), 

[[Arduino] using l293d](https://ulrichbuschbaum.wordpress.com/2014/09/17/the-l293d-motor-driver-and-makeblock/)


Using transistors: (1)[http://electronics.stackexchange.com/questions/7235/motor-driver-using-only-a-2n2222-transistor], very weak

## Connecting via ssh:
```
ssh -Y user@raspberrypi-url
```

## Access rasbberry Pi without monitor and ethernet 

Assuming we have an operating system (raspbian) installed.

1. Plug the SD-card into a computer. 

2. Automatic connection to wifi. Edit `/etc/wpa_supplicant/wpa_supplicant.conf` and add the following lines:

```
network={
    ssid="my-network-name"
    psk="my-network-pass"
}
```

In the end the file should look like this:
```
country=GB
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="my-network-name"
    psk="my-network-pass"
}
```

`country` field is essential. Wifi wont work without it. In the log you will see `raspberrypi systemd[1]: Started Disable WiFi if country not set.`


3. Enable SSH access. Create an empty file `ssh` in `/boot/`.

4. Plug the card back into your raspberry, turn on. 

Now you can connect to raspberry via ssh:

    ssh pi@raspberrypi
    
or 

    ssh pi@<IP-OF-YOUR-RASPBERRY>




## Reading input (button) from GPIO
[without interrupts, raspi.tv](http://raspi.tv/2013/rpi-gpio-basics-4-setting-up-rpi-gpio-numbering-systems-and-inputs)



## RaspberryPi Zero pins Layout
![GPIO raspberry pins scheme]({filename}/2016/12/gpio.png)

![pins layout photo]({filename}/2016/12/gpio-raspberry-zero.png) [image source](http://pi4j.com/pins/model-zero-rev1.html)

Interactive website for pinout of Raspberry Pi for different interfaces [Pinout](https://pinout.xyz/#)




## Other
* [Example of using 545043 power supply](https://www.sunfounder.com/learn/Super_Kit_V2_for_RaspberryPi/lesson-7-how-to-drive-a-dc-motor-super-kit-for-raspberrypi.html)

* [description of sn74hc595](http://www.ti.com/lit/ds/symlink/sn74hc595.pdf)

* [blog about building security robot](https://seregus.wordpress.com/)

* [h bridge using 2n2222 transistors for dc motor control. + reverse](http://www.instructables.com/id/H-Bridge-on-a-Breadboard/?ALLSTEPS); [another version](http://electronics.stackexchange.com/questions/7235/motor-driver-using-only-a-2n2222-transistor);
* [another version of h bridge](http://www.electronicsteacher.com/robotics/robotics-tutorial/advanced-robotics/controlling-dc-motors.php)
* [Build a Raspberry Pi Telepresence Rover ](http://www.bot-thoughts.com/2013/04/raspberry-pi-telepresence-rover.html) using [Pololu DRV8835](/motor-drivers-controllers.html)

* My DIY [remote controlled robot on raspberry pi](https://github.com/serge-m/robot-remote-control) with camera. 

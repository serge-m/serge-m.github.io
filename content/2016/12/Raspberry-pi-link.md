Title: Raspberry Pi Links
Author: SergeM
Date: 2016-12-31 21:30:00
Tags: links


[Description of I2C interface](https://learn.sparkfun.com/tutorials/i2c)

[Raspberry Pi SPI and I2C Tutorial ](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)


Continuous deployment (Russian)
[Непрерывная кросс компиляция на Raspberry PI](https://m.habrahabr.ru/post/318840/)

## Controlling motors

### Brushless motor

[Control brushless motor with ESC](https://solenerotech1.wordpress.com/2013/09/09/tutorialhow-to-control-a-brushless-motor-with-raspberry-pi/). Without additional controllers

[With  PCA9685 PWM Board](http://raspberrypi.stackexchange.com/a/36317) (stackexchange thread)

[One more thread](https://www.raspberrypi.org/forums/viewtopic.php?t=46732)

### multiple servos 
[Controlling one servo](http://razzpisampler.oreilly.com/ch05.html). No additional controllers needed

[Adafruit 16 Channel Servo Driver with Raspberry Pi
Created by Kevin Townsend. pdf. (pca-9685)](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-16-channel-servo-driver-with-raspberry-pi.pdf)

### Stepper motors / DC (brushed) motors
[with l293d](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors?view=all)

[[Raspberry]stepper and dc motor using specializer HAT](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi?view=all) 
Based on PC9865 PWM board and TB6612 chipset. 1.2A per channel current capability (20ms long bursts of 3A peak)

[[Raspberry]Drive a DC motor forward and in reverse with variable speed](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-9-controlling-a-dc-motor?view=all) (with l293d, adafruit lesson 9)

[[Micropython board]control  dc motor with pca9685](https://learn.adafruit.com/micropython-hardware-pca9685-dc-motor-and-stepper-driver?view=all) 

[Video with specialized dc motor controller L293D](https://www.youtube.com/watch?v=W7cV9_W12sM)

[using L293D and 4N35 opto isolator](https://medium.com/@seyoum14/using-a-dc-motor-to-run-a-propeller-with-raspberry-pi-e5a570864e6f#.q7qutomrv)

[Adafruit DRV8871 motor driver, 1 dc motor](https://learn.adafruit.com/adafruit-drv8871-brushed-dc-motor-driver-breakout?view=all)

It is possible to have frequency controlled dc driver connected through Adafruit 16 Channel Servo Driver. 
See [post](https://www.raspberrypi.org/forums/viewtopic.php?t=12067&p=161140). [controller, ~100 Euro](http://www.robotshop.com/en/sabertooth-dual-regenerative-motor-driver.html), powerfull

from arduino: 
[using drv8833 driver](https://ulrichbuschbaum.wordpress.com/2014/10/28/using-the-drv8833-motor-driver/), 
[using l293d](https://ulrichbuschbaum.wordpress.com/2014/09/17/the-l293d-motor-driver-and-makeblock/)


Using transistors: (1)[http://electronics.stackexchange.com/questions/7235/motor-driver-using-only-a-2n2222-transistor]

## Connecting via ssh:
```
ssh -Y user@raspberrypi-url
```


## Reading input (button) from GPIO
[without interrupts, raspi.tv](http://raspi.tv/2013/rpi-gpio-basics-4-setting-up-rpi-gpio-numbering-systems-and-inputs)

## RaspberryPi Zero pins Layout
![GPIO raspberry pins scheme]({filename}/2016/12/gpio.png)

![pins layout photo]({filename}/2016/12/gpio-raspberry-zero.png) [image source](http://pi4j.com/pins/model-zero-rev1.html)

## Other
[Example of using 545043 power supply](https://www.sunfounder.com/learn/Super_Kit_V2_for_RaspberryPi/lesson-7-how-to-drive-a-dc-motor-super-kit-for-raspberrypi.html)

[description of sn74hc595](http://www.ti.com/lit/ds/symlink/sn74hc595.pdf)

[blog about building security robot](https://seregus.wordpress.com/)

[h bridge using 2n2222 transistors for dc motor control. + reverse](http://www.instructables.com/id/H-Bridge-on-a-Breadboard/?ALLSTEPS); [another version](http://electronics.stackexchange.com/questions/7235/motor-driver-using-only-a-2n2222-transistor);
[another version of h bridge](http://www.electronicsteacher.com/robotics/robotics-tutorial/advanced-robotics/controlling-dc-motors.php)

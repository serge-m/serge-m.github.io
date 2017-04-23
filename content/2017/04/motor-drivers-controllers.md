Title: Motor drivers / controllers 
Author: SergeM
Date: 2017-04-23 12:11:00
Slug: motor-dirvers-controllers
Tags: raspberry, pi


Articles about raspberry pi: [here](/raspberry-pi-links.html)
SN74HC595 shift register. Controlling from Raspberry: [here](/sn74hc595-shift-register.html)


[Comparison of Polou DC motor drivers](https://www.pololu.com/search/compare/11)

[Comparison of stepper motor drivers](https://www.pololu.com/search/compare/120,156,155,154/0,s,8,1,35,32,21,22,23,25/24,27,28,31,30,39,38,33,78,155,157/x)


## DC motors


### Pololu DRV8833 Dual Motor Driver Carrier
[exp-tech 4,95€](http://www.exp-tech.de/pololu-drv8833-dual-motor-driver-carrier)  
two DC motors or one stepper motor  
2.7‌‌–10.8 V  
1.2 A continuous (2 A peak) per motor

Motor outputs can be paralleled to deliver 2.4 A continuous (4 A peak) to a single motor  
Reverse-voltage protection circuit  

<img src="{filename}/2017/04/drivers/Pololu DRV8833.png" width="250">

[datasheet](http://www.pololu.com/file/0J534/drv8833.pdf)



### Pololu DRV8835 Dual Motor Driver Carrier
[exp-tech 4,20 €](http://www.exp-tech.de/drv8835-dual-motor-driver-carrier)

[Pololu DRV8835 Dual Motor Driver Kit for Raspberry Pi, exp-tech, 7,12 €](http://www.exp-tech.de/pololu-drv8835-dual-motor-driver-kit-for-raspberry-pi-b)

[pololu 4.49 $](https://www.pololu.com/product/2135)

Pololu DRV8835 Dual Motor Driver Kit for Raspberry Pi:  
[pololu 7.49 $](https://www.pololu.com/product/2753)  
[exp-tech 7.12 €](http://www.exp-tech.de/pololu-drv8835-dual-motor-driver-kit-for-raspberry-pi-b)  
For Arduino: [exp-tech 6,60 €](http://www.exp-tech.de/pololu-drv8835-dual-motor-driver-shield-for-arduino)


[Chip only 1,74 €](http://www.mouser.de/ProductDetail/Texas-Instruments/DRV8835DSSR)

[Python library](https://github.com/pololu/drv8835-motor-driver-rpi)


Motor supply voltage: 1.5 V to 11 V  
Logic supply voltage 2 V to 7 V  
Output current: 1.2 A continuous (1.5 A peak) per motor  
Two possible interface modes: PHASE/ENABLE (default – one pin for direction, another for speed) or IN/IN (outputs mostly mirror inputs)  

Very similar to DRV8833 dual motor driver carrier in operating voltage range and continuous current rating, but the DRV8835 

* has a lower minimum operating voltage, 
* offers an extra control interface mode, 
* is 0.1" smaller in each dimension. 

The DRV8833 has a higher peak current rating (2 A per channel vs 1.5 A), optional built-in current-limiting, and no need for externally supplied logic voltage.

Mode 1:  
<img src="{filename}/2017/04/drivers/drv8835.png" width="250">

Mode 2:  
<img src="{filename}/2017/04/drivers/drv8835-mode2.png" width="250">



### Pololu DRV8801 Single Brushed DC Motor Driver Carrier
[exp-tech 5,20€](http://www.exp-tech.de/pololu-drv8801-single-brushed-dc-motor-driver-carrier)  
[polou.com 4,95$](https://www.pololu.com/product/2136)

<img src="{filename}/2017/04/drivers/Pololu DRV8801 1.jpg" width="250">
<img src="{filename}/2017/04/drivers/Pololu DRV8801 2.jpg" width="250">  

Drives a single brushed DC motor  
Motor supply voltage: 8–36 V  
Logic supply voltage: 3.3–6.5 V  
Output current: 1 A continuous (2.8 A peak)  
Simple interface requires only two I/O lines (one for direction and another for speed)  
Current sense output proportional to motor current (approx. 500 mV per A)  
Inputs are 3V- and 5V-compatible  
Under-voltage lockout and protection against over-current and over-temperature  


### Pololu A4990 Dual Motor Driver Carrier
[exp-tech 5,95 €](http://www.exp-tech.de/a4990-dual-motor-driver-carrier)

[pololu 5.95$](https://www.pololu.com/product/2137)

[Arduino library](https://github.com/pololu/a4990-motor-shield)

<img src="{filename}/2017/04/drivers/A4990 Dual Motor Driver Carrier.png" width="250">


Dual-H-bridge motor driver: 
can drive two DC motors or one bipolar stepper motor  
Operating voltage: 6‌‌–32 V  
Output current: 0.7 A continuous per motor  
Current control limits peak current to 0.9 A per motor  
Inputs are 3V- and 5V-compatible  

Robust:  
Reverse-voltage protection circuit  
Can survive input voltages up to 40 V  
Under-voltage and over-voltage protection  
Over-temperature protection  
Short-to-supply, short-to-ground, and shorted-load protection  


### Dual MC33926 Motor Driver Carrier
[   29.95$ ](https://www.pololu.com/product/1213)

    Motor channels:     2
    Minimum operating voltage:  5 V
    Maximum operating voltage:  28 V
    Continuous output current per channel:  2.5 A
    Current sense:  0.525 V/A
    Maximum PWM frequency:  20 kHz
    Minimum logic voltage:  2.5 V
    Maximum logic voltage:  5.5 V
    Reverse voltage protection?:    Y



## Steppers


### Pololu DRV8880 Stepper Motor Driver Carrier
[exp-tech 7,45 €](http://www.exp-tech.de/pololu-drv8880-stepper-motor-driver-carrier)

6.5 V to 45 V supply voltage range  
Built-in regulator (no external logic voltage supply needed)  
Can interface directly with 3.3 V and 5 V systems  
Over-temperature thermal shutdown, over-current shutdown, short circuit protection, and under-voltage lockout  
4-layer, 2 oz copper PCB for improved heat dissipation  
Exposed solderable ground pad below the driver IC on the bottom of the PCB  
Module size, pinout, and interface match those of our A4988 stepper motor driver carriers in most respects (see the bottom of this page for more information)  





### Pololu A4988 Stepper Motor Driver Carrier
[7,95 €](http://www.exp-tech.de/a4988-stepper-motor-driver-carrier-black-edition)

Minimum operating voltage:  8 V  
Maximum operating voltage:  35 V  
Continuous current per phase:   1.2 A2  
Maximum current per phase:  2 A3  
Minimum logic voltage:  3 V  
Maximum logic voltage:  5.5 V  
Microstep resolutions:  full, 1/2, 1/4, 1/8, and 1/16  
Reverse voltage protection?:    N  



### Pololu DRV8824 Stepper Motor Driver Carrier, Low Current
[6,99 €](http://www.exp-tech.de/pololu-drv8824-stepper-motor-driver-carrier-low-current)

<img src="{filename}/2017/04/drivers/pololu-drv8824-stepper-motor-driver-carrier-low-current.png" width="250">

Minimum operating voltage:  8.2 V  
Maximum operating voltage:  45 V  
Continuous current per phase:   0.75 A  
Maximum current per phase:  1.2 A  
Minimum logic voltage:  2.5 V  
Maximum logic voltage:  5.25 V  
Microstep resolutions:  full, 1/2, 1/4, 1/8, 1/16, and 1/32  
Reverse voltage protection?:    N  

    Simple step and direction control interface
    Adjustable current control lets you set the maximum current output with a potentiometer, which lets you use voltages above your stepper motor’s rated voltage to achieve higher step rates
    Intelligent chopping control that automatically selects the correct current decay mode (fast decay or slow decay)
    45 V maximum supply voltage
    Built-in regulator (no external logic voltage supply needed)
    Over-temperature thermal shutdown, over-current shutdown, and under-voltage lockout
    Short-to-ground and shorted-load protection
    4-layer, 2 oz copper PCB for improved heat dissipation
    Exposed solderable ground pad below the driver IC on the bottom of the PCB
    Module size, pinout, and interface match those of our A4988 stepper motor driver carriers in most respects 



## Voltage regulators

[Step-Up/Step-Down Voltage Regulators](https://www.pololu.com/category/133/step-up-step-down-voltage-regulators)
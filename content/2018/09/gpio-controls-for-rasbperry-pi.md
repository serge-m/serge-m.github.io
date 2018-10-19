Title: GPIO controls for Rasbperry Pi
Author: SergeM
Date: 2018-09-23 07:11:34
Slug: gpio-controls-for-rasbperry-pi
Tags: raspberry, pi, raspberry pi, gpio, services


## Libraries for GPIO
### Node JS



### Python

#### Using RPi.GPIO
* [How to Exit GPIO programs cleanly, avoid warnings and protect your Pi](https://raspi.tv/2013/rpi-gpio-basics-3-how-to-exit-gpio-programs-cleanly-avoid-warnings-and-protect-your-pi)
* [Setting up RPi.GPIO, numbering systems and inputs](http://raspi.tv/2013/rpi-gpio-basics-4-setting-up-rpi-gpio-numbering-systems-and-inputs)
* On using hardware PWM without sudo due to permissions for /dev/gpiomem:  [discussion](https://forum.ubiquityrobotics.com/t/unable-to-use-hardware-pwm-without-sudo-due-to-permissions-for-dev-gpiomem/84)

### General

#### pigpio
The library also provides a service.
It can be useful if you don't want to give root access to the client applications and want to control PWM for example.

Here is how to create a system service for `pigpiod`:

Create file 
/etc/systemd/system/pigpiod.service: 

```
[Unit]
Description=pigpiod service

[Service]
ExecStart=/usr/bin/pigpiod -g -n localhost

RestartSec=5
Restart=always

[Install]
WantedBy=multi-user.target

```

run and check status

```bash
sudo systemctl start pigpiod.service
sudo systemctl status pigpiod.service
```

should be something like this:
```
● pigpiod.service - pigpiod service
   Loaded: loaded (/etc/systemd/system/pigpiod.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2018-09-19 12:22:30 UTC; 1s ago
 Main PID: 10074 (pigpiod)
   CGroup: /system.slice/pigpiod.service
           └─10074 /usr/bin/pigpiod -l -g

```

Now enable the service:
```
sudo systemctl enable pigpiod.service
```

Now `pigpriod` has to run on startup of your raspberry pi and provide interface to gpio:
```
pigs w 4 1
```

If something went wrong and the pigpiod service doesn't start you will see
```bash
$ pigs w 4 1 
socket connect failed

```

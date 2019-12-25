:date: 2019-12-24 10:02

:title: Capture PWM signal using Arduino

:author: SergeM

:slug: capture-pwm-signal-using-arduino

:tags: arduino, pwm, robocar, pwm, c++


Parsing PWM signals
=======================

For my `robocar project <robocar.html>`_ I needed to understand the mechanism of pulse width modulation of the remote control.

My intention was to use Arduino as a proxy between RC-receiver and servos/ESC to be able to record the used input for imitation learning.
Human driver (me) sends steering commands via the remote control (transmitter). RC receiver converts radio signal into PWM signal. Arduino captures and maybe filters the signal, saves it somehow and sends it to the servos/ESC.

For analysis of the PWM signal I have found a library ``PinChangeInterrupt``: 

.. code-block:: cpp

    #include <PinChangeInterrupt.h>

the wires from the receiver are connected to the pins 10 and 11 of my arduino nano:

.. code-block:: cpp

   const int pin_pwm_in_steering = 11;
   const int pin_pwm_in_throttle = 10;

Let's create ``PwmListener`` class that listens to the interrupts on the given pin and returns the width of the last impulse.

.. code-block:: cpp

  class PwmListener
  {
    volatile unsigned int pwm_value_;   // last pwm value
    volatile unsigned long prev_time_; // last time of the impulse
  public:
    const int pin; // pin to listen
    const int pin_as_pc_int; // pin index according to PC int 

  public:
    PwmListener(int pin_, int default_value);
  
    // this function will be called on the interrupts
    void process(); 
    
    unsigned long micros_since_last_signal() const;  

    // return the latest pwm value
    unsigned int value() const; 
    unsigned long prev_time_micros() const;
  };


Full code:

.. code-block:: cpp

    class PwmListener
    {
      volatile unsigned int pwm_value_;
      volatile unsigned long prev_time_;
    public:
      const int pin;
      const int pin_as_pc_int;
    
    public:
      PwmListener(int pin_, int default_value):
        pin(pin_), pwm_value_(default_value), prev_time_(0), pin_as_pc_int(digitalPinToPCINT(pin_))
      {}
    
      void process() {
        uint8_t trigger = getPinChangeInterruptTrigger(pin_as_pc_int);
        if(trigger == RISING)
          prev_time_ = micros();
        else if(trigger == FALLING)
          pwm_value_ = micros_since_last_signal();
        else {
          // Wrong usage
        }
      }
    
      unsigned long micros_since_last_signal() const {
        return micros() - prev_time_; 
      }
    
      unsigned int value() const {
        return pwm_value_;
      }
    
      unsigned long prev_time_micros() const {
        return prev_time_;
      }
    };


now we create two listeners and define dummy caller functions for them. The dummy functions are needed to pass them by pointer.

.. code-block:: cpp

    PwmListener pwm_listener_steering (pin_pwm_in_steering, DEFAULT_PULSE_WIDTH);
    PwmListener pwm_listener_throttle (pin_pwm_in_throttle, DEFAULT_PULSE_WIDTH);
    void interrupt_steering() { pwm_listener_steering.process(); }
    void interrupt_throttle() { pwm_listener_throttle.process(); }
    
later in the ``setup()`` function we have to set up the pins:

.. code-block:: cpp

    void setup() {
      // starting input pwm monitoring...
      pinMode(pwm_listener_steering.pin, INPUT);
      attachPinChangeInterrupt(pwm_listener_steering.pin_as_pc_int, &interrupt_steering, CHANGE);
      pinMode(pwm_listener_throttle.pin, INPUT);
      attachPinChangeInterrupt(pwm_listener_throttle.pin_as_pc_int, &interrupt_throttle, CHANGE);
    
     // setting up serial interface
      Serial.begin(115200);
      Serial.println("info: waiting for output pwm controller..."); 
    }


on every loop we send the values to the host computer:

.. code-block:: cpp
    
    void loop() { 
      const int steering =   pwm_listener_steering.value();
      const int throttle =   pwm_listener_throttle.value();
      // avoiding unnecessary duplication by filtering out small perturbations
      if (
        abs(steering - old_steering) > 10 || 
        abs(throttle - old_throttle) > 10 
        ) 
      { 
        sprintf(buf, "in: %d %d\n", steering, throttle);
        Serial.print(buf);
        old_steering = steering;
        old_throttle = throttle;
      }
    }


We have also enabled the serial interface to report the values to the host machine (connected via USB).

On the host machine we run python listener:

.. code-block:: python
    import serial
    
    ports = ['/dev/ttyUSB0', '/dev/ttyUSB1']
    
    
    def main():
        for port in ports:
            print("connecting to port {}".format(port))
            try:
                with serial.Serial(port, 115200, timeout=0.01) as ser:
                    print('connected')
                    process(ser)
                    return
            except serial.serialutil.SerialException as e:
                if e.errno == 2:
                    continue
                raise
        raise FileNotFoundError("Unable to open ports {}".format(ports))
    
    
    def process(ser):
        while(True):
            line = ser.readline()  # read a '\n' terminated line
            if line != b'':
                print(line)
    
    
    if __name__ == '__main__':
        main()


Analysis
========

I have got the following graph (interactive):

.. raw:: html
    :file: static/2019-12-pwm_visualization.html

Let's consider steering series. It has three parts.

1. actual signal. The values are around 1380. The change couple of times. That corresponds to what I actually did.

2. Some strange signal values around 10000. I don't know what is it.

3. Some rare noise in between. I also don't know why it's there.

We still can use that values with some filtering of the outliers.

Another interesting thing is that steering and throttle channels have different default values. For steering it is 1380 and for throttle it is 1540. I could adjust that values a bit, but anyway it is around 1400 for one and 1500 for another.

At the same time when I send PWM signal generated by Arduino I have to use 1400 as default for both to make it work properly. I don't know what causes that shift in my measurements.

See also 
========

1. `gist with the data <https://gist.github.com/serge-m/5f07fd676b52c4741f2bea275eced729>`_

2. `robocar project <robocar.html>`_

3. `robocar main repository <https://github.com/serge-m/sergem_robocar>`_

4. `wiki <https://github.com/serge-m/sergem_robocar/wiki>`_ for robocar

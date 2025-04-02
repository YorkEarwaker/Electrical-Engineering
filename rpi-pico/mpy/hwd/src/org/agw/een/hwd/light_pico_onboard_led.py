
# https://thepihut.com/blogs/raspberry-pi-tutorials/raspberry-pi-pico-getting-started-guide
# light RPi Pico 2 W onboard led
# GPIO pin 25, GPIO25, 'LED'
# 1 = HIGH (on), 0 = LOW (off)

from machine import Pin
onboardLED = Pin('LED', Pin.OUT)
onboardLED.value(1)
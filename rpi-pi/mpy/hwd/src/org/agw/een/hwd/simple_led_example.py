
# https://thepihut.com/blogs/raspberry-pi-tutorials/raspberry-pi-pico-getting-started-guide
# Simple led example project
# simple circuit using RPi Pico W 2 & breadbaord

from machine import Pin
import time

led1 = Pin(18, Pin.OUT)
led2 = Pin(19, Pin.OUT)
led3 = Pin(20, Pin.OUT)

led1.value(1)
led2.value(1)
led3.value(1)

time.sleep(5)

led1.value(0)
led2.value(0)
led3.value(0)

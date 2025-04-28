#        _ _   _ _ _      _
#       /   ) / _ _ )  _ \ )
#      / (| |/ /  _ _ \ ) \ \
#     /  _    (  (_  ) \ \ \ \
#    / /  | |\ \ _ )  \_) \_) \
#   (_/   |_| \ _ _ /\ _ _ _ _ )
#   Anthropogenic Global Warming
# --------------------------------
# 
# Code sources
#
# MicroPython,
# machine module, 
# https://docs.micropython.org/en/latest/library/machine.html
#
# machine module, Pin class,
# https://docs.micropython.org/en/latest/library/machine.Pin.html
#
# time module, 
# https://docs.micropython.org/en/latest/library/time.html
#
# Exception
# https://docs.micropython.org/en/latest/genrst/builtin_types.html#exception
# OSError
# https://docs.micropython.org/en/latest/library/builtins.html#OSError
#
# DHT22 driver, 
# https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver
# https://docs.micropython.org/en/latest/esp8266/tutorial/dht.html
# https://mpython.readthedocs.io/en/v2.2.1/library/micropython/dht.html
#
# DHT22 sensor, Aosong (AM2302) (temperature, humidity), hardware
# https://thepihut.com/products/dht22-temperature-humidity-sensor-extras
#
# Conversion of scales of temperature,
# https://en.wikipedia.org/wiki/Conversion_of_scales_of_temperature
#
# References - trouble shooting, tutorials
# https://forums.raspberrypi.com/viewtopic.php?t=372629
# https://electrocredible.com/raspberry-pi-pico-dht22-micropython-tutorial/
# https://randomnerdtutorials.com/raspberry-pi-pico-dht11-dht22-micropython/
#
# RPi Pico 2 W pinout diagram
# https://datasheets.raspberrypi.com/picow/pico-2-w-pinout.pdf
# https://pico.pinout.xyz/
#
# DHT22 sensor, Aosong (AM2302), datasheet
# https://cdn.sparkfun.com/assets/f/7/d/9/c/DHT22.pdf
# https://cdn-shop.adafruit.com/datasheets/Digital+humidity+and+temperature+sensor+AM2302.pdf
# https://files.seeedstudio.com/wiki/Grove-Temperature_and_Humidity_Sensor_Pro/res/AM2302-EN.pdf
# 
# Sensor without I2C in 1-wire mode (eg. DHT11, DHT22, AM2301, AM2302):
#
#    1=VDD, 2=Data, 3=NC, 4=GND
#
# Pin sequence numbers, left to right, 1 2 3 4, with DHT sensor forward facing
#    _____
#   /_____\  Simplified       | --- | --------- |
#  |       | Front of         | 1   | VDD       |
#  |       | DHT22            | 2   | SDA       |
#  |_______| sensor           | 3   | NULL      |
#  |_______| Aosong, CN       | 4   | GND       |
#   | | | |                   | --- | --------- |
#   1 2 3 4
#
# | --------------------------------------------------------------------------------------------------------- |
# | Raspberry Pi Pico, DHT22, pin map                                                                         |
# | ------- | --------- | ------------- | ------ | ---------------------------------------------------------- |
# | DHT pin | Function  | RPi Pico      | Wire   | Description                                                |
# |         |           | Use,   pin NN |        |                                                            |
# | ------- | --------- | ------------- | ------ | ---------------------------------------------------------- |
# | 1       | VDD       | 3V3,   pin 36 | Red    | power supply, 3.3V - 5.5V                                  |
# | 2       | SDA       | GP2,   pin 04 | Yellow | DATA, signal, any GPIO, with a 10k Ohm pull up resistor    |
# | 3       | NULL      |               |        | NC, Empty, Don't connect                                   |
# | 4       | GND       | GND,   pin 28 | Black  | Ground                                                     |
# | ------- | --------- | ------------- | ------ | ---------------------------------------------------------- |   
#
# SDA = Serial data, bidirectional port,  

# #
# import libraries to use in this programme
from machine import Pin, RTC
from time import sleep
from dht import DHT22 # DHT11, # esp32 driver/module

# #
# The GPIO pin number to read in the sensor measurement readings into the microcontroller
pin = Pin(2, Pin.IN) # GP2

# #
# The sensor takes the GPIO number to recieve commands to execute and return data back to
snr_tsd = DHT22(pin)
# print('snr_tsd {}'.format(snr_tsd)) # debug

# #
# create a Real Time Clock instance, to use to get the current date and time
rtc = RTC()

while True:
    #print('while True: in') # debug
    try:
        #print('try: in') # debug
        
        # #
        # wait for five seconds before next reading
        sleep(5) # five seconds
        #print('sleep(5): done') # debug
        
        # #
        # get the date and time, from the Real Time Clock instance
        dt_tm = rtc.datetime() # get the current date and time
        print('current date & time: {}'.format(dt_tm)) # debug, date and time
        
        # #
        # Read the sensor values
        snr_tsd.measure()
        #print('snr_tsd.measure(): done') # debug
        snr_tsd_tmp = snr_tsd.temperature() # # e.g. 23.6 (°C) celsius
        #print('snr_tsd.temperature(): done'.format(snr_tsd_tmp)) # debug
        snr_tsd_hmd = snr_tsd.humidity() # e.g. 41.3 (% RH) relative humidity
        #print('snr_tsd.humidity(): done'.format(snr_tsd_hmd)) # debug
        
        # #
        # Convert values for output
        tmp_frh = (snr_tsd_tmp * (9/5)) + 32.0 # convert celsius to fahrenheit
        #print('tmp_frh = (snr_tsd_tmp * (9/5)) + 32.0: done'.format(tmp_frh)) # debug
        
        # #
        # Print the meteorological variables
        print('Temperature: {} °C'.format(snr_tsd_tmp) ) # celsius
        print('Temperature: {} °F'.format(tmp_frh) )     # fahrenheit
        print('Humidity: {} %RH'.format(snr_tsd_hmd) )   # relative humidity
        
        # #
        # catch error
    except OSError as e:
        print('OSError. Sensor reading failed. {} '.format(e) )
        
        
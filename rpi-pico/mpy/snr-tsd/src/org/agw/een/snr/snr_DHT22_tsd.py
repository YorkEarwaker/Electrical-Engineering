# Code sources
#
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
# Pin numbers, left to right, 1 2 3 4, with DHT sensor forward facing
# Pin sequence number: 1 2 3 4 (from left to right direction)
# | ------------------------------------------------------------------------------------- | ------ |
# | DHT pin | Function                                                     | RPi Pico pin | Wire   |
# | ------- | ------------------------------------------------------------ | ------------ | ------ |
# | 1       | VDD, power supply, 3.3V - 5.5V                               | 3V3,  pin 36 | Red    |
# | 2       | SDA, DATA, signal, any GPIO, with a 10k Ohm pull up resistor | GP4,  pin 06 | Yellow |
# | 3       | NULL, NC, Empty, Don't connect                               |              |        |
# | 4       | GND, Ground                                                  | GND,  pin 28 | Black  |
# | ---------------------------------------------------------------------- | ------------ | ------ |    
#
# SDA = Serical data, bidirectional port,  


from machine import Pin
from time import sleep
import dht # esp32 driver/module

#pin = Pin(4, Pin.IN)
pin = Pin(4)

# sensor
snr_tsd = dht.DHT22(pin)
#result = snr_tsd.read()

print('snr_tsd {}'.format(snr_tsd))

while True:
    print('while True: in')
    try:
        print('try: in')
        sleep(5) # five seconds
        print('sleep(5): done')
        snr_tsd.measure()
        print('snr_tsd.measure(): done')
        snr_tsd_tmp = snr_tsd.temperature() # # e.g. 23.6 (°C) celsius
        print('snr_tsd.temperature(): done'.format(snr_tsd_tmp))
        snr_tsd_hmd = snr_tsd.humidity() # e.g. 41.3 (% RH) relative humidity
        print('snr_tsd.humidity(): done'.format(snr_tsd_hmd))
        tmp_frh = (snr_tsd_tmp * (9/5)) + 32.0 # convert celsius to fahrenheit
        print('tmp_frh = (snr_tsd_tmp * (9/5)) + 32.0: done'.format(tmp_frh))
        # do print readings
        print('Temperature: {} °C'.format(snr_tsd_tmp) )
        print('Temperature: {} °F'.format(tmp_frh) )
        print('Humidity: {} '.format(snr_tsd_hmd) )
    except OSError as e:
        print('OSError. Sensor reading failed. {} '.format(e) )
        
        
# Time series data tsd (mpy)

MicroPython for sensor snr for time series data tsd for numerical weather prediction nwp, 

For consumption by climate models for example,

## Goals & Objectives

* Complete sensor reading PoC for open source weather station OSWS project, time series data collection, part of autonomous meteorological network \amn subproject in Climate Model repository

## Status

TODO
* <todo: consider, temperature humidity air pressure readings, BME280 PoC, wip, much more complex than the DHT22 PoC,  >
* <todo: consider, Bosch BME180 and BMP085 and BME680 and other environmental sensors from Bosch for Climate Model \amn sub project >
* <todo: consider, Bosch sensor catalogue for concerns things other than environmental, >

DONE
* <done: intent to commit>
* <done: consider, temperature humidity readings, DHT22 PoC >
* <done: consider, RPi Pico, 12C1 bus is prefered over I2C0 internal bus. BME280 PoC, >
* <done: consider, RPi PIco, I2C preferred?/default? over SPI, BM280 PoC, it is easier so most common approach taken >
* <done: consider, can wiring be completed such that a switch / toggle can be made between I2C1 and SPI1? , can this be achieve with Pico? look to pinout,. Likely yes using the default SPI0 GPIO pins G16 G17 G18 G19 physical pins 21 22 24 25, 24 & 25 also acting as SDA and SCL for I2C1 >
* <done: consider, complete diagram, for BME280, but likely won't work for both SPI and I2C >
* ...

## Readings

### DHT22

>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot

current date & time: (2025, 4, 25, 4, 12, 7, 25, 0)
Temperature: 19.3 °C
Temperature: 66.74001 °F
Humidity: 52.5 %RH
current date & time: (2025, 4, 25, 4, 12, 7, 30, 0)
Temperature: 19.3 °C
Temperature: 66.74001 °F
Humidity: 52.6 %RH
current date & time: (2025, 4, 25, 4, 12, 7, 35, 0)
Temperature: 19.3 °C
Temperature: 66.74001 °F
Humidity: 52.6 %RH
current date & time: (2025, 4, 25, 4, 12, 7, 41, 0)
Temperature: 19.3 °C
Temperature: 66.74001 °F
Humidity: 52.5 %RH

### BME280

... to be completed

## References

Terms
* Sensor [WP](https://en.wikipedia.org/wiki/Sensor), device for detecting change in environment, 
* Conversion of scales of temperature, [WP](https://en.wikipedia.org/wiki/Conversion_of_scales_of_temperature)

Documentation
* MicroPython, docs [WS](https://docs.micropython.org/en/latest/index.html#), micropython org
* MicroPython, docs, RP2, [WS](https://docs.micropython.org/en/latest/rp2/quickref.html), micropython org
* MicroPython, docs, ESP32, dht, driver, [WS](https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver), micropython org
* MicroPython, docs, ESP32, Temperature and humidity, [WS](https://docs.micropython.org/en/latest/esp8266/tutorial/dht.html), micropython org
* MicroPython, ESP32, dht, driver, [WS](https://mpython.readthedocs.io/en/v2.2.1/library/micropython/dht.html), class library, readthedocs io, 
* ...

Datasheet
* BME280 sensor, datasheet, [PDF](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf), from Bosch web server, Document revision 1.24, Document release date February 2024, Document number BST-BME280-DS001-24, Sales Part Number (SPN) 0 273 141 185, Bosch Sensortech [WS](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/)
* BME280 sensor, datasheet, [PDF](https://files.waveshare.com/upload/9/91/BME280_datasheet.pdf), from Waveshare file server, Document revision 1.0 Document release date November 11th, 2014 Document number BST-BME280-DS001-09 Technical reference code(s) 0 273 141 185, BME280 sensor, Waveshare, [WS](https://www.waveshare.com/wiki/BME280_Environmental_Sensor), wiki, with some spec stuff of interest and coding help
* BME280 sensor, datasheet, [PDF](https://raw.githubusercontent.com/rm-hull/bme280/master/doc/tech-spec/BME280.pdf), from GitHub web server, Document revision 1.1 Document release date May 07th, 2015 Document number BST-BME280-DS001-10 Technical reference code(s) 0 273 141 185,, PyPi project [WS](https://pypi.org/project/RPi.bme280/) 


Hardware - Bosch 
* BME280 sensor, Waveshare, CN, (temperature, humidity, air pressure), [WS](https://thepihut.com/products/bme280-environmental-sensor), The Pi Hut, appears as though the BME280 chip is a clone manufactured in CN, under licence from Bosch, any delta from Bosch? 
* Bosch Sensortec [WS](https://www.bosch-sensortec.com/), BME280, many others, DE, 
* BME280 driver, Bosch [GH](https://github.com/boschsensortec/BME280_SensorAPI), C/C++
* BME280 driver, PyPi [WS](https://pypi.org/project/RPi.bme280/), home [GH](https://github.com/rm-hull/bme280), Python, RPi.bme280 0.2.4, Richard Hull, linked Bosch datasheet similar to Waveshare, Document revision 1.1 Document release date May 07th, 2015 Document number BST-BME280-DS001-10 Technical reference code(s) 0 273 141 185, 12C four pin only, not Waveshare, 

Hardware - Aosong
* DHT22 sensor, Aosong (AM2302), CN, (temperature, humidity), [WS](https://thepihut.com/products/dht22-temperature-humidity-sensor-extras), The Pi Hut


News Papers - DHT22/DHT11 with RPi Pico 
* DHT11 sensor with Raspberry Pi Pico, [WS](https://forums.raspberrypi.com/viewtopic.php?t=372629), forums, raspberrypi
* Interpreting response for DHT11 on PICO, [WS](https://forums.raspberrypi.com/viewtopic.php?t=339751), forums, raspberrypi, see breadboard *
* Raspberry Pi Pico With DHT22 – MicroPython Tutorial, [WS](https://electrocredible.com/raspberry-pi-pico-dht22-micropython-tutorial/), electrocredible
* [WS](https://randomnerdtutorials.com/raspberry-pi-pico-dht11-dht22-micropython/), ramdomnerdtutorials

News Papers - DHT22/DHT11 with PyCom
* DHT Pure Python library for Pycom board, [WS](https://github.com/JurassicPork/DHT_PyCom), dht class 

News Papers - BME280, Waveshare, RPi
* bme280 sensor not being picked up, [WS](https://forums.raspberrypi.com/viewtopic.php?p=2280887&hilit=bme280+waveshare#p2280887), Forums, Raspberry Pi, 
* bme280 remote i/o error, [WS](https://forums.raspberrypi.com/viewtopic.php?t=348060), Forums, Raspberry Pi, 

News Papers - BME280 with RPi Pico, various BME280 vendors & products, 
* Raspberry Pi Pico: BME280 Get Temperature, Humidity, and Pressure (MicroPython), [WS](https://randomnerdtutorials.com/raspberry-pi-pico-bme280-micropython/), Randomtutorials, 
* BME280 with Raspberry Pi Pico using MicroPython, [WS](https://microcontrollerslab.com/bme280-raspberry-pi-pico-micropython-tutorial/), Microcontrollerslab 
* Raspberry Pi Pico W Wireless BME280 Web Server, [WS](https://microcontrollerslab.com/raspberry-pi-pico-w-wireless-bme280-web-server/), Microcontrollerslab 
* Make Simple Raspberry Pi Pico W Weather Station With BME280 [WS](https://www.electromaker.io/project/view/make-simple-raspberry-pi-pico-w-weather-station-with-bme280), electromaker
* Ardfruit, CircuitPython, BME280, [WS](https://docs.circuitpython.org/projects/bme280/en/latest/)
* Using the BME280 I2C Temperature and Pressure Sensor in Python, [WS](https://www.raspberrypi-spy.co.uk/2016/07/using-bme280-i2c-temperature-pressure-sensor-in-python/), Raspberry Pi Spy, 

News Papers - BME280 with Raspberry Pi, various BME280 vendors & products, 
* Pico with BME280 breakout (via Explorer Base and MicroPython) [WS](https://forums.pimoroni.com/t/pico-with-bme280-breakout-via-explorer-base-and-micropython/16055), pimoroni
* ...

News Papers - BME280 with ESP32
* MicroPython: BME280 with ESP32 and ESP8266 (Pressure, Temperature, Humidity), [WS](https://randomnerdtutorials.com/micropython-bme280-esp32-esp8266/), Randomtutorials, 
* ...
* ...

News Papers - RPi Pico pinout, SPI, I2C, ...
* SPI pins on pico, [WS](https://forums.raspberrypi.com/viewtopic.php?t=301247), Forums, Raspberry Pi, 
* How to use both SPI0 and SPI1? [WS](https://forums.raspberrypi.com/viewtopic.php?t=341966), Forums, Raspberry Pi, C/C++ 
* Pi pico default pi pico pins? [WS](https://forums.raspberrypi.com/viewtopic.php?t=352871), Forums, Raspberry Pi, 
* ...
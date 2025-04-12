# Time series data tsd (mpy)

MicroPython for sensor snr for time series data tsd for numerical weather prediction nwp, 

For consumption by climate models for example,

## Goals & Objectives

* Complete sensor reading PoC for open source weather station OSWS project, time series data collection, part of autonomous meteorological network \amn subproject in Climate Model repository

## Status

TODO
* <todo: consider, temperature humidity readings, DHT22 PoC >
* <todo: consider, temperature humidity air pressure readings, BME280 PoC >

DONE
* <done: intent to commit>

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
* ...

Hardware
* DHT22 sensor, Aosong (AM2302), (temperature, humidity), [WS](https://thepihut.com/products/dht22-temperature-humidity-sensor-extras), The Pi Hut
* BME280 sensor, , (temperature, humidity, air pressure), [WS](https://thepihut.com/products/bme280-environmental-sensor), The Pi Hut

News Papers - DHT22/DHT11 with RPi Pico 
* DHT11 sensor with Raspberry Pi Pico, [WS](https://forums.raspberrypi.com/viewtopic.php?t=372629), forums, raspberrypi
* Interpreting response for DHT11 on PICO, [WS](https://forums.raspberrypi.com/viewtopic.php?t=339751), forums, raspberrypi, see breadboard *
* Raspberry Pi Pico With DHT22 – MicroPython Tutorial, [WS](https://electrocredible.com/raspberry-pi-pico-dht22-micropython-tutorial/), electrocredible
* [WS](https://randomnerdtutorials.com/raspberry-pi-pico-dht11-dht22-micropython/), ramdomnerdtutorials

News Papers - DHT22/DHT11 with PyCom
* DHT Pure Python library for Pycom board, [WS](https://github.com/JurassicPork/DHT_PyCom), dht class 

News Papers - BME280 with RPi Pico
* ...
# Code sources
#
# MicroPython,
# RP2 module, quick reference
# https://docs.micropython.org/en/latest/rp2/quickref.html # module
#
# machine module
# https://docs.micropython.org/en/latest/library/machine.html # module

# machine module, Pin class
# https://docs.micropython.org/en/latest/library/machine.Pin.html # class

# machine module SPI class
# https://docs.micropython.org/en/latest/library/machine.SPI.html # class

# machine module I2C class, i2c.scan(), 
# https://docs.micropython.org/en/latest/library/machine.I2C.html # class
#
# BME280 driver
# Will likely have to write own driver from other examples for the Waveshare BME280 sensor
#
# The Richard Hull, BME280, driver refere to the Raspberry Pi (RPi) pinout not the Rasberry Pi Pico (RPi Pi) pinout,
# R Hull, I2C four pin device only, not six pin I2C/ISP Waveshare
# see RPi pinout below
# Assess R Hull driver for I2C , 
# https://pypi.org/project/RPi.bme280/
#
# RPi Spy, Matt Hawkins, Raspberry Pi, also Pico?
# https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/bme280.py
#
# BME280 sensor, Waveshare, environmental sensor
# https://thepihut.com/products/bme280-environmental-sensor
#
# Conversion of scales of temperature,
# https://en.wikipedia.org/wiki/Conversion_of_scales_of_temperature
#
# References - trouble shooting, tutorials
# https://forums.raspberrypi.com/viewtopic.php?t=381625
#
# RPi Pico 2 W pinout diagram
# https://datasheets.raspberrypi.com/picow/pico-2-w-pinout.pdf
# https://pico.pinout.xyz/
#
# RPi Pi pinout diagram,
# https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio
# https://pinout.xyz/
# https://projects.raspberrypi.org/en/projects/physical-computing/1
# 
# Raspberry Pi kernal overlays, to modify kernal without module changes, <todo: does this also apply to Pico?>
# Configuration file '/boot/config.txt', enable use of SPI1 by line; dtoverlay=spi1-3cs 
# https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/overlays/README
#
# I2C  
# Resistors between, host controller e.g. microcontroller like RPi Pico, target device e.g. sensor like BME280
# Example sensors with no onboard resistors; DHT22, AM2320
# <todo: confirm resistor's onboard Waveshare BME280, >
# https://learn.adafruit.com/working-with-i2c-devices/pull-up-resistors
# 
# How to Scan and Detect I2C Addresses, RPi Pico, Ardfruit lib i2cdetect?
# https://learn.adafruit.com/scanning-i2c-addresses/raspberry-pi
# 
# BME280 datasheet, Waveshare, CN,
# https://www.waveshare.com/wiki/BME280_Environmental_Sensor
# https://www.waveshare.net/wiki/Pioneer600_Datasheets
# https://www.waveshare.net/wiki/RPi_LCD_Datasheets
# Schematic
# https://files.waveshare.com/upload/4/42/BME280-Environmental-Sensor-Schematic.pdf
# Manual, Bosch file?, on Waveshare CN web site,
# https://files.waveshare.com/upload/9/91/BME280_datasheet.pdf
# Related, Bosch datasheet
# https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/
# https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf
# Related, PyPi driver project
# https://raw.githubusercontent.com/rm-hull/bme280/master/doc/tech-spec/BME280.pdf
#
# Pin sequence numbers, left to right, 1 2 3 4, with BME sensor forward facing
#
#   ___________ 
#  |           | Simplified
#  |           | Front of
#  |           | BME280
#  |___________| sensor
#  |___________| Waveshare, CN
#   | | | | | |
#   1 2 3 4 5 6
# 
# | --------------------------------------------------------------------------------------------- |
# | Raspberry Pi Pico, BME280, pin map, I2C1 and SPI0                                             |
# | ------- | --------- | ---- | ------------------ | ------ | ---- | --------_--------- | ------ |
# | BME pin | Function  | I2C  | RPi Pico           | Wire   | SPI  | RPi Pico           | Wire   |
# |         |           |      | Use,  I2C1, pin NN |        |      | Use,  SPI0, pin NN |        |  
# | ------- | --------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
# | 1       | VCC       | VCC  | 3V3,        pin 36 | Red    | VCC  | 3V3,        pin 36 | Red    | 
# | 2       | GND       | GND  | GND,        pin 28 | Black  | GND  | GND,        pin 28 | Black  | 
# | 3       | SDA/MOSI  | SDA  | GP18, SDA,  pin 24 | Yellow | MOSI | GP19, TX,   pin 25 |        | 
# | 4       | SCL/SCK   | SCL  | GP19, SCL,  pin 25 | Blue?  | SCK  | GP18, SCK,  pin 24 |        | 
# | 5       | ADDR/MISO | ADDR |                    |        | MISO | GP16, RX,   pin 21 |        | 
# | 6       | CS        | CS   |                    |        | CS   | GP17, CSn   pin 22 |        | 
# | ------- | --------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
# Candidate wiring and pin allocation, ensure programatically enable pins, don't rely on Pico 'defaults'
# This wiring for programatic switch between I2C and SPI may not be possible
# if I2C requires BME pin 5 and 6 to be NC not connected.
# Also as can be seen from the mapping above mapping issues for BME pin 3 and BME pin 4. For example;
# For I2C; BME pin 3 is I2C SDA maps to GP18 I2C1 SDA pin 24
# For SPI; BME pin 3 is SPI MOSI maps to GP19 SPI0 TX pin 25
#
# Other realted terms on other manufacturer's sensors, 
# MOSI/SDI Serial Data In
# MISO/SDO Serial Data Out
#
# I2C and SPI connection models,
# CS = Logic HIGH for I2C (default), logic LOW for SPI
# 
# | -------------------------------------------------------------------------------------------------------- |
# | I2C interface                                                                                            |
# | --- | --------- | ---------- | ---------- | ---------- | ----------------------------------------------- |
# | BME | Function  | Arduino    | STM32      | Raspberry  | Description                                     |
# | pin | pin       | interface  | interface  | Pi         |                                                 |
# | --- | --------- | ---------- | ---------- | ---------- | ----------------------------------------------- |
# | 1   | VCC       | 3.3V/5V    | 3.3V /5V   | 3.3V /5V   | Power input                                     |
# | 2   | GND       | GND        | GND        | GND        | Ground                                          |
# | 3   | SDA       | A4         | PB7        | SDA        | I2C data line                                   |
# | 4   | SCL       | A5         | PB6        | SCL        | I2C clock line                                  |
# | 5   | ADDR      | NC/GND     | NC/GND     | NC/GND     | Address chip select (default is high):          |
# |     |           |            |            |            | When the voltage is high, the address is 0 x 77 |
# |     |           |            |            |            | When the voltage is low, the address is: 0 x 76 |
# | 6   | CS        | NC         | NC         | NC         | NC                                              |
# | --- | --------- | ---------- | ---------- | ---------- | ----------------------------------------------- |
# 
# | -------------------------------------------------------------------------------------------------------- |
# | SPI interface                                                                                            |
# | --- | --------- | ---------- | ---------- | ---------- | ----------------------------------------------- |
# | BME | Function  | Arduino    | STM32      | Raspberry  | Description                                     |
# | pin | pin       | interface  | interface  | Pi         |                                                 |
# | --- | --------- | ---------- | ---------- | ---------- | ----------------------------------------------- | 
# | 1   | VCC       | 3.3V /5V   | 3.3V /5V   | 3.3V /5V   | 3.3VPower input                                 |
# | 2   | GND       | GND        | GND        | GND        | Ground                                          |
# | 3   | MOSI      | D11        | PA7        | MOSI       | SPI data input                                  |
# | 4   | SCK       | D13        | PA5        | SCK        | SPI clock input                                 |
# | 5   | MISO      | D12        | PA6        | MISO       | SPI data output                                 |
# | 6   | CS        | D10        | PB6        | GP27?      | SPI Chip select, active when voltage is low     |
# | --- | --------- | ---------- | ---------- | ---------- | ----------------------------------------------- |
# 27, GP27 seem's incorrect from Waveshare docs re Rasberry Pi, <todo: validate this >
#
# Inter Intergerated Circuit I2C
# a two-wire serial protocol
# Pico pinout, two I2C controllers, I2C0 and I2C1. Preferred use I2C1.
# Each with several GPIO pins for SDA (Serial Data) and SCL (Serial Clock) signals.
# I2C0 internal I2C bus reserved for GPU, but can be used for general communcation
# if CSI1 and DSI1 interfaces are not used or are controlled by firmware. 
# I2C1 external I2C bus better for connecting sensors or peripherals.
# Not used for internal functions and can be used freely for general communications.
# Raspberry Pi Pico default I2C interface I2C1
# Raspberry Pi Pico default I2C1 pins, GP2 (SDA), GP3 (SCL),
#
# Two pull up resistor required for I2C electrical interface,
# One resistor between SDA and VCC
# One resistor between SCL and VCC
# SDA = DATA, signal, a GPIO I2C SDA, with a 10k Ohm pull up resistor? 
# SCL = Clock, a GPIO I2C SCL, with a 10k Ohm pull up resistor?
# Or resistor's onboard sensor, i.e. BME280,? <todo: confirm resistor's onboard Waveshare BME280>
# 
# | ---------------------------------------------------------------------- |
# | RPi Pico, I2C0 Pinout,                                                 |
# | Default I2C0 Pins: GP4 (SDA), GP5 (SCL)                                |
# | --------- | -------------------------------------- | ----------------- |
# | Function  | RPi Pico GPIO                          | Description       |
# | pin       | <todo: Board pin NN line below GPIO?>  |                   |
# | --------- | -------------------------------------- | ----------------- |
# | SDA       | GP0, GP4, GP8, GP12, GP16, GP20,       | Serial Data       |
# | SCL       | GP1, GP5, GP9, GP13, GP17, GP21,       | Serial Clock      |
# | ---------------------------------------------------------------------- |
#
# | ---------------------------------------------------------------------- |
# | RPi Pico, I2C1 Pinout, default preferred 12C interface                 |
# | Default I2C1 Pins: GP2 (SDA), GP3 (SCL)                                |
# | --------- | -------------------------------------- | ----------------- |
# | Function  | RPi Pico GPIO                          | Description       |
# | pin       |                                        |                   |
# | --------- | -------------------------------------- | ----------------- |
# | SDA       | GP2, GP6, GP10, GP14, GP18, GP26,      | Serial Data       |
# | SCL       | GP3, GP7, GP11, GP15, GP19, GP27,      | Serial Clock      |
# | ---------------------------------------------------------------------- |
#
# Serial Peripheral Interface SPI
# RPi Pico, two SPI controllers, SPI0 and SPI1. 
# Raspberry Pi Pico SPI0 default pins,
# GP19 (MOSI/TX), GP18 (SCK), GP17 (CS) and GP16 (MISO/RX)
# Using SPI1 may require additional manural configuration of onboard files for Raspberry Pi. <todo: check this is the case for Pico too?>
# Raspberry Pi, configure dtoverlay in'/boot/config.txt' to enable SPI1, e.g. dtoverlay=spi1-3cs . 
# 
# | ---------------------------------------------------------------------------- |
# | RPi Pico, SPI0 Pinout, default preferred SPI interface                       |
# | Default SPI0 Pins: GP19 (MOSI/TX), GP18 (SCK), GP17 (CS), GP16 (MISO/RX)     |
# | --------- | -------------------------------------- | ----------------------- |
# | Function  | RPi Pico GPIO                          | Description             |
# | pin       |                                        |                         |
# | --------- | -------------------------------------- | ----------------------- |
# | CLK       | GP2, GP6, GP18,                        | Clock                   |
# | MOSI      | GP3, GP7, GP19,                        | Master Out Slave In     |
# | MISO      | GP0, GP4, GP16,                        | Master In  Slave Out    |
# | CS        | GP1, GP5, GP17,                        | Chip Select             |
# | ---------------------------------------------------------------------------- |
#
# | ---------------------------------------------------------------------------- |
# | RPi Pico, SPI1 Pinout,                                                       |
# | Default SPI1 Pins: ?                                                         |
# | --------- | -------------------------------------- | ----------------------- |
# | Function  | RPi Pico GPIO                          | Description             |
# | pin       |                                        |                         |
# | --------- | -------------------------------------- | ----------------------- |
# | CLK       | GP10, GP14,                            | Clock                   |
# | MOSI      | GP11, GP15,                            | Master Out Slave In     |
# | MISO      | GP8,  GP12,                            | Master In  Slave Out    |
# | CS        | GP9,  GP13,                            | Chip Select             |
# | ---------------------------------------------------------------------------- |
# 

# #
# import libraries to use in this programme
#from bme import BME280 # sensor driver, this to source or more likely have to create code for
from machine import RTC

rtc = RTC()
rtc.datetime() # get the date and time




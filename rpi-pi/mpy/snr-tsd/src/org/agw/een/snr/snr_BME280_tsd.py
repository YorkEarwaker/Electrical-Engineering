# Code sources
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
# | --------------------------------------------------------------------------------- |
# | Raspberry Pi Pico, BME280, pin map, I2C1 and SPI0                                 |
# | ------- | --------- | ---- | ------------ | ------ | ---- | ------------ | ------ |
# | BME pin | Function  | I2C  | RPi Pico pin | Wire   | SPI  | RPi Pico pin | Wire   |
# | ------- | --------- | ---- | ------------ | ------ | ---- | ------------ | ------ |
# | 1       | VCC       | VCC  | 3V3,  pin 36 | Red    | VCC  | 3V3,  pin 36 |        | 
# | 2       | GND       | GND  | GND,  pin 28 | Black  | GND  | GND,  pin 28 |        | 
# | 3       | SDA/MOSI  | SDA  | G19,  pin 25 | Yellow | MOSI | G19,  pin 25 |        | 
# | 4       | SCL/SCK   | SCL  | G18,  pin 24 | Yellow | SCK  | G18,  pin 24 |        | 
# | 5       | ADDR/MISO | ADDR |              |        | MISO | G16,  pin 22 |        | 
# | 6       | CS        | CS   |              |        | CS   | G17   pin 21 |        | 
# | ------- | --------- | ---- | ------------ | ------ | ---- | ------------ | ------ |
# SDA/MOSI? = DATA, signal, any GPIO, with a 10k Ohm pull up resistor? Or resistor's onboard sensor? 
#
# I2C and SPI connection models, 
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
# | 6   | CS        | D10        | PB6        | G27        | SPI Chip select, active when voltage is low     |
# | --- | --------- | ---------- | ---------- | ---------- | ----------------------------------------------- |
# 
# Pico pinout, two I2C controllers, I2C0 and I2C1. <todo: confirm this is true for Pico>
# Each with several GPIO pins for SDA (Serial Data) and SCL (Serial Clock) signals.
# I2C0 internal I2C bus reserved for GPU, but can be used for general communcation
# if CSI1 and DSI1 interfaces are not used or are controlled by firmware. 
# I2C1 external I2C bus better for connecting sensors or peripherals.
# Not used for internal functions and can be used freely for general communications.
# 
# I2C0 Pinout
# SDA (Serial Data) Pins: GP0, GP4, GP8, GP12, GP16, GP20
# SCL (Serial Clock) Pins: GP1, GP5, GP9, GP13, GP17, GP21
# I2C1 Pinout
# SDA (Serial Data) Pins: GP2, GP6, GP10, GP14, GP18, GP26
# SCL (Serial Clock) Pins: GP3, GP7, GP11, GP15, GP19, GP27
# Default I2C Pins
# Default I2C0 Pins: GP4 (SDA) and GP5 (SCL)
# Default I2C1 Pins: GP2 (SDA) and GP3 (SCL)
#
# RPi Pico, two SPI controllers, SPI0 and SPI1. 
# Raspberry Pi Pico SPI0 default pins,
# GPIO19 (MOSI/TX), GPIO18 (SCK), GPIO17 (CS) and GPIO 16 (MISO/RX)
# Using SPI1 may require additional manural configuration of onboard files. <todo: check this is the case>
# 
# SPI0 Pinout
# CLK (Clock): GPIO2, GPIO6, GPIO18
# MOSI (Master Out Slave In): GPIO3, GPIO7, GPIO19
# MISO (Master In Slave In): GPIO0, GPIO4, GPIO16
# CS (Chip Select): GPIO1, GPIO5, GPIO17
# SPI1 Pinout
# CLK (Clock): GPIO10, GPIO14
# MOSI (Master Out Slave In): GPIO11, GPIO15
# MISO (Master In Slave In): GPIO8, GPIO12
# CS (Chip Select): GPIO9, GPIO13
# 

# #
# import libraries to use in this programme
from bme import BME280 # sensor driver, this to source or more likely have to create code for




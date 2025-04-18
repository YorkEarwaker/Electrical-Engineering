# Code sources
#
# BME280 driver
# Will likely have to write own driver from other examples for the Waveshare BME280 sensor
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
#
# RPi Pico 2 W pinout diagram
# https://datasheets.raspberrypi.com/picow/pico-2-w-pinout.pdf
#
# BME280 datasheet, Waveshare, CN, 
# https://www.waveshare.com/wiki/BME280_Environmental_Sensor
# https://www.waveshare.net/wiki/Pioneer600_Datasheets
# Schematic
# https://files.waveshare.com/upload/4/42/BME280-Environmental-Sensor-Schematic.pdf
# Manual, Bosch file?, on Waveshare CN web site,
# https://files.waveshare.com/upload/9/91/BME280_datasheet.pdf
# Related, Bosch datasheet
# https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/
# https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf
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
# | ------- | --------- | ---- | ------------ | ------ | ---- | ------------ | ------ |
# | BME pin | Function  | I2C  | RPi Pico pin | Wire   | SPI  | RPi Pico pin | Wire   |
# | ------- | --------- | ---- | ------------ | ------ | ---- | ------------ | ------ |
# | 1       | VCC       | VCC  | 3V3,  pin 36 | Red    | VCC  |              |        | 
# | 2       | GND       | GND  | GND,  pin 28 | Black  | GND  |              |        | 
# | 3       | SDA/MOSI  | SDA  | GP?,  pin ?? | Yellow | MOSI |              |        | 
# | 4       | SCL/SCK   | SCL  |              |        | SCK  |              |        | 
# | 5       | ADDR/MISO | ADDR |              |        | MISO |              |        | 
# | 6       | CS        | CS   |              |        | CS   |              |        | 
# | ------- | --------- | ---- | ------------ | ------ | ---- | ------------ | ------ |
# SDA/MOSI? = DATA, signal, any GPIO, with a 10k Ohm pull up resistor?
#
# I2C and SPI connection models, I2C preferred?/default?
# 
# | -------------------------------------------------------------------
# | I2C interface
# | --- | --------- | ---------- | ---------- | ---------- | -----------
# | BME | Function  | Arduino    | STM32      | Raspberry  | Describe
# | pin | pin       | interface  | interface  |            |
# | --- | --------- | ---------- | ---------- | ---------- | -----------
# | 1   | VCC       | 3.3V/5V    | 3.3V /5V   | 3.3V /5V   | Power input
# | 2   | GND       | GND        | GND        | GND        | Ground
# | 3   | SDA       | A4         | PB7        | SDA        | I2C data line
# | 4   | SCL       | A5         | PB6        | SCL        | I2C clock line
# | 5   | ADDR      | NC/GND     | NC/GND     | NC/GND     | Address chip select (default is high):
# |     |           |            |            |            | When the voltage is high, the address is 0 x 77
# |     |           |            |            |            | When the voltage is low, the address is: 0 x 76
# | 6   | CS        | NC         | NC         | NC         | NC
# | --- | --------- | ---------- | ---------- | ---------- | -----------
# 
# | -------------------------------------------------------------------
# | SPI interface
# | --- | --------- | ---------- | ---------- | ---------- | -----------
# | BME | Function  | Arduino    | STM32      | Raspberry  | Describe
# | pin | pin       | interface  | interface  |            |
# | --- | --------- | ---------- | ---------- | ---------- | -----------
# | 1   | VCC       | 3.3V /5V   | 3.3V /5V   | 3.3V /5V   | 3.3VPower input
# | 2   | GND       | GND        | GND        | GND        | Ground
# | 3   | MOSI      | D11        | PA7        | MOSI       | SPI data input
# | 4   | SCK       | D13        | PA5        | SCK        | SPI clock input
# | 5   | MISO      | D12        | PA6        | MISO       | SPI data output
# | 6   | CS        | D10        | PB6        | 27         | SPI Chip select, active when voltage is low
# | --- | --------- | ---------- | ---------- | ---------- | -----------
# 
#

# #
# import libraries to use in this programme
from bschsnrtc import BME280 # sensor driver, this to source or more likely have to create code for




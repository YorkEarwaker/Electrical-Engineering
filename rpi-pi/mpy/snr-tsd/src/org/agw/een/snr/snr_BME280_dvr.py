#        _ _   _ _ _      _
#       /   ) / _ _ )  _ \ )
#      / (| |/ /  _ _ \ ) \ \
#     /  _    (  (_  ) \ \ \ \
#    / /  | |\ \ _ )  \_) \_) \
#   (_/   |_| \ _ _ /\ _ _ _ _ )
#   Anthropogenic Global Warming
# --------------------------------
# 
# Code Sources
#
# MicroPython,
# RP2 module, quick reference
# https://docs.micropython.org/en/latest/rp2/quickref.html # module
# 
# machine module
# https://docs.micropython.org/en/latest/library/machine.html # modul# machine module I2C class, i2c.scan(), 
# https://docs.micropython.org/en/latest/library/machine.I2C.html # class
#
# Waveshare CN web site,
# https://files.waveshare.com/upload/9/91/BME280_datasheet.pdf
# Related, Bosch datasheet
# https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/
# https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf
# 
# Tutorials 
# https://randomnerdtutorials.com/raspberry-pi-pico-bme280-micropython/
# https://github.com/RuiSantosdotme/ESP-MicroPython/blob/master/code/WiFi/HTTP_Client_IFTTT_BME280/BME280.py
# https://microcontrollerslab.com/raspberry-pi-pico-w-wireless-bme280-web-server/
#
# Pin sequence numbers, left to right, 1 2 3 4 5 6, with BME sensor forward facing
# 
#   ___________ 
#  |           | Simplified       | --- | --------- |
#  |           | Front of         | 1   | VCC       |
#  |           | BME280           | 2   | GND       |
#  |___________| sensor           | 3   | SDA/MOSI  |
#  |___________| Waveshare, CN    | 4   | SCL/SCK   |
#   | | | | | |                   | 5   | ADDR/MISO |     
#   1 2 3 4 5 6                   | 6   | CS        |
#                                 | --- | --------- | 
# 
# 4.2.2 Trimming parameter readout,
# Bosch Sensortec, BME280 Data sheet
# | ------------------------------------------------------------ |
# | Compensation parameter storage, naming and data type         |
# | -- | ---------------- | ------------------- | -------------- |
# | ID | Register Address | Register content    | Data type      |
# | -- | ---------------- | ------------------- | -------------- |
# | 1  | 0x88 / 0x89      | dig_T1 [7:0]/[15:8] | unsigned short |
# | 2  | 0x8A / 0x8B      | dit_T2 [7:0]/[15:8] | signed short   |
# | 3  | 0x
# | 4  | 0x
# | 5  | 0x
# | 6  | 0x
# | 7  | 0x
# | 8  | 0x
# | 9  | 0x
# | 10 | 0x
# | 11 | 0x
# | 12 | 0x
# | 13 | 0xA1             | dig_H1 [7:0]        | unsigned char  |
# | 14 | 0xE1 / 0xE2      | dig_H2 [7:0]/[15:8] | signed short   |
# | 15 | 0xE3             | dig_H3 [7:0]        | unsigned char  |
# | 16 | 0xE4 / 0xE5[3:0] | dig_H4 [11:4]/[3:0] | signed short   |
# | 17 | 0xE5[7:4] / 0xE6 | dig_H5 [3:0]/[11:4] | signed short   |
# | 18 | 0xE7             | dig_H6              | signed char    |
# | -- | ---------------- | ------------------- | -------------- |



# #
# import libraries to use in this programme
from machine import I2C
import time

# I2C registry address default for BME280
default_bme280_I2C_reg_addr = 0x78

# #
# oversampling modes
# filter modes
# data rates

# Sensor oversampling mode settings for BME280
oversampling_mode_01 = 1
oversampling_mode_02 = 2
oversampling_mode_03 = 4
oversampling_mode_04 = 8
oversampling_mode_05 = 16

# 







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
# 
# I2C Software
# https://docs.micropython.org/en/latest/rp2/quickref.html#software-i2c-bus
# https://docs.micropython.org/en/latest/library/machine.I2C.html#machine-softi2c
#
# I2C Hardware
# https://docs.micropython.org/en/latest/rp2/quickref.html#hardware-i2c-bus
# https://docs.micropython.org/en/latest/library/machine.I2C.html#machine-i2c
#
# Pin
# 
# 
# CircuitPython, Rob J Wells, 
# https://github.com/robjwells/circuitpython-waveshare-1602, has datasheets,
# datasheet, https://github.com/robjwells/circuitpython-waveshare-1602/blob/main/LCD1602_RGB_Module.pdf
#
# Raspberry Pi Pico 2 W, pin out
# https://datasheets.raspberrypi.com/picow/pico-2-w-pinout.pdf
# https://picow.pinout.xyz/
#
# I2C Bus org
# https://www.i2c-bus.org/
# https://www.i2c-bus.org/addressing/
# 
# I2C-bus specification and user manual, NXP Semiconductors,
# https://www.nxp.com/docs/en/user-guide/UM10204.pdf
#
# Hitachi HD44780 controller, is used as basis for operation for LCD1602
# MIT, https://academy.cba.mit.edu/classes/output_devices/44780.pdf # ** seems useful, full datasheet
# datasheet, https://github.com/robjwells/circuitpython-waveshare-1602/blob/main/HD44780.pdf # partial datasheet
# wikipedia, https://en.wikipedia.org/wiki/Hitachi_HD44780_LCD_controller # overview
#
# PCA9633DP2, RGB backlight is driven by NXP PCA9633 chip accessable via I2C
# NXP Semiconductors, https://www.nxp.com/products/power-drivers/lighting-driver-and-controller-ics/led-drivers/4-bit-fm-plus-ic-bus-led-driver:PCA9633
# datasheet, https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf # **seems useful, registry addresses, 
#
# mouser electronics, https://www.mouser.co.uk/ProductDetail/NXP-Semiconductors/PCA9633DP2118?qs=LOCUfHb8d9tlQy5ehY0dtQ%3D%3D
# datasheet, https://www.mouser.co.uk/datasheet/2/302/PCA9633-3139106.pdf
# 
# AIP31068L, LCD controller
# datasheet, https://www.orientdisplay.com/wp-content/uploads/2022/08/AIP31068L.pdf
# 
# similar?/same? https://support.newhavendisplay.com/hc/en-us/articles/4414486901783--AiP31068
# https://support.newhavendisplay.com/hc/en-us/article_attachments/4414498095511
# similar?/same? https://seeeddoc.github.io/Grove-LCD_RGB_Backlight/res/JHD1214Y_YG_1.0.pdf
# 
# Display
# LCD1602 RGB backlight character LCD, Waveshare, 16x2 characters LCD, RGB Backlight, 3.3V/5V, 
# I2C bususing I2C bus to display text or adjust RGB backlight, (Raspberry Pi/Jetson Nano/Arduino examples)
# https://www.waveshare.com/LCD1602-RGB-Module.htm # product page
# https://www.waveshare.com/wiki/LCD1602_RGB_Module # wiki
# https://files.waveshare.com/upload/5/5b/LCD1602-RGB-Module-demo.zip # micropython examples,
# datasheet, https://www.waveshare.com/wiki/File:LCD1602_RGB_Module.pdf
# https://www.waveshare.com/w/upload/2/2e/LCD1602_RGB_Module.pdf
# https://files.waveshare.com/upload/4/4d/LCD1602_I2C_Module.pdf
#
#
# Context diagram
# Assuming only the microcontroller interacts with the device.
#  ____________________________________________  ____________________________________
# |            Electrical Engineering          ||        Internet of Things          | 
#                   In Scope                               Out of Scope
#  ____________________________________________  _________________  _________________
# |                                            ||                 ||                 |
#  Device                  Microcontroller          SomeThing-M^J     SomeThing′-N^K 
#  ______   do x      _________________________    do p     ______    do p′    ______ 
# |      |<----------|      __________Flash__  |<----------|      |<----------|      |
# |      |  get y    |     |    Micro        | |   get q   |      |   get q′  |      |
# |      |<----------|     |  _ Python_____  | |<----------|      |<----------|      |
# |      |  do w     | CPU | |  Drvr Prog  | | |   do r    |      |   do r′   |      |
# |      |<----------| |_|<--|<-|_|<-|_|   | | |---------->|      |---------->|      |
# |      |  get z    |     |_|_____________|_| |   get s   |      |   get s′  |      |
# |______|<----------|_________________________|---------->|______|---------->|______|
#
# A device is any external hardware component wired (integrated) to and programatically controlled by
# the hardware microcontroller. The microcontroller executes programme software which use driver software,
# both of which might be installed on the microcontroller, to issue commands to the device to do something
# or get information the device has saved in the device memory banks. The device driver software is specialist
# software that has been written to communicate specifically with a particular external device.
# The device might do some activity, as a result of a command received from a programme using the device driver
# running on the microcontroller, and save information about the activity to specific address locations
# in the device memory bank registers. The first programme that issued the do activity command, or second programme,
# might then get the information from the memory bank registers of the device and return the information to the
# microcontroller.
# 
# Another thing, hardware or software, might issue commands to the microcontroller to do something
# and get information from the microcontroller memory bank. The internet of things is out of scope
# in this context. But this electrical engineering context A might be used in as part of a larger
# system of systems IoT context B.
# <todo: context text work in progress, last reviewed 01/05/2025, wip>
#
# Display
# Pin sequence numbers, left to right, 1 2 3 4, with circuit board and LCD display forward facing
#
#   _________________________________________
#  |◯   _________________________________ ◯| Simplified       | --- | --------- | Device 
#  |VCC |                                 |  | Front of         | 1   | VCC       | pins functions
#  |GND |                                 |  | LCD              | 2   | GND       |
#  |SCL |                                 |  | Display          | 3   | SCL       |
#  |SDA |_________________________________|  | Waveshre, CN     | 4   | SDA       |
#  |◯_____________________________________◯| Device           | --- | --------- |
# 
# | -------------------------------------------------------------------------------------------------------------- |
# | Raspberry Pi Pico, LCD1602 RGB, pin map                                                                        |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- |
# | LCD pin | Function  | RPi Pico           | Wire   | Description                                                |
# |         |           | Use,  I2C1, pin NN |        |                                                            |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- |
# | 1       | VCC       | 3V3,        pin 36 | Red    | 3.3V ~ 5V power input                                      |
# | 2       | GND       | GND,        pin 38 | Black  | Ground                                                     |
# | 3       | SCL       | GP07, SCL , pin 10 | Blue   | I2C clock pin                                              |
# | 4       | SDA       | GP06, SDA , pin 09 | Yellow | I2C data pin                                               |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- | 
# 
# I2C control interface
# LCD controller AiP31068 
# RGB driver PCA9633
# 
# 
# 
#
# Circuit diagram
# Simplified view of Rpi Pico microntroller and LCD dispaly device circuit
#                   _________________________________________
#                  |◯   _________________________________ ◯| Simplified       | --- | --------- | Device 
#   |--------------|VCC |                                 |  | Front of         | 1   | VCC       | pins functions
#   | |------------|GND |                                 |  | LCD              | 2   | GND       |
#   | | |----------|SCL |                                 |  | Display          | 3   | SCL       |
#   | | | | -------|SDA |_________________________________|  | Waveshre, CN     | 4   | SDA       |
#   | | | |        |◯_____________________________________◯| Device           | --- | --------- |
#   | | | |                                                                      
#   1 2 3 4
#   | | | |                                                
#   |-)-)-)---------------------------------------------------------------|
#     | | |                                                               |
#     |-)-)-------------------------------------------------------------| |
#       | |                                                             | |
#       | |                            RPi Pico 2 W pinout              | |
#       | |                                  _____                      | |
#       | |                            -----|     |-----                | |
#       | |                         1-| o ◯|_____|◯ o |-40            | |
#       | |                         2-| o     USB     o |-39            | |
#       | |                         3-| o             o |-38-----GND----| |
#       | |                         4-| o             o |-37              |
#       | |                         5-| o             o |-36---3V3(OUT)---|    
#       | |                         6-| o  __         o |-35
#       | |                         7-| o |__| Flash  o |-34
#       | |                         8-| o   _______   o |-33
#       | |---I2C1 SDA------GP6-----9-| o  | ARM   |  o |-32
#       |-----I2C1 SCL------GP7----10-| o  | 2035  |  o |-31
#                                  11-| o  |_______|  o |-30
#                                  12-| o             o |-29
#                                  13-| o             o |-28
#                                  14-| o             o |-27
#                                  15-| o             o |-26
#                                  16-| o             o |-25
#                                  17-| o             o |-24
#                                  18-| o             o |-23
#                                  19-| o             o |-22
#                                  20-| o ◯       ◯ o |-21
#                                      -----------------
#
#
# Circuit diagram
# Simplified view of Rpi Pico microntroller and DHT22 device circuit
#    _____
#   /_____\  Simplified       | --- | --------- | Device 
#  |       | Front of         | 1   | VDD       | pins functions
#  |       | DHT22            | 2   | SDA       |
#  |_______| sensor           | 3   | NULL      |
#  |_______| Aosong, CN       | 4   | GND       |
#   | | | |  Device           | --- | --------- |       
#   1 2 3 4
#   | |   |                                                _____ R1 10kΩ (10kOhm) pull up resistor
#   |-)---)-----------------------------------------------|_____|-----|
#     |   |                                                           |
#     |   |---------------------------------------------------------| |
#     |                                                             | |
#     |                            RPi Pico 2 W pinout              | |
#     |                                  _____                      | |
#     |                            -----|     |-----                | |
#     |                         1-| o ◯|_____|◯ o |-40            | |
#     |                         2-| o     USB     o |-39            | |
#     |                         3-| o             o |-38-----GND----| |
#     |---I2C1 SDA------GP2-----4-| o             o |-37              |
#                               5-| o             o |-36---3V3(OUT)---|    
#                               6-| o  __         o |-35
#                               7-| o |__| Flash  o |-34
#                               8-| o   _______   o |-33
#                               9-| o  | ARM   |  o |-32
#                              10-| o  | 2035  |  o |-31
#                              11-| o  |_______|  o |-30
#                              12-| o             o |-29
#                              13-| o             o |-28
#                              14-| o             o |-27
#                              15-| o             o |-26
#                              16-| o             o |-25
#                              17-| o             o |-24
#                              18-| o             o |-23
#                              19-| o             o |-22
#                              20-| o ◯       ◯ o |-21
#                                  -----------------
#


# #
# libraries and classes to use in this program
import dsp_lcd1602_dvr as LCD1602
from machine import Pin, RTC
from time import sleep
from dht import DHT22

# #
# The GPIO pin number to read in the sensor measurement readings into the microcontroller
pin = Pin(2, Pin.IN) # GP2

# #
# The sensor driver takes the GPIO number of the RPi GPIO pin connected to the sensor device SDA pin
# to send commands to the sensor to execute
# and retrieve data measurements back read from the sensor's memory
snr_tsd = DHT22(pin)
# print('snr_tsd {}'.format(snr_tsd)) # debug

# #
# create a Real Time Clock instance, to use to get the current date and time
rtc = RTC()

# #
# Colour values to set the background
# an positive integer number between 0 and 255,
# 0 is no colour i.e. black, 255 is full colour i.e. white,
# when all colour amounts are set to 0 or 255
red_amount   = 64
green_amount = 128
blue_amount  = 64

# create and instance of an lcd display
# <todo: make these arguments variables with meaningful names>
lcd_display = LCD1602.LCD1602(16, 2) 

# set background colour        
lcd_display.setRGB(red_amount, green_amount, blue_amount)

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
        # print('current date & time: {}'.format(dt_tm)) # debug, date and time
        
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
        
        #
        lcd_display.clear()
        
        #
        lcd_display.setCursor(0, 0)

        #
        lcd_display.printout('{} C, {} F'.format(snr_tsd_tmp, tmp_frh))
        
        #
        lcd_display.setCursor(0, 1)
                
        #
        lcd_display.printout('{} %RH'.format(snr_tsd_hmd))
        
        # #
        # Print the meteorological variables
        print('Temperature: {} °C'.format(snr_tsd_tmp) ) # celsius
        print('Temperature: {} °F'.format(tmp_frh) )     # fahrenheit
        print('Humidity: {} %RH'.format(snr_tsd_hmd) )   # relative humidity
        
        # #
        # catch error
    except OSError as e:
        print('OSError. Sensor reading failed. {} '.format(e) )

        







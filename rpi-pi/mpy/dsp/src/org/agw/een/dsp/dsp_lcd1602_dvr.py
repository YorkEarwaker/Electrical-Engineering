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
# Note. This code is based on the code provided by the Waveshare demo code.
#

# #
# import other libraries or classes from libs that will be used in this code
import time
from machine import Pin, I2C

# Device I2C Address
# page 6, https://www.waveshare.com/w/upload/2/2e/LCD1602_RGB_Module.pdf
addr_i2c_lcd   =  (0x7c>>1) # AiP31068L (LCD) Slave Address : 0X7C
addr_i2c_rgb   =  (0xc0>>1) # PCA9633DP2 (RGB) Slave Address: 0XC0

# #
# I2C bus
# define values; clock pin, serial data pin, clock frequency
i2c_bus = 1
i2c_scl_pin = Pin(7) # GP7, I2C1 scl
i2c_sda_pin = Pin(6) # GP6, I2C1 sda
#clock_freq = 400_000 # 400kHz
i2c_clock_freq = 400000 # 400kHz, 1000 = 1KHz

# #
# create an i2c instance of the display
def i2c_inst(bus, scl, sda, freq):
    
    try:
        
        display_i2c = I2C(bus,
                          scl = scl,
                          sda = sda,
                          freq = freq)
        print(f'display_i2c: {display_i2c}'.format(display_i2c) ) # debug
        return display_i2c
        
    except Exception as e:
        print(f'I2C, initialisation exception: {e}'.format(e) )

# create an I2C instance to communicate with the display
display_i2c = i2c_inst(i2c_bus,
                       i2c_scl_pin,
                       i2c_sda_pin,
                       i2c_clock_freq)
# print(f'display_i2c: {display_i2c}'.format(display_i2c) ) # debug

# #
# Register addresses

# colour
reg_addr_red    = 0x04
reg_addr_green  = 0x03
reg_addr_blue   = 0x02
reg_addr_mode1  = 0x00
reg_addr_mode2  = 0x01
reg_addr_output = 0x08

#color define

REG_RED    =     0x04
REG_GREEN  =     0x03
REG_BLUE   =     0x02
REG_MODE1  =     0x00
REG_MODE2  =     0x01
REG_OUTPUT =     0x08
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

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
#
# machine module
# https://docs.micropython.org/en/latest/library/machine.html # module
#
# time module
# https://docs.micropython.org/en/latest/library/time.html # module, MicroPython subset of CPython
# https://docs.python.org/3.5/library/time.html#module-time # module CPython, additional information
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
# Books
# Getting started with, MicroPython on Raspberry Pi Pico, The Official Raspberry Pi Pico Guide
# Chapter 8, Temperature Guage
# Use your Raspberry Pi Pico's built in ADC to convert analogue
# inputs, and also to read its internal temperature sensor
#
# Analogue to digital converter ADC
# Is an internal part of the RPi Pico microcontroller RP2040 CPU and RP2035 CPU.
# ADC resolution, tweleve (12) bits resolution, number of digital bits, 12 bit = 0 -4095, Micorpython converts to 16 bit = 65,535 
# ADC channels, three (3) channels, number of analogue signals it can accept at any one time to convert to digital signal.
# ADC channels, GPIO pins; GP26 ADC0, GP27 ADC1, GP28 ADC3, analogue channels 0, 1, 2, respectively, the three analogue channels, external
# ADC channels, micorcontroller internal; ADC.CORE_TEMP, analogue channel 3, the fourth analogue channel, internal 
#
# Ciruit diagram
# Analogue to digical converter ADC
# Temprature
#
# 
# <todo: finish wiring diagram, >
# <todo: consider removing 12C interface pin information from diagram, distracting? not necessary? >
# <todo: consider removing GND and 3V3(OUT) no external device access PICO power out for interanl analogue temp reading >
#                               | |                           
#                               | |---------------------------------------|
#                               |                                         |
#                               |---------------------------------------| |
#                                                                       | |
#                                      RPi Pico 2 W pinout              | |
#                                            _____                      | |
#                                      -----|     |-----                | |
#                                   1-| o ◯|_____|◯ o |-40            | |
#                                   2-| o     USB     o |-39            | |
#                                   3-| o             o |-38-----GND----| |
#                                   4-| o             o |-37              |
#                                   5-| o             o |-36---3V3(OUT)---|    
#                                   6-| o  __         o |-35-------------ADC_VREF-
#                                   7-| o |__| Flash  o |-34----GP28-------ADC2---
#                                   8-| o   _______   o |-33----GND--------AGND---
#                                   9-| o  | ARM   |  o |-32----GP27-------ADC1-----I2C1 SCL--
#                                  10-| o  | 2035  |  o |-31----GP26-------ADC0-----I2C1 SDA--
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

# #
# import libraries for use in this programme
import machine
import time

# #
# device, PICO internal temperature sensor
sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)

# #
# conversion parameter, max voltage (3.3) times (*) the max value analogue input reading can be (65535)
conversion_factor =  3.3 / (65535)

while True:
    
    # sleep for five seconds
    time.sleep(5)
    
    # read data as raw value from temperature sensor
    raw_reading = sensor_temp.read_u16()
    
    # convert raw reading from alanog to digital value, also decimal value 
    converted_raw_reading = raw_reading * conversion_factor
    
    # temperature as centigrade
    temperature = 27 - (converted_raw_reading - 0.706) / 0.001721
    
    # print the values to the console / shell
    print(f"PICO CPU temperature: {temperature}, converted raw reading: {converted_raw_reading}, raw reading: {raw_reading} . "
       .format(temperature, converted_raw_reading, raw_reading))
    
    # write the temperature value to file
    # <todo: write to file, but only to sdc not to PICO flash, so dependency of sdc code, noted 23/06/2025 >







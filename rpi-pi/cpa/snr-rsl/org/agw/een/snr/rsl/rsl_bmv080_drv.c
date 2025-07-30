/#

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
# C/C++
# 
# 
# Raspberry Pi Pico, pinout
# Note. It may not be possible to interact with BMV080 via RPi Pico, TBC
# RPi Pi 2, [PDF](https://datasheets.raspberrypi.com/picow/pico-2-w-pinout.pdf)
# RPi Pi 2, [WS](https://pico2.pinout.xyz/)
# RPi Pi 1, [WS](https://picow.pinout.xyz/)
# 
# Raspberry Pi Pico, datasheets
# Raspberry Pi Pico 2 Datasheet, [PDF](https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf) # An Rp2350-based microcontroller board
# RP2350 Datasheet, [PDF](https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf) # A microcontroller by Raspberry Pi
# 
# Bosch Sensor
# BMV080, particulate matter sensor, https://www.bosch-sensortec.com/products/environmental-sensors/particulate-matter-sensor/bmv080/
#
# Bosch SDK
# Download SDK for BMV080, [WS](https://www.bosch-sensortec.com/software-tools/double-opt-in-forms/sdk-v11-0-0.html) # online request form, 
# BMV080 Sensor Driver Binary Size Information, SDK v11.2.0, [PDF](https://www.bosch-sensortec.com/media/boschsensortec/software_tools/software/bmv080_1/supported_platforms/bmv080_binary_size_information.pdf)
#
# Bosch Datasheets
# BMV080 Ultra-mini Particulate Matter Sensor – Datasheet, Document revision 1.3, Document release date May 2025, Document number BST-BMV080-DS000-11, Sales part number(s) 0273.017.054-1NV
# BMV080 Ultra-mini Particulate Matter Sensor - Datasheet, BST-BMV080-DS000, [PDF](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmv080-ds000.pdf)
# BMV080 Ultra-mini Particulate Matter Sensor – Integration Guideline, Document revision 1.3, Document release date May 2025, Document number BST-BMV080-AN000-03, Sales part number 0273.017.054-1NV
# BMV080 Ultra-mini Particulate Matter Sensor – Integration Guideline, BST-BMV080-AN000-03, [PDF](https://www.bosch-sensortec.com/media/boschsensortec/downloads/handling_soldering_mounting_instructions/bst-bmv080-hs000.pdf)
#
# Sparkfun Breakout board, product purchase
# PiHut, https://thepihut.com/products/sparkfun-air-quality-pm1-pm2-5-pm10-sensor-bmv080-qwiic
# Sparkfun, 
#
# Sparkfun SDK
# Toolkit of common functionality for use within SparkFun Libraries 
# SparkFun_Toolkit, [GH](https://github.com/sparkfun/SparkFun_Toolkit/tree/main) # GitHub
# Arduino Library to support the Bosch BMV080 Particulate Matter Air Quality Sensor PM2.5 via I2C and SPI. 
# SparkFun_BMV080_Arduino_Library, [GH](https://github.com/sparkfun/SparkFun_BMV080_Arduino_Library/tree/main) # GitHub
# 
# Sparkfun Datasheets
# 
# 
# 
# I2C
# Inter-Integrated Circuit (I2C) [WS](https://leanpub.com/rpitandt/read#leanpub-auto-inter-integrated-circuit-i2c)
#
# Probably not in first instance be able to use MicroPython, Sparkfun and Bosch example code in C/C++
# Use these files to some initial cicuit design images and collect some links to relevant sources
# 
# Context diagram
# Assuming only the microcontroller interacts with the device.
#  ____________________________________________  ____________________________________
# |            Electrical Engineering          ||        Internet of Things          | 
#                   In Scope                               Out of Scope
#  ____________________________________________  _________________  _________________
# |                                            ||                 ||                 |
#  Device                  Microcontroller          SomeThing-M^J     SomeThing′-N^K 


# |      |  get z    |     |_|_____________|_| |   get s   |      |   get s′  |      |
# |______|<----------|_________________________|---------->|______|---------->|______|
#



# 
# Sensor
# 
# 
# 
# Sunspark BMV080 breakout board
# 
# 
# 
# Cicuit diagram
# RPi Pico and Sunspark BMV080 breakout board
# 
#
#
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
#       | |                         9-| o  | ARM   |  o |-32
#       | |                        10-| o  | 2035  |  o |-31
#       | |---I2C0 SDA------GP8----11-| o  |_______|  o |-30
#       |-----I2C0 SCL------GP9----12-| o             o |-29
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

# For I2C, the recommended baudrate is 400kHz, for BMV080 sensor over I2C, 
#/
/*
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
# C reference, https://en.cppreference.com/w/c.html
# Cpp reference, https://en.cppreference.com/index.html
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

# Bosch Sensortec | BMV080 Ultra-mini Particulate Matter Sensor – Datasheet 3 | 53, : revision 1.3, BST-BMV080-DS000-11, accessed 2025-08-01
# Table 1: PM2.5 specific AQI and cautionary statements defined by the EPA
# | ----------------- | ------------------ | -------------------------------------------------------------------------------- |
# | PM2.5             | Air quality index  | Air quality index description                                                    |
# | breakpoints       | (AQI) category     |                                                                                  |
# | (μg/m³, 24-hour   |                    |                                                                                  |
# | average)          |                    |                                                                                  |
# | ----------------- | ------------------ | -------------------------------------------------------------------------------- |
# | 0.0 – 12.0        | Good               | Air quality is satisfactory, and air pollution poses little or no risk.          |
# | 12.1 – 35.4       | Moderate           | Air quality is acceptable. However, there may be a risk for some pople,          |
# |                   |                    | particularly those who are unusually sensitive to air pollution.                 |
# | 35.5 – 55.4       | Unhealthy for      | Members of sensitive groups may experience health effects. The general           |
# |                   | sensitive groups   | public is less likely to be affected.                                            |
# | 55.5 – 150.4      | Unhealthy          | Some members of the general public may experience health effects;                |
# |                   |                    | members of sensitive groups may experience more serious health effects.          |
# | 150.5 – 250.4     | Very unhealthy     | Health alert: the risk of health effects is increased for everyone.              |
# | > 250.4           | Hazardous          | Health warnings of emergency conditions: everyone is more likely to be affected. |
# | ----------------- | ------------------ | -------------------------------------------------------------------------------- |


# 
# Sensor - simplified diagram
# BMV080 laser based optical technology
# Measure particulate matter mass concentration based on particle counts and relative partical velocity in space.
# Natural ambient air flow in the proximity of the sensor is used for measurement. So device funtions fan free.
# Simplified top view of BMV080; ZIF, PCB, Passives, Lens & laser
#      
#       ZIF                 Flex              Passives    Lens &
#                           PCB                           laser
#   ____||_____--------------------------------------------------
#  |                |    |--------| (___)   |      , ,   |     | |    
#  |                |    |        |         | =#-  # #   |-----| |
#  |                |    |        |         | =#- ,","   | (@)-| |
#  |                |    |        |         |     # #    |-----| |
#  |___________     |(_) |--------|         |     " "    |     | |
#       ||     --------------------------------------------------
# 
# 
# Sensor - pinout
# <todo: complete simplified ZIF pinout for sensor, here?>
#
#    | 
#    \____________________
#     |  [] [] [] []
#     |  [] [] [] []
#  ___|  [] /\ [] /\
# |      []|  |[]|  |
# |___   []|  |[]|  |
#     |  /\ \//  \\/
#     | |  |[]|  |[]
#     | |  |[]|  |[]
#     |  \/ [] \/ []
#     \---------------
#        |  |
#       13  |
#          12
#
# I2C Addresses
# https://docs.sparkfun.com/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080/assets/board_files/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080_v10_Schematic.pdf
# Takes the form of a material conditional truth table, logic gate, binary algebra, 
#  ____________________________________
# | AB1 | AB0 | I2C Address            |
# |------------------------------------|
# |  0  |  0  | 0x54                   |
# |  0  |  1  | 0x55                   |
# |  1  |  0  | 0x56                   |
# |  1  |  1  | 0x57 (default)         |
# |------------------------------------|
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
*/


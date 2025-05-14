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
#
# Raspberry Pi Pico 2 W, pin out
# https://datasheets.raspberrypi.com/picow/pico-2-w-pinout.pdf
# https://picow.pinout.xyz/
#
# 
# Display
# LCD1602 RGB backlight character LCD, Waveshare, 16x2 characters LCD, RGB Backlight, 3.3V/5V, 
# I2C bususing I2C bus to display text or adjust RGB backlight, (Raspberry Pi/Jetson Nano/Arduino examples)
# https://www.waveshare.com/LCD1602-RGB-Module.htm # product page
# https://www.waveshare.com/wiki/LCD1602_RGB_Module # wiki
# https://files.waveshare.com/upload/5/5b/LCD1602-RGB-Module-demo.zip # micropython examples,
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


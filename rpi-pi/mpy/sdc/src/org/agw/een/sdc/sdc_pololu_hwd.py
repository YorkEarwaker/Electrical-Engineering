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
# machine module
# https://docs.micropython.org/en/latest/library/machine.html # module
#
# machine module, Pin class
# https://docs.micropython.org/en/latest/library/machine.Pin.html # class
#
# machine module SPI class
# https://docs.micropython.org/en/latest/library/machine.SPI.html # class
#
#
# Raspberry Pi Pico 2 W, pin out
# https://datasheets.raspberrypi.com/picow/pico-2-w-pinout.pdf
# https://picow.pinout.xyz/
#
# 
# SD Card
# Pololu Breakout Board for MicroSD Cards, Not v3.3 logic shifted for use in v5 systems integration, 
# product, https://www.pololu.com/product/2597),
# schematic, https://www.pololu.com/file/0J808/breakout-board-for-microsd-card-schematic.pdf
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
# Micro SD Card circuit board
# Pin sequence numbers, left to right, 1 2 3 4 5 6 7 8 9 10 11, with circuit board and SD Card holder (SPI 'CRUD') forward facing
#            ________ 
#           |        |  Micro SD Card
#           |        |  Storage
#           <        |  e.g. 32GB
#            |       |  SD Card.s use V3.3
#            |_______|
#                     
#      -------------------
#   1-|o|---__________--|o|-5  Simplified       | --- | ----------- | Device            | --- | ----------- | Device                                                                   
#   2-|o|| |  ________  |o|-6  Front of         | 1   | GND (VSS)   | pins functions    | 5   | GND (VSS)   | pins functions    
#   3-|o|| | |___||___| |o|-7  Micro SD Card    | 2   | VDD         |                   | 6   | VDD         |                   
#   4-|o||_|            |o|-8  Holder           | 3   | DAT2        |                   | 7   | DI          |                   
#     | |    | |    | | |o|-9  SPI 'CRUD'       | 4   | IRQ/DAT1    |                   | 8   | DO          |                   
#     | |    | |    | | |o|-10 Pololu, ??       | --- | ----------- |                   | 9   | SCLK        |                   
#     | |____|_|____|_|_|o|-11 Board                                                    | 10  | CS (Chip S) |
#      -------------------                                                              | 11  | CD (Card D) |
#                                                                                       | --- | ----------- |
# 
# | ----------------------------------------------------------------------------------------------- |
# | Raspberry Pi Pico, Pololu (POL), pin map, ISP0 and SDIO - wip                                   |
# | ------- | ----------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
# | POL pin | Function    | SPI  | RPi Pico           | Wire   | SDIO | RPi Pico           | Wire   |
# |         |             |      | Use,  SPI0, pin NN |        |      | Use,  SD,   pin NN |        |  
# | ------- | ----------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
# | 1       | GND (VSS)   | GND  |                    |        | GND  | GND,        pin ?? |        | 
# | 2       | VDD         | VDD  |                    |        | VDD  | 3V3,        pin ?? |        | 
# | 3       | DAT2        |      |                    |        |      | GP??, ??,   pin ?? |        | 
# | 4       | IRQ/DAT1    |      |                    |        |      | GP??, ?? ,  pin ?? |        | 
# | 5       | GND (VSS)   | GND  | GND,        pin 38 | Black  | GND  | GND,        pin 38 | Black  | 
# | 6       | VDD         | VDD  | 3V3,        pin 36 | Red    | VDD  | 3V3,        pin 36 | Red    |
# | 7       | DI          |      | GP??, ???,  pin ?? | Yellow |      | GP??, ???,  pin ?? |        |
# | 8       | DO          |      | GP??, ???,  pin ?? |        |      | GP??, ???,  pin ?? |        |
# | 9       | SCLK        |      | GP??, ???,  pin ?? |        |      | GP??, ???,  pin ?? |        |
# | 10      | CS (Chip S) |      | GP??, ???,  pin ?? |        |      | GP??, ???,  pin ?? |        |
# | 11      | CD (Card D) |      |                    |        |      | GP??, ???,  pin ?? |        | 
# | ------- | ----------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
#
# 
# | -------------------------------------------------------------------------------------------------------------- |
# | SPI interface - wip                                                                                            |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- |
# | POL pin | Function  | RPi Pico           | Wire   | Description                                                |
# |         |           | Use,  SPI0, pin NN |        |                                                            |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- |
# | 5       | GND (VSS) | GND,        pin 38 | Black  | Ground                                                     |
# | 6       | VDD       | 3V3,        pin 36 | Red    | 3.3V power input                                           |
# | 7       | DI        | GP??,     , pin    |        |                                                            |
# | 8       | DO        | GP??,     , pin    |        |                                                            |
# | 9       | SCLK      | GP??,     , pin    |        |                                                            |
# | 10      | CS        | GP??,     , pin    |        |                                                            |
# | 11      | CD        | GP??,     , pin    |        | Null?                                                      |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- | 
#
# | -------------------------------------------------------------------------------------------------------------- |
# | SD  interface - wip                                                                                            |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- |
# | POL pin | Function  | RPi Pico           | Wire   | Description                                                |
# |         |           | Use,  SDIO, pin NN |        |                                                            |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- |
# 
# -------------------- WIP
# https://www.pololu.com/product/2597, retrieved 14/05/2025, 15:34, UK BST,
# 
# The following tables describe the function of each pin on the breakout board in SPI and SD mode:
# 
# Pin	Description
# GND (VSS)	Power and logic ground
# VDD	Supply voltage (2.7 V to 3.6 V for standard microSD cards)
# CD	Card detect. When a card is inserted, this pin is floating; when no card is inserted, it is shorted to ground. A pull-up resistor can be used to pull the line high when a card is present.
# SPI mode	SD mode
# Pin	Description	Pin	Description
# DI	Data in (MOSI)	CMD	Command/response
# DO	Data out (MISO)	DAT0	Data (bit 0)
# SCLK	Clock	CLK	Clock
# CS	Chip select (active low)	DAT3	Data (bit 3)
# —
# IRQ	Reserved
# Interrupt (active low; SDIO devices only)	DAT1
# IRQ	Data (bit 1)
# Interrupt (active low; SDIO devices only)
# —	Reserved	DAT2	Data (bit 2)
# Warning: Standard microSD cards use 3.3 V logic level signals, so level shifters or voltage dividers are required when connecting one to a 5 V system.
# 
# 
# 
#
# Circuit diagram - work in progress
# Simplified view of Rpi Pico microntroller and micro SD Card breakout board (device) circuit
# Pin sequence numbers, left to right, 1 2 3 4 5 6 7 8 9 10 11, with circuit board and SD Card holder (SPI 'CRUD') forward facing
# <todo: determine if Pololu device can be wired to Pico for dual use, SPI and SDIO, using same pinout but different mpy code pin allocation?>
#            ________ 
#           |        |  Micro SD Card
#           |        |  Storage
#           <        |  e.g. 32GB
#            |       |  SD Card's use V3.3
#            |_______|
#                     
#      -------------------
#   1-|o|---__________--|o|-5  Simplified       | --- | ----------- | Device            | --- | ----------- | Device                                                                   
#   2-|o|| |  ________  |o|-6  Front of         | 1   | GND (VSS)   | pins functions    | 5   | GND (VSS)   | pins functions    
#   3-|o|| | |___||___| |o|-7  Micro SD Card    | 2   | VDD         |                   | 6   | VDD         |                   
#   4-|o||_|            |o|-8  Holder           | 3   | DAT2        |                   | 7   | DI          |                   
#     | |    | |    | | |o|-9  SPI 'CRUD'       | 4   | IRQ/DAT1    |                   | 8   | DO          |                   
#     | |    | |    | | |o|-10 Pololu, ??       | --- | ----------- |                   | 9   | SCLK        |                   
#     | |____|_|____|_|_|o|-11 Board                                                    | 10  | CS (Chip S) |
#      -------------------                                                              | 11  | CD (Card D) |
#                                                                                       | --- | ----------- |
#   | | | |                     | | | | |  |  |                                                             
#   1 2 3 4                     5 6 7 8 9 10 11
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
#                                   6-| o  __         o |-35
#                                   7-| o |__| Flash  o |-34
#                                   8-| o   _______   o |-33
#                                   9-| o  | ARM   |  o |-32
#                                  10-| o  | 2035  |  o |-31
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


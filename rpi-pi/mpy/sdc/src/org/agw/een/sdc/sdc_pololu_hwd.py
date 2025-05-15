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
# Serial Periferal Interface SPI
# https://en.wikipedia.org/wiki/Serial_Peripheral_Interface
#
# Secure Digital Interface
# https://en.wikipedia.org/wiki/SD_card
#
# Secure Digital Input Output
# https://en.wikipedia.org/wiki/SD_card#SDIO_cards
# https://www.tech-faq.com/sdio.html
# 
# SD Card board
# Pololu Breakout Board for MicroSD Cards, Not v3.3 logic shifted for use in v5 systems integration, 
# product, https://www.pololu.com/product/2597),
# schematic, https://www.pololu.com/file/0J808/breakout-board-for-microsd-card-schematic.pdf
#
# SD Card pinout, SD card, micro SD card
# https://pinoutguide.com/Memory/sdcard_pinout.shtml
# https://allpinouts.org/pinouts/connectors/memory/secure-digital-sd-card/
# https://www.electroniccircuitsdesign.com/pinout/sd-microsd-card-pinout.html
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
# 
# | ----------------------------------------------------------------------------------------------- |
# | Raspberry Pi Pico, Pololu (POL), pin map, ISP and SDIO - wip                                    |
# | ------- | ----------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
# | POL pin | Function    | SPI  | RPi Pico           | Wire   | SDIO | RPi Pico           | Wire   |
# |         |             |      | Use,  SPI1, pin NN |        |      | Use,  SD,   pin NN |        |  
# | ------- | ----------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
# | 1       | GND (VSS)   | —    | Null?              | NC?    | GND  | GND,        pin 38 |        | 
# | 2       | VDD         | —    | Null?              | NC?    | VDD  | 3V3,        pin 36 |        | 
# | 3       | DAT2        | —    | Null               | NC     | DAT2 | GP??, ??,   pin ?? |        | 
# | 4       | IRQ/DAT1    | —    | Null               | NC     | DAT1 | GP??, ?? ,  pin ?? |        | 
# | 5       | GND (VSS)   | —    | GND,        pin 38 | Black  | GND  | GND,        pin 38 | Black  | 
# | 6       | VDD         | —    | 3V3,        pin 36 | Red    | VDD  | 3V3,        pin 36 | Red    |
# | 7       | DI          | MOSI | GP11, TX,   pin 15 | Yellow | CMD  | GP??, ???,  pin ?? |        |
# | 8       | DO          | MISO | GP12, RX,   pin 16 |        | DAT0 | GP??, ???,  pin ?? |        |
# | 9       | SCLK        | SCLK | GP10, SCK,  pin 14 |        | CLK  | GP??, ???,  pin ?? |        |
# | 10      | CS (Chip S) | SS   | GP13, CSn,  pin 17 |        | DAT3 | GP??, ???,  pin ?? |        |
# | 11      | CD (Card D) | —    | Null?              | NC?    | CD   | GP??, ???,  pin ?? |        | 
# | ------- | ----------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
# <todo: consider, if not using SD mode, assume POL pin's 1 and 2, GND (VSS) and VDD respectively,
#        are not wired in SPI mode? >
# <todo: consider, if using SD mode, assume POL pin's 1 and 2, GND (VSS) and VDD respectively,
#        are wired in SD mode to RPi Pico GND pin 38 and 3V3 pin 36 respectively? >
# 
# | -------------------------------------------------------------------------------------------------------------- |
# | SPI interface - wip                                                                                            |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- |
# | POL pin | Function  | RPi Pico           | Wire   | Description                                                |
# |         |           | Use,  SPI1, pin NN |        |                                                            |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- |
# | 5       | GND (VSS) | GND,        pin 38 | Black  | Ground                                                     |
# | 6       | VDD       | 3V3,        pin 36 | Red    | 3.3V power input                                           |
# | 7       | DI        | GP11, TX,   pin 15 |        | Data in, MOSI, Host transmist TX, serial data from RPi Pi  |
# | 8       | DO        | GP12, RX,   pin 16 |        | Data out, MISO, Host recieve RX, serial data from device   |
# | 9       | SCLK      | GP10, SCK,  pin 14 |        | Clock, clock signal from RPi Pi                            |
# | 10      | CS        | GP13, CSn,  pin 17 |        | Chip select (active low)                                   |
# | 11      | CD        | NULL?              | NC?    | Card detect <todo: remove this line?                       |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- | 
#
# | -------------------------------------------------------------------------------------------------------------- |
# | SD interface - wip                                                                                             |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- |
# | POL pin | Function  | RPi Pico           | Wire   | Description                                                |
# |         |           | Use,  SDIO, pin NN |        |                                                            |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- |
# | 1       | VSS?      | GP??, ????, pin ?? |        |                                                            |
# | 2       | VDD       | GP??, ????, pin ?? |        |                                                            |
# | 3       | DAT2      | GP??, ????, pin ?? |        |                                                            |
# | 4       | DAT1      | GP??, ????, pin ?? |        |                                                            |
# | 5       | VSS?      | GP??, ????, pin ?? |        |                                                            |
# | 6       | VDD       | GP??, ????, pin ?? |        |                                                            |
# | 7       | CMD       | GP??, ????, pin ?? |        |                                                            |
# | 8       | DAT0      | GP??, ????, pin ?? |        |                                                            |
# | 9       | CLK       | GP??, ????, pin ?? |        |                                                            |
# | 10      | DAT3      | GP??, ????, pin ?? |        |                                                            |
# | 11      | CD        | GP??, ????, pin ?? |        | Card detect                                                |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- | 
# 
# 
# https://www.pololu.com/product/2597, retrieved 14/05/2025, 15:34, UK BST,
# The following tables describe the function of each pin on the breakout board in SPI and SD mode:
# | -------------------------------------------------------------------------------------------------------------- |
# | Pololu (POL) pin out                                                                                           |
# | ------- | --------- | ---------------------------------------------------------------------------------------- |
# | POL Pin | Function  | Description                                                                              |
# | ------- | --------- | ---------------------------------------------------------------------------------------- |
# | 1, 5    | GND (VSS) | Power and logic ground                                                                   |
# | 2, 6    | VDD       | Supply voltage (2.7 V to 3.6 V for standard microSD cards)                               |
# | 11      | CD        | Card detect. When a card is inserted, this pin is floating; when no card is inserted,    |
# |         |           | it is shorted to ground. A pull-up resistor can be used to pull the line high when       |
# |         |           | a card is present.                                                                       |
# | ------------------------------------------------------ | ----------------------------------------------------- |
# |                        SPI Mode                        |                        SD Mode                        |
# | ------- | --------- | -------------------------------- | ------- | --------- | ------------------------------- |
# | POL Pin | Function  | Description                      | POL Pin | Function  | Description                     |
# | ------- | --------- | -------------------------------- | ------- | --------- | ------------------------------- |
# | 7       | DI        | Data in (MOSI)                   | 7       | CMD       | Command/response                |
# | 8       | DO        | Data out (MISO)                  | 8       | DAT0      | Data (bit 0)                    |
# | 9       | SCLK      | Clock                            | 9       | CLK       | Clock                           |
# | 10      | CS        | Chip select (active low)         | 10      | DAT3      | Data (bit 3)                    |
# | 4       | —         | Reserved                         | 4       | DAT1      | Data (bit 1)                    |
# | 4       | IRQ       | Interrupt (active low;           | 4       | IRQ       | Interrupt (active low; SDIO     |
# |         |           |            SDIO devices only)    |         |           |            SDIO devices only)   |
# | 3       | —         | Reserved                         | 3       | DAT2      | Data (bit 2)                    |
# | ------- | --------- | -------------------------------- | ------- | --------- | ------------------------------- |
#  Warning: Standard microSD cards use 3.3 V logic level signals, so level shifters or voltage dividers
#           are required when connecting one to a 5 V system.
# 
# SD Card nine (9) pin pinout, micro sd card eight (8) pin pinout - wip
# <todo: micro SD card 'pin out' map to SPI>
# <todo: micro SD card 'pin out' map to SD interface >
# <todo: micro SD card 'pin out' map to Pololu SD Card 'reader' board device >
#
# SD Card pinout
#
#     9  1  2  3  4  5  6 7 8
#     ________________________
#    /  [ ][ ][ ][ ][ ][ ][][]|        Pin  SD      SPI
#   /[ ][ ][ ][ ][ ][ ][ ][][]|        1    CD/DAT3 CS
#   |[ ][ ][ ][ ][ ][ ][ ][][]|        2    CMD     DI
#   |[ ]                      |        3    VSS1    VSS1
#   |                         |        4    VDD     VDD
#   |                         |        5    CLK     SCLK
#   |           SD           _|        6    VSS2    VSS2
#   |                      _/          7    DAT0    DO
#   |                    _/            8    DAT1    —
#   |                  _/              9    DAT2    —
#   |                _/
#    ^-^-^-^-^-^-^-^
#
#  Micro SD Card pinout
#
#    1 2 3 4 5 6 7 8
#    ________________
#   |[][][][][][][][]|        Pin  SD      SPI
#   |[][][][][][][][]|        1    DAT2    —
#   |[][][][][][][][]|        2    CD/DAT3 CS
#   |                |        3    CMD     DI
#   |                |        4    VDD     VDD
#  /      micro      |        5    CLK     SCLK
#  --      SD        |        6    VSS     VSS
#  /                 |        7    DAT0    DO
#  |                 |        8    DAT1    —
#  |_________________|
#
# Circuit diagram - work in progress
# Simplified view of Rpi Pico microntroller and micro SD Card breakout board (device) circuit
# Pin sequence numbers, left to right, 1 2 3 4 5 6 7 8 9 10 11, with circuit board and SD Card 'reader' (SPI 'CRUD') forward facing
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
#   4-|o||_|            |o|-8  Reader           | 3   | DAT2        |                   | 7   | DI          |                   
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


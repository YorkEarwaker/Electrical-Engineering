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
# machine module SDCard class – secure digital memory card
# https://docs.micropython.org/en/latest/library/machine.SDCard.html
#
# machine module Timer
# https://docs.micropython.org/en/latest/library/machine.Timer.html
#
# vfs – virtual filesystem control
# https://docs.micropython.org/en/latest/library/vfs.html
#
# os/uos
# https://docs.micropython.org/en/latest/library/os.html
# https://docs.micropython.org/en/v1.15/library/uos.html
# https://docs.python.org/3/library/os.html
# https://docs.python.org/3/library/functions.html#open # modes,
# https://docs.python.org/3/tutorial/inputoutput.html#tut-files
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#
# RPi, Quick reference for the RP2
# https://docs.micropython.org/en/latest/rp2/quickref.html
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
# SD Card specifications
# SD Simplified Specifications, https://www.sdcard.org/downloads/pls/
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
# Micro SD Card 'reader' circuit board
# Pin sequence numbers, left to right, 1 2 3 4 5 6 7 8 9 10 11, with circuit board and SD Card 'reader' (SPI 'CRUD') forward facing
#            _________
#           |         |  Micro SD Card
#           |         |  Storage
#           <         |  e.g. 32GB
#            |        |  SD Card's use V3.3
#            |________|
#                     
#      -------------------
#   1-|o|---__________--|o|-5  Simplified       | --- | ----------- | Device            | --- | ----------- | Device                                                                   
#   2-|o|| |  ________  |o|-6  Front of         | 1   | GND (VSS)   | pin function      | 5   | GND (VSS)   | pin function    
#   3-|o|| | |___||___| |o|-7  Micro SD Card    | 2   | VDD         |                   | 6   | VDD         |                   
#   4-|o||_|            |o|-8  Reader           | 3   | DAT2        |                   | 7   | DI          |                   
#     | |    | |    | | |o|-9  SPI 'CRUD'       | 4   | IRQ/DAT1    |                   | 8   | DO          |                   
#     | |    | |    | | |o|-10 Pololu, ??       | --- | ----------- |                   | 9   | SCLK        |                   
#     | |____|_|____|_|_|o|-11 Board                                                    | 10  | CS (Chip S) |
#      -------------------                                                              | 11  | CD (Card D) |
#                                                                                       | --- | ----------- |
# 
# | ----------------------------------------------------------------------------------------------- |
# | Raspberry Pi Pico, Pololu (POL), pin map, SPI and SDI - wip                                     |
# | ------- | ----------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
# | POL pin | Function    | SPI  | RPi Pico           | Wire   | SDI  | RPi Pico           | Wire   |
# |         |             |      | Use,  SPI1, pin NN |        |      | Use,  SD,   pin NN |        |  
# | ------- | ----------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
# | 1       | GND (VSS)   | —    | Null?              | NC?    | GND  | GND,        pin 38 |        | 
# | 2       | VDD         | —    | Null?              | NC?    | VDD  | 3V3,        pin 36 |        | 
# | 3       | DAT2        | —    | Null               | NC     | DAT2 | GP??, ??,   pin ?? |        | 
# | 4       | IRQ/DAT1    | —    | Null               | NC     | DAT1 | GP??, ?? ,  pin ?? |        | 
# | 5       | GND (VSS)   | —    | GND,        pin 38 | Black  | GND  | GND,        pin 38 | Black  | 
# | 6       | VDD         | —    | 3V3,        pin 36 | Red    | VDD  | 3V3,        pin 36 | Red    |
# | 7       | DI          | MOSI | GP11, TX,   pin 15 | Orange | CMD  | GP??, ???,  pin ?? |        |
# | 8       | DO          | MISO | GP12, RX,   pin 16 | Yellow | DAT0 | GP??, ???,  pin ?? |        |
# | 9       | SCLK        | SCLK | GP10, SCK,  pin 14 | Blue   | CLK  | GP??, ???,  pin ?? |        |
# | 10      | CS (Chip S) | SS   | GP13, CSn,  pin 17 | Green  | DAT3 | GP??, ???,  pin ?? |        |
# | 11      | CD (Card D) | —    | Null?              | NC?    | CD   | GP??, ???,  pin ?? |        | 
# | ------- | ----------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
# <todo: consider, if not using SD mode, assume POL pin's 1 and 2, GND (VSS) and VDD respectively,
#        are not wired in SPI mode? >
# <todo: consider, if using SD mode, assume POL pin's 1 and 2, GND (VSS) and VDD respectively,
#        are wired in SD mode to RPi Pico GND pin 38 and 3V3 pin 36 respectively? >
# 
# | -------------------------------------------------------------------------------------------------------------- |
# | SPI interface - Pololu breakout board micro SD Card module, map                                                |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- |
# | POL pin | Function  | RPi Pico           | Wire   | Description                                                |
# |         |           | Use,  SPI1, pin NN |        |                                                            |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- |
# | 5       | GND (VSS) | GND,        pin 38 | Black  | Ground                                                     |
# | 6       | VDD       | 3V3,        pin 36 | Red    | 3.3V power input                                           |
# | 7       | DI        | GP11, TX,   pin 15 | Orange | Data in, MOSI, Host transmist TX, serial data from RPi Pi  |
# | 8       | DO        | GP12, RX,   pin 16 | Yellow | Data out, MISO, Host recieve RX, serial data from device   |
# | 9       | SCLK      | GP10, SCK,  pin 14 | Blue   | Clock, clock signal from RPi Pi                            |
# | 10      | CS        | GP13, CSn,  pin 17 | Green  | Chip select (active low)                                   |
# | 11      | CD        | NULL, --,   --- -- | NC     | Card detect, not used in SPI mode                          |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- | 
#
# | -------------------------------------------------------------------------------------------------------------- |
# | SD Interface - wip                                                                                             |
# | ------- | --------- | ------------------ | ------ | ---------------------------------------------------------- |
# | POL pin | Function  | RPi Pico           | Wire   | Description                                                |
# |         |           | Use,  SDI,  pin NN |        |                                                            |
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
# | 4       | IRQ       | Interrupt (active low;           | 4       | IRQ       | Interrupt (active low;          |
# |         |           |            SDIO devices only)    |         |           |            SDIO devices only)   |
# | 3       | —         | Reserved                         | 3       | DAT2      | Data (bit 2)                    |
# | ------- | --------- | -------------------------------- | ------- | --------- | ------------------------------- |
#  Warning: Standard microSD cards use 3.3 V logic level signals, so level shifters or voltage dividers
#           are required when connecting one to a 5 V system.
# 
# SD Card nine (9) pin pinout, micro sd card eight (8) pin pinout - wip
# <todo: micro SD card 'pin out' map to Pololu SD Card 'reader' board device >
#
# SD Card pinout - elaborate
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
#  Micro SD Card pinout - elaborate
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
#           _________
#          |         |  Micro SD Card                                                                | --- | ----------- | Device            
#          |         |  Storage                                                                      | 1   | _           | pin function    
#          <         |  e.g. 32GB                                                                    | 2   | CS          | in SPI mode 
#           |        |  SD Card's use V3.3                                                           | 3   | DI          |       
#           |________|                                                                               | 4   | VDD         | 
#            ||||||||                                                                                | 5   | SCLK        | 
#            12345678                                                                                | 6   | VSS         | 
#                                                                                                    | 7   | DO          | 
#                                                                                                    | 8   | _           | 
#                                                                                                    | --- | ----------- | 
#      -------------------
#   1-|o|---__________--|o|-5 -----------------| Simplified       | --- | ----------- | Device       | --- | ----------- | Device                                                                   
#   2-|o|| |  ________  |o|-6 ---------------| | Front of         | 1   | GND (VSS)   | pin function | 5   | GND (VSS)   | pin function    
#   3-|o|| | |___||___| |o|-7 -------------| | | Micro SD Card    | 2   | VDD         | no pins      | 6   | VDD         | all pins                  
#   4-|o||_|            |o|-8 -----------| | | | Reader           | 3   | DAT2        | used in      | 7   | DI          | but not 11          
#     | |    | |    | | |o|-9 ---------| | | | | SPI 'CRUD'       | 4   | IRQ/DAT1    | SPI mode     | 8   | DO          | used in        
#     | |    | |    | | |o|-10-------| | | | | | Pololu, ??       | --- | ----------- |              | 9   | SCLK        | SPI mode           
#     | |____|_|____|_|_|o|-11       | | | | | | Board                                               | 10  | CS (Chip S) |
#      -------------------           | | | | | |                                                     | 11  | CD (Card D) |
#                                    | | | | | |                                                     | --- | ----------- |
#   | | | |                          | | | | | |                                                           
#   1 2 3 4                      11 10 9 8 7 6 5
#                                    | | | | | |
#      |-----------------------------| | | | | |                           
#      |     |-------------------------| | | |-(--------------------------|
#      | |---(---------------------------| |   |                          |
#      | | |-(-----------------------------|   |------------------------| |
#      | | | |                                                          | |
#      | | | |                         RPi Pico 2 W pinout              | |
#      | | | |                               _____                      | |
#      | | | |                         -----|     |-----                | |
#      | | | |                      1-| o ◯|_____|◯ o |-40            | |
#      | | | |                      2-| o     USB     o |-39            | |
#      | | | |                      3-| o             o |-38-----GND----| |
#      | | | |                      4-| o             o |-37              |
#      | | | |                      5-| o             o |-36---3V3(OUT)---|    
#      | | | |                      6-| o  __         o |-35
#      | | | |                      7-| o |__| Flash  o |-34
#      | | | |                      8-| o   _______   o |-33
#      | | | |                      9-| o  | ARM   |  o |-32
#      | | | |                     10-| o  | 2035  |  o |-31
#      | | | |                     11-| o  |_______|  o |-30
#      | | | |                     12-| o             o |-29
#      | | | |                     13-| o             o |-28
#      | | | |-SPI1 SCK----GP10----14-| o             o |-27
#      | | |---SPI1 TX-----GP11----15-| o             o |-26
#      | |-----SPI1 RX-----GP12----16-| o             o |-25
#      |-------SPI1 CSn----GP13----17-| o             o |-24
#                                  18-| o             o |-23
#                                  19-| o             o |-22
#                                  20-| o ◯       ◯ o |-21
#                                      -----------------
# additional suplimental pinout information for GP10, GP11, GP12, GP13, is elieded from now to simplify diagram
# therefore UART and I2C interface information is not shown. This may change in later itterations of the diagram
# as requirements change.

# #
# import libraries for use in this programme
# small form factor removable storage media, for SD Card, and also for MMC and eMMC
from machine import Pin, RTC, SPI, Timer
#import sdcard
from sdcard import SDCard # sdcard.SDCard,
from time import sleep
import os # <todo: use 'os' instead of 'uos'? documentation for MicroPython is not clear, >

# #
# Parameters common to all ports
# slot, selects which of the available interfaces to use. Leaving this unset will select the default interface.
# width, selects the bus width for the SD/MMC interface. This many data pins must be connected to the SD card.
# cd, can be used to specify a card-detect pin.
# wp, can be used to specify a write-protect pin.
# sck, can be used to specify an SPI clock pin.
# miso, can be used to specify an SPI miso pin.
# mosi, can be used to specify an SPI mosi pin.
# cs, can be used to specify an SPI chip select pin.
#
# Parameters only on ESP port
# cmd, can be used to specify the SD CMD pin (ESP32-S£ only)
# data, can be used to specify a list or tuple of SD data bus pins (ESP32-S3 only)
# freq, selects the SD/MMC interface frequencey in HZ.
# 
# SDCard(slot=1, width=1, cd=None, wp=None, sck=None, miso=None, mosi=None, cs=None, cmd=None, data=None, freq=20000000)
# https://docs.micropython.org/en/latest/library/machine.SDCard.html, from MicroPython docs
#
# Important! This is not how the sdcard.py RPi implementation works.
# RPi sdcard.py takes an SPI object instantiated with necessary values for an SPI connection,
# instead of individual values for an SPI connection as above.

# #
# SPI bus, instantiaion parameters

spi_bus = 1                 # valid values; 1 xor 0, SPI1 = 1 and SPI0 = 0
spi_baudrate = 1000000
spi_polarity = 0
spi_phase = 0
spi_bits = 8
spi_firstbit = SPI.MSB

spi_sck_pin = Pin(10)           # GP10, SCK,  pin 14 | POL  9, SCLK,        SCLK | Blue
spi_miso_pin = Pin(12)          # GP12, RX,   pin 16 | POL  8, DO,          MISO | Yellow
spi_mosi_pin = Pin(11)          # GP11, TX,   pin 15 | POL  7, DI,          MOSI | Orange

# create an chip select pin for sdcard.py SDCard to use
# start pin high, 
spi_cs_pin = Pin(13, Pin.OUT)   # GP13, CSn,  pin 17 | POL 10, CS (Chip S), SS   | Green
#print(f'cs_pin: {cs_pin}'.format(cs_pin) ) # debug

# #
# SD Card file 
# 
# create a path for os.mount to use
# the volume lable to use for the sd card to be accessed by Rpi Pico
sd_os_path = '/sd'
#print(f'sd_mount_path: {sd_mount_path}'.format(sd_mount_path) ) # debug

file_name = 'pico-cpu-temp-log.txt'
file_path = sd_os_path + '/' + file_name
#print(f'file path: {file_path}'.format(file_path)) # debug

# #
# device, PICO internal temperature sensor
#
pico_core_temp = machine.ADC(machine.ADC.CORE_TEMP)

# conversion parameter, max voltage (3.3) times (*) the max value analogue input reading can be (65535)
conversion_factor =  3.3 / (65535)

# #
# create a Real Time Clock instance, to use to get the current date and time
rtc = RTC()

# #
# initialize spi instance for use by SDCard driver
# 
def spi_inst(bus, baudrate, polarity, phase, bits, firstbit, sck, mosi, miso):

    try:
        # sd_card_spi, set values for SPI instance connection to sd card reader module
        sd_card_spi = SPI(bus,
                          baudrate = baudrate,
                          polarity = polarity,
                          phase = phase,
                          bits = bits,
                          firstbit = firstbit,
                          sck = sck,
                          mosi = mosi,
                          miso = miso )
        print(f'sd_card_spi: {sd_card_spi}'.format(sd_card_spi) ) # debug
        return sd_card_spi
        
    except Exception as e:
        print(f'SPI, initialisation exception: {e}'.format(e) )


# create an spi instance for sdcard.py SDCard to use
sd_card_spi = spi_inst(spi_bus,
                       spi_baudrate,
                       spi_polarity,
                       spi_phase,
                       spi_bits,
                       spi_firstbit,
                       spi_sck_pin,
                       spi_mosi_pin,
                       spi_miso_pin )
# print(f'spi instance, returned: {sd_card_spi}'.format(sd_card_spi)) # debug

# #
# initialise the sd card driver, for Rpi Pico to access sd card over SPI
# 
def sd_card_inst(spi, cs):
    
    try:
        micro_sd_card = SDCard(spi, cs) # SDCard from sdcard.py
        print(f'micro sd card: {micro_sd_card}'.format(micro_sd_card) ) # debug
        return micro_sd_card
    
    except Exception as e:
        print(f'SDCard, initialisation exception: {e}'.format(e) )

# create an sd card instance
micro_sd_card = sd_card_inst(sd_card_spi, spi_cs_pin)
# print(f'sd card, returned: {micro_sd_card}'.format(micro_sd_card)) # debug

# #
# the operating system os to mount the sd card at the path name provided
#
def os_mount_sd_card(sdc, path):
    
    try:
        os.mount(sdc, path) # 
        # print(f'os mount point: {os_mount_point}'.format(os_mount_point) ) # debug
        
    except Exception as e:
        print(f'os, mount exception: {e}'.format(e) )

# make the sd card accessable to RPi Pico 
os_mount_sd_card(micro_sd_card, sd_os_path)

# #
# list the current directory structure at the path name provided
#
def list_directory_structure(path):
    
    try:
        sys_vol_info = os.listdir(path)
        print(f'sys vol info: {sys_vol_info}'.format(sys_vol_info) ) # debug
    
    except Exception as e:
        print(f'os, list directory exception: {e}'.format(e) )

# List the directory to show any existing files
list_directory_structure(sd_os_path) # debug

# #
# Log the rpi pico internal cpu temperature
# 
# CRUD operation in the sd card file system
# 
# CPython docs
# 'r' open for reading (default)
# 'w' open for writing, truncating the file first
# 'x' open for exclusive creation, failing if the file already exists
# 'a' open for writing, appending to the end of file if it exists
# 'b' binary mode
# 't' text mode (default)
# '+' open for updating (reading and writing)
#
# is used with machine.Timer can only use one argument which must be the timer.
# 
def log_pico_cpu_temp(timer):
    
    # don't like using global variables but for this case of machine.Timer have no other choice for now.
    # <todo: consider, other options for time delayed operations, class callback as option, threading.Timer as option, others? >
    path = file_path 
    
    file_found = check_file_exists(path) 
    #print(f'file exists: {file_found}'.format(file_found) )
    
    try:
        
        # create a new file on the sd card, create a new file only if it does not already exist
        # <todo: break this out into a sperarate def, include header Temperature, DateTime, Location, after file creation.>
        # <todo: get geolocation data to add to log file, gps, other, >
        if (not file_found):
            with open(path, 'x') as log_file:
                print(f'file: new created, {log_file}'.format(log_file))
                pass
        
        # check_file_size(path) # debug
        
        # read data as raw value from temperature sensor
        raw_reading = pico_core_temp.read_u16()
        
        # #
        # get the date and time, from the Real Time Clock instance
        dt_tm = rtc.datetime() # get the current date and time
        
        # convert raw reading from alanog to digital value, also decimal value
        converted_raw_reading = raw_reading * conversion_factor
        
        # temperature as centigrade
        temperature = 27 - (converted_raw_reading - 0.706) / 0.001721
        
        # write the temperature value to file
        # <todo: write to file, but only to sdc not to PICO flash, so dependency of sdc code, noted 23/06/2025 >
        # crUd
        # update/write to the new file on the sd card, append does not truncate the file
        with open (path, 'a') as log_file:
            log_file.write(str(temperature) + ', ' + str(dt_tm) + ', ' + '\n')
            print(f'temperature: {str(temperature)}, at date & time: {str(dt_tm)}'.format(str(temperature), str(dt_tm)) # debug, temperature, date and time
            
            # print('PICO CPU temperature: sucessfully logged.') # debug, info
            # print the values to the console / shell
            # print(f"PICO CPU temperature: {temperature}, converted raw reading: {converted_raw_reading}, raw reading: {raw_reading} . "
            #      .format(temperature, converted_raw_reading, raw_reading)) # debug
    
    except Exception as e:
        print(f'file io, exception: {e}'.format(e) )
            
    # check_file_exists(path) # debug, returns True
    # check_file_size(path) # debug, 
    # delete_file(path)
    
# #
# Delete a file 
# 
def delete_file(path):
    
    try:
        # delete the file,
        os.remove(path)
        file_found = check_file_exists(path) # debug
        if (not file_found): # debug
            print(f'file deleted os.remove: {not file_found}'.format(not file_found) ) # debug
        
    except Exception as e:
        print(f'file delete os.remove, exception: {e}'.format(e) )
    
# #
# check if the file exists, has already been created
# 
def check_file_exists(path):
    
    #<todo: consider, other mechanisms to achieve file existance check>
    #file_check = os.path.exists(path) # does not seem to be available in MicroPython
    #file_check = os.stat(path) # need to better understand how to use this for file exists function
    #print(f'os, path exsist to file: {file_check}'.format(file_check) )
       
    try:
        with open (path, 'r') as the_file:
            #the_file.close()
            pass
        
        file_found = True
    
    except Exception as e:
        file_found = False
        print(f'file access, exception: {e}'.format(e) )

    print(f'file exists: {file_found}'.format(file_found) )
    return file_found

# #
# Check the size of the file as length of content as string.
# <todo: consider returning length? or is the point the debug statement? different use cases? >
def check_file_size(path):
        
    try:
        
        # cRud
        # read from the new file on the sd card
        with open (path, 'r') as log_file:
            file_content = log_file.read()
            print(f'file size: {len(file_content)} unicode chars'.format(len(file_content))) # debug
        
    except Exception as e:
        print(f'string length, exception: {e}'.format(e) )
   
# #
# Read file content
# <todo: consider return file contents too>
def read_file(path):
    
    try:
        
        # <todo: consider, is this necessary at all>
        # cRud
        # read from the appended file on the sd card
        with open (path, 'r') as log_file:
            all_content = log_file.read()
            print(f'file content: {all_content}'.format(all_content))

    except Exception as e:
        print(f'file read, exception: {e}'.format(e) )


# log initial first reading
# log the rpi pico internal cpu temperature
log_pico_cpu_temp(None)

# <todo: consider, refactor this or call from elewhere, >
timer_pico_cpu_temp_log = Timer(period=15000, mode=Timer.PERIODIC, callback=log_pico_cpu_temp)

# Idle programe between readings
# <todo: consider, refactor this into a def function, >
try:
    
    while True:
        # sleep for zero point one seconds
        sleep(0.1)
    
except KeyboardInterrupt:
    timer_pico_cpu_temp_log.deinit() # garbage collection
    check_file_exists(file_path) # debug, returns True
    check_file_size(file_path) # debug,
    read_file(file_path) # debug
    # delete_file(file_path)
    print('Logging interupt; keyboard')


# #
# sucsess
#



# #
# Unsucsessful
# 
# >>> %Run -c $EDITOR_CONTENT
# 
# MPY: soft reboot
# Traceback (most recent call last):
#   File "<stdin>", line 526
# SyntaxError: invalid syntax
# >>> 




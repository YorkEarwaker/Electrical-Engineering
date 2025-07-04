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
# RP2 module, quick reference
# https://docs.micropython.org/en/latest/rp2/quickref.html # module
#
# machine module
# https://docs.micropython.org/en/latest/library/machine.html # module
#
# machine module, Pin class
# https://docs.micropython.org/en/latest/library/machine.Pin.html # class
#
# machine module SPI class
# https://docs.micropython.org/en/latest/library/machine.SPI.html # class
#
# machine module I2C class, i2c.scan(), 
# https://docs.micropython.org/en/latest/library/machine.I2C.html # class
#
# BME280 driver
# Will likely have to write own driver from other examples for the Waveshare BME280 sensor
#
# The Richard Hull, BME280, driver refere to the Raspberry Pi (RPi) pinout not the Rasberry Pi Pico (RPi Pi) pinout,
# R Hull, I2C four pin device only, not six pin I2C/ISP Waveshare
# see RPi pinout below
# Assess R Hull driver for I2C , 
# https://pypi.org/project/RPi.bme280/
#
# RPi Spy, Matt Hawkins, Raspberry Pi, also Pico?
# https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/bme280.py
#
# BME280 sensor, Waveshare, environmental sensor
# https://thepihut.com/products/bme280-environmental-sensor
#
# Conversion of scales of temperature,
# https://en.wikipedia.org/wiki/Conversion_of_scales_of_temperature
#
# References - trouble shooting, tutorials
# https://forums.raspberrypi.com/viewtopic.php?t=381625
#
# RPi Pico 2 W pinout diagram
# https://datasheets.raspberrypi.com/picow/pico-2-w-pinout.pdf
# https://pico.pinout.xyz/
#
# RPi Pi pinout diagram,
# https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio
# https://pinout.xyz/
# https://projects.raspberrypi.org/en/projects/physical-computing/1
# 
# Raspberry Pi kernal overlays, to modify kernal without module changes, <todo: does this also apply to Pico?>
# Configuration file '/boot/config.txt', enable use of SPI1 by line; dtoverlay=spi1-3cs 
# https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/overlays/README
#
# I2C  
# Resistors between, host controller e.g. microcontroller like RPi Pico, target device e.g. sensor like BME280
# Example sensors with no onboard resistors; DHT22, AM2320
# <todo: confirm resistor's onboard Waveshare BME280, >
# https://learn.adafruit.com/working-with-i2c-devices/pull-up-resistors
# 
# How to Scan and Detect I2C Addresses, RPi Pico, Ardfruit lib i2cdetect?
# https://learn.adafruit.com/scanning-i2c-addresses/raspberry-pi
# 
# BME280 datasheet, Waveshare, CN,
# https://www.waveshare.com/wiki/BME280_Environmental_Sensor
# https://www.waveshare.net/wiki/Pioneer600_Datasheets
# https://www.waveshare.net/wiki/RPi_LCD_Datasheets
# Schematic
# https://files.waveshare.com/upload/4/42/BME280-Environmental-Sensor-Schematic.pdf
# Manual, Bosch file?, on Waveshare CN web site,
# https://files.waveshare.com/upload/9/91/BME280_datasheet.pdf
# Related, Bosch datasheet
# https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/
# https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf
# Related, PyPi driver project
# https://raw.githubusercontent.com/rm-hull/bme280/master/doc/tech-spec/BME280.pdf
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
# Sensor
# Pin sequence numbers, left to right, 1 2 3 4 5 6, with circuit board and BME sensor forward facing
#
#       [.] BME280 sensor device, circa factor larger than actual size
#   ___________ 
#  |    [.]    | Simplified       | --- | --------- | Circuit board 
#  |           | Front of         | 1   | VCC       | pins functions
#  |           | BME280           | 2   | GND       |
#  |___________| sensor           | 3   | SDA/MOSI  |
#  |___________| Waveshare, CN    | 4   | SCL/SCK   |
#   | | | | | |  Circuit board    | 5   | ADDR/MISO |     
#   1 2 3 4 5 6                   | 6   | CS        |
#                                 | --- | --------- | 
# 
# | --------------------------------------------------------------------------------------------- |
# | Raspberry Pi Pico, BME280, pin map, I2C1 and SPI0                                             |
# | ------- | --------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
# | BME pin | Function  | I2C  | RPi Pico           | Wire   | SPI  | RPi Pico           | Wire   |
# |         |           |      | Use,  I2C1, pin NN |        |      | Use,  SPI0, pin NN |        |  
# | ------- | --------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
# | 1       | VCC       | VCC  | 3V3,        pin 36 | Red    | VCC  | 3V3,        pin 36 | Red    | 
# | 2       | GND       | GND  | GND,        pin 38 | Black  | GND  | GND,        pin 38 | Black  | 
# | 3       | SDA/MOSI  | SDA  | GP18, SDA,  pin 24 | Blue   | MOSI | GP19, TX,   pin 25 |        | 
# | 4       | SCL/SCK   | SCL  | GP19, SCL,  pin 25 | Yellow | SCK  | GP18, SCK,  pin 24 |        | 
# | 5       | ADDR/MISO | ADDR |                    | Orange | MISO | GP16, RX,   pin 21 |        | 
# | 6       | CS        | CS   |                    | Green  | CS   | GP17, CSn   pin 22 |        | 
# | ------- | --------- | ---- | ------------------ | ------ | ---- | ------------------ | ------ |
# Candidate wiring and pin allocation, ensure programatically enable pins, don't rely on Pico 'defaults'
# This wiring for programatic switch between I2C and SPI may not be possible
# if I2C requires BME pin 5 and 6 to be NC not connected.
# Also as can be seen from the mapping above mapping issues for BME pin 3 and BME pin 4. For example;
# For I2C; BME pin 3 is I2C SDA maps to GP18 I2C1 SDA pin 24
# For SPI; BME pin 3 is SPI MOSI maps to GP19 SPI0 TX pin 25
#
# Other realted terms on other manufacturer's sensors, 
# MOSI/SDI Serial Data In
# MISO/SDO Serial Data Out
#
# I2C and SPI connection models,
# CS = Logic HIGH for I2C (default), logic LOW for SPI
# 
# | -------------------------------------------------------------------------------------------------------- |
# | I2C interface                                                                                            |
# | --- | --------- | ---------- | ---------- | ---------- | ----------------------------------------------- |
# | BME | Function  | Arduino    | STM32      | Raspberry  | Description                                     |
# | pin | pin       | interface  | interface  | Pi         |                                                 |
# | --- | --------- | ---------- | ---------- | ---------- | ----------------------------------------------- |
# | 1   | VCC       | 3.3V/5V    | 3.3V /5V   | 3.3V /5V   | Power input                                     |
# | 2   | GND       | GND        | GND        | GND        | Ground                                          |
# | 3   | SDA       | A4         | PB7        | SDA        | I2C data line                                   |
# | 4   | SCL       | A5         | PB6        | SCL        | I2C clock line                                  |
# | 5   | ADDR      | NC/GND     | NC/GND     | NC/GND     | Address chip select (default is high):          |
# |     |           |            |            |            | When the voltage is high, the address is 0 x 77 |
# |     |           |            |            |            | When the voltage is low, the address is: 0 x 76 |
# | 6   | CS        | NC         | NC         | NC         | NC                                              |
# | --- | --------- | ---------- | ---------- | ---------- | ----------------------------------------------- |
# 
# | -------------------------------------------------------------------------------------------------------- |
# | SPI interface                                                                                            |
# | --- | --------- | ---------- | ---------- | ---------- | ----------------------------------------------- |
# | BME | Function  | Arduino    | STM32      | Raspberry  | Description                                     |
# | pin | pin       | interface  | interface  | Pi         |                                                 |
# | --- | --------- | ---------- | ---------- | ---------- | ----------------------------------------------- | 
# | 1   | VCC       | 3.3V /5V   | 3.3V /5V   | 3.3V /5V   | 3.3VPower input                                 |
# | 2   | GND       | GND        | GND        | GND        | Ground                                          |
# | 3   | MOSI      | D11        | PA7        | MOSI       | SPI data input                                  |
# | 4   | SCK       | D13        | PA5        | SCK        | SPI clock input                                 |
# | 5   | MISO      | D12        | PA6        | MISO       | SPI data output                                 |
# | 6   | CS        | D10        | PB6        | GP27?      | SPI Chip select, active when voltage is low     |
# | --- | --------- | ---------- | ---------- | ---------- | ----------------------------------------------- |
# 27, GP27 seem's incorrect from Waveshare docs re Rasberry Pi, <todo: validate this >
#
# Inter Intergerated Circuit I2C
# a two-wire serial protocol
# Pico pinout, two I2C controllers, I2C0 and I2C1. Preferred use I2C1.
# Each with several GPIO pins for SDA (Serial Data) and SCL (Serial Clock) signals.
# I2C0 internal I2C bus reserved for GPU, but can be used for general communcation
# if CSI1 and DSI1 interfaces are not used or are controlled by firmware. 
# I2C1 external I2C bus better for connecting sensors or peripherals.
# Not used for internal functions and can be used freely for general communications.
# Raspberry Pi Pico default I2C interface I2C1
# Raspberry Pi Pico default I2C1 pins, GP2 (SDA), GP3 (SCL),
#
# Two pull up resistor required for I2C electrical interface,
# One resistor between SDA and VCC
# One resistor between SCL and VCC
# SDA = DATA, signal, a GPIO I2C SDA, with a 10k Ohm pull up resistor? 
# SCL = Clock, a GPIO I2C SCL, with a 10k Ohm pull up resistor?
# Or resistor's onboard sensor, i.e. BME280,? <todo: confirm resistor's onboard Waveshare BME280>
# 
# | ---------------------------------------------------------------------- |
# | RPi Pico, I2C0 Pinout,                                                 |
# | Default I2C0 Pins: GP4 (SDA), GP5 (SCL)                                |
# | --------- | -------------------------------------- | ----------------- |
# | Function  | RPi Pico GPIO                          | Description       |
# | pin       | <todo: Board pin NN line below GPIO?>  |                   |
# | --------- | -------------------------------------- | ----------------- |
# | SDA       | GP0, GP4, GP8, GP12, GP16, GP20,       | Serial Data       |
# | SCL       | GP1, GP5, GP9, GP13, GP17, GP21,       | Serial Clock      |
# | ---------------------------------------------------------------------- |
#
# | ---------------------------------------------------------------------- |
# | RPi Pico, I2C1 Pinout, default preferred 12C interface                 |
# | Default I2C1 Pins: GP2 (SDA), GP3 (SCL)                                |
# | --------- | -------------------------------------- | ----------------- |
# | Function  | RPi Pico GPIO                          | Description       |
# | pin       |                                        |                   |
# | --------- | -------------------------------------- | ----------------- |
# | SDA       | GP2, GP6, GP10, GP14, GP18, GP26,      | Serial Data       |
# | SCL       | GP3, GP7, GP11, GP15, GP19, GP27,      | Serial Clock      |
# | ---------------------------------------------------------------------- |
#
# Serial Peripheral Interface SPI
# RPi Pico, two SPI controllers, SPI0 and SPI1. 
# Raspberry Pi Pico SPI0 default pins,
# GP19 (MOSI/TX), GP18 (SCK), GP17 (CS) and GP16 (MISO/RX)
# Using SPI1 may require additional manual configuration of onboard files for Raspberry Pi. <todo: check this is the case for Pico too?>
# Raspberry Pi, configure dtoverlay in'/boot/config.txt' to enable SPI1, e.g. dtoverlay=spi1-3cs . 
# 
# | ---------------------------------------------------------------------------- |
# | RPi Pico, SPI0 Pinout, default preferred SPI interface                       |
# | Default SPI0 Pins: GP19 (MOSI/TX), GP18 (SCK), GP17 (CS), GP16 (MISO/RX)     |
# | --------- | -------------------------------------- | ----------------------- |
# | Function  | RPi Pico GPIO                          | Description             |
# | pin       |                                        |                         |
# | --------- | -------------------------------------- | ----------------------- |
# | CLK       | GP2, GP6, GP18,                        | Clock                   |
# | MOSI      | GP3, GP7, GP19,                        | Master Out Slave In     |
# | MISO      | GP0, GP4, GP16,                        | Master In  Slave Out    |
# | CS        | GP1, GP5, GP17,                        | Chip Select             |
# | ---------------------------------------------------------------------------- |
#
# | ---------------------------------------------------------------------------- |
# | RPi Pico, SPI1 Pinout,                                                       |
# | Default SPI1 Pins: ?                                                         |
# | --------- | -------------------------------------- | ----------------------- |
# | Function  | RPi Pico GPIO                          | Description             |
# | pin       |                                        |                         |
# | --------- | -------------------------------------- | ----------------------- |
# | CLK       | GP10, GP14,                            | Clock                   |
# | MOSI      | GP11, GP15,                            | Master Out Slave In     |
# | MISO      | GP8,  GP12,                            | Master In  Slave Out    |
# | CS        | GP9,  GP13,                            | Chip Select             |
# | ---------------------------------------------------------------------------- |
#
# Circuit diagram
# Simplified view of Rpi Pico microntroller and Waveshare PCB BME280 sensor device circuit.
# The I2C interface works with current circuit design. 02/05/2025
#
# <todo: consider, might need two of these, one for I2C interface and another for SPI interface >
# <todo: consider, this wiring diagram probably won't work due to conflicts identified above
#        in table 'Raspberry Pi Pico, BME280, pin map, I2C1 and SPI0' current state of breadboard>
#   ___________ 
#  |    [.]    | Simplified       | --- | --------- | Circuit board 
#  |           | Front of         | 1   | VCC       | pins functions
#  |           | BME280           | 2   | GND       |
#  |___________| sensor           | 3   | SDA/MOSI  |
#  |___________| Waveshare, CN    | 4   | SCL/SCK   |
#   | | | | | |  Circuit board    | 5   | ADDR/MISO |     
#   1 2 3 4 5 6                   | 6   | CS        |
#   | | | | | |                   | --- | --------- |
#   |-)-)-)-)-)-------------------------------------------------------| 
#     | | | | |                                                       | 
#     |-)-)-)-)-----------------------------------------------------| |
#       | | | |                                                     | |
#       | | | |                    RPi Pico 2 W pinout              | |
#       | | | |                          _____                      | | 
#       | | | |                    -----|     |-----                | |
#       | | | |                 1-| o ◯|_____|◯ o |-40            | | 
#       | | | |                 2-| o     USB     o |-39            | |
#       | | | |                 3-| o             o |-38-----GND----| |
#       | | | |                 4-| o             o |-37              |
#       | | | |                 5-| o             o |-36---3V3(OUT)---|     
#       | | | |                 6-| o  __         o |-35
#       | | | |                 7-| o |__| Flash  o |-34
#       | | | |                 8-| o   _______   o |-33
#       | | | |                 9-| o  | ARM   |  o |-32
#       | | | |                10-| o  | 2035  |  o |-31
#       | | | |                11-| o  |_______|  o |-30
#       | | | |                12-| o             o |-29
#       | | | |                13-| o             o |-28
#       | | | |                14-| o             o |-27
#       | | | |                15-| o             o |-26
#       | | | |                16-| o             o |-25----GP19-----ISP0 TX----I2C1 SCL-------------------|
#       | | | |                17-| o             o |-24----GP18-----ISP0 SCK---I2C1 SDA-------------------)-|
#       | | | |                18-| o             o |-23                                                   | |
#       | | | |                19-| o             o |-22----GP17-----ISP0 CSn---I2C0 SCL---UART0 RX----|   | |
#       | | | |                20-| o ◯       ◯ o |-21----GP16-----ISP0 RX----I2C0 SDA---UART0 TX----)-| | |
#       | | | |                    -----------------                                                   | | | |
#       | | | |----------------------------------------------------------------------------------------| | | |
#       | | |--------------------------------------------------------------------------------------------| | |
#       | |------------------------------------------------------------------------------------------------| |
#       |----------------------------------------------------------------------------------------------------|
#

# #
# Import libraries to use in this programme
from machine import Pin, I2C, RTC
from time import sleep
#import snr_bme280_dvr as BME280 # snr_bme280_dvr, must be present on Rpi Pico as file download
import org.agw.een.snr.snr_bme280_dvr as BME280 # driver installed in RPi Pico micropython

# #
# define values; clock pin, serial data pin, clock frequency
scl_pin = Pin(19) # GP19, I2C1 scl
sda_pin = Pin(18) # GP18, I2C1 sda
#clock_freq = 400_000 # 400kHz
clock_freq = 1000 # 1kHz

# #
# Initialise I2C communication
#i2C = I2C(id=0, scl=Pin(5), sda=Pin(4), freq=1000)
i2c = I2C(1, scl=scl_pin, sda=sda_pin, freq=clock_freq) # 
#print('i2c object: {}'.format(i2c)) # debug, I2C configuration values

# # Debug only
# scan for devices at the RPi pins on the I2C hardware bus, should return [119]
#dvcs = i2c.scan() # scan for devices
#print('devices: {}'.format(dvcs)) # debug, I2C devices found

# #
# create a Real Time Clock instance, to use to get the current date and time
rtc = RTC()

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
        print('current date & time: {}'.format(dt_tm)) # debug, date and time
        
        # #
        # Initialise BME280 sensor
        bme = BME280.BME280(i2c=i2c)
        #print('bme initialised: {}'.format(bme)) # debug
        
        # #
        # Read sensor data
        tempC = bme.temperature
        #print('bme.temperature(): {}'.format(tempC)) # debug
        hum = bme.humidity
        #print('bme.humidity(): {}'.format(hum)) # debug
        pres = bme.pressure
        #print('bme.humidity(): {}'.format(pres)) # debug
        
        # #
        # Convert temperature to fahrenheit
        tempF = (bme.read_temperature()/100) * (9/5) + 32
        tempF = str(round(tempF, 2)) + 'F'
        #print('tempF: {}'.format(tempF)) # debug
        
        # #
        # Print sensor readings
        print('Temperature: ', tempC)
        print('Temperature: ', tempF)
        print('Humidity: ', hum)
        print('Pressure: ', pres)
    
    except Exception as e:
        # Handle any exceptions during sensor reading
        print('Ooops. Code boo-boo. Time for cinnamon bun and a nice cupa cha. An error occurred: ', e)
        

# # # Old code put this somewhere else
#
# # import libraries to use in this programme
# #from bme import BME280 # sensor driver, this to source or more likely have to create code for
# from machine import RTC, Pin, I2C
# 
# # #
# # get the current date and time
# rtc = RTC()
# dt_tm = rtc.datetime() # get the date and time
# print('current date & time: {}'.format(dt_tm)) # debug, date and time
# 
# 
# # ###############
# # Work in progress wip
# # ###############
# 
# # #
# # initialize the I2C class, scan for attachded devices
# # in wiring for candiate circuit this should return empty []
# # see table; Raspberry Pi Pico, BME280, pin map, I2C1 and SPI0 
# i2c = I2C(0) # default assignment; scl=Pin(5), sda=Pin(4)
# print('i2c object: {}'.format(i2c)) # debug, I2C configuration values
# 
# # scan for devices at the default pin values
# dvcs = i2c.scan() # scan for devices
# print('devices: {}'.format(dvcs)) # debug, I2C devices found
# 
# # #
# # define values; clock pin, serial data pin, clock frequency
# scl_pin = Pin(19) # GP19, I2C1 scl
# sda_pin = Pin(18) # GP18, I2C1 sda
# clock_freq = 400_000 # 400kHz
# 
# # #
# # assign values; to I2C1 hardware bus . 
# i2c = I2C(1, scl=scl_pin, sda=sda_pin, freq=clock_freq) # hardware bus, I2C1,
# print('i2c object: {}'.format(i2c)) # debug, I2C configuration values
# 
# # scan for devices at the RPi pins on the I2C hardware bus, should return [119]
# dvcs = i2c.scan() # scan for devices
# print('devices: {}'.format(dvcs)) # debug, I2C devices found
# 
# buf = bytearray(10)
# buf = i2c.readfrom(119, 10) # read ten (10) from address 119
# print('bytes read from device at address on i2c: {}'.format(buf)) # debug, I2C configuration values
# 
# 
# 

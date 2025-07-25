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
# | 3       | SCL       | GP09, SCL , pin 12 | Blue   | I2C clock pin                                              |
# | 4       | SDA       | GP08, SDA , pin 11 | Yellow | I2C data pin                                               |
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
# For a fuller discussion of BME280 sensor see the following link which will likely at some point get stale, 
# https://github.com/YorkEarwaker/Electrical-Engineering/blob/main/rpi-pi/mpy/snr-tsd/src/org/agw/een/snr/snr_bme280_tsd.py , retrieved: 2025-07-24
# See also related projects README.md 


# #
# libraries and classes to use in this program
# <todo: put in org.agw..... package structure for import statement and comment out the dev env import statement>
#import dsp_lcd1602_dvr as LCD1602 # dev env, driver .py file saved to rpi-pico flash in Thonny IDE
from org.agw.een.dsp import dsp_lcd1602_dvr as LCD1602 # qa env, driver installed as distribution package in Thonny IDE
from machine import Pin, I2C, RTC
from time import sleep
#import snr_bme280_dvr as BME280 # snr_bme280_dvr, must be present on Rpi Pico as file download
import org.agw.een.snr.snr_bme280_dvr as BME280 # driver installed in RPi Pico micropython

# #
# define values; clock pin, serial data pin, clock frequency
i2c_bus_snr = 1 # 0 or 1
i2c_scl_pin_snr = Pin(19) # GP19, I2C1 scl
i2c_sda_pin_snr = Pin(18) # GP18, I2C1 sda
#clock_freq = 400_000 # 400kHz
i2c_clock_freq_snr = 1000 # 1kHz

# #
# Initialise I2C communication
#i2C = I2C(id=0, scl=Pin(5), sda=Pin(4), freq=1000)
sensor_i2c = I2C(i2c_bus_snr, scl=i2c_scl_pin_snr, sda=i2c_sda_pin_snr, freq=i2c_clock_freq_snr) # 
#print('i2c object: {}'.format(i2c)) # debug, I2C configuration values

# # Debug only
# scan for devices at the RPi pins on the I2C hardware bus, should return [119]
dvcs = sensor_i2c.scan() # scan for devices
print('devices: {}'.format(dvcs)) # debug, I2C devices found

# #
# Initialise BME280 sensor
bme = BME280.BME280(i2c=sensor_i2c)
#print('bme initialised: {}'.format(bme)) # debug

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
        print('current date & time: {}'.format(dt_tm)) # debug, date and time
        
        # #
        # Read sensor data
        tempC = bme.temperature
        #print('bme.temperature(): {}'.format(tempC)) # debug
        hum = bme.humidity
        #hum2 = bme.read_humidity()
        #hum = round(hum, 2)
        #print('bme.humidity(): {}'.format(hum2)) # debug
        # hectopascal (1 hPa = 100 Pa), which is equal to one millibar,
        # and the kilopascal (1 kPa = 1000 Pa),
        # which is equal to one centibar.
        pres = bme.pressure # hPa/mbar
        #pres2 = bme.read_pressure()
        #pres = str(round(pres, 2))
        #print('bme.pressure(): {}'.format(pres2)) # debug
        
        # #
        # Convert temperature to fahrenheit
        tempF = (bme.read_temperature()/100) * (9/5) + 32
        tempF = str(round(tempF, 2)) + 'F'
        #tempF = str(round(tempF, 2))
        #print('tempF: {}'.format(tempF)) # debug
             
        # #
        # Display values on an screen
        
        # Each cycle wipe the screen clear of any previous text
        lcd_display.clear()
        
        # Place the cursor to the top left hand side of the screen to start writting the first line
        lcd_display.setCursor(0, 0)

        # Write temperature in Celsius and Fahrenheit
        lcd_display.printout('{}, {}'.format(tempC, tempF))
        
        # Plase the cursor to the bottom left hand side of the screen to start writting the second line
        lcd_display.setCursor(0, 1)
        
        # Write the relative humidity as percentage
        lcd_display.printout('{}, {}'.format(hum, pres))
        
        # #
        # Print sensor readings to shell
        print('Temperature: ', tempC)
        print('Temperature: ', tempF)
        print('Humidity: ', hum)
        print('Pressure: ', pres)
    
    except Exception as e:
        # Handle any exceptions during sensor reading
        #print('Ooops. Code boo-boo. Time for cinnamon bun and a nice cupa cha. An error occurred: ', e)   
        print('OSError. Sensor reading failed. {} '.format(e) )

        







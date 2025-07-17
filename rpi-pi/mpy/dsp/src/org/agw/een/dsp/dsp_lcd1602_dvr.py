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
# 
# I2C-bus specification and user manual, NXP Semiconductors,
# https://www.nxp.com/docs/en/user-guide/UM10204.pdf
#
# Bit Numbering
# https://en.wikipedia.org/wiki/Bit_numbering
#
# Hexadecimal notation,
# prefix 0x, C/C++, Java, Python
# suffix h, assembly
# https://www.electronics-tutorials.ws/binary/bin_3.html
# https://en.wikipedia.org/wiki/Assembly_language
# https://en.wikipedia.org/wiki/Bit_numbering
# https://en.wikipedia.org/wiki/Bitwise_operation
# https://en.wikipedia.org/wiki/Bit_field
# 
# Hitachi HD44780 controller, is used as basis for operation for LCD1602
# MIT, https://academy.cba.mit.edu/classes/output_devices/44780.pdf # ** seems useful, full datasheet
# datasheet, https://github.com/robjwells/circuitpython-waveshare-1602/blob/main/HD44780.pdf # partial datasheet
# wikipedia, https://en.wikipedia.org/wiki/Hitachi_HD44780_LCD_controller # overview
#
# PCA9633DP2, RGB backlight is driven by NXP PCA9633 chip accessable via I2C
# NXP Semiconductors, https://www.nxp.com/products/power-drivers/lighting-driver-and-controller-ics/led-drivers/4-bit-fm-plus-ic-bus-led-driver:PCA9633
# datasheet, https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf # ** seems useful, register addresses,

#
# mouser electronics, https://www.mouser.co.uk/ProductDetail/NXP-Semiconductors/PCA9633DP2118?qs=LOCUfHb8d9tlQy5ehY0dtQ%3D%3D
# datasheet, https://www.mouser.co.uk/datasheet/2/302/PCA9633-3139106.pdf
# 
# AIP31068L, LCD controller
# datasheet, https://www.orientdisplay.com/wp-content/uploads/2022/08/AIP31068L.pdf # **
# https://i2cdevices.org/addresses/0x7c # 01100000
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
#
# Registers
# 
# PCA9633, https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf
# <todo: prityfy in a with some table structure, virtical bar and underscore, >
# Table 6. Register summary
#Register number (hex) D3 D2 D1 D0 Name Type Function
#00h 0 0 0 0 MODE1 read/write Mode register 1
#01h 0 0 0 1 MODE2 read/write Mode register 2
#02h 0 0 1 0 PWM0 read/write brightness control LED0
#03h 0 0 1 1 PWM1 read/write brightness control LED1
#04h 0 1 0 0 PWM2 read/write brightness control LED2
#05h 0 1 0 1 PWM3 read/write brightness control LED3
#06h 0 1 1 0 GRPPWM read/write group duty cycle control
#07h 0 1 1 1 GRPFREQ read/write group frequency
#08h 1 0 0 0 LEDOUT read/write LED output state
#09h 1 0 0 1 SUBADR1 read/write I2C-bus subaddress 1
#0Ah 1 0 1 0 SUBADR2 read/write I2C-bus subaddress 2
#0Bh 1 0 1 1 SUBADR3 read/write I2C-bus subaddress 3
#0Ch 1 1 0 0 ALLCALLADR read/write LED All Call I2C-bus address
#
#[1] Only D[3:0] = 0000 to 1100 are allowed and will be acknowledged. D[3:0] = 1101, 1110, or 1111 are reserved and will not be acknowledged.
#[2] When writing to the Control register, bit 4 must be programmed with logic 0 for proper device operation.
#
#
# PCA9633, https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf
# <todo: prityfy in a with some table structure, virtical bar and underscore, >
#Table 9. PWM0 to PWM3 - PWM registers 0 to 3 (address 02h to 05h) bit description
# Address Register Bit Symbol Access Value Description
# 02h PWM0 7:0 IDC0[7:0] R/W 0000 0000* PWM0 Individual Duty Cycle
# 03h PWM1 7:0 IDC1[7:0] R/W 0000 0000* PWM1 Individual Duty Cycle
# 04h PWM2 7:0 IDC2[7:0] R/W 0000 0000* PWM2 Individual Duty Cycle
# 05h PWM3 7:0 IDC3[7:0] R/W 0000 0000* PWM3 Individual Duty Cycle
# A 97 kHz fixed frequency signal is used for each output. Duty cycle is controlled through
# 256 linear steps from 00h (0 % duty cycle = LED output off) to FFh (99.6 % duty cycle =
# LED output at maximum brightness). Applicable to LED outputs programmed with LDRx
# = 10 or 11 (LEDOUT register).
#
# Note. This code is based on the code provided by the Waveshare demo code.
#

# #
# import other libraries or classes from libs that will be used in this code
import time
from machine import Pin, I2C

# Device I2C Address
#
# Bit shifting concern, likely equivalent components are being used.
# Very confused about all of this. The reasoning below is likely not entirely correct.
# The equivalent device is probably not listed at https://i2cdevices.org/addresses/
# 
# 一 LCD Controller IC: AiP31068L or Equivalent
# concern? 0x7c = 01111100, 0x3e = 00111110, 0x7c>>1 = 0x3e = 00111110
# https://i2cdevices.org/addresses/0x3e , very confusing as two distinct products might be referenced
# datasheet? https://www.nxp.com/docs/en/data-sheet/PCF8574_PCF8574A.pdf
# datasheet? https://fscdn.rohm.com/en/products/databook/datasheet/ic/driver/lcd_segment/bu97960muv-e.pdf 
#
# 一 RGB Controller IC: PCA9633DP2 or Equivalent
# concern? 0xc0 = 11000000, 0x60 = 01100000, 0xc0>>1 = 0x60 = 01100000
# https://i2cdevices.org/addresses/0x60
# https://i2cdevices.org/devices/pca9685
# datasheet? https://www.nxp.com/docs/en/data-sheet/MAG3110.pdf , probably not this component
#
# page 6, https://www.waveshare.com/w/upload/2/2e/LCD1602_RGB_Module.pdf
addr_i2c_lcd   =  (0x7c>>1) # AiP31068L (LCD) Slave Address : 0X7C,
addr_i2c_rgb   =  (0xc0>>1) # PCA9633DP2 (RGB) Slave Address: 0XC0, 

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
# <todo: locate correct referrences to register tables and document sections,
#  in datasheets; HD44780, AIP31068L, PCA9633DP2>

# #
# PCA9633DP2 RGB I2C controller
# 
# Colour definition registers, red, green, blue, amber?
# Every screen grid postion has four (4) light emmiting diodes LEDs <todo: is this true?>
# one of each of amber, red, green, blue
#
# PCA9633, , , https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf
# 05h 0 1 0 1 PWM3 read/write brightness control LED3
# ? amber <todo: confirm use of amber diode in this lCD screen>

# PCA9633, , , https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf
# 04h 0 1 0 0 PWM2 read/write brightness control LED2
reg_addr_red    = 0x04

# PCA9633, , , https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf
# 03h 0 0 1 1 PWM1 read/write brightness control LED1
reg_addr_green  = 0x03

# PCA9633, , , https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf
# 02h 0 0 1 0 PWM0 read/write brightness control LED0
reg_addr_blue   = 0x02

# #
# PCA9633, 7.3.1 Mode register 1, MODE1, https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf
# Table 7. MODE1 -  Mode register 1 (address 00h)
# 00h 0 0 0 0 MODE1 read/write Mode register 1
reg_addr_mode1  = 0x00 # 

# PCA9633, 7.3.2 Mode register 2, MODE2, https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf
# Table 8. MODE2 - Mode register 2 (address 01h)
# 01h 0 0 0 1 MODE2 read/write Mode register 2
reg_addr_mode2  = 0x01 # 

# PCA9633, 7.3.6 LED driver output state, LEDOUT, https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf
# Table 12. LEDOUT - LED driver output state register (address 08h)
# 08h 1 0 0 0 LEDOUT read/write LED output state
reg_addr_output = 0x08 #

# #
# AIP31068L LCD I2C controller, (historic HD44780) 
# 
# AIP31068L, 4.2、INSTRUCTION DESCRIPTION, https://www.orientdisplay.com/wp-content/uploads/2022/08/AIP31068L.pdf
# AIP31068L, Table 3. Instruction Table, https://www.orientdisplay.com/wp-content/uploads/2022/08/AIP31068L.pdf
# see also
# HD44780U, https://academy.cba.mit.edu/classes/output_devices/44780.pdf
# HD44780U, Instructions, Table 6 Instructions, https://academy.cba.mit.edu/classes/output_devices/44780.pdf#%5B%7B%22num%22%3A106%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C-6%2C848%2C0.88%5D
# HD44780U, Instruction Description, https://academy.cba.mit.edu/classes/output_devices/44780.pdf#%5B%7B%22num%22%3A121%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C-6%2C848%2C0.88%5D
# HD44780U, Figure 11 Instruction (1)
# 1) Clear Display, Clear all the display data. Return cursor to the original status,
#    namely, bring the cursor to the left edge on the first line of the display.
# bitmask 0x01 hexadecimal = register bit position, if value is set to 1 = binary 00000001 = decimal   1
reg_addr_clear_display     = 0x01 # bit 1,

# 2) Return Home, Return cursor to its original site and return display to its original status, if shifted.
# bitmask 0x02 hexadecimal = register bit position, if value is set to 1 = binary 00000010 = decimal   2
reg_addr_return_home       = 0x02 # bit 2,

# 3) Entry Mode Set, Set the moving direction of cursor and display.
# bitmask 0x04 hexadecimal = register bit position, if value is set to 1 = binary 00000100 = decimal   4
reg_addr_entry_mode_set    = 0x04 # bit 3,

# 4) Display ON/OFF Control, Control display/cursor/blink ON/OFF 1 bit register.
# bitmask 0x08 hexadecimal = register bit position, if value is set to 1 = binary 00001000 = decimal   8
reg_addr_display_control   = 0x08 # bit 4,

# 5) Cursor or Display Shift, Shifting of right/left cursor position or display without writing or reading
#    of display data. This instruction is used to correct or search display data.
# bitmask 0x10 hexadecimal = register bit position, if value is set to 1 = binary 00010000 = decimal  16
reg_addr_cursor_shift      = 0x10 # bit 5,

# 6) Function Set, data (8 bit or 4 bit), line, font
# bitmask 0x20 hexadecimal = register bit position, if value is set to 1 = binary 00100000 = decimal  32
reg_addr_function_set      = 0x20 # bit 6,

# 7) Set CGRAM Address, Set CGRAM address to AC. This instruction makes CGRAM data available from MPU.
# bitmask 0x40 hexadecimal = register bit position, if value is set to 1 = binary 01000000 = decimal  64
reg_addr_set_cgram_address = 0x40 # bit 7,

# 8) Set DDRAM Address, Set DDRAM address to AC. This instruction makes DDRAM data available from MPU.
# bitmask 0x80 hexadecimal = register bit position, if value is set to 1 = binary 10000000 = decimal 128
reg_addr_set_ddram_address = 0x80 # bit 8, 

# #
# AIP31068L LCD I2C controller, (historic HD44780)
# 
# AIP31068L, https://www.orientdisplay.com/wp-content/uploads/2022/08/AIP31068L.pdf
# HD44780U, https://academy.cba.mit.edu/classes/output_devices/44780.pdf
# Values for entry mode set
# 3) Entry Mode Set, Set the moving direction of cursor and display.
reg_addr_entry_mode_set_right = 0x00 # 
reg_addr_entry_mode_set_left = 0x02 # 
reg_addr_entry_mode_set_shift_increment = 0x01 # 
reg_addr_entry_mode_set_shift_decrement = 0x00 # 

# #
# AIP31068L LCD I2C controller, (historic HD44780)
# 
# AIP31068L, https://www.orientdisplay.com/wp-content/uploads/2022/08/AIP31068L.pdf
# HD44780U, https://academy.cba.mit.edu/classes/output_devices/44780.pdf
# Values for control
# 4) Display ON/OFF Control, Control display/cursor/blink ON/OFF 1 bit register.

# #
# AIP31068L LCD I2C controller, (historic HD44780)
# 
# AIP31068L, https://www.orientdisplay.com/wp-content/uploads/2022/08/AIP31068L.pdf
# HD44780U, https://academy.cba.mit.edu/classes/output_devices/44780.pdf
# Values for cursor position
# 5) Cursor or Display Shift, Shifting of right/left cursor position or display without writing or reading
#    of display data. This instruction is used to correct or search display data.

# #
# AIP31068L LCD I2C controller, (historic HD44780)
# 
# AIP31068L, https://www.orientdisplay.com/wp-content/uploads/2022/08/AIP31068L.pdf
# HD44780U, https://academy.cba.mit.edu/classes/output_devices/44780.pdf
# Values for text
# 6) Function Set, data (8 bit or 4 bit), line, font

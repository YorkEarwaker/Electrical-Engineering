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
#
# Probably not in first instance be able to use MicroPython, Sparkfun and Bosch example code in C/C++
# Use these files to some initial cicuit design images and collect some links to relevant sources
# see also notes on C/C++ (cpa) equivalent project;
# https://github.com/YorkEarwaker/Electrical-Engineering/blob/main/rpi-pi/cpa/snr-rsl/org/agw/een/snr/rsl/rsl_bmv080_drv.c

# #
# import other libraries or classes from libs that will be used in this code
from machine import Pin, I2C

# #
# I2C bus
# define values; clock pin, serial data pin, clock frequency
# One device or string of devices per controller only,
# So only two strings of devices active at any one time one for one set for bus 0 one set for bus 1
# One device or string of devices on i2c 0, One device or string of devices on i2c 1
# Limit 127 devices in total, limit one (1) i2c 'hub' and six (6) devices per daisy chain,
# Limits are set by the USB specification, and power consumption and bandwidth considerations
i2c_bus_rsl = 0
i2c_scl_pin_rsl = Pin(9) # GP9, I2C0 scl
i2c_sda_pin_rsl = Pin(8) # GP8, I2C0 sda
#clock_freq = 400_000 # 400kHz
i2c_clock_freq_rsl = 400000 # 400kHz, 1000 = 1KHz

# #
# create an i2c instance of the particulate matter sensor
def i2c_inst(bus, scl, sda, freq):
    
    try:
        
        pm_sensor_i2c = I2C(bus,
                          scl = scl,
                          sda = sda,
                          freq = freq)
        print(f'pm_sensor_i2c: {pm_sensor_i2c}'.format(pm_sensor_i2c) ) # debug
        return pm_sensor_i2c
        
    except Exception as e:
        print(f'I2C, initialisation exception: {e}'.format(e) )

# create an I2C instance to communicate with the particulate matter sensor
pm_sensor_i2c = i2c_inst(i2c_bus_rsl,
                       i2c_scl_pin_rsl,
                       i2c_sda_pin_rsl,
                       i2c_clock_freq_rsl)
# print(f'pm_sensor_i2c: {pm_sensor_i2c}'.format(pm_sensor_i2c) ) # debug

# debug
# <todo: iterate to return False is the empty list [] is returned. >
def check_i2c_on_bus(i2c):
    list_of_valid_i2c_addresses = i2c.scan() # debug
    print(f'pm_sensor_i2c.scan() address list: {list_of_valid_i2c_addresses}'.format(list_of_valid_i2c_addresses)) # debug

# debug
# check that the particulate matter sensor was recognised on the I2C bus
check_i2c_on_bus(pm_sensor_i2c)
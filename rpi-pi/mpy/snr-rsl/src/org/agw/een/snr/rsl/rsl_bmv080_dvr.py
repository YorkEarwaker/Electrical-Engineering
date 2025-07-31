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

# Probably not in first instance be able to use MicroPython, Sparkfun and Bosch example code in C/C++
# Use these files to some initial cicuit design images and collect some links to relevant sources
# see also notes on C/C++ (cpa) equivalent project;
# https://github.com/YorkEarwaker/Electrical-Engineering/blob/main/rpi-pi/cpa/snr-rsl/org/agw/een/snr/rsl/rsl_bmv080_drv.c

# #
# Import libraries for use in the programme
from machine import I2C
import time

# #
# I2C addresses for the device
# Logic set on BMV080 device as material conditional logic table
# https://docs.sparkfun.com/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080/assets/board_files/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080_v10_Schematic.pdf
reg_addr_i2c_bmv080_prime       = 0x57 # default
reg_addr_i2c_bmv080_secondary_a = 0x56 # 
reg_addr_i2c_bmv080_secondary_b = 0x55 # 
reg_addr_i2c_bmv080_secondary_c = 0x54 # 

# hard coded for default value.
# <todo: consider, a set i2c address function definition, getters and setters, >
reg_addr_i2c_bmv080 = reg_addr_i2c_bmv080_prime

# using snr_bme280_dvr.py as a template for this driver.
# I2C
# generic registry reading methods
class Device:
    
    def __init__(self, address, i2c):
        self._address = address
        self._i2c = i2c
        
# BMV080 particle sensor 
# 
class BMV080:
    
    def __init__(self, address=reg_addr_i2c_bmv080, i2c=None, **kwargs):
        
        if i2c is None:
            rasise ValueError('An I2C object is required.')
        self._device = Device(address, i2c)
        
    
        
    

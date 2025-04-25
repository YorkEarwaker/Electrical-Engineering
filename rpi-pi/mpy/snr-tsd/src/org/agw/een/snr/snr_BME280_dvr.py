#        _ _   _ _ _      _
#       /   ) / _ _ )  _ \ )
#      / (| |/ /  _ _ \ ) \ \
#     /  _    (  (_  ) \ \ \ \
#    / /  | |\ \ _ )  \_) \_) \
#   (_/   |_| \ _ _ /\ _ _ _ _ )
#  Anthropogeneic Global Warming
#  -------------------------------
# 
# Code Sources
# 
# https://randomnerdtutorials.com/raspberry-pi-pico-bme280-micropython/
# https://github.com/RuiSantosdotme/ESP-MicroPython/blob/master/code/WiFi/HTTP_Client_IFTTT_BME280/BME280.py
# https://microcontrollerslab.com/raspberry-pi-pico-w-wireless-bme280-web-server/
#
# 
# 

# 
from machine import I2C
import time

# I2C registry default address for BME280

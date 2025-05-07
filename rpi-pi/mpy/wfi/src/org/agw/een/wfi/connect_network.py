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
# network module,
#
# rp2 module,
# 
#
# time module, 
# https://docs.micropython.org/en/latest/library/time.html
#
#
# Context diagram -- work in progress
# Assuming only the microcontroller interacts with only local Wifi network of things.
#  __________________________  _______________________________________________________________________  _____________________________________
# |  Electrical Engineering  ||                      Local Internet of Things                         ||             Global  IoT             |
#        Out of Scope                                         In Scope                                               Out of Scope
#  __________________________  _______________________________________________________________________  _____________________________________
# |                          ||                                           Wifi                 local  ||                                     |
#  Device                           Microcontroller                       Router               Device      Regional Telco    SomeThing′-N^K 
#  ______   do x               _____________________________    do p     ________    do p     ________              ______   do p′     ______ 
# |      |<-------------------|            __________Flash  |<----------|        |<----------|        |            |      |<----------|      |
# |      |  get y             |           |    Micro      | |   get q   |  Wifi  |   get q   |  Wifi  |            |      |  get q′   |      |
# |      |<---------- --------| Wifi      |  _ Python_    | |<----------|  Radio |<----------|  Radio |            |      |<----------|      |
# |      |  do w              | Radio CPU | |   Prog  |   | |  do r     |  |_|   |   do r    |  |_|   |            |      |  do r'    |      |
# |      |<-------------------| |_|<--|_|<--|<--|_|   |   | |---------->|        |---------->|  CPU   |            |      |---------->|      |
# |      |  get z             |           |_|_________|___| |   get s   |        |   get s   |  |_|   |            |      |  get s′   |      |
# |______|<-------------------|_____________________________|---------->|        |---------->|  Prog  |            |      |---------->|______|
#                                                              ________ |        |           |  |_|   |            |      |
#                                                             |         |        |   do r′   |        |            |      |
#                                                             |         |        |<----------|        |            |      |
#                                                             |         |        |   get s′  |        |            |      |
#                                                             |         |        |<----------|________|            |      |
#                                                             |  Out    |  RJ45  |               do r'             |      |
#                                                             |  of     |  Telco |-------------------------------->|      |
#                                                             |  Scope  |  In/Out|               get s′            |      |
#                                                             |         |  |_|   |-------------------------------->|      |
#                                                             |         |        |               do p′             |      |
#                                                             |         |        |<--------------------------------|      |
#                                                             |         |        |               get q′            |      |
#                                                             |________ |________|<--------------------------------|______|


# #
# import libraries to use in this programme
import time
import network
import rp2

# The country code, locale
rp2.country("GB")

wifi_network_name = "Your-Wifi-Network-Name"
wifi_network_password = "Your-Wifi-Network-Password"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_network_name, wifi_network_password)



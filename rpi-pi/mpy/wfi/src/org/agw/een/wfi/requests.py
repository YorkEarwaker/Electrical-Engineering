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
# https://docs.micropython.org/en/latest/library/network.html # module
# https://docs.micropython.org/en/latest/library/network.WLAN.html # class
#
# RP2 module, quick reference
# https://docs.micropython.org/en/latest/rp2/quickref.html # module
#
# time module, 
# https://docs.micropython.org/en/latest/library/time.html # module
#
# Get started with MicroPython on Raspberry Pi Pico, 2nd Edition, Gareth Halfadree, Ben Everard
# Chapter 11, Wi-Fi connectivity with Pico W and Pico 2 W
# Turn Raspberry Pi Pico W into a network-connected node for the
# Internet of Things as you learn to unleash its Wi-Fi powers
#
# ISO 3166 Alpha-2 format
# https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
# https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
# 
# Context diagram -- work in progress
# Assuming only the microcontroller interacts with only local Wifi network of things.
# <todo: consider, mpy likely connects direct to wifi via driver not cpu.
# confirm one way or the other. code has to execute in cpu, so assume okay, >
#  __________________________  _______________________________________________________________________  _____________________________________
# |  Electrical Engineering  ||                      Local Internet of Things                         ||             Global  IoT             |
#        Out of Scope                                         In Scope                                               In Scope
#  __________________________  _______________________________________________________________________  _____________________________________
# |                          ||                                           Wifi                 local  ||                                     |
#  Device                           Microcontroller                       Router               Device      Regional Telco    SomeThing′-N^K 
#  ______   do x               _____________________________    do p     ________    do p     ________              ______   do p′     ______ 
# |      |<-------------------|            __________Flash  |<----------|        |<----------|        |            |      |<----------|      |
# |      |  get y             |           |    Micro      | |   get q   |  Wifi  |   get q   |  Wifi  |            |      |  get q′   |      |
# |      |<---------- --------| Wifi      |  _ Python_    | |<----------|  Radio |<----------|  Radio |            |      |<----------|      |
# |      |  do w              | Radio CPU | |   Prog  |   | |   do r    |  |_|   |   do r    |  |_|   |            |      |  do r'    |      |
# |      |<-------------------| |_|<--|_|<--|<--|_|   |   | |---------->|        |---------->|  CPU   |            |      |---------->|      |
# |      |  get z             |           |_|_________|___| |   get s   |        |   get s   |  |_|   |            |      |  get s′   |      |
# |______|<-------------------|_____________________________|---------->|        |---------->|  Prog  |            |      |---------->|______|
#                                                                       |        |           |  |_|   |            |      |
#                                                                       |        |   do r′   |        |            |      |
#                                                                       |        |<----------|        |            |      |
#                                                                       |        |   get s′  |        |            |      |
#                                                                       |        |<----------|________|            |      |
#                                                                       |  RJ45  |               do r'             |      |
#                                                                       |  Telco |-------------------------------->|      |
#                                                                       |  In/Out|               get s′            |      |
#                                                                       |  |_|   |-------------------------------->|      |
#                                                                       |        |               do p′             |      |
#                                                                       |        |<--------------------------------|      |
#                                                                       |        |               get q′            |      |
#                                                                       |________|<--------------------------------|______|
#
# Local device with wifi radio might be a computer like a laptop of a mobile phone or another microcontroller on the same wifi network.
#
#                                                           
#                                      RPi Pico 2 W pinout  
#                                            _____          
#                                      -----|     |-----  
#                                   1-| o ◯|_____|◯ o |-40
#                                   2-| o     USB     o |-39
#                                   3-| o             o |-38
#                                   4-| o             o |-37
#                                   5-| o             o |-36
#                                   6-| o  __         o |-35
#                                   7-| o |__| Flash  o |-34
#                                   8-| o   _______   o |-33
#                                   9-| o  | ARM   |  o |-32
#                                  10-| o  | 2035  |  o |-31
#                                  11-| o  |_______|  o |-30
#                                  12-| o  __         o |-29
#                                  13-| o |__| Areal  o |-28
#                                  14-| o  _________  o |-27
#                                  15-| o |  Wi-Fi  | o |-26
#                                  16-| o |  Radio  | o |-25
#                                  17-| o |_________| o |-24
#                                  18-| o             o |-23
#                                  19-| o             o |-22
#                                  20-| o ◯       ◯ o |-21
#                                      -----------------
#
# 

# #
# Import libraries to use in this programme
import time # to initiate delays
import network # to interact with RPi Pico W/2 W radio
import rp2 # to interact with RP2040 and RP2035 microcontroller, RPi Pico 1 and RPi Pico 2 .
import requests # 

# #
# Radio communication regulation requirements differ by jurisdiction
# Radio frequency band usage differs from one jurisdiction to another
# The country code, locale of microcontroller
# To enable the microcontroller to use all permitted radio frequencies and Wi-Fi channels
# Inform RPi Pico where in the world it is
# So as to transmit in only authorised radio frequencies for the country / jurisdiction
# Transmitting on unauthorised frequencies may break the law, and also cause radio interference
rp2.country("GB") # ISO 3166 Alpha-2 format

# #
# define Wi-Fi network credentials, uid and pwd
#<todo: read SSID and PSK from a properties file. >
# 
# Service Set Identifier SSID
wifi_network_name_ssid = "Your-Wi-Fi-Network-Name" # SSID
# Pre-Shared Key PSK
wifi_network_password_psk = "Your-Wi-Fi-Network-Password" # PSK

# #
# Connect to local Wi-Fi network
# RPi Pico W and 2 W onboard single band radio, so restricted to a single frequency spectrum 2.4GHz .
# WLAN wireless local area network, 
wlan = network.WLAN(network.STA_IF) # station mode, like any device that connects to the network, mobile phone, laptop, 
#wlan = network.WLAN(network.AP_IF) # access point mode, permit other devices to connect to the RPi Pico 
wlan.active(True) # turn RPi Pico radio on
wlan.connect(wifi_network_name_ssid, wifi_network_password_psk) # connect to the local network with credentials supplied

# #
# Check for connection status, 
# status message meanings
#  0 = the connection is down
#  1 = the radio is currently joining a network
#  2 = the radio connected but was not given an IP address by the router
#  3 = the radio has successfully connected to the network
# -1 = the radio link has failed
# -2 = the radio is connected but there is no underlying network
# -3 = the network password was rejected
# 
max_wait = 30
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1 # subtract one from max_wait
    print('Waiting for Wi-Fi connection ...')
    time.sleep(1) # wait for one second

if wlan.status() != 3: # not equals three (3) means there was some network or programe condition which cause a failure to connect
    raise RuntimeError("Network connection failed")
else: # status is three (3) means sucessful connection to the wifi network 
    print("Connected to Wi-Fi network {}. ".format(wlan.isconnected()) ) # boolean, True if connected
    print("Network: RPi Pico IP, Subnet, Gateway, DNS, {}. ".format(wlan.ifconfig()) ) # IP-level network interface parameters: IP address, subnet mask, gateway and DNS server .
# #
# make an http request to simple site at NPR
# and other internet content
#
# response = requests.get("http://text.npr.org/")
# response = requests.get("http://ipecho.net/plain")
# response = requests.get("http://earthquake.usgs.gov/fdsnws/event/"
#                        "1/query?format=text&limit=10")
response = requests.get("http://artscene.textfiles.com/"
                        "asciiart/peace.art")
[print(x) for x in response.content.splitlines()]
response.close()

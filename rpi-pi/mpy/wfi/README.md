# Wireless fidelity wfi (mpy)

MicroPython mpy WiFi, microcontroller, RPi Pico 2 W, Pico onboard WiFi 4, IEEE 802.11n, 

## Status

TODO
* <todo: consider, MicroPython RPi Pico wifi connection to laptop, >
* <todo: consider, MicroPython RPi Pico wifi connection to mobile phone, >

DONE
* <done: intent to commit>

## Connections

### Connect to local Wi-Fi router

Note the network IP level information has been changed to values in MicroPython docs

>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot

Waiting for Wi-Fi connection ...
Waiting for Wi-Fi connection ...
Waiting for Wi-Fi connection ...
Waiting for Wi-Fi connection ...
Connected to Wi-Fi network True. 
Network: RPi Pico IP, Subnet, Gateway, DNS, ('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'). 

### Connect to internet

>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot

Waiting for Wi-Fi connection ...
Waiting for Wi-Fi connection ...
Waiting for Wi-Fi connection ...
Connected to Wi-Fi network True. 
Network: RPi Pico IP, Subnet, Gateway, DNS, ('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'). 
b'<!DOCTYPE html>'
b'<html lang="en">'
b'<head>'
b'    <title>NPR : National Public Radio</title>'
b'    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">'
b'    <meta name="viewport" content="width=device-width">'
b'    <link id="favicon" rel="shortcut icon" type="image/png" href="">'
b'    <style>'
b'        body {'
b'    display: block;'
b'    padding: 0px 20px;'
b'    max-width: 550px;'
b'    margin: 0 auto;'
b'    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";'
b'}'
b''
b'.full-version-link {'
b'    margin-left: 15px;'
b'}'
b''
b'.slug-line {'
b'    font-size: 1.1rem;'
b'    margin-bottom: 15px;'
b'}'
b''
b'.hr-line {'
b'    position: relative;'
b'    height: 4px;'
b'}'
b''
b'.hr-line:after {'
b'    background: linear-gradient(to right, #e60000 0%, #e60000 33.33%, #000000 33.33%, #000000 66.66%, #3366CC 66.66%);'
b'    position: absolute;'
b"    content: '';"
b'    height: 4px;'
b'    right: 0;'
b'    left: 0;'
b'    top: 0;'
b'}'
b''
b'hr.gray {'
b'    border: .5px solid gray;'
b'}'
b''
b'.story-title {'
b'    line-height: 2rem;'
b'    font-size: 1.5rem;'
b'    margin: 0;'
b'}'
b''
b'.topic-heading {'
b'    line-height: 2rem;'
b'    font-size: 1.5rem;'
b'}'
b''
b'.topic-container>ul {'
b'    padding: 0;'
b'    line-height: 1.4rem;'
b'}'
b''
b'.topic-container li {'
b'    display: block;'
b'    padding-bottom: 15px;'
b'}'
b''
b'.topic-container {'
b'    margin-top: 20px;'
b'}'
b''
b'.topic-date {'
b'    margin: 20px 0;'
b'    font-style: italic;'
b'}'
b''
b'.paragraphs-container {'
b'    line-height: 1.5rem;'
b'}'
b''
b'.button:link,'
b'.button:visited {'
b'    background-color: white;'
b'    color: black;'
b'    border: 2px solid black;'
b'    padding: 4px 8px;'
b'    text-align: center;'
b'    text-decoration: none;'
b'    display: inline-block;'
b'}'
b''
b'.button:hover,'
b'.button:active {'
b'    background-color: black;'
b'    color: white;'
b'}'
b''
b'.lower-nav-container {'
b'    margin-top: 40px;'
b'}'
b''
b'.lower-nav-container li {'
b'    margin-left: 0;'
b'    display: inline;'
b'    padding-right: 20px;'
b'}'
b''
b'h6 {'
b'  text-transform: uppercase;'
b'}'
b''
b'    </style>'
b'</head>'

Portion of the text html above brought back from NPR .

## References

Terms
* WiFi [WP](https://en.wikipedia.org/wiki/Wi-Fi)

Documentation
* MicroPython, wlan [WS](https://docs.micropython.org/en/latest/rp2/quickref.html#wlan), wifi

Datasheet
* Raspberry Pi, datasheet [PDF](https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf), Connecting to the Internet with Raspberry Pi Pico W-series. Getting online with C/C++ or MicroPython on W-series devices.

Books
* Get Started with MicroPython on Raspberry Pi Pico, Chapter 11, Wi-Fi connectivity with Pico W and Pico 2 W
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
{% raw %}b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <title>NPR : National Public Radio</title>\n    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">\n    <meta name="viewport" content="width=device-width">\n    <link id="favicon" rel="shortcut icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAHlJREFUOBFjYBgFFIcA48cYpf/opvAv+YouxODXshZDbFONDSMLSJRv8V245KdYZTD7//8XcDFGRgkwe2O1NVzMv/UomA02AMQCaUQ2CCQG0ohsEEgMphHEBgEmCIWdRNeMTRXYBTBnw2iYQpjTYXx022Hio/RAhwAAjXEfJrIXnj4AAAAASUVORK5CYII=">\n    <style>\n        body {\n    display: block;\n    padding: 0px 20px;\n    max-width: 550px;\n    margin: 0 auto;\n    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";\n}\n\n.full-version-link {\n    margin-left: 15px;\n}\n\n.slug-line {\n    font-size: 1.1rem;\n    margin-bottom: 15px;\n}\n\n.hr-line {\n    position: relative;\n    height: 4px;\n}\n\n.hr-line:after {\n    background: linear-gradient(to right, #e60000 0%, #e60000 33.33%, #000000 33.33%, #000000 66.66%, #3366CC 66.66%);\n    position: absolute;\n    content: \'\';\n    height: 4px;\n    right: 0;\n    left: 0;\n    top: 0;\n}\n\nhr.gray {\n    border: .5px solid gray;\n}\n\n.story-title {\n    line-height: 2rem;\n    font-size: 1.5rem;\n    margin: 0;\n}\n\n.topic-heading {\n    line-height: 2rem;\n    font-size: 1.5rem;\n}\n\n.topic-container>ul {\n    padding: 0;\n    line-height: 1.4rem;\n}\n\n.topic-container li {\n    display: block;\n    padding-bottom: 15px;\n}\n\n.topic-container {\n    margin-top: 20px;\n}\n\n.topic-date {\n    margin: 20px 0;\n    font-style: italic;\n}\n\n.paragraphs-container {\n    line-height: 1.5rem;\n}\n\n.button:link,\n.button:visited {\n    background-color: white;\n    color: black;\n    border: 2px solid black;\n    padding: 4px 8px;\n    text-align: center;\n    text-decoration: none;\n    display: inline-block;\n}\n\n.button:hover,\n.button:active {\n    background-color: black;\n    color: white;\n}\n\n.lower-nav-container {\n    margin-top: 40px;\n}\n\n.lower-nav-container li {\n    margin-left: 0;\n    display: inline;\n    padding-right: 20px;\n}\n\nh6 {\n  text-transform: uppercase;\n}\n\n    </style>\n</head>\n\n\n<body>\n<header>\n  <p>Text-Only Version <a class="full-version-link button" href="https://www.npr.org/">Go To Full Site</a></p>\n</header>
{% endraw %}

## References

Terms
* WiFi [WP](https://en.wikipedia.org/wiki/Wi-Fi)

Documentation
* MicroPython, wlan [WS](https://docs.micropython.org/en/latest/rp2/quickref.html#wlan), wifi

Datasheet
* Raspberry Pi, datasheet [PDF](https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf), Connecting to the Internet with Raspberry Pi Pico W-series. Getting online with C/C++ or MicroPython on W-series devices.

Books
* Get Started with MicroPython on Raspberry Pi Pico, Chapter 11, Wi-Fi connectivity with Pico W and Pico 2 W
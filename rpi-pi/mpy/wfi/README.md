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
Network: RPi Pico IP, Subnet, Gateway, DNS, ('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'). {% raw %}
b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <title>NPR : National Public Radio</title>\n    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">\n    <meta name="viewport" content="width=device-width">\n    <link id="favicon" rel="shortcut icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAHlJREFUOBFjYBgFFIcA48cYpf/opvAv+YouxODXshZDbFONDSMLSJRv8V245KdYZTD7//8XcDFGRgkwe2O1NVzMv/UomA02AMQCaUQ2CCQG0ohsEEgMphHEBgEmCIWdRNeMTRXYBTBnw2iYQpjTYXx022Hio/RAhwAAjXEfJrIXnj4AAAAASUVORK5CYII=">\n    <style>\n        body {\n    display: block;\n    padding: 0px 20px;\n    max-width: 550px;\n    margin: 0 auto;\n    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";\n}\n\n.full-version-link {\n    margin-left: 15px;\n}\n\n.slug-line {\n    font-size: 1.1rem;\n    margin-bottom: 15px;\n}\n\n.hr-line {\n    position: relative;\n    height: 4px;\n}\n\n.hr-line:after {\n    background: linear-gradient(to right, #e60000 0%, #e60000 33.33%, #000000 33.33%, #000000 66.66%, #3366CC 66.66%);\n    position: absolute;\n    content: \'\';\n    height: 4px;\n    right: 0;\n    left: 0;\n    top: 0;\n}\n\nhr.gray {\n    border: .5px solid gray;\n}\n\n.story-title {\n    line-height: 2rem;\n    font-size: 1.5rem;\n    margin: 0;\n}\n\n.topic-heading {\n    line-height: 2rem;\n    font-size: 1.5rem;\n}\n\n.topic-container>ul {\n    padding: 0;\n    line-height: 1.4rem;\n}\n\n.topic-container li {\n    display: block;\n    padding-bottom: 15px;\n}\n\n.topic-container {\n    margin-top: 20px;\n}\n\n.topic-date {\n    margin: 20px 0;\n    font-style: italic;\n}\n\n.paragraphs-container {\n    line-height: 1.5rem;\n}\n\n.button:link,\n.button:visited {\n    background-color: white;\n    color: black;\n    border: 2px solid black;\n    padding: 4px 8px;\n    text-align: center;\n    text-decoration: none;\n    display: inline-block;\n}\n\n.button:hover,\n.button:active {\n    background-color: black;\n    color: white;\n}\n\n.lower-nav-container {\n    margin-top: 40px;\n}\n\n.lower-nav-container li {\n    margin-left: 0;\n    display: inline;\n    padding-right: 20px;\n}\n\nh6 {\n  text-transform: uppercase;\n}\n\n    </style>\n</head>\n\n\n<body>\n<header>\n  <p>Text-Only Version <a class="full-version-link button" href="https://www.npr.org/">Go To Full Site</a></p>\n</header>\n\n\n<main>\n  <p>\n    \n  </p>\n\n  <div class="topic-container">\n    <h1 class="topic-heading">NPR : National Public Radio</h1>\n    <div class="hr-line"></div>\n    <p class="topic-date">Thursday, May 8, 2025</p>\n    <ul>\n      \n        <li><a class="topic-title" href="/nx-s1-5383918">Economists warn Trump\'s research cuts could have dire consequences for GDP</a></li>\n      \n        <li><a class="topic-title" href="/g-s1-64816">Americans are already seeing Trump\'s tariffs kick in. They sent in receipts to prove it</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5389973">Trump announces a trade deal with the U.K., the first since his tariffs sent markets reeling</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5389925">Cancer-causing chemicals are in many beauty products women use, a study finds</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5387739">Glittering blue creatures are washing up on California beaches. Here\'s why</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5390452">No new pope elected yet after black smoke pours out of Sistine Chapel\'s chimney</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5388480">Once-fringe activists are fighting to be the voice of the anti-abortion movement</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5389747">80 years after VE Day a veteran says, \'I hope people will see the futility of it all\'</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5387659">Georgia\'s Brian Kemp becomes latest swing state governor to decline a run for Senate</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5371628">Discovering a mom we never knew, in letters she saved from WWII soldiers</a></li>\n      \n        <li><a class="topic-title" href="/g-s1-64726">A federal court rules that R\xc3\xbcmeysa \xc3\x96zt\xc3\xbcrk must be transferred to detention in Vermont</a></li>\n      \n        <li><a class="topic-title" href="/g-s1-64640">After an Arizona man was shot, an AI video of him addresses his killer in court</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5389907">Wanda Sykes is grateful her audience sticks with her</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5389885">Medicaid payments barely keep hospital mental health units afloat. Federal cuts could sink them</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5389962">Trump picks Casey Means for surgeon general after his first nominee withdraws</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5382445">GOP-led states are passing new restrictions for voters to get issues on the ballot</a></li>\n      \n        <li><a class="topic-title" href="/1234569831">Sampha: Tiny Desk Concert</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5388994">On Teacher Appreciation Week, union leaders say teachers are underpaid and under attack</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5377615">How one writer quit dieting and discovered her strength through weightlifting</a></li>\n      \n        <li><a class="topic-title" href="/nx-s1-5389922">The USDA\'s chief says the agency is trying to fill key jobs after paying 15,000 workers to leave</a></li>\n      \n    </ul>\n  </div>\n</main>\n\n\n<div class="hr-line"></div>\n<nav>\n<p>Topics</p>\n<ul>\n    <li><a href="/1001">News</a></li>\n    <li><a href="/1008">Culture</a></li>\n    <li><a href="/1039">Music</a></li>\n</ul>\n</nav>\n\n\n<footer>\n  <nav class="lower-nav-container">\n    <li><a href="/614470770">Contact Us</a></li>\n    <li><a href="/179876898">Terms of Use</a></li>\n    <li><a href="/179881519">Permissions</a></li>\n    <li><a href="/179878450">Privacy Policy</a></li>\n  </nav>\n\n  <p>&copy NPR</p>\n</footer>\n\n</body>\n</html>\n'
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
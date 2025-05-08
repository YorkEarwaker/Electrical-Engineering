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
b''
b''
b'<body>'
b'<header>'
b'  <p>Text-Only Version <a class="full-version-link button" href="https://www.npr.org/">Go To Full Site</a></p>'
b'</header>'
b''
b''
b'<main>'
b'  <p>'
b'    '
b'  </p>'
b''
b'  <div class="topic-container">'
b'    <h1 class="topic-heading">NPR : National Public Radio</h1>'
b'    <div class="hr-line"></div>'
b'    <p class="topic-date">Thursday, May 8, 2025</p>'
b'    <ul>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5383918">Economists warn Trump\'s research cuts could have dire consequences for GDP</a></li>'
b'      '
b'        <li><a class="topic-title" href="/g-s1-64816">Americans are already seeing Trump\'s tariffs kick in. They sent in receipts to prove it</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5389973">Trump announces a trade deal with the U.K., the first since his tariffs sent markets reeling</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5377615">How one writer quit dieting and discovered her strength through weightlifting</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5387739">Glittering blue creatures are washing up on California beaches. Here\'s why</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5390452">No new pope elected yet after black smoke pours out of Sistine Chapel\'s chimney</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5389925">Cancer-causing chemicals are in many beauty products women use, a study finds</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5389747">80 years after VE Day a veteran says, \'I hope people will see the futility of it all\'</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5387659">Georgia\'s Brian Kemp becomes latest swing state governor to decline a run for Senate</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5371628">Discovering a mom we never knew, in letters she saved from WWII soldiers</a></li>'
b'      '
b'        <li><a class="topic-title" href="/g-s1-64726">A federal court rules that R\xc3\xbcmeysa \xc3\x96zt\xc3\xbcrk must be transferred to detention in Vermont</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5389962">Trump picks Casey Means for surgeon general after his first nominee withdraws</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5389907">Wanda Sykes is grateful her audience sticks with her</a></li>'
b'      '
b'        <li><a class="topic-title" href="/g-s1-64640">After an Arizona man was shot, an AI video of him addresses his killer in court</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5389885">Medicaid payments barely keep hospital mental health units afloat. Federal cuts could sink them</a></li>'
b'      '
b'        <li><a class="topic-title" href="/1234569831">Sampha: Tiny Desk Concert</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5382445">GOP-led states are passing new restrictions for voters to get issues on the ballot</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5388994">On Teacher Appreciation Week, union leaders say teachers are underpaid and under attack</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5388480">Once-fringe activists are fighting to be the voice of the anti-abortion movement</a></li>'
b'      '
b'        <li><a class="topic-title" href="/nx-s1-5389922">The USDA\'s chief says the agency is trying to fill key jobs after paying 15,000 workers to leave</a></li>'
b'      '
b'    </ul>'
b'  </div>'
b'</main>'
b''
b''
b'<div class="hr-line"></div>'
b'<nav>'
b'<p>Topics</p>'
b'<ul>'
b'    <li><a href="/1001">News</a></li>'
b'    <li><a href="/1008">Culture</a></li>'
b'    <li><a href="/1039">Music</a></li>'
b'</ul>'
b'</nav>'
b''
b''
b'<footer>'
b'  <nav class="lower-nav-container">'
b'    <li><a href="/614470770">Contact Us</a></li>'
b'    <li><a href="/179876898">Terms of Use</a></li>'
b'    <li><a href="/179881519">Permissions</a></li>'
b'    <li><a href="/179878450">Privacy Policy</a></li>'
b'  </nav>'
b''
b'  <p>&copy NPR</p>'
b'</footer>'
b''
b'</body>'
b'</html>'

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
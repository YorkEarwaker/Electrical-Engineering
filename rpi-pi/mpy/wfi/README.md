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

>	b''

>	b''

>	b'VVVVVVV, VVVVVVVV   .VVV.    ,VVVVVV, VVVVVVVV    ,VVVVVV, VV.   VV'

>	b"VV   .VV VV        .VV VV.   VV    '' VV          VV'  'VV VVV.  VV"

>	b"VVVVVVV' VVVVVV    VVVVVVV   VV       VVVVVV      VV    VV VVVV. VV"

>	b'VV       VV      .VV     VV  VV    ,, VV          VV.  .VV VV  VVVV'

>	b"VV       VVVVVVV.VV       VV.'VVVVVV' VVVVVVVV    'VVVVVV' VV   VVV"

>	b''

>	b'           VVVVVVVV    .VVV.    VVVVVVV, VVVVVVVV VV    VV'

>	b'           VV         .VV VV.   VV    VV    VV    VV    VV'

>	b"           VVVVVV    .VVVVVVV.  VVVVVVV'    VV    VVVVVVVV"

>	b'           VV       .VV     VV. VV  VV.     VV    VV    VV'

>	b'           VVVVVVVV.VV       VV.VV   VV.    VV    VV    VV'

>	b''

>	b''

>	b''

>	b'                     /:'

>	b'                    ///:,'

>	b'                   //////:,'

>	b'      .W.          ////////:,.'

>	b'     .WWW,         ///////////::,.'

>	b'    .WWWWWW,       ////////////////::,,.'

>	b'   .WWWWWWWWW,.     ////////////////////::,,.'

>	b'  .WWWWWWWWWWWWW,.  ///////////////////////////:,.              ()'

>	b'  WWWWWWWWWWWWWWWWW,.//////////////////////////////.            /'

>	b'  WWWWWWWWWWWWWWWWWWWWW:,.//////////////////////////.        Y  :'

>	b'  WWWWWWWWWWWWWWWWWWWWWWWWWWW:,,.///////////////////.        : /  ()'

>	b'  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW:,,.///////////.,,.      Y  /'

>	b'   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW:,///.:WWWWWW,    :----'

>	b'   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW,//,WWWWWWWWW:  /'

>	b'    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW///:WWWWWWWWWW./'

>	b"     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'///:WWWWWWWWVVV."

>	b"      'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'/////WWWWWWW//''V."

>	b"       'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW:,./.,WWWWWW//"

>	b"         'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW//W,"

>	b"            'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW//WWW,"

>	b"                 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW//WWWWW:"

>	b"                   '''WWWWWWWWWWW/''WWWWWWWWWWWWWWWWWWWW:"

>	b"                        '''''''  ,WWWWWWWWWWWWWWWWWWWWWW'"

>	b"                            .,,::WWWWWWWWWWWWWWWWWWWWWW'"

>	b"                      .,,:WWWWWWWWWWWWWWWWWWWWWWWWWWW:'"

>	b"            ..,,,,,:WWWWWWWWWWWWWWWWWWWWWWWWWWWW::''"

>	b"       'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW:'''"

>	b"        ''WWWWWWWWWWWWWWWWWWWWWWWWWW'"

>	b"          '''WWWWWWWWWWWWWWWWWWWWW'"

>	b"             '''WWWWWWWWWWWWWWWW'"

>	b"                 '''WWWWWWWWW'"

>	b"                       '''"

>	b'\x1a\x00\x00\x00\x00\x00\x00\x00'

Ascii text above brought back from; artscene textfiles com asciiart peace.art . Formated in markdown blockqoute and newline

## References

Terms
* WiFi [WP](https://en.wikipedia.org/wiki/Wi-Fi)

Documentation
* MicroPython, wlan [WS](https://docs.micropython.org/en/latest/rp2/quickref.html#wlan), wifi

Datasheet
* Raspberry Pi, datasheet [PDF](https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf), Connecting to the Internet with Raspberry Pi Pico W-series. Getting online with C/C++ or MicroPython on W-series devices.

Books
* Get Started with MicroPython on Raspberry Pi Pico, Chapter 11, Wi-Fi connectivity with Pico W and Pico 2 W
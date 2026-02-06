# Raspberry Pi Zero rpi-z

Single board computer SBC. 

## Notes

Please see
* For directions on headless connection to RPi Zero 2 W with 1) standard USB A to Micro USB B cable or 2) Raspberry Pi Debug Probe or 3) USB TTL to UART cable. Work in progress.
* Headless, RPi Zero 2 W, configuration & connection guide, [WS](https://forums.raspberrypi.com/viewtopic.php?t=394836), Raspberry Pi Forums
* The official Getting Started Raspberry Pi Documentation does not cover the use case described in the forum post.
* For attempts at process see inline below headings; Output - headless to RPi Zero 2 W with ...

This should not be difficult; to communicate with RPi Zero headless. But it is in different use cases. This is a barrier to entry for use of the Raspberry Pi product range particularly its SBC's . Headless via standard USB A to Micro USB B cable must be the minimum use case in the Raspberry Pi Documentation. To date none of the three use cases above are officially documented.

## Status

TODO
* <todo: consider, hello world project>
* <todo: consider, test USB device disconnection issue with RPi OS and RPi Pico, does RPi OS endlessly increment USB device number as Ubuntu does? RPi OS on RPi Zero SBC, >
* <todo: consider, use as platform for Bosch Particlate Sensor for C code application sensor particulate value readings, >
* <todo: consider, list prerequisits for headless RPi Zero access of various sorts, setup before powering on, ssh file, WiFi wpa_supplicant.conf, Ethernet USB On-The-Go, Bluetooth, other, and so on, >
* <todo: consider, RYO voltage down shift device, resistors? research and test, for use with RPi Pico MCU powered by 5V RPi Zero SBC, >
* <todo: consider, investigate Ethernet connection to RPi Zero, first order of priority, On-The-Go cable RPi Zero type micro USB B  peripheral Dell laptop standard USB A acts as host, seemed not to work, buy anther cable, probs not, likely RPI Zero config issue, in Ubuntu desktop open bootfs add modules-load=dwc2,g_ether after rootwait in cmdline.txt and add dtoverlay=dwc2 under all section in config.txt, from tutorial, source offical Raspberry Pi docs, >
* <todo: consider, investigate Ethernet connection to RPi Zero, first order of priority, USB cable RPi Zero type micro B USB peripheral Dell laptop USB C acts as host, >
* <todo: consider, RPi Zero as mountable flash device, see RPi Magaizine article in references below, >
* <todo: consider, reuse old laptop screen as second dispaly for Dell and/or display for RPi Zero SBC, see references below for example, >
* <todo: consider, investigate scavange old laptop keyboard as standalone keyboard, probs more difficult than screen dispaly reuse? >
* <todo: consider, to setup RPi Zero correctly will have to purchase secondary BoM items, screen display, keyboard, and so on, >
* <todo: consider, is there some way to make headless RPi Zero work with USB cable work?, or is this just impossible? see heading; Output - headless to RPi Zero 2 W with USB cable, >
* <todo: consider, ascii art, in stand alone files to reflect changes made here. >

DONE
* <done: consider, intent to commit>
* <done: consider, as deployment option for Bosch BMV080 particulate matter sensor, >
* <done: consider, bill of materials for RPi Zero, compelted offline BoM in spreadsheet circa £64 inclusive 'useful' extras, >
* <done: consider, purchase of RPi Zero 2 W, and other items, completed, >
* <done: consider, for future use, first pass at wpa_supplicat.conf file, a Debian configuration file for WiFi, see referrences below,  >
* <done: consider, does the Micro USB B - OTG? - on the RPi Debug Probe device exhibit disconnection issue with the Linux Ubuntu LTS 24.04.3, Yes! likely same kernel issue, >
* <done: consider, request login credentials from The Pi Hut for the Micro SD Card with RPi OS pre installed, email sent 2026-01-01, >
* <done: consider, ascii art, RPi Zero , GPIO pinout diagram and table with pin descriptors, for inclusion in code file comment headers for circuit diagrams, wip>

## Hardware

Bill of materials, BoM, original
* Raspberry Pi Zero 2 W, [WS](https://www.raspberrypi.com/products/raspberry-pi-zero/), Raspberry Pi, acquired
* Power Supply, 12.75 Raspberry Pi, acquired
* Micro SD Card, with RPi OS preinstalled, [WS](https://thepihut.com/products/noobs-preinstalled-sd-card?variant=20649315598398), Raspberry Pi, acquired
* Micro SD Card Adapter, Raspberry Pi, acquired
* Micro SD to SD Extension Cable, acquired
* USB cable, standard USB A to Micro USB B, acquired

Bill of material, BoM +, USB to TTL serial communication device, UART, USB to TTL serial interface board, interface boards with serial bridge chip onboard
* Raspberry Pi Debug Probe, (RP2404), com [WS](https://www.raspberrypi.com/products/debug-probe/), Raspberry Pi, acquired
* USB TTL, CP2102 UART Interface Board, (CP2102), [WS](https://cpc.farnell.com/sb-components/sku24797/usb-ttl-cp2102-uart-interface/dp/SC20242), CPC Farnell, SD Components [WS](https://shop.sb-components.co.uk/products/usb-ttl), acquired, 

Bill of material, BoM +, To be considered --- to be purchased only if necessary, don't have one as intent was use headless from start, but may have to buy one for other purposes
* HDMI cable, Mini HDMI plug to HDMI plug, connect RPi Zero Mini HDMI socket to display (screen) HDMI socket, acquired
* Display (screen), pending tbd, will have to meet broader requirements than this project
* Keyboard, pending tbd, will have to meet broader requirements than this project

Bill of material, BoM +, To be considered --- helper tech
* 40 Pin Raspberry Pi PCB GPIO Quick Connect Clip, [WS](https://www.kickstarter.com/projects/flatmax/pcb-quick-connect-clip-40-pin-raspberry-pi-compati), looks very interesting! no solder RPi SBC's prototyping, pending tbd,

Diagram of the eight main components on board the RPi Zero single board computer SBC. Larger than actual physical form factor.
```
        ---------------------------------------------------------------------------
      |         o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o          | 
      |         o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o       ___|_
      |  ____________                              GPIO                         |   | |
      |  \           |        _________________                                =| C |C|
      |  >   Micro   |       |       SOC       |    _____________              =| a |S|
      |  >    SD     |       |    BCM2710A1    |   |             |             =| m |I|
      |  >   Card    |       |                 |   |    WIFI     |             =| e |-|
      |  |   Slot    |       |     RP3A0-AU    |   |  Bluetooth  |             =| r |2|
      |  ------------        |       2041      |   |             |              | a | |
      |       ____________   |      200826     |    -------------               |   | |
      |      |   MTCONN   |   -----------------     _________     _________     -------
      |      |    Mini    |                        |   OTG   |   | PWR IN  |        |
      |      |    HDMI    |                        | USB 2.0 |   | USB 5V  |        |
       ------/____________\------------------------/_________\---/_________\--------
```

Warning! Will require to shift voltage down to 3V with 'bridge' device if 
* RPi Zero SBC provides 5V power to breadboard power rail 1 via its GPIO pins,
* RPi Pico MCU requires 3V power, if powered by connection via breadboard to power rails,
* Voltage shift device takes 5V power from power rail 1 charge passes through shift device down shifted to 3V to power rail 2. Use resistors to RYO down shift power instead of COTS device?
* RPi Pico MCU and other 3V devices take power for breadboard power rail 2.

## Software

### Prerequisites
Requirement for a serial communication program on Dell Ubuntu laptop to communicate via RPi Debug Probe, USB to UART connection, with RPi Zero 2 W . 

Software - Serial communication tool, candidates
* GNU Screen, [WP](https://en.wikipedia.org/wiki/GNU_Screen), org [WS](https://www.gnu.org/software/screen/), GNU
* GNU Screen, User Manual, org [WS](https://www.gnu.org/software/screen/manual/screen.html), GNU
* GNU Screen, Quick Reference, net [WS](https://aperiodic.net/screen/quick_reference), Aperiodic, like from WP page
* Minicom, org [WS](https://salsa.debian.org/minicom-team/minicom), Salsa, Debian, 
* Minicom, Ubuntu Introduction, com [WS](https://help.ubuntu.com/community/Minicom), Ubuntu

### Libs

Raspberry Pi
* raspberry-gcc10.2.1-r2, SYS GCC for Windows x32 bit Platforms,[WS](https://sysprogs.com/getfile/2076/raspberry-gcc10.2.1-r2.exe/)
* raspberry64-gcc10.2.1, SYS GCC for Windows x64 bit Platforms, [WS](https://sysprogs.com/getfile/1804/raspberry64-gcc10.2.1.exe)


## Output - headless to RPi Zero 2 W with USB TTL to UART
Third Process. Attempting to connect to the RPi Zero 2 W 'headless. Using USB TTL to UART interface board. USB to serial conversion may also support, RS232, ... 
* Partial success! :) 50% 
* Two sub processes; firstly USB provides power, secondly mains provides power
* Interface boards have serial bridge chip onboard
* Chips listed may have greater capability in addition to capability as Serial bridge chips 
* Some interface boards will have six (6) or more pins
* The example circuit diagram shows an interface board with four (4) pins
* Integration (interface) boards can be bought as stand alone units. That is without cable and jumper wires and casing, which have to be purchased separately. But offer greater component reuse if used for no solder prototyping.

Primary Sources - serial bridge chip, USB to serial conversion
* RP2404, PDF, Raspberry Pi, datasheet, <todo: source datasheet from manufacturer>
* PL2303, [PDF](https://www.puntoflotante.net/PL2303.pdf), , datasheet, <todo: source datasheet from manufacturer>
* PL2303GS, <todo: is this specifically Arduino compatible? >
* PL2303HX, 
* PL2303TA, <todo: is this specifically RPi compatible? >
* CP2102, board [PDF](https://www.farnell.com/datasheets/4020550.pdf), bridge chip Silicon Laboratories [PDF](https://cdn.sparkfun.com/assets/c/7/7/b/f/cp2102.pdf), Silicon Laboratories CP2102/9 [PDF](https://www.silabs.com/documents/public/data-sheets/CP2102-9.pdf), datasheet, 
* CH340, 
* CH340C, [PDF](https://www.farnell.com/cad/4020551.pdf), , datasheet, <todo: source datasheet from manufacturer>
* <todo; other datasheets for other serial bridge chip sets to be sourced for other interface boards, ... >

Secondary Sources
* ...

Context Diagram - USB provides power, USB TTL to UART 3V + USB power 5V
* Sub process one
```                                   
             RPi Zero 2 W                             USB TTL to UART device                                   Dell Ubuntu
             -----------             Serial                -----------                Serial                   -----------
            |       o o |          Connection        UART |o       ___| Some        Connection                |___        |
            |       o o | GPIO ---------------------- PIN |o  SBC |___  USB ------------------- standard USB A ___|       |
            |       o o |      Sink < Power < Source  OUT |o          | A/B/C   Sink < Power < Source         |           |
             -----------            < Data >               -----------               < Data  >                 -----------
                                                      Serial Bridge Chip SBC
```
Circuit Diagram - USB provides power, USB TTL to UART 3V + USB power 5V
* Sub process one
* Work in progress to finish, safety circuit dependency
```     
USB TTL to UART device
Interface board with or without a cable or casing
to one or more of; USB A, Micro USB B, USB C, ...
                                                  Chip set. PL2303, CP2102, ... others
                                                  Software. ?
             _______
            |       |         ʌ  To Host          | ---------- | ----------- | --------|------------------------------- |
            | USB A |                             | Pin Number | UART Signal | Colour  | Description                    | 
           -|_______|-                            | ---------- | ----------- | ---------------------------------------- |
           |         |        <  The USB          | 1          | TX          | Green   | 3V3 logic (Output of USB port) |
Serial     |   ___   |           Plug             | 2          | GND         | Black   | GND       (Ground)             |
Bridge  >  |  |SBC|  |                            | 3          | RX          | White   | 3V3 logic (Input to USB port)  |
Chip       |   ---   |                            | 4          | PWR         | Red     | 5V 500mA  (Power)              |
           |         |        v  To Target        | ---------- | ----------- | --------|------------------------------- |
Pin Out >  | o o o o |           UART 
            ---------  
             |     |          <  The device cable
              |||||           <  The (serial UART) jumper wires, may be coloured differently from pinout table example
             1 2 3 4            
             | | | | PWR in this scenario            
             |-(-(-(--------|
               | |-(-----|  |       
               |---(--|  |  |
                   |  |  X  X
   Safety circuit--|  |  T  R
   here to stop       |      
   reverse polirity   |  T  T
   & over voltage     |  R  R         
   TBD-------------|  |  A  A
                   |  |  U  U
                   |  |   
                R  R    14 15
                W  W     O  O
                P  P  D  I  I
                V  V  N  P  P
                5  5  G  G  G
        ---------------------------------------------------------------------------
                2  4  6  8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40            Raspberry Pi Zero GPIO
      |         o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o          | 
      |         o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o          |
                1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 
```
Circuit Diagram - Safety circuit, 
* <todo; consider, reverse polarity protection, Schottky diod rated 2A, or MOFSET based protection circuit, >
* <todo; consider, voltage ragulator and over voltage, low drop out (LDO) regulator, or buckly regulator, transient voltage surpressor TVS diode, >
* <todo; consider, prevent overcurrent damage, 2.5A to 3A amp fuse, smothing capacitors 100μF 10μF, crowbar circuit, >
* <todo: consider, other electical charge protection measures, tbd ... >
* Sub process one
* Work in progress to finish
```
TBD 
                   |          ʌ To the circuit board, the USB plug to host USB port
                   |          < 5V, the circuit board PWR jumper wire, 5V from host
             . . . 4            
                   | PWR in this scenario            
                   |  
   Safety circuit--|  
   here to stop             
   reverse polirity    <todo: safety circuit diagram here, see candidate componenets above, wip >
   & over voltage              
   TBD-------------|   
                   |   
                 | |   
                 2 4    
                 | |            v To the Raspberry Pi Zero GPIO, the target
    5V|--------- |-|            < 5V, GPIO pins connected directly to 5V net, RPi Zero device, 

```
Context Diagram - mains provides power, USB TTL to UART 3V + mains power 5V
* Sub process two
```                                   
             RPi Zero 2 W                       USB TTL to UART device                                   Dell Ubuntu
             -----------          Serial             -----------                Serial                   -----------
   PWR IN   |___    o o |       Connection     UART |o       ___| Some        Connection                |___        |
Micro USB B  ___|   o o | GPIO ---------------- PIN |o  SBC |___  USB ------------------- standard USB A ___|       |
 Src > Snk  |       o o |                       OUT |o          | A/B/C   Sink < Power < Source         |           |
             -----------         < Data >            -----------               < Data >                  -----------
                                                Serial Bridge Chip SBC
```

Circuit Diagram - mains provides power, USB TTL to UART 3V + mains power 5V
* Sub process two
```     
USB TTL to UART device
Interface board with or without a cable or casing
to one or more of; USB A, Micro USB B, USB C, ...
                                                  Chip set. PL2303, CP2102, ... others
                                                  Software. ?
             _______
            |       |         ʌ  To Host          | ---------- | ----------- | --------|------------------------------- |
            | USB A |                             | Pin Number | UART Signal | Colour  | Description                    | 
           -|_______|-                            | ---------- | ----------- | ---------------------------------------- |
           |         |        <  The USB          | 1          | TX          | Green   | 3V3 logic (Output of USB port) |
Serial     |   ___   |           Plug             | 2          | GND         | Black   | GND       (Ground)             |
Bridge  >  |  |SBC|  |                            | 3          | RX          | White   | 3V3 logic (Input to USB port)  |
Chip       |   ---   |                            | 4          | PWR         | Red     | 5V 500mA  (Power)              |
           |         |        v  To Target        | ---------- | ----------- | --------|------------------------------- |
Pin Out >  | o o o o |           UART 
            ---------  
             |     |          <  The device cable
              |||||           <  The (serial UART) jumper wires, may be coloured differently from pinout table example
             1 2 3 4            
             | | | | PWR N/A in this scenario            
             |-(-(----------|
               | |-------|  |       
               |------|  |  |
                      |  X  X
                      |  T  R
                      |      
                      |  T  T
                      |  R  R         
                      |  A  A
                      |  U  U
                      |   
                R  R    14 15
                W  W     O  O
                P  P  D  I  I
                V  V  N  P  P
                5  5  G  G  G
        ---------------------------------------------------------------------------
                2  4  6  8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40            Raspberry Pi Zero GPIO
      |         o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o          | 
      |         o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o          |
                1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 
```

### Prerequisites
Requirement for a serial communication program on Dell Ubuntu laptop to communicate via USB TTL serial cable, USB to UART connection, with RPi Zero 2 W . 

Hardware - USB to UART serial communication device, examples one of the items below
* USB to TTL Serial Cable for Raspberry Pi (PL2303TA) [WS](https://thepihut.com/products/usb-to-ttl-serial-cable-debug-console-cable-for-raspberry-pi), The Pi Hut, 
* PL2303 PL2303HX/PL2303TA USB To RS232 TTL Converter Adapter Module with Dust-proof Cover PL2303HX for arduino download cable, [WS](https://www.aliexpress.com/item/1005007103101747.html), Aliexpress, appears Raspberry Pi compatible, appears the same product as The Pi Hut but lower cost. 
* The PL2303 PL2303HX/PL2303TA integration (interface) boards, stand alone. PL2303 USB UART Module (USB-A)
* USB TTL, CP2102 UART Interface Board, (CP2102), [WS](https://cpc.farnell.com/sb-components/sku24797/usb-ttl-cp2102-uart-interface/dp/SC20242), CPC Farnell, acquired, 
* A N Other cable or device for USB to UART connectivity, Caution! requires TX/RX 3V3 to RPi Zero 2 W via GPIO pin UART connection, otherwise likely have to use resistors and a bread board to pull down to 3V3, many serial communication integration boards are TX/RX 3V3 .

### Connect RPi Zero 2 W to USB TTL serial cable
* Scenario one/Scenario two
* Scenario two. Identical in concept and mostly similar in execution to RPi Debug Probe [WS](https://github.com/YorkEarwaker/Electrical-Engineering/tree/main/rpi-z#output---headless-to-rpi-zero-2-w-with-raspberry-pi-debug-probe), 
* Login credentials were created previously in the RPi Debug Probe TTL serial UART connection, see link above, and there is no need to replicate that step again here. If the RPi Debug Probe example has not been first completed then ensure the login credentials are created for this example.
* TBD


Scenario One (1) 
* TBD
* Sub process one aka scenario one

Scenario Two (2)
* Success! :)
* Sub process two aka scenario two
* Could not have been done without the help of the RPi Forum Team, [WS](https://forums.raspberrypi.com/viewtopic.php?p=2356894#p2356894), images of contact

``` 
$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0cf3:e300 Qualcomm Atheros Communications QCA61x4 Bluetooth 4.0
Bus 001 Device 003: ID 138a:0091 Validity Sensors, Inc. VFS7552 Touch Fingerprint Sensor
Bus 001 Device 004: ID 04f3:24a1 Elan Microelectronics Corp. Touchscreen
Bus 001 Device 005: ID 0c45:6713 Microdia Integrated_Webcam_HD
Bus 001 Device 008: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
```
* The USB cable USB A to host Dell Ubuntu had come lose twice and reinserted fully a couple of times. In other words the USB A to host was inserted three times.
* The last listed was the serial connection used to contact the RPi Zero RPi OS.
``` 
$ sudo dmesg | grep -i tty
[sudo] password for york-earwaker: 
[29139.966128] usb 1-2: cp210x converter now attached to ttyUSB0
[29163.876803] cp210x ttyUSB0: cp210x converter now disconnected from ttyUSB0
[29181.313053] usb 1-2: cp210x converter now attached to ttyUSB0
[29306.171881] cp210x ttyUSB0: cp210x converter now disconnected from ttyUSB0
[29328.868968] usb 1-2: cp210x converter now attached to ttyUSB0
```

``` 
$ lsusb -t
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/16p, 480M
    |__ Port 002: Dev 008, If 0, Class=Vendor Specific Class, Driver=cp210x, 12M
    |__ Port 004: Dev 002, If 0, Class=Wireless, Driver=btusb, 12M
    |__ Port 004: Dev 002, If 1, Class=Wireless, Driver=btusb, 12M
    |__ Port 007: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
    |__ Port 009: Dev 004, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 012: Dev 005, If 0, Class=Video, Driver=uvcvideo, 480M
    |__ Port 012: Dev 005, If 1, Class=Video, Driver=uvcvideo, 480M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/8p, 5000M
```

``` 
$ usbip list -l
 - busid 1-12 (0c45:6713)
   Microdia : unknown product (0c45:6713)

 - busid 1-2 (10c4:ea60)
   Silicon Labs : CP210x UART Bridge (10c4:ea60)

 - busid 1-4 (0cf3:e300)
   Qualcomm Atheros Communications : QCA61x4 Bluetooth 4.0 (0cf3:e300)

 - busid 1-7 (138a:0091)
   Validity Sensors, Inc. : VFS7552 Touch Fingerprint Sensor (138a:0091)

 - busid 1-9 (04f3:24a1)
   Elan Microelectronics Corp. : unknown product (04f3:24a1)
```

```
$  sudo screen /dev/ttyUSB0 115200
```

``` 
zero-first-contact
Password: 
Linux raspberrypi 6.6.31+rpt-rpi-v7 #1 SMP Raspbian 1:6.6.31-1+rpt1 (2024-05-29) armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jul  6 02:49:12 BST 2024 on tty1
zero-first-contact@raspberrypi:~$ sudo shutdown -h now

Broadcast message from root@raspberrypi on pts/0 (Sat 2024-07-06 03:47:23 BST):

The system will power off now!

[ 3522.515842] reboot: Power down 
```
* In a separate Terminal cli on Dell Ubuntu
``` 
$ sudo screen -list
There is a screen on:
	12442.pts-2.york-earwaker-XPS-15-9560	(01/06/2026 05:19:49 PM)	(Attached)
1 Socket in /run/screen/S-root.

$ sudo screen -XS 12442 quit

$ sudo screen -list
No Sockets found in /run/screen/S-root.

```
* In the terminal in which the screen session connection was made to RPi Zero RPi OS
* The GNU Screen session terminated gracefully
``` 
$ sudo screen /dev/ttyUSB0 115200
[sudo] password for york-earwaker: 
[screen is terminating]

$ 
```
* The serial connection is still present due to stopping GNU Screen gracefully.
* Therefore another connection could have been made if the RPi Zero had not be shut down.
* <todo: consider, graceful GNU Screen session termination then reconnection to RPi Zero RPi OS, >
``` 
$ sudo dmesg | grep -i tty
[29139.966128] usb 1-2: cp210x converter now attached to ttyUSB0
[29163.876803] cp210x ttyUSB0: cp210x converter now disconnected from ttyUSB0
[29181.313053] usb 1-2: cp210x converter now attached to ttyUSB0
[29306.171881] cp210x ttyUSB0: cp210x converter now disconnected from ttyUSB0
[29328.868968] usb 1-2: cp210x converter now attached to ttyUSB0
```

## Output - headless to RPi Zero 2 W with Raspberry Pi Debug Probe
Second Process. Attempting to connect to the RPi Zero 2 W 'headless. Using Raspberry Pi Debug Probe interface board.
* Success! :)
* Could not have been achieved without the help of the RPi Forum Team. [WS](https://forums.raspberrypi.com/viewtopic.php?t=394836)

Primary Sources
* Raspberry Pi 3-pin Debug Connector Specification, [PDF](https://datasheets.raspberrypi.com/debug/debug-connector-specification.pdf), Raspberry Pi Datasheet, Error in pinout table
* Raspberry Pi Debug Probe, Product Brief, [PDF](https://datasheets.raspberrypi.com/debug/raspberry-pi-debug-probe-product-brief.pdf), Raspberry Pi Datasheet
* Raspberry Pi Debug Probe, User Guide, [WS](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html), Raspberry Pi Documentation
* Raspberry Pi Debug Probe, Firmware, [GH](https://github.com/raspberrypi/debugprobe), GitHub, Raspberry Pi, 
* USB org, [WS](https://www.usb.org/), USB Implementers Forum, Inc., USB specifications, 

Secondary Sources - troubleshooting help
* Headless, RPi Zero 2 W, configuration & connection guide, [WS](https://forums.raspberrypi.com/viewtopic.php?t=394836), Raspberry Pi Forums

Context Diagram
```
             RPi Zero 2 W                          RPi Debug Probe                                       Dell Ubuntu
             -----------          Serial             -----------                Serial                   -----------
   PWR IN   |___    o o |       Connection          |___     ___|   OTG?      Connection                |___        |
Micro USB B  ___|   o o | GPIO ------------ UART JST ___|SBC|___ Micro USB B ------------ standard USB A ___|       |
 Src > Snk  |       o o |                           |           |         Sink < Power < Source         |           |
             -----------         < Data >            -----------               < Data  >                 -----------
                                                 Serial Bridge Chip SBC
```

Circuit Diagram
```
Raspberry Pi Debug Probe
Interface board in a casing to 
Micro USB B
                                                        Chip set. RP2040
                                                        Software. Picoprobe
                  _________
            ------\ Micro /------   ʌ  To Host          | ---------- | ----------- | ------------------------------ |
           |      | USB B |      |                      | Pin Number | UART Signal | Serial Debug Signal            | Colour  | Description
           |      |_______|      |                      | ---------- | ----------- | ------------------------------ |
Serial     |         ___         |  <  The Debug        | 1          | TX          | SC (Serial Clock)              | Orange  | TX/SC (Output from Probe)
Bridge  >  |        |SBC|        |     Host             | 2          | GND         | GND                            | Black   | GND   (Ground)
Chip       |         ---         |                      | 3          | RX          | SD (bidirectional serial data) | Yellow  | RX/SD (Input to Probe or I/O)
           |                     |  v  To Target        | ---------- | ----------- | ------------------------------ |
           |    _____   _____    |     U = UART, D = DEBUG SWD
           |   |  U  | |  D  |   |  <  1.0mm pitch 3-pin JST ‘SH’ connector either BM03B-SRSS-TB (top entry)
            ---      ---       ---     or SM03B-SRSS-TB (side entry) types, or compatible alternatives . 
                | | |   | | |       <  The (serial UART/debug SWD) jumper wires, 
                1 2 3   1 2 3
                | | |
                | | |----|
                |-(------(--|
                  |---|  |  |
                      |  X  X
                      |  T  R
                      |      
                      |  T  T
                      |  R  R         
                      |  A  A
                      |  U  U
                      |   
                R  R    14 15
                W  W     O  O
                P  P  D  I  I
                V  V  N  P  P
                5  5  G  G  G
        ---------------------------------------------------------------------------
                2  4  6  8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40            Raspberry Pi Zero GPIO
      |         o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o          | 
      |         o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o          |
                1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 
```

### Prerequisites
Requirement for a serial communication program on Dell Ubuntu laptop to communicate via RPi Debug Probe, USB to UART connection, with RPi Zero 2 W . 

Hardware - 
* Raspberry Pi Debug Probe, com [WS](https://www.raspberrypi.com/products/debug-probe/), Raspberry Pi, built in resistors for 3V to RPi Zero 2 W GPIO pin UART connection 
* A N Other debug probe of a similar nature, intermediary between host and RPi Zero

### Connect RPi Zero 2 W to RPi Debug Probe
Attempt 1
* Success! :)
* Attach Micro USB B to RPi Debug Probe, 
* Attach JST connector to RPi Debug Probe, see ascii diagram above
* Attach UART and GND leads to RPi Zero GPIO pin, see ascii diagram above
* Plugin mains Power to RPi Zero
* Plugin USB A from RPi Debug Probe to Dell Ubuntu host
* Find name of serial ports
``` 
$ sudo dmesg | grep tty
[14643.777551] cdc_acm 1-2:1.1: ttyACM0: USB ACM device
[15365.882091] cdc_acm 1-2:1.1: ttyACM0: USB ACM device
```
* list tree of USB devices
```
$ lsusb -t
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/16p, 480M
    |__ Port 002: Dev 007, If 0, Class=Vendor Specific Class, Driver=[none], 12M
    |__ Port 002: Dev 007, If 1, Class=Communications, Driver=cdc_acm, 12M
    |__ Port 002: Dev 007, If 2, Class=CDC Data, Driver=cdc_acm, 12M
    |__ Port 004: Dev 002, If 0, Class=Wireless, Driver=btusb, 12M
    |__ Port 004: Dev 002, If 1, Class=Wireless, Driver=btusb, 12M
    |__ Port 007: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
    |__ Port 009: Dev 004, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 012: Dev 005, If 0, Class=Video, Driver=uvcvideo, 480M
    |__ Port 012: Dev 005, If 1, Class=Video, Driver=uvcvideo, 480M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/8p, 5000M
```
* list USB devices
```
$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0cf3:e300 Qualcomm Atheros Communications QCA61x4 Bluetooth 4.0
Bus 001 Device 003: ID 138a:0091 Validity Sensors, Inc. VFS7552 Touch Fingerprint Sensor
Bus 001 Device 004: ID 04f3:24a1 Elan Microelectronics Corp. Touchscreen
Bus 001 Device 005: ID 0c45:6713 Microdia Integrated_Webcam_HD
Bus 001 Device 007: ID 2e8a:000c Raspberry Pi Debug Probe (CMSIS-DAP)
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
```
* 
```
$ usbip list -l
 - busid 1-12 (0c45:6713)
   Microdia : unknown product (0c45:6713)

 - busid 1-2 (2e8a:000c)
   unknown vendor : unknown product (2e8a:000c)

 - busid 1-4 (0cf3:e300)
   Qualcomm Atheros Communications : QCA61x4 Bluetooth 4.0 (0cf3:e300)

 - busid 1-7 (138a:0091)
   Validity Sensors, Inc. : VFS7552 Touch Fingerprint Sensor (138a:0091)

 - busid 1-9 (04f3:24a1)
   Elan Microelectronics Corp. : unknown product (04f3:24a1)
```
* Unplug USB A from Dell Ubuntu, connection to RPi Debug Probe for a USB to UART connection to RPi Zero 2 W GPIO pins.
* Unplug power supply unit PSU from mains socket with cable to Micro USB B PWR IN for RPi Zero 2 W 

### Login from Dell Ubuntu host to RPi Zero 2 W via RPi Debug Probe with UART serial connection
Attempt 2.
* Success! :)
* Added to /bootfs/config.txt
```
[all]
enable_uart=1
```
* Create /bootfs/userconf.txt file as per RPi docs headless instructions, configure user manually [WS](https://www.raspberrypi.com/documentation/computers/configuration.html#configuring-a-user)
```
Synopsis of userconf.txt, usage
Create file then add username and password as per RPi Docs instructions.
/bootfs/userconf.txt
In cli terminal

$ touch userconf.txt

Open file userconf.txt and enter your-user-name:password, on a single line.
The password must be generated with OpenSSL as per instructions in link above.
```
* Put MicroSD Card Adapter back into Extension cable in RPi Zero env
* Plugin jumper wires to RPi Zero GPIO, see above circuit diagram above.
* Plugin USB A, from RPi Debug Probe, to Dell Ubuntu, 
* Plugin PSU to main socket, 
* Wait a two or three minutes for ACT LED on RPi Zero go solid green
* Open Terminal cli in Ubuntu Gnome
* See if RPi Debug Probe is recognized as a device on the USB bus. It is.
```
$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0cf3:e300 Qualcomm Atheros Communications QCA61x4 Bluetooth 4.0
Bus 001 Device 004: ID 04f3:24a1 Elan Microelectronics Corp. Touchscreen
Bus 001 Device 005: ID 0c45:6713 Microdia Integrated_Webcam_HD
Bus 001 Device 006: ID 138a:0091 Validity Sensors, Inc. VFS7552 Touch Fingerprint Sensor
Bus 001 Device 009: ID 2e8a:000c Raspberry Pi Debug Probe (CMSIS-DAP)
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
```
* Find name of serial ports. Its there.
```
$ sudo dmesg | grep -i tty
[132519.801811] cdc_acm 1-2:1.1: ttyACM0: USB ACM device
```
* Make serial connection request with serial port and baud rate to GNU Screen
```
$ sudo screen /dev/ttyACM0 115200
```
* Connected to empty screen shell
* typed user-name into empty screen, then pressed return key
* A password prompt appears, typed user-password, the pressed return key
* Login Success!
```
zero-first-contact
Password: 
Linux raspberrypi 6.6.31+rpt-rpi-v7 #1 SMP Raspbian 1:6.6.31-1+rpt1 (2024-05-29) armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jul  6 01:20:08 BST 2024 on tty1
zero-first-contact@raspberrypi:~$ 

zero-first-contact@raspberrypi:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Raspbian
Description:    Raspbian GNU/Linux 12 (bookworm)
Release:        12
Codename:       bookworm

zero-first-contact@raspberrypi:~$ cat /etc/os-release
PRETTY_NAME="Raspbian GNU/Linux 12 (bookworm)"
NAME="Raspbian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=raspbian
ID_LIKE=debian
HOME_URL="http://www.raspbian.org/"
SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"
```
+ MicroSD card with pre installed RPi OS, The RPi OS is 32-bit and not 64-bit as advertised.
```
zero-first-contact@raspberrypi:~$ uname -m
armv7l

zero-first-contact@raspberrypi:~$ dpkg-architecture --query DEB_HOST_ARCH
armhf

zero-first-contact@raspberrypi:~$ getconf LONG_BIT
32
```
* In a separate terminal cli on Dell Ubunutu host find the session id, of GNU Screen
```
$ sudo screen -list
There is a screen on:
	34451.pts-2.york-earwaker-XPS-15-9560	(01/01/2026 12:30:10 PM)	(Attached)
1 Socket in /run/screen/S-root.
```
* Shutting down RPi Zero gracefully, for the first time!
```
$ sudo shutdown -h now

Broadcast message from root@raspberrypi on pts/0 (Sat 2024-07-06 02:48:57 BST):

The system will power off now!

zero-first-contact@raspberrypi:~$ [ 5362.946387] reboot: Power down

```
* Shutting down GNU Screen gracefully, using session id 
```
TBD
```
* Update the exit from GNU Screen gracefully WIP - pulled out USB A before completing this. Next time.


## Output - headless to RPi Zero 2 W with USB cable
First Process. Attempting to connect to the RPi Zero 2 W 'headless' with USB cable. Using RPi documentation, RPi Forum, Online tutorials. 
* TBD, 
* <todo: consider, other things to try, >
* See first attempts at Appendix 01, 

Primary Sources
* Getting started, [WS](https://www.raspberrypi.com/documentation/computers/getting-started.html), Raspberry Pi Documentation, 

Secondary Sources
* Re: Headless, RPi Zero 2 W, configuration & connection guide, [WS](https://forums.raspberrypi.com/viewtopic.php?p=2358391#p2356519), Sat Jan 03, 2026 9:55 pm, Raspberry Pi Forum, attempt this proposed solution in link, 

Context Diagram - serial communication over Universal Serial Bus USB
```
     RPi Zero 2 W                                                          Dell Ubuntu
     -----------                         USB x.xx                          -----------
    |        ___|    OTG                   API                            |___        |
    |       |___  Micro USB B ----------------------------- standard USB A ___|       |
    |           |                  Sink < Power < Source                  |           |
     -----------                        < Data  >                          -----------
```
Circuit Diagram
``` 
     N/A
```
TBD?


## Output - Create OS image for use on RPi Zero 2 W
* Partial success, wip
* <done: consider, Optionally configure OS during the flash installation process to Micro SD Card >
* <done: consider, add [all] enable_uart=1 to config.txt to enable contact over serial bridge chip device, like rpi debug probe or usb ttl serial device, RPi Lite Trixie OS, >
* <todo: consider, connect over SSH and WiFi from Dell Ubuntu host to RPi Lite Trixie OS on RPi Zero 2 W, question asked in RPi Forum 14 January 2026, >
* <done: consider, connect over SSH and WiFi from Dell Ubuntu host to Ubuntu Core 24 OS on RPi Zero 2 W,  >

Primary Sources
* TBC

Secondary Sources
* Re: Headless, RPi Zero 2 W, configuration & connection guide, [WS](https://forums.raspberrypi.com/viewtopic.php?p=2358391#p2358391), Wed Jan 14, 2026 11:16 am, Raspberry Pi Forum, request for help re WiFi and SSH

After OS installation onto MicroSD Card. For steps requiring serial connection, to OS running on RPI Zero 2 W, circuit diagram and discussion, either of the approaches in links inline below should work
* Output - headless to RPi Zero 2 W with USB TTL to UART, [GH](https://github.com/YorkEarwaker/Electrical-Engineering/tree/main/rpi-z#output---headless-to-rpi-zero-2-w-with-usb-ttl-to-uart)
* Output - headless to RPi Zero 2 W with Raspberry Pi Debug Probe, [GH](https://github.com/YorkEarwaker/Electrical-Engineering/tree/main/rpi-z#output---headless-to-rpi-zero-2-w-with-raspberry-pi-debug-probe)

Candidate OSI's to install first attempts
* RPi OS Lite Trixie, first iteration success
* RPi OS Desktop Trixie, tbd
* Ubuntu Core 24, first iteration success

Install the RPi Imager software to flash Micro SD Cards with OS images OSI
```
$ sudo snap install rpi-imager
rpi-imager 1.9.3 from Dave Jones (waveform) installed

$ rpi-imager --version
Gtk-Message: 16:18:26.732: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
Qt: Session management error: Could not open network socket
rpi-imager version 1.9.3
Repository: https://downloads.raspberrypi.org/os_list_imagingutility_v4.json

```

### RPi OS Lite Trixie
* Success! :)

Get, download, RPi OS Lite Trixie, 64bit, 
* Raspberry Pi OS downloads [WS](https://www.raspberrypi.com/software/operating-systems/), Raspberry Pi, software
* Local file retrieved 9 01 2026 19:39:56

Check SHA256 hash
```
$ echo "681a775e20b53a9e4c7341d748a5a8cdc822039d8c67c1fd6ca35927abbe6290 *2025-12-04-raspios-trixie-arm64-lite.img.xz" | shasum -a 256 --check
2025-12-04-raspios-trixie-arm64-lite.img.xz: OK
```

* first use of RPi Imager, 
* write RPi OS Lite Trixie image (OSI) to Micro SD Card, A1, 
```
Raspberry Pi Imager v1.9.3

Raspberry Pi Device
Raspberry Pi Zero 2 W

Operating System
2025-12-04-raspios-trixie-arm64-lite.img.xz

Storage
A1 Micro SD Card. 
Internal SD card reader - 31.3 GB
Mounted as /media/york-earwaker/0403-0201

OS Customisation
Fully customised
```
* After installation is completed, remove and reinsert the MicroSD Card to add configuration key values
* To allow UART connection to RPi Zero 2 W
* Added to /bootfs/config.txt
```
[all]
enable_uart=1

```
* Take card from Dell Ubuntu
* Put card into RPi Zero 2 W env, SD Extension Cable in this case, 
* Plug in USB TTL device to Dell Ubuntu host USB A, 
* Mains plugged in, two or three minutes, steady green light ACT LED .

Make serial connection, USB TTL to UART
* Success! :)
* In a terminal cli window get usb devices, 
```
$ lsusb -t
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/16p, 480M
    |__ Port 002: Dev 006, If 0, Class=Vendor Specific Class, Driver=cp210x, 12M
    |__ Port 004: Dev 002, If 0, Class=Wireless, Driver=btusb, 12M
    |__ Port 004: Dev 002, If 1, Class=Wireless, Driver=btusb, 12M
    |__ Port 007: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
    |__ Port 009: Dev 004, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 012: Dev 005, If 0, Class=Video, Driver=uvcvideo, 480M
    |__ Port 012: Dev 005, If 1, Class=Video, Driver=uvcvideo, 480M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/8p, 5000M


$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0cf3:e300 Qualcomm Atheros Communications QCA61x4 Bluetooth 4.0
Bus 001 Device 003: ID 138a:0091 Validity Sensors, Inc. VFS7552 Touch Fingerprint Sensor
Bus 001 Device 004: ID 04f3:24a1 Elan Microelectronics Corp. Touchscreen
Bus 001 Device 005: ID 0c45:6713 Microdia Integrated_Webcam_HD
Bus 001 Device 006: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

$ lsusb -d 10c4:ea60
Bus 001 Device 006: ID 10c4:ea60 Silicon Labs CP210x UART Bridge

$ lsusb -s 001:006
Bus 001 Device 006: ID 10c4:ea60 Silicon Labs CP210x UART Bridge


$ lsusb -s 001:006 -v

Bus 001 Device 006: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
Couldn't open device, some information will be missing
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               1.10
  bDeviceClass            0 [unknown]
  bDeviceSubClass         0 [unknown]
  bDeviceProtocol         0 
  bMaxPacketSize0        64
  idVendor           0x10c4 Silicon Labs
  idProduct          0xea60 CP210x UART Bridge
  bcdDevice            1.00
  iManufacturer           1 Silicon Labs
  iProduct                2 CP2102 USB to UART Bridge Controller
  iSerial                 3 0001
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x0020
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          0 
    bmAttributes         0x80
      (Bus Powered)
    MaxPower              100mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           2
      bInterfaceClass       255 Vendor Specific Class
      bInterfaceSubClass      0 [unknown]
      bInterfaceProtocol      0 
      iInterface              2 
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x01  EP 1 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval               0

```

* In a terminal cli window get serial connected devices, 
```
$ sudo dmesg | grep -i tty
[sudo] password for york-earwaker: 
[    0.010361] ACPI: SSDT 0x000000007855AE40 00050D (v02 INTEL  TbtTypeC 00000000 INTL 20160422)
[    0.192054] printk: legacy console [tty0] enabled
[    8.512078] Bluetooth: RFCOMM TTY layer initialized
[ 1816.408470] usb 1-2: cp210x converter now attached to ttyUSB0

```
* Open serial connection with screen
```
$ sudo screen /dev/ttyUSB0 115200
```
* In a separate terminal cli window, list screen instances, 
```
$ sudo screen -list
There is a screen on:
	8417.pts-2.york-earwaker-XPS-15-9560	(01/14/2026 10:33:48 AM)	(Attached)
1 Socket in /run/screen/S-root.
```
* Enter user id into empty screen with no prompt
* Enter password into password prompt
* Press Return
```
york-earwaker
Password: 
Linux raspberrypi 6.12.47+rpt-rpi-v8 #1 SMP PREEMPT Debian 1:6.12.47-1+rpt1 (2025-09-16) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
york-earwaker@raspberrypi:~$ 
```
* Query the RPi OS instance
```
$ lsb_release -a
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 13 (trixie)
Release:        13
Codename:       trixie

$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.2
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"


$ uname -m
aarch64
$ dpkg-architecture --query DEB_HOST_ARCH
arm64
$ getconf LONG_BIT
64
```
* gracefully shut down RPi Zero 2 W from terminal cli
* Green ACT LED is off
```
$ sudo shutdown -h now

Broadcast message from root@raspberrypi on pts/0 (Thu 2025-12-04 18:57:31 GMT):

The system will power off now!

york-earwaker@raspberrypi:~$ 
                                                                                
reboot: Power down 
```
* quit the screen instance, 
```
$ sudo screen -XS 8417 quit
```
In the original terminal cli after separate terminal cli quits screen.
```
$ sudo screen /dev/ttyUSB0 115200
[screen is terminating]

$ sudo screen -list
No Sockets found in /run/screen/S-root.
```
* USB TTL serial communication bridge device still present due to graceful gnu screen process quit.
```
$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0cf3:e300 Qualcomm Atheros Communications QCA61x4 Bluetooth 4.0
Bus 001 Device 003: ID 138a:0091 Validity Sensors, Inc. VFS7552 Touch Fingerprint Sensor
Bus 001 Device 004: ID 04f3:24a1 Elan Microelectronics Corp. Touchscreen
Bus 001 Device 005: ID 0c45:6713 Microdia Integrated_Webcam_HD
Bus 001 Device 006: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

$ sudo dmesg | grep -i tty
[    0.010361] ACPI: SSDT 0x000000007855AE40 00050D (v02 INTEL  TbtTypeC 00000000 INTL 20160422)
[    0.192054] printk: legacy console [tty0] enabled
[    8.512078] Bluetooth: RFCOMM TTY layer initialized
[ 1816.408470] usb 1-2: cp210x converter now attached to ttyUSB0
```
* Unplug USB A to Dell Ubuntu host from USB TTL serial
* CP2102 UART Bridge red PWR LED is off.
* Dell Ubuntu reports USB device CP2102 is disconnected and no longer reported as  Bus 001 Device 006
```
$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0cf3:e300 Qualcomm Atheros Communications QCA61x4 Bluetooth 4.0
Bus 001 Device 003: ID 138a:0091 Validity Sensors, Inc. VFS7552 Touch Fingerprint Sensor
Bus 001 Device 004: ID 04f3:24a1 Elan Microelectronics Corp. Touchscreen
Bus 001 Device 005: ID 0c45:6713 Microdia Integrated_Webcam_HD
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

$ sudo dmesg | grep -i tty
[    0.010361] ACPI: SSDT 0x000000007855AE40 00050D (v02 INTEL  TbtTypeC 00000000 INTL 20160422)
[    0.192054] printk: legacy console [tty0] enabled
[    8.512078] Bluetooth: RFCOMM TTY layer initialized
[ 1816.408470] usb 1-2: cp210x converter now attached to ttyUSB0
[ 6793.849051] cp210x ttyUSB0: cp210x converter now disconnected from ttyUSB0
```

### Ubuntu Core 24
* Success! :)
* This process is likely to be a lot more involved, and may not be resolved in short order
* Made contact via Ubuntu Core 24 instance on RPi Zero 2 W.
* 90%? 

Prerequisites
* Ubuntu One Account [WS](https://login.ubuntu.com/), Ubuntu, login to existing account, or create one, to add SSH keys
* Use Ubuntu One SSH [WS](https://documentation.ubuntu.com/core/how-to-guides/manage-ubuntu-core/use-ubuntu-one-ssh/#), Ubuntu, docs, follow instructions on how to create SSH keys
* SSH/OpenSSH/Keys [WS](https://help.ubuntu.com/community/SSH/OpenSSH/Keys), Ubuntu, docs, help, more detail on Ubuntu One SSH formats and usage, 
* How to Use ssh-keygen to Generate a New SSH Key? [WS](https://www.ssh.com/academy/ssh/keygen) SSH 

SSH, - used in configuration of OS when first booted 
* generate SSH key, see 'Use Ubuntu One SSH' and 'SSH/OpenSSH/Keys'
* before importing the SSH key in Ubuntu One SSH, change the SSH key comment
* change the SSH key comment, default comment is < username >@< host > to help identify the key use case, comment is for key identification purposes, not used as part of ssh login, comment is a human readable identifier for the key, < username >@< host > is metadata and not used in the keys cryptographic generation or fingerprint calculation, the comment may be any string and need not follow the default < username >@< host > format, 
* <todo: consider, what if any are the character constraints for the comment string?  UTF-8? >
```
$ ssh-keygen -c -C "citizen-developer@rpi-0-2-w-ubuntu-core-24" -f ~/.ssh/id_ubuntucore
Enter passphrase: 
Old comment: york-earwaker@york-earwaker-XPS-15-9560
Comment 'citizen-developer@rpi-0-2-w-ubuntu-core-24' applied

```
* After importing the SSH key the following was displayed on the Ubuntu One SSH key web page
```
The following key was added to your account: citizen-developer@rpi-0-2-w-ubuntu-core-24

SSH keys

citizen-developer@rpi-0-2-w-ubuntu-core-24
```

Get, download, Ubuntu Core 24, 64bit, raspi
* Thank you for downloading Ubuntu Core 24 for Raspberry Pi, com [WS](https://ubuntu.com/download/raspberry-pi/thank-you?version=24&architecture=core-24-arm64+raspi), Ubuntu, download
* Local file retrieved 8 01 2026 18:08:49

Check SHA256 hash
```
$ echo "f8e1c4882e7bb0b9357dd41789f94ea6f9ad7caa50ce7a16b32a1e628f591c74 *ubuntu-core-24-arm64+raspi.img.xz" | shasum -a 256 --check
ubuntu-core-24-arm64+raspi.img.xz: OK
```

* second use of RPi Imager, 
* write Ubuntu Core 24 OS image (OSI) to Micro SD Card, A1, 
```
Raspberry Pi Imager v1.9.3

Raspberry Pi Device
Raspberry Pi Zero 2 W

Operating System
ubuntu-core-24-arm64+raspi.img.xz

Storage
A1 Micro SD Card. 
Internal SD card reader - 31.3 GB
Mounted as /media/york-earwaker/0403-0201

OS Customisation
Fully customised
Values left over from first use. These were left more or less unchanged. 
It does not seem as though these values had any effect for Ubuntu Core 24 OS image install.
```
* <todo: consider, confirm RPi Imager config values have no effect on Ubuntu Core install, cynically? 
As an asside they seemed only partially effective on RPi OS Trixie install for Imager v1.9.3 . 
But likely not used at all on Ubuntu Core 24 install. >
* Ubuntu Core 24 has only a single partition on newly formatted and installed MicroSD Card, A1, 
```
ubuntu-seed
```
* The /ubuntu-seed/config.txt file already contained enable_uart=1, so no need to add it, 
```
# Enable the serial pins
enable_uart=1
```
* Take card from Dell Ubuntu
* Put card into RPi Zero 2 W env, SD Extension Cable in this case, 
* Plug in USB TTL device to Dell Ubuntu host USB A, 
* Mains plugged in, two or three minutes, steady green light ACT LED was not shown.
* The green ACT LED blinked once or twice and then went out.

Make serial connection, USB TTL to UART
* Success! :) 
* <done: consider, make a serial connection, > 
* <todo: consider, calrify statements, clarify cli window task, consistent cli window naming, >
* In a terminal cli window get usb devices, 
```

$ sudo dmesg | grep -i tty
[sudo] password for york-earwaker: 
[28477.843947] usb 1-2: cp210x converter now attached to ttyUSB0

$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0cf3:e300 Qualcomm Atheros Communications QCA61x4 Bluetooth 4.0
Bus 001 Device 003: ID 138a:0091 Validity Sensors, Inc. VFS7552 Touch Fingerprint Sensor
Bus 001 Device 004: ID 04f3:24a1 Elan Microelectronics Corp. Touchscreen
Bus 001 Device 005: ID 0c45:6713 Microdia Integrated_Webcam_HD
Bus 001 Device 006: ID 10c4:ea60 Silicon Labs CP210x UART Bridge
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

$ lsusb -t
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/16p, 480M
    |__ Port 002: Dev 006, If 0, Class=Vendor Specific Class, Driver=cp210x, 12M
    |__ Port 004: Dev 002, If 0, Class=Wireless, Driver=btusb, 12M
    |__ Port 004: Dev 002, If 1, Class=Wireless, Driver=btusb, 12M
    |__ Port 007: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
    |__ Port 009: Dev 004, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 012: Dev 005, If 0, Class=Video, Driver=uvcvideo, 480M
    |__ Port 012: Dev 005, If 1, Class=Video, Driver=uvcvideo, 480M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/8p, 5000M


$ sudo screen -list
No Sockets found in /run/screen/S-root.
```
* In second cli terminial - to start serial connection to RPi Zero 2 W and configure Ubuntu Core 24
```
$ sudo screen /dev/ttyUSB0 115200
```
* In first cli terminal find screen session id
```
york-earwaker@york-earwaker-XPS-15-9560:~$ sudo screen -list
[sudo] password for york-earwaker: 
There is a screen on:
	33579.pts-2.york-earwaker-XPS-15-9560	(01/20/2026 02:32:55 PM)	(Attached)
1 Socket in /run/screen/S-root.
york-earwaker@york-earwaker-XPS-15-9560:~$ 

```
* In a terminal cli window get serial connected devices, 
```
$ sudo dmesg | grep -i tty
[23144.736428] usb 1-2: cp210x converter now attached to ttyUSB0

```
* Open serial connection with screen
```
$ sudo screen /dev/ttyUSB0 115200
```
* In a separate terminal cli window, list screen instances, 
```
$ sudo screen -list
 
There is a screen on:
	10537.pts-2.york-earwaker-XPS-15-9560	(01/16/2026 01:38:49 PM)	(Attached)
1 Socket in /run/screen/S-root.

```
* Blank gnu screen cli, press return? twice? wait two min? 
* <done: consider, test . in actuality entered UID then PWD but don't think they were needed, the UID and PWD characters were NOT shown on the screen window, needs further clarification on specific tasks required, in second attempt pressed return key twice, once may have been sufficient, likely one single return key would be needed tbd?, >
* <done: consider, configure Ubuntu Core via cli interface over serial connection, wip, requires ironing out of some wrinkles but 90% there? >
* Eventually cli ascii Ubuntu configuration options displayed, in gnu screen window.

Configure Ubuntu Core
* Success! :)
* 90%+ . Some outstanding concerns to clarify, 
* <todo: consider, enumerate ideal best set of task steps to configure Ubuntu Core 24 in this manner, via USB TTL UART serial connection, >
* <todo: consider, alternate configuration with username and password signon via USB TTL UART, for UID/PWD behaviour similar to RPi OS Lite Trixie, >
* First configuration page,
```
================================================================================
  Ubuntu Core                                                                 
================================================================================
  Configure the network and setup an administrator account on this all-snap   
  Ubuntu Core system.                                                         
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                 [ OK         ]    
```
* ...
* Several other pages are presented for configuration entry
* <todo: provide some descriptions and outstanding issues, questions, >
* <todo: provide some other connection and configuration detials, >
* Ends with SSH enabled Ubuntu Core 24 , 

SSH into Ubuntu Core 24
* Success! :)
* from SSH connection cli terminal window
* From a third cli terminal window, ssh to Ubuntu OS on RPi Zero 2 W.
```
$ ssh yorkearwaker@192.168.1.216
The authenticity of host '192.168.1.216 (192.168.1.216)' can't be established.
ED25519 key fingerprint is SHA256:CXPlZpQ1KhmexXF7Vik8BpypBE4TciMWstjvO3qbUhk.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.1.216' (ED25519) to the list of known hosts.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Welcome to Ubuntu Core 24

* Documentation: https://ubuntu.com/core/docs

This is a pre-built Ubuntu Core image. Pre-built images are ideal for
exploration as you develop your own custom Ubuntu Core image.

To learn how to create your custom Ubuntu Core image, see our guide:

* Getting Started: https://ubuntu.com/core/docs/get-started

In this image, why not create an IoT web-kiosk. First, connect a
screen, then run:

   snap install ubuntu-frame wpe-webkit-mir-kiosk
   snap set wpe-webkit-mir-kiosk url=https://ubuntu.com/core

For more ideas, visit:

* First steps: https://ubuntu.com/core/docs/first-steps
yorkearwaker@localhost:~$ 
```
* from SSH connection cli terminal window
* Query OS regarding version, bit size, architecture, ...
```
yorkearwaker@localhost:~$ lsb_release -a
-bash: lsb_release: command not found

yorkearwaker@localhost:~$ cat /etc/os-release
NAME="Ubuntu Core"
VERSION="24"
ID=ubuntu-core
PRETTY_NAME="Ubuntu Core 24"
VERSION_ID="24"
HOME_URL="https://snapcraft.io/"
BUG_REPORT_URL="https://bugs.launchpad.net/snappy/"

$ hostnamectl
   Static hostname: (unset)                         
Transient hostname: localhost
         Icon name: computer
        Machine ID: c10d229ece794a13b3c54dceb4646669
           Boot ID: 612f003984c845a68e5e11bc4339d680
  Operating System: Ubuntu Core 24                  
            Kernel: Linux 6.8.0-1043-raspi
      Architecture: arm64

yorkearwaker@localhost:~$ uname -m
aarch64

yorkearwaker@localhost$ dpkg-architecture --query DEB_HOST_ARCH
-bash: dpkg-architecture: command not found

yorkearwaker@localhost:~$ getconf LONG_BIT
64
```
* from SSH connection cli terminal window
* gracefully shut down/power down RPi Zero 2 W, 
```
yorkearwaker@localhost:~$ sudo shutdown -h now

Broadcast message from root@localhost on pts/1 (Tue 2026-01-20 15:19:06 UTC):

The system will power off now!

client_loop: send disconnect: Broken pipe
york-earwaker@york-earwaker-XPS-15-9560:~$ 
```
* from USB TTL UART connection cli terminal window
* In second? cli window, 
```
Personalize your account at https://login.ubuntu.com.
[ 3117.309421] (sd-umoun[2071]: Failed to unmount /run/shutdown/mounts/f6aafb86c2c57db9: Device or resource busy
[ 3117.347740] (sd-remou[2072]: Failed to remount '/run/shutdown/mounts/a494a4d0bdbe165b' read-only: Device or resource busy
[ 3117.367215] (sd-umoun[2073]: Failed to unmount /run/shutdown/mounts/a494a4d0bdbe165b: Device or resource busy
[ 3117.410659] shutdown[1]: Could not detach loopback /dev/loop1: Device or resource busy
[ 3117.419450] shutdown[1]: Unable to finalize remaining file systems, loop devices, ignoring.
[ 3117.449232] reboot: Power down
```
* from host cli terminal window, admin cli
* in first? cli window
* terminate gnu screen session
```
$ sudo screen -XS 33579 quit
```
* from host cli terminal window, USB TTL to UART cli
* In second? cli window
```
$ sudo screen /dev/ttyUSB0 115200
[sudo] password for york-earwaker: 
[screen is terminating]
```
* from host cli terminal window, admin cli
* in first? cli window
```
$ sudo screen -list
No Sockets found in /run/screen/S-root.
```
* from host cli terminal window, admin cli
* in first? cli window - nothing was returned.
```
$ sudo dmesg | grep -i tty
```
* Pull out USB A from USB TTL to UART serial bridge chip board.
* Unplug RPi Zero 2 W, 
* Concern the ubuntu core 24 system did not finish setup process


## Environment Tests

### Test USB cable for data and power
Success! :)
* cable 3 should work with RPi Zero 2 W SBC in the OTG Micro USB B socket, data and power

Cable addition
* cable 1; USB A (male) to USB A (male) , 1.5 m
* cable 2; USB A (female) to Micro USB B (male), 10? cm
* cable 3 = cable 1 + cable 2; USB A (male) to Micro USB B (male)

Test 
* Plug cable 1 and cable 2 together; cable 3 = cable 1 USB A (male) to cable 2 USB A (female) 
* Plug cable 3 Micro USB B (male) to RPi Pico 2 W
* Plug cable 3 USB A (male) to Dell Laptop Ubuntu LTS 24.04.3, The laptop is powered on
* Note. the LED had previously been turned off on the RPi Pico 2 W, 
* So the LED is does not light up when the Micro USB B end of cable 3 is plugged into the Pico MCU Micro USB B socket.
* Open Thonny IDE, Thonny recognizes RPi Pico 2 W MCU, 
```
MicroPython v1.25.0-preview.539.gdb8542707 on 2025-04-10; Raspberry Pi Pico 2 W with RP2350
Type "help()" for more information.
>>> 
MicroPython v1.25.0-preview.539.gdb8542707 on 2025-04-10; Raspberry Pi Pico 2 W with RP2350
Type "help()" for more information.
>>>
```
* Write MicroPython code in Thonny Shell window to execute in RPi Pico 2 W MCU environment. 
* Mpy code is shown below to; turn Pico LED light on. 
```
>>> from machine import Pin
>>> led = Pin("LED", Pin.OUT)
>>> led.on()
>>> 
```
* RPi Pico 2 W LED is turned on solid green
* Note. code is shown with developer input errors for completeness
```
>>> from machine import Pin
>>> led = Pin("LED", Pin.Out)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Pin' has no attribute 'Out'
>>> led = Pin("LED", Pin.OUT)
>>> led.on
<bound_method>
>>> led.on()
>>> 
```


## References

Terms
* USB On-The-Go, [WP](https://en.wikipedia.org/wiki/USB_On-The-Go), 
* UART, 

Circuit boards
* Bridge chip, 
* Jumper, [WP](https://en.wikipedia.org/wiki/Jumper_(computing)), 
* Jumper block , 
* Jumper shunt, 

Raspberry Pi Zero - datasheets, user guides, documentation
* Getting started, [WS](https://www.raspberrypi.com/documentation/computers/getting-started.html), Raspberry Pi Documentation
* Raspberry Pi Zero 2 W Product Brief, [PDF](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-product-brief.pdf), Raspberry Pi Datasheet
* Raspberry Pi Zero Pinout, [WS](https://forums.raspberrypi.com/viewtopic.php?t=378242), Raspberry Pi Forum
* Raspberry Pi Zero Pinout, [WS](https://pinout.xyz/), xyz
* Raspberry Pi Zero Schematic, [PDF](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-reduced-schematics.pdf), Raspberry Pi Datasheet
* Raspberry Pi Zero Test Pads [PDF](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-test-pads.pdf), Raspberry Pi Datasheet
* Raspberry Pi Zero Mechanical Drawing [PDF](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-mechanical-drawing.pdf), Raspberry Pi Datasheet
* Raspberry Pi A2-Class Micro SD Card Product Brief [PDF](https://datasheets.raspberrypi.com/sd-card/sd-card-product-brief.pdf), [WS](https://www.raspberrypi.com/products/sd-cards/), Raspberry Pi Datasheet
* Micro SD Card, Application Performance Class, [WS](https://www.sdcard.org/developers/sd-standard-overview/application-performance-class/), SD Association, A2/A1
* Raspberry Pi SD Cards and the Raspberry Pi Bumper: your new favourite accessories [WS](https://www.raspberrypi.com/news/sd-cards-and-bumper/), News, Raspberry Pi
* Raspberry Pi 3-pin Debug Connector Specification, [PDF](https://datasheets.raspberrypi.com/debug/debug-connector-specification.pdf), Raspberry Pi Datasheet
* Raspberry Pi Product Information Portal, [WS](https://pip.raspberrypi.com/), Raspberry Pi PIP Portal

Raspberry Pi Imager - flash OS to SD Card, OS; RPi OS Trixie, Ubuntu Core 24, ...
* Raspberry Pi Imager, code [GH](https://github.com/raspberrypi/rpi-imager), [WS](https://www.raspberrypi.com/software/), Ubuntu snap [WS](https://snapcraft.io/install/rpi-imager/ubuntu), install Imager, to be able to flash RPi OS/Ubuntu Core 24/... to Micro SD Cards, 
* A new Raspberry Pi Imager, [WS](https://www.raspberrypi.com/news/a-new-raspberry-pi-imager/), 24 November 2025, Tom Dewey, v 2.x
* Ubuntu, How to create an Ubuntu Server SDcard for Raspberry Pi, [WS](https://ubuntu.com/tutorials/how-to-sdcard-ubuntu-server-raspberry-pi#1-overview), Ubuntu, Raspberry Pi Imager
* Ubuntu, Install Ubuntu on a Raspberry Pi, [WS](https://ubuntu.com/download/raspberry-pi), Ubuntu, Raspberry Pi Imager
* Ubuntu, Use Raspberry Pi Imager, [WS](https://documentation.ubuntu.com/core/tutorials/try-pre-built-images/use-raspberry-pi-imager/), Ubuntu core, Docs, Raspberry Pi Imager

Ubuntu OS
* Raspberry Pi, [WS](https://wiki.ubuntu.com/ARM/RaspberryPi), Ubuntu, wiki
* Ubuntu, Raspberry Pi Foundation Raspberry Pi Zero 2, Development board system certified with Ubuntu, [WS](https://ubuntu.com/certified/202201-29909), Ubuntu, IoT, 
* Ubuntu, Testing Platforms, [WS](https://documentation.ubuntu.com/core/reference/testing-platforms/), Ubuntu core, Docs, 
* Ubuntu, How to SHA256 Sum, [WS](https://help.ubuntu.com/community/HowToSHA256SUM), Community, 

SSH - OpenSSH, Ubuntu One 
* How do I change my private key passphrase? [WS](https://serverfault.com/questions/50775/how-do-i-change-my-private-key-passphrase), StackExchange, ServerFault, 
* How do I remove the passphrase for the SSH key without having to create a new key? [WS](https://stackoverflow.com/questions/112396/how-do-i-remove-the-passphrase-for-the-ssh-key-without-having-to-create-a-new-ke), 
* How To: Change Passphrase for SSH Private Key [WS](https://www.unixtutorial.org/changing-passphrase-to-your-ssh-private-key/) Unix Tutorials, 
* What significance does the user/host at the end of an SSH public key file hold? , [WS](https://serverfault.com/questions/743548/what-significance-does-the-user-host-at-the-end-of-an-ssh-public-key-file-hold), StackExchange, ServerFault, 
* How can I change the comment field of an RSA key (SSH)? [WS](https://superuser.com/questions/361764/how-can-i-change-the-comment-field-of-an-rsa-key-ssh), 

Ubun OS - tutorials, still relevant?
* Ubuntu Core & Raspberry Pi Zero 2 W, [WS](https://askubuntu.com/questions/1384864/ubuntu-core-raspberry-pi-zero-2-w), 2 January 2022, Ask Ubuntu
* Install 64 bit OS on Raspberry Pi zero 2 W, [WS](http://qengineering.eu/install-64-os-on-raspberry-pi-zero-2.html), 14 February 2022, Q Engineering

Raspberry Pi OS
* Trixie — the new version of Raspberry Pi OS, [WS](https://www.raspberrypi.com/news/trixie-the-new-version-of-raspberry-pi-os/), 2 October 2025, Simon Long
* Raspberry Pi OS downloads, [WS](https://www.raspberrypi.com/software/operating-systems/) 

SD Cards - Command Queuing (CQ) or Application Performance Class (A1/A2) optimizations appear unsupported for RPi Zero 2 W, 
* Testing class A2 SD cards with Command Queueing on Pi 5, [WS](https://forums.raspberrypi.com/viewtopic.php?t=367459), Raspberry Pi Forum, 
* Raspberry Pi Zero 2 W maximum SD card capacity, [WS](https://raspberrypi.stackexchange.com/questions/147757/raspberry-pi-zero-2-w-maximum-sd-card-capacity), StackExchange, Raspberry Pi
* Should I get A1 or A2 spec'd Micro SD card for my phone? { closed } [WS](https://android.stackexchange.com/questions/214545/should-i-get-a1-or-a2-specd-micro-sd-card-for-my-phone), StackExchange, Android 
* ...

Ubuntu Core 24 - RPi Zero 2 W
* Ubuntu 24.04 LTS 64 bit won't run on a Raspberry Pi Zero 2 W - why is it in the imager's menu?, [WS](https://forums.raspberrypi.com/viewtopic.php?t=371534), 

WiFi - Debian, RPi OS, Ubuntu
* WiFi, wpa_supplicant file, [WS](https://wiki.debian.org/WiFi/HowToUse#wpa_supplicant) , debian, 

RPi Zero 2 W - LED ACT
* Pi Zero status LED meaning, [WS](https://forums.raspberrypi.com/viewtopic.php?t=216095), 16 Jun 2018, Raspberry Pi Forum
* 

Safety circuit - 5V power * to * GPIO pins
* rPI Zero W 5 V output, [WS](https://raspberrypi.stackexchange.com/questions/69120/rpi-zero-w-5-v-output), StackExchange, Raspberry Pi, 
* Power your Raspberry Pi: expert advice for a supply, [WS](https://magazine.raspberrypi.com/articles/power-supply), 2017, Russell Barnes, Raspberry Pi Magazine, 
* Can I power a Pi through a 5V pin?, [WS](https://raspberrypi.stackexchange.com/questions/73126/can-i-power-a-pi-through-a-5v-pin), StackExchange, Raspberry Pi, 
* Re: RPi B+ test pads [WS](https://forums.raspberrypi.com/viewtopic.php?f=28&t=89522&p=628505&hilit=pp1#p628505), Raspberry Pi Forum, 
* Powering Rpi Zero from 5V gpio pin, [WS](https://forums.raspberrypi.com/viewtopic.php?t=286257), Raspberry Pi Forum, 
* Powering a Pi5 from GPIO, [WS](https://www.reddit.com/r/cyberDeck/comments/1ds8pea/powering_a_pi5_from_gpio/), Reddit, CyberDeck, 
* Switching Raspberry Pi 5V with GPIO pin [WS](https://electronics.stackexchange.com/questions/665716/switching-raspberry-pi-5v-with-gpio-pin), StackExchange, Electrical Engineering, 
* Can I power the Raspberry Pi Zero W through GPIO the same way as with a Pi 3?, [WS](https://forums.raspberrypi.com/viewtopic.php?t=285282), Raspberry Pi Forum, 
* ...

### Tutorials
* might be some value in these, but it was hard to find while starting to find a headless solution

Headless - SSH, RPi Zero OTG USB Ethernet, 
* How do I turn off the green LED on my RPI Zero 2 W? [WS](https://forums.raspberrypi.com/viewtopic.php?t=328550), Raspberry Pi Forums, 
* How to boot up & start using raspberry pi using laptop as a monitor, [WS](https://raspberrypi.stackexchange.com/questions/84349/how-to-boot-up-start-using-raspberry-pi-using-laptop-as-a-monitor), StackExchange, Raspberry Pi, 
* Add ssh and wpa_supplicant.conf Files, [WS](https://seengreat.com/wiki/123/raspberry-pi-zero-2-w?#toc6), SeenGreat, 
* Raspberry Pi Zero W headless using wpa_supplicant.conf not working, [WS](https://raspberrypi.stackexchange.com/questions/67649/raspberry-pi-zero-w-headless-using-wpa-supplicant-conf-not-working), StackExchange, Raspberry Pi, 
* Connect to a Raspberry Pi Zero over USB on Ubuntu, [WS](https://johnnymatthews.dev/blog/2021-02-06-connect-to-raspberry-pi-zero-over-usb-on-ubuntu/), Johnny Matthews
* Setting up Pi Zero OTG - The quick way (No USB keyboard, mouse, HDMI monitor needed), [WS](https://gist.github.com/gbaman/975e2db164b3ca2b51ae11e45e8fd40a), gbaman, github
* How to Setup a Raspberry Pi Without a Monitor or Keyboard (Video Tutorial), [WS](https://www.reddit.com/r/raspberry_pi/comments/dzgke0/how_to_setup_a_raspberry_pi_without_a_monitor_or/), Reddit, 
* How To Set Up Raspberry Pi Zero 2 W - Headless Mode, [WS](https://albert-fit.com/how-to-set-up-raspberry-pi-zero-2-w-headless-mode/), 12/01/2024, Albert Fit 
* RPi Zero USB OTG (usb-ethernet device), [WS](https://forums.raspberrypi.com/viewtopic.php?t=221259), Raspberry Pi Forums, 
* Setup a Raspberry Pi headless tutorial, [WS](https://www.reddit.com/answers/466d38d5-7d9f-44ac-8927-5fa52f5ec57c/?q=Setup%20a%20Raspberry%20Pi%20headless%20tutorial&source=PDP)
* How to connect to a Raspberry Pi Zero to an Ubuntu laptop by USB?, [WS](https://superuser.com/questions/1150562/how-to-connect-to-a-raspberry-pi-zero-to-an-ubuntu-laptop-by-usb), StackExchange, Superuser,
* wpa_supplicant.conf not applied on first boot — ssh file removed but Wi-Fi not configured (Pi Zero W), [WS](https://forums.raspberrypi.com/viewtopic.php?t=391776), Forums, Raspberry Pi, 
* Headless start not working for Raspberry Pi Zero W, [WS](https://forums.raspberrypi.com/viewtopic.php?t=389951), Forums, Raspberry Pi,
* Setup a Raspberry Pi for headless use with USB serial console, [WS](https://www.tal.org/tutorials/setup-raspberry-pi-headless-use-usb-serial-console), TalOrg

Headless - SSH file location
* Placing SSH File on New SDCard, [WS](https://forums.raspberrypi.com/viewtopic.php?t=314900), Forums, Raspberry Pi, 
* "Put an empty 'ssh' file in /boot/" trick not working anymore [WS](https://raspberrypi.stackexchange.com/questions/98719/put-an-empty-ssh-file-in-boot-trick-not-working-anymore), StackExchange, Raspberry Pi, 
* Enabling SSH by default on Raspbian Stretch [WS](https://raspberrypi.stackexchange.com/questions/73119/enabling-ssh-by-default-on-raspbian-stretch), StackExchange, Raspberry Pi, 

Headless - RPi Zero soft shut down, hard shut down
* How to do a soft shutdown on headless Pi? [WS](https://forums.raspberrypi.com/viewtopic.php?t=306320), Forums, Raspberry Pi, 
* Shutting down the Pi safely without SSH or a monitor?, [WS](https://raspberrypi.stackexchange.com/questions/59529/shutting-down-the-pi-safely-without-ssh-or-a-monitor), StackExchange, Raspberry Pi, 
* Turning off power on a PI Zero W, [WS](https://forums.raspberrypi.com/viewtopic.php?t=215796), Forums, Raspberry Pi, 

Headless - RPi Zero power on
* Using Both PWR and USB in OTG Mode on the Pi Zero [WS](https://forums.raspberrypi.com/viewtopic.php?t=223891)

SD Card, MicroSD card removal
* Can I temporarily remove the SD card while my device is turned on?, [WS](https://raspberrypi.stackexchange.com/questions/3759/can-i-temporarily-remove-the-sd-card-while-my-device-is-turned-on), StackExchange, Raspberry Pi, 

UART
* Attaching to a Raspberry Pi's Serial Console (UART) for debugging, [WS](https://www.jeffgeerling.com/blog/2021/attaching-raspberry-pis-serial-console-uart-debugging), 1 October 2021

USB Ethernet - Ubuntu, RPi OS, debian, linux, 
* How to set up an usb/ethernet interface in Linux? [WS](https://unix.stackexchange.com/questions/386162/how-to-set-up-an-usb-ethernet-interface-in-linux), StackExchange, Unix Linux
* How to Share your USB Device in Ubuntu 24.04 over LAN, [WS](https://ubuntuhandbook.org/index.php/2024/09/share-usb-ubuntu-lan/), Ubuntu Handbook, **** Looks important generally, not sure it is relevant with USB RPi Zero connection to Dell laptop.
* RTL8125 2.5GbE Ethernet port not working in Ubuntu 24.04, [WS](https://discourse.ubuntu.com/t/rtl8125-2-5gbe-ethernet-port-not-working-in-ubuntu-24-04/55551/1), Discourse, Ubuntu, 
* No Network Connection with 24.04 and r8125 Ethernet, [WS](https://discourse.ubuntu.com/t/no-network-connection-with-24-04-and-r8125-ethernet/58589), Discourse, Ubuntu, 
* ...

USB OTG - Raspberry Pi 
* STICKY: USB device not working on Raspberry Pi Zero, 1, 2, 3? Click here!, [WS](https://forums.raspberrypi.com/viewtopic.php?t=53832&sid=e1f95c7352ca64da9a75c5c7d0b71f87), Forums, Raspberry Pi, 
* STICKY: USB Ethernet Gadget A Beginner's Guide, [WS](https://forums.raspberrypi.com/viewtopic.php?t=306121), Forums, Raspberry Pi, thagrol
* Guides [GH](https://github.com/thagrol/Guides), GitHub, thagrol
* STICKY: Bookworm, Point to Point Ethernet (inc g_ether), [WS](https://forums.raspberrypi.com/viewtopic.php?t=364247), GitHub, thagrol


Ethernet, connect via USB, ... 
* ... to source

BlueTooth
* ... to source

### Projects

Flash
* Make a Pi Zero W Smart USB flash drive , [WS](https://magazine.raspberrypi.com/articles/pi-zero-w-smart-usb-flash-drive), Russell Barnes. 

Screen
* Re-purposed Laptop Screen for Raspberry Pi, [WS](https://www.instructables.com/Re-purposed-Laptop-Screen-for-Raspberry-Pi/), AutoDesk Instructables, lerigsby12 in Circuits, Raspberry Pi
* Home Raspberry Pi Desktop With Old Laptop Screen, [WS](https://www.instructables.com/Home-Raspberry-Pi-Desktop-With-Old-Laptop-Screen/), AutoDesk Instructables, Ashu_d in Circuits, Raspberry Pi
* Connect Pi to an old laptop screen, [WS](https://raspberrypi.stackexchange.com/questions/848/connect-pi-to-an-old-laptop-screen), StackExchange, Raspberry Pi, 
* Old laptop display (40pins)how to use as a raspberry pi 4 B display(15pins), [WS](https://forums.raspberrypi.com/viewtopic.php?t=277682), Forums, Raspberry Pi, 
* Re-purposing old laptop LCD via Raspberry Pi, [WS](https://forums.raspberrypi.com/viewtopic.php?t=255727), Forums, Raspberry Pi, 
* Using laptop screen with RPI, [WS](https://forums.raspberrypi.com/viewtopic.php?t=234270), Forums, Raspberry Pi, 

## Appendix 01 - First connection attempts, various,
* Failure :( 
* to connect from Dell Ubuntu to RPi Zero 2 W, RPi OS 32bit Bookworm, pre installed, A2 MicroSD Card, Raspberry Pi
* But good learning :) 
* <todo: consider, thinning out some of the tutorials and append to this section, append to Appendix 01? or create Appendix 02? >
* Clean up, RPi OS on RPi MiroSD Card, below after changes made during Output - headless to RPi Zero 2 W with USB cable - first connection attempts
* Both are moot as these first attempts were unsuccessful!

### Output - headless to RPi Zero 2 W with USB cable - first connection attempts
* First Process. Attempting to connect to the RPi Zero 2 W 'headless' with USB cable. Using RPi documentation, RPi Forum, Online tutorials. 
* Failure :(
* Based of past experience with RPi Pico MCU's connection to host via USB power and data, but not how RPi Zero works, shame
* On the up side good learning loop to have pursued. 
* However this level of effort is likely a barrier to entry for many.
* See references heading below for many of the resources tried without success.

Primary Sources
* Getting started, [WS](https://www.raspberrypi.com/documentation/computers/getting-started.html), Raspberry Pi Documentation, 

Secondary Sources
* Many online information, inclusive; tutorials, Raspberry Pi Forum, etc...
* See References heading section below, many

### Create SSH file on SD Card
Remote Access, Enable the SSH server, [WS](ttps://www.raspberrypi.com/documentation/computers/remote-access.html#enable-the-ssh-server), Raspberry Pi Documentation
* Place RPi MicroSD Card with preinstalled RPi OS in MicroSD Card Adapter, 
* Put MicroSD Card Adapter into laptop
* Create ssh file as per instructions in link above.
```

york-earwaker@york-earwaker-XPS-15-9560:/media/york-earwaker/rootfs/boot/firmware$ sudo touch ssh

[sudo] password for york-earwaker: 
york-earwaker@york-earwaker-XPS-15-9560:/media/york-earwaker/rootfs/boot/firmware$ dir

ssh

york-earwaker@york-earwaker-XPS-15-9560:/media/york-earwaker/rootfs/boot/firmware$ ls
ssh

york-earwaker@york-earwaker-XPS-15-9560:/media/york-earwaker/rootfs/boot/firmware$ ls -l

total 0
-rw-r--r-- 1 root root 0 Dec 18 15:41 ssh
```

### Headless, power on RPi Zero
Success! 
* Put SD Card into RPi Zero, using an extension cable for easier access and to improve life of micro SD Card and RPi Zero
* Put power adapter micro USB into PWR IN USB slot
* Plugged in 12.75 Raspberry Pi Power adapter into mains
* ACT Led, green light flashed on and off for a while, assuming during RPi OS boot sequence,
* ACT Led, green light is permanently on after a while
* probably a mistake without having made necessary changes to SD card RPi OS changes first, unlikely ssh file creation was not sufficient see above, 

### Headless, connect to RPi Zero from Dell laptop, USB cable
Attempt 1
* Failed :(
* <todo: tried this, but encountering difficulties, no first contact yet,  >
* <issue; had not set up the RPi Zero correctly beforehand, so failure >
* <issue; bad to use both usb OTG to host usb A and usb pwr in, so might have fired RPi Zero, oh dear, >
* RPi Zero powered from mains with micro USB PWR IN port, see previous heading Headless, power on RPi Zero .
* RPi Zero on, ACT Led solid green great, no flashing good as flashing Led can indicate issues, 
* Plug in USB cable (data and power), Dell A standard type USB port, RPi Zero micro USB port, Pi Hut website reports cable compatible with Zero and carries data, 
* On Dell host, attempted ssh connection via terminal cli; , but no contact
``` 
$ ssh pi@raspberrypi 

$ ssh pi@raspberrypi raspberry
$ ssh pi@raspberrypi.local
$ ssh pi@raspberrypi.local raspberry

```
* Restarted Dell laptop with USB cable attached
* On Dell host, attempted ssh connection via terminal cli $ ssh instructions again but no contact after Dell Ubuntu reboot, 
* On Dell host, attempted via terminal cli $ nm-connection-editor instruction but Network Connection window did not list RPi Zero, likely as necessary Ethernet config had not been done on RPi Zero beforehand, did list local WiFi router, and Bluetooth mobile phone, 
* Can't access RPi OS file system, so can't shut it down gracefully, powering off,
* Option 1. remove SD card and make changes likely harms SD card file system, and changes likely won't be recognized until reboot anyway, which currently can't be done gracefully
* Option 2. unplug RPi Zero from mains will likely also harm SD card file system, mitigate buy new micro SD Card
* Option 3. add power down button to RPi Zero GPIO pins for equivalent of hard shut down on PC by holding down power button? But dangerous to do while the RPi Zero is powered on and might lead to worse damage to actual RPI Zero. Investigate if this is possible may be less harmful than; removing SD card (option 1), pulling the plug (option 2) 
* Option 4. explore Dell Ubuntu LTS 24.04.3 via Gnome desktop or terminal cli, what might be done to make contact with RPi OS on RPi Zero, 
* Option 5. keep RPi Zero powered on and purchase keyboard and display. Investigate if RPi Zero needs to have these plugged in before booting to have these devices recognized, probably not.
* Option 6. short GPIO pins, which ones? Also will likely cause damage to SD card file system and likely damage RPi Zero too.
* Option 7. USB On-The-Go adapter, already used micro USB B from peripheral RPi Zero to standard USB A host Dell, so addition of an adapter only overhead, micro USB B to peripheral to standard USB A host is another approach

Dell Ubuntu does not seem to see RPi Zero 2 W. 
```

$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0cf3:e300 Qualcomm Atheros Communications QCA61x4 Bluetooth 4.0
Bus 001 Device 003: ID 138a:0091 Validity Sensors, Inc. VFS7552 Touch Fingerprint Sensor
Bus 001 Device 004: ID 04f3:24a1 Elan Microelectronics Corp. Touchscreen

Bus 001 Device 005: ID 0c45:6713 Microdia Integrated_Webcam_HD
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
```

Attempt 2
* Failure :(
* <note: ssh file had already been created see heading above, >
* Unplugged Micro USB B OTG data from RPi Zero, it was also supplying power from Dell laptop, had naively assumed only data
* Shut down RPi Zero. Ensure ACT Led is not flashing, pull out Micro USB B power adapter plug to mains, Option 2 above, 
* <issue: may have broken RPi Zero due to power from both Micro USB B OTG from Dell and Micro USB B power adapter to mains, >
* Retrieve MicroSD Card from RPi Zero. In this instance eject the MicroSD Card Adapter it from the reader slot at the end of MicroSD Card cable ribbon.
* Put MicroSD Card Adapter containing MicroSD Card into Dell laptop, two file system partitions are mounted; bootfs, rootfs
* Open bootfs partition
* Open cmdline.txt enter modules-load=dwc2,g_ether after rootwait, save cmdline.txt
```
console=serial0,115200 console=tty1 root=PARTUUID=f35edfdd-02 rootfstype=ext4 fsck.repair=yes rootwait modules-load=dwc2,g_ether quiet splash plymouth.ignore-serial-consoles

```
* Open config.txt enter under heading \[all\] dtoverlay=dwc2 , save config.txt
```

# For more options and information see

# http://rptl.io/configtxt
# Some settings may impact device functionality. See link above for details


# Uncomment some or all of these to enable the optional hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on

#dtparam=spi=on

# Enable audio (loads snd_bcm2835)
dtparam=audio=on

# Additional overlays and parameters are documented

# /boot/firmware/overlays/README


# Automatically load overlays for detected cameras
camera_auto_detect=1


# Automatically load overlays for detected DSI displays
display_auto_detect=1


# Automatically load initramfs files, if found
auto_initramfs=1


# Enable DRM VC4 V3D driver
dtoverlay=vc4-kms-v3d

max_framebuffers=2

# Don't have the firmware create an initial video= setting in cmdline.txt.

# Use the kernel's default instead.
disable_fw_kms_setup=1


# Disable compensation for displays with overscan
disable_overscan=1



# Run as fast as firmware / board allows

arm_boost=1


[cm4]

# Enable host mode on the 2711 built-in XHCI USB controller.
# This line should be removed if the legacy DWC2 controller is required

# (e.g. for USB device mode) or if USB support is not required.

otg_mode=1


[cm5]

dtoverlay=dwc2,dr_mode=host


[all]

dtoverlay=dwc2
```
* Plug in USB B OTG plug for power and data
* Attempt ssh in host terminal cli $ ssh pi@raspberrypi raspberry and combinations but no luck

Attempt 3
* Failed so far :(
* <todo: note, there are also duplicate empty ssh file as per RPi docs example. Also cmdline.txt which only contains; modules-load=dwc2,g_ether , and config.text which only contains on two seperte lines; [all] dtoverlay=dwc2 , this as boot directory files of same indicated put same in firmware directory, >
```
york-earwaker@york-earwaker-XPS-15-9560:/media/york-earwaker/rootfs/boot/firmware$ ls -l

total 8

-rw-r--r-- 1 root root 26 Dec 20 13:25 cmdline.txt

-rw-r--r-- 1 root root 21 Dec 20 13:26 config.txt
-rw-r--r-- 1 root root  0 Dec 18 15:41 ssh

```
* Created ssh file in /media/york-earwaker/bootfs host terminal cli $ touch ssh
* Plug in USB A to Dell laptop for power and data to RPi Zero Micro USB B OTG port, wait a few minutes but can't ssh
* There appears there might be an Ethernet problem with Ubuntu LTS 24.04.3 . Have seen various Ethernet issues reported online with 24.04.1 . Unclear if these apply to 24.04.3 . 
* Can't see USB Ethernet/Netchip Ethernet in Setting>Networks panel.
```
$ nmcli connection show
NAME                UUID                                  TYPE       DEVICE 
BT-2QAFZ5           da27f6e8-a9c4-412e-ba5d-c4afffb0edbe  wifi       wlp2s0 
lo                  04b471a3-29bf-4d19-8fc8-1e0190e7cd60  loopback   lo     
Galaxy A14 Network  7d0e2e6d-34a0-41a7-b58f-5e18c49cc177  bluetooth  --  
```
* list usb as table
```
$ lsusb -t
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/16p, 480M
    |__ Port 004: Dev 002, If 0, Class=Wireless, Driver=btusb, 12M
    |__ Port 004: Dev 002, If 1, Class=Wireless, Driver=btusb, 12M
    |__ Port 007: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
    |__ Port 009: Dev 004, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 012: Dev 005, If 0, Class=Video, Driver=uvcvideo, 480M
    |__ Port 012: Dev 005, If 1, Class=Video, Driver=uvcvideo, 480M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/8p, 5000M
```
* After RPi Zero power off and place MicroSD Card Adapter into Dell laptop to view /bootfs directory ssh file, created above, is no longer there.

### Headless, connect to RPi Zero 2 W from Dell laptop, Wifi
Attempt 1
* Failure :(
* <todo: try this, but will likely require changes to RPi OS config files, >
* doing this in parallel testing for ssh

* Unplug USB A from Dell laptop, RPi Zero powered down, hard power off
* Put MicroSD Card Adapter, containing MiroSD Card with pre installed RPi OS, in laptop
* Navigate to rootfs/etc/wpa_supplicant directory, found there an admin rights protected file wpa_supplicant.conf 
* Opened as Administrator, file contained the following
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
```
* Edit wpa_supplicant.conf file with with local respective values for country=, ssid=, psk=, 
* Content of  with additions as below, 
```

country=your_country_code

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev

update_config=1


network={

    ssid="Your_Wi-Fi_SSID"
    psk="Your_Wi-Fi_Password"

    key_mgmt=WPA-PSK

    priority=1
}

```
* Saved wpa_supplicant.conf file
* Unmount partitions and pull MicroSd Card Adapter out of Dell laptop Ubuntu LTS 24.04.3,
* Put MicroSd Card Adapter into RPi Zero 2 W 
* Plug in USB A into Dell laptop to Power on RPi Zero 2 W
* Can't see RPi Zero in WiFi Router Hub control panel, not detailed here
* Can't see RPi Zero with nmcli connection show, as below
```
$ nmcli connection show

NAME                UUID                                  TYPE       DEVICE 

BT-2QAFZ5           da27f6e8-a9c4-412e-ba5d-c4afffb0edbe  wifi       wlp2s0 
lo                  9500dc08-d067-48d8-899f-ca89bbfa4cde  loopback   lo     

Galaxy A14 Network  a897e654-7ea7-4d9e-b130-5d4f226e8d5e  bluetooth  --

```
* Can't see RPi Zero with lsusb
```

$ lsusb

Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 0cf3:e300 Qualcomm Atheros Communications QCA61x4 Bluetooth 4.0

Bus 001 Device 003: ID 138a:0091 Validity Sensors, Inc. VFS7552 Touch Fingerprint Sensor

Bus 001 Device 004: ID 04f3:24a1 Elan Microelectronics Corp. Touchscreen
Bus 001 Device 005: ID 0c45:6713 Microdia Integrated_Webcam_HD

Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
```
* Can't see RPi Zero with ping
```
$ ping raspberrypi.local
ping: raspberrypi.local: Name or service not known

```
* Load Ethernet driver? $ sudo modprobe r8152 , don't think it did any thing, probs needs installing?
* Can't see RPi Zero with $ usbip list -l, lists only usual Dell laptop component parts on bus 001 
```

$ sudo modprobe r8152
$ usbip list -l

 - busid 1-12 (0c45:6713)

   Microdia : unknown product (0c45:6713)


 - busid 1-4 (0cf3:e300)

   Qualcomm Atheros Communications : QCA61x4 Bluetooth 4.0 (0cf3:e300)

 - busid 1-7 (138a:0091)

   Validity Sensors, Inc. : VFS7552 Touch Fingerprint Sensor (138a:0091)


 - busid 1-9 (04f3:24a1)

   Elan Microelectronics Corp. : unknown product (04f3:24a1)

```
* Install latest Ubuntu updates
* $ sudo apt update 
* $ sudo apt full-upgrade
* rebooted, not seemingly able to connect to RPi Zero, 
* Quite possibly RPi Zero requires other things to setup, likely also Ubuntu, but what?

Attempt 2
* Failure :(
* Unplugged USB cable from Dell
* Put MicroSD Card Adapter back into Dell laptop, 
* Put wpa_supplicant.conf file in /bootfs directory
* $ touch wpa_supplicant.conf, creates the file 
* Open in Text Editor add WiFi details
* Edit wpa_supplicant.conf file with with local respective values for country=, ssid=, psk=, 
* Content of file as below with placeholder values replaced with actual values, 
```

country=your_country_code

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={

    ssid="Your_Wi-Fi_SSID"

    psk="Your_Wi-Fi_Password"
    key_mgmt=WPA-PSK
    priority=1
}
```
* Put MicroSD Card Adapter back into RPi Zero env
* Plugged in USB cable to Dell laptop, RPi Zero ACT LED did not light green, not even flashing
* Rebooted Dell Ubuntu 24.04.3 with USB cable plugged in, RPi Zero ACT LED did not light green, not even flashing 
* Unplugged USB cable from Dell
* Put MicroSD Card Adapter back into Dell laptop, moved to trash, wpa_supplicant.conf file from /bootfs directory
* Put MicroSD Card Adapter back into RPi Zero env
* Plugged in USB cable to Dell laptop, RPi Zero ACT LED did not light green, not even flashing
* Unplugged USB cable from Dell
* Unplugged USB cable from RPi Zero
* Ejected MicroSD Card Adapter from RPi Zero env, 
* Took out the MicroSD Card from the Adapter, replaced the MicroSD Card back into the Adapter
* Plugged USB cable back to RPi Zero
* Plugged USB cable back to Dell
* RPi Zero ACT LED solid green, after initial flashing, 
* But no joy
```
$ lsusb -t

/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/16p, 480M
    |__ Port 004: Dev 002, If 0, Class=Wireless, Driver=btusb, 12M

    |__ Port 004: Dev 002, If 1, Class=Wireless, Driver=btusb, 12M

    |__ Port 007: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
    |__ Port 009: Dev 004, If 0, Class=Human Interface Device, Driver=usbhid, 12M

    |__ Port 012: Dev 005, If 0, Class=Video, Driver=uvcvideo, 480M

    |__ Port 012: Dev 005, If 1, Class=Video, Driver=uvcvideo, 480M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/8p, 5000M



$ usbip list -l
 - busid 1-12 (0c45:6713)

   Microdia : unknown product (0c45:6713)


 - busid 1-4 (0cf3:e300)

   Qualcomm Atheros Communications : QCA61x4 Bluetooth 4.0 (0cf3:e300)


 - busid 1-7 (138a:0091)

   Validity Sensors, Inc. : VFS7552 Touch Fingerprint Sensor (138a:0091)



 - busid 1-9 (04f3:24a1)
   Elan Microelectronics Corp. : unknown product (04f3:24a1)



$ nmcli connection show
NAME                UUID                                  TYPE       DEVICE 

BT-2QAFZ5           da27f6e8-a9c4-412e-ba5d-c4afffb0edbe  wifi       wlp2s0 

lo                  92afa887-aa67-4e0b-b77a-b6e41ffc920e  loopback   lo     
Galaxy A14 Network  a897e654-7ea7-4d9e-b130-5d4f226e8d5e  bluetooth  --    

```
* Might have failed first time due to faulty USB connection

Attempt 3
* Failure :(
* Unplugged USB cable from Dell
* Put MicroSD Card Adapter back into Dell laptop, 
* Put wpa_supplicant.conf file in /bootfs directory
* $ touch wpa_supplicant.conf, creates the file 
* Open in Text Editor add WiFi details
* Edit wpa_supplicant.conf file with with local respective values for country=, ssid=, psk=, 
* Content of file as below with placeholder values replaced with actual values, 
```

country=your_country_code
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev

update_config=1


network={


    ssid="Your_Wi-Fi_SSID"


    psk="Your_Wi-Fi_Password"

    key_mgmt=WPA-PSK

    priority=1
}

```
* Put MicroSD Card Adapter back into RPi Zero env
* Plugged in USB cable to Dell laptop, RPi Zero ACT LED light solid green, after initial flashing
* Hub Manager for local WiFi Router network, shows only 2 devices - Dell PC and Mobile Phone Galaxy A14 - connected to router via WiFi 5Ghz channel, 0 devices via 2.4GHz channel.
* Likely issue locale country code setting for RPi OS, see 2019-06-20: in [WS](https://downloads.raspberrypi.com/raspios_lite_armhf/release_notes.txt), from [WS](https://forums.raspberrypi.com/viewtopic.php?t=391776)

### Clean up, RPi OS on RPi MiroSD Card
Removing things done to RPi OS from the first process. 
* Remove from /bootfs/cmdline.txt
```
modules-load=dwc2,g_ether
```
* Remove from /bootfs/config.txt
```
[all] 
dtoverlay=dwc2
```
* Move to trash /bootfs/wpa_supplicant.conf
* Remove via cli /rootfs/boot/firmware/cmdline.txt
* Remove via cli /rootfs/boot/firmware/config.txt
```
york-earwaker@york-earwaker-XPS-15-9560:/media/york-earwaker/rootfs/boot/firmware$ ls -l
total 8
-rw-r--r-- 1 root root 26 Dec 20 13:25 cmdline.txt
-rw-r--r-- 1 root root 21 Dec 20 13:26 config.txt
-rw-r--r-- 1 root root  0 Dec 18 15:41 ssh
york-earwaker@york-earwaker-XPS-15-9560:/media/york-earwaker/rootfs/boot/firmware$ sudo rm cmdline.txt
[sudo] password for york-earwaker: 
york-earwaker@york-earwaker-XPS-15-9560:/media/york-earwaker/rootfs/boot/firmware$ ls -l
total 4
-rw-r--r-- 1 root root 21 Dec 20 13:26 config.txt
-rw-r--r-- 1 root root  0 Dec 18 15:41 ssh
york-earwaker@york-earwaker-XPS-15-9560:/media/york-earwaker/rootfs/boot/firmware$ sudo rm config.txt
york-earwaker@york-earwaker-XPS-15-9560:/media/york-earwaker/rootfs/boot/firmware$ ls -l
total 0
-rw-r--r-- 1 root root 0 Dec 18 15:41 ssh
```
* Retain /rootfs/boot/firmware/ssh, as per instructions in RPi Documentation
* Edit /rootfs/etc/wpa_supplicant file wpa_supplicant.conf, to remove additional wifi config text, returns to original state of
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
```

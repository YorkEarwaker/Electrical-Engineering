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
* <todo: consider, ascii art, RPi Zero , GPIO pinout diagram and table with pin descriptors, for inclusion in code file comment headers for circuit diagrams, >
* <todo: consider, list prerequisits for headless RPi Zero access of various sorts, setup before powering on, ssh file, WiFi wpa_supplicant.conf, Ethernet USB On-The-Go, Bluetooth, other, and so on, >
* <todo: consider, RYO voltage down shift device, resistors? research and test, for use with RPi Pico MCU powered by 5V RPi Zero SBC, >
* <todo: consider, investigate Ethernet connection to RPi Zero, first order of priority, On-The-Go cable RPi Zero type micro USB B  peripheral Dell laptop standard USB A acts as host, seemed not to work, buy anther cable, probs not, likely RPI Zero config issue, in Ubuntu desktop open bootfs add modules-load=dwc2,g_ether after rootwait in cmdline.txt and add dtoverlay=dwc2 under all section in config.txt, from tutorial, source offical Raspberry Pi docs, >
* <todo: consider, investigate Ethernet connection to RPi Zero, first order of priority, USB cable RPi Zero type micro B USB peripheral Dell laptop USB C acts as host, >
* <todo: consider, RPi Zero as mountable flash device, see RPi Magaizine article in references below, >
* <todo: consider, reuse old laptop screen as second dispaly for Dell and/or display for RPi Zero SBC, see references below for example, >
* <todo: consider, investigate scavange old laptop keyboard as standalone keyboard, probs more difficult than screen dispaly reuse? >
* <todo: consider, to setup RPi Zero correctly will have to purchase secondary BoM items, screen display, keyboard, and so on, >
* <todo: consider, is there some way to make headless RPi Zero work with USB cable work?, or is this just impossible? see heading; Output - headless to RPi Zero 2 W with USB cable, >

DONE
* <done: consider, intent to commit>
* <done: consider, as deployment option for Bosch BMV080 particulate matter sensor, >
* <done: consider, bill of materials for RPi Zero, compelted offline BoM in spreadsheet circa £64 inclusive 'useful' extras, >
* <done: consider, purchase of RPi Zero 2 W, and other items, completed, >
* <done: consider, for future use, first pass at wpa_supplicat.conf file, a Debian configuration file for WiFi, see referrences below,  >
* <done: consider, does the Micro USB B - OTG? - on the RPi Debug Probe device exhibit disconnection issue with the Linux Ubuntu LTS 24.04.3, Yes! likely same kernel issue, >

## Hardware

Bill of materials, BoM, original
* Raspberry Pi Zero 2 W, [WS](https://www.raspberrypi.com/products/raspberry-pi-zero/), Raspberry Pi, acquired
* Power Supply, 12.75 Raspberry Pi, acquired
* Micro SD Card, with RPi OS preinstalled, Raspberry Pi, acquired
* Micro SD Card Adapter, Raspberry Pi, acquired
* Micro SD to SD Extension Cable, acquired
* USB cable, standard USB A to Micro USB B, acquired

Bill of material, BoM +, USB to UART device, 
* Raspberry Pi Debug Probe, com [WS](https://www.raspberrypi.com/products/debug-probe/), Raspberry Pi, acquired
* USB to TTL Serial Cable for Raspberry Pi [WS](https://thepihut.com/products/usb-to-ttl-serial-cable-debug-console-cable-for-raspberry-pi), The Pi Hut, pending tbd
* USB TTL, CP2102 UART INTERFACE BOARD, [WS](https://cpc.farnell.com/sb-components/sku24797/usb-ttl-cp2102-uart-interface/dp/SC20242), CPC Farnell, acquired, treat as USB to TTL Serial Cable equivalent? 

BoM, To be considered --- to be purchased only if necessary, don't have one as intent was use headless from start, but may have to buy one
* HDMI cable, with Mini HDMI plug to display (screen) socket plug, 
* Display (screen), 
* Keyboard, 
* 40 Pin Raspberry Pi PCB GPIO Quick Connect Clip, [WS](https://www.kickstarter.com/projects/flatmax/pcb-quick-connect-clip-40-pin-raspberry-pi-compati), looks very interesting! no solder

Diagram of the eight main components on board the RPi Zero single board computer SBC. Larger than actual physical form factor.
```
        ---------------------------------------------------------------------------
      |         O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O          | 
      |         O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O       ___|_
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
Third Process. Attempting to connect to the RPi Zero 2 W 'headless. Using USB TTL to UART 
* TBD
* Two sub processes; firstly USB provides power, secondly mains provides power

Context Diagram - USB provides power, USB TTL to UART 3V + USB power 5V
* Sub process one
```
             RPi Zero 2 W                                                        Dell Ubuntu
             -----------                         Serial                          -----------
            |       o o |                      Connection                       |___        |
            |       o o | GPIO ---------------------------------- standard USB A ___|       |
            |       o o |                  Sink < Power < Source                |           |
             -----------                        < Data  >                        -----------
```
Circuit Diagram - USB provides power, USB TTL to UART 3V + USB power 5V
* Sub process one
* Work in progress to finish
```     
             _______
            |       |         ʌ  To Host          | ---------- | ----------- | --------|------------------------------- |
            | USB A |                             | Pin Number | UART Signal | Colour  | Description                    |
           -|_______|-                            | ---------- | ----------- | ---------------------------------------- |
           |         |        <  The USB          | 1          | TX          | Green   | 3V3 logic (Output of USB port) |
           |         |           Plug             | 2          | GND         | Black   | GND       (Ground)             |
           |         |                            | 3          | RX          | White   | 3V3 logic (Input to USB port)  |
           |         |        v To Target         | 4          | PWR         | Red     | 5V 500mA  (Power)              |
           |         |           UART             | ---------- | ----------- | --------|------------------------------- |
            ---------             
             |     |   
             |     |           <  The USB cable
              |||||            <  The USB jumper wires
             1 2 3 4            
             | | | |  
        
        
                      |  |  |
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
      |         O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O          | 
      |         O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O          |
                1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 
```
Context Diagram - mains provides power, USB TTL to UART 3V + mains power 5V
* Sub process two
```
             RPi Zero 2 W                                                        Dell Ubuntu
             -----------                         Serial                          -----------
   PWR IN   |___    o o |                      Connection                       |___        |
Micro USB B  ___|   o o | GPIO ---------------------------------- standard USB A ___|       |
 Src > Snk  |       o o |                                                       |           |
             -----------                        < Data  >                        -----------
```
Circuit Diagram - mains provides power, USB TTL to UART 3V + mains power 5V
* Sub process two
* Work in progress to finish
```     
             _______
            |       |         ʌ  To Host          | ---------- | ----------- | --------|------------------------------- |
            | USB A |                             | Pin Number | UART Signal | Colour  | Description                    |
           -|_______|-                            | ---------- | ----------- | ---------------------------------------- |
           |         |        <  The USB          | 1          | TX          | Green   | 3V3 logic (Output of USB port) |
           |         |           Plug             | 2          | GND         | Black   | GND       (Ground)             |
           |         |                            | 3          | RX          | White   | 3V3 logic (Input to USB port)  |
           |         |        v To Target         | 4          | PWR         | Red     | 5V 500mA  (Power)              |
           |         |           UART             | ---------- | ----------- | --------|------------------------------- |
            ---------             
             |     |   
             |     |           <  The USB cable
              |||||            <  The USB jumper wires
             1 2 3 4            
             | | | |   
        
        
                      |  |  |
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
      |         O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O          | 
      |         O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O          |
                1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 
```

### Prerequisites
Requirement for a serial communication program on Dell Ubuntu laptop to communicate via USB TTL serial cable, USB to UART connection, with RPi Zero 2 W . 

Hardware - USB to UART connection, one of the items below
* USB to TTL Serial Cable for Raspberry Pi [WS](https://thepihut.com/products/usb-to-ttl-serial-cable-debug-console-cable-for-raspberry-pi), The Pi Hut, 
* A N Other cable or device for USB to UART connectivity, Caution! requires 3V to RPi Zero 2 W via GPIO pin UART connection, so likely have to use resistors and a bread board to pull down to 3V .

### Connect RPi Zero 2 W to USB TTL serial cable
* Scenario one/Scenario twoS
TBD

## Output - headless to RPi Zero 2 W with Raspberry Pi Debug Probe
Second Process. Attempting to connect to the RPi Zero 2 W 'headless. Using Raspberry Pi Debug Probe.
* TBD

Primary Sources
* Raspberry Pi 3-pin Debug Connector Specification, [PDF](https://datasheets.raspberrypi.com/debug/debug-connector-specification.pdf), Raspberry Pi Datasheet, Error in pinout table
* Raspberry Pi Debug Probe, Product Brief, [PDF](https://datasheets.raspberrypi.com/debug/raspberry-pi-debug-probe-product-brief.pdf), Raspberry Pi Datasheet
* Raspberry Pi Debug Probe, User Guide, [WS](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html), Raspberry Pi Documentation
* Raspberry Pi Debug Probe, Firmware, [GH](https://github.com/raspberrypi/debugprobe), GitHub, Raspberry Pi, 
* USB org, [WS](https://www.usb.org/), USB Implementers Forum, Inc., USB specifications, 

Secondary Sources
* Headless, RPi Zero 2 W, configuration & connection guide, [WS](https://forums.raspberrypi.com/viewtopic.php?t=394836), Raspberry Pi Forums

Context Diagram
```
             RPi Zero 2 W                           RPi Debug Probe                                      Dell Ubuntu
             -----------          Serial             -----------                Serial                   -----------
   PWR IN   |___    o o |       Connection          |___     ___|   OTG?      Connection                |___        |
Micro USB B  ___|   o o | GPIO ------------ UART JST ___|   |___ Micro USB B ------------ standard USB A ___|       |
 Src > Snk  |       o o |                           |           |         Sink < Power < Source         |           |
             -----------         < Data >            -----------               < Data  >                 -----------
```
Circuit Diagram
```     
            _________
      ------\ Micro /------   ʌ  To Host          | ---------- | ----------- | ------------------------------ |
     |      | USB B |      |                      | Pin Number | UART Signal | Serial Debug Signal            | Colour  | Description
     |      |_______|      |                      | ---------- | ----------- | ------------------------------ |
     |                     |  <  The Debug        | 1          | TX          | SC (Serial Clock)              | Orange  | TX/SC (Output from Probe)
     |     Raspberry Pi    |     Host             | 2          | GND         | GND                            | Black   | GND   (Ground)
     |     Debug Probe     |                      | 3          | RX          | SD (bidirectional serial data) | Yellow  | RX/SD (Input to Probe or I/O)
     |                     |  v To Target         | ---------- | ----------- | ------------------------------ |
     |    _____   _____    |     U = UART
     |   |  U  | |  D  |   |     D = DEBUG
      ---      ---       ---     1.0mm pitch 3-pin JST ‘SH’ connector either BM03B-SRSS-TB (top entry) 
          | | |   | | |          or SM03B-SRSS-TB (side entry) types, or compatible alternatives .
          1 2 3   1 2 3
          | | |----------|
          |-(------------(--|
            |---------|  |  |
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
      |         O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O          | 
      |         O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O  O          |
                1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 
```

### Prerequisites
Requirement for a serial communication program on Dell Ubuntu laptop to communicate via RPi Debug Probe, USB to UART connection, with RPi Zero 2 W . 

Hardware - 
* Raspberry Pi Debug Probe, com [WS](https://www.raspberrypi.com/products/debug-probe/), Raspberry Pi, built in resistors for 3V to RPi Zero 2 W GPIO pin UART connection 
* A N Other debug probe of a similar nature, intermediary between host and RPi Zero

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

### Connect RPi Zero 2 W to RPi Debug Probe
Attempt 1
* Success! :)
* Clean up, see above
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
* Success! of sorts, but no cigar. RPi OS login credentials issues
* <todo: first read RPi Debug Probe documentation, work in progress>
* Added to /bootfs/config.txt
```
[all]
enable_uart=1
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
Bus 001 Device 008: ID 2e8a:000c Raspberry Pi Debug Probe (CMSIS-DAP)
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
```
* Find name of serial ports. Its there.
```
$ sudo dmesg | grep -i tty
[67346.152493] cdc_acm 1-2:1.1: ttyACM0: USB ACM device
```
* Make serial connection request with serial port and baud rate to GNU Screen
```
$ sudo screen /dev/ttyACM0 115200
```
* Connected to empty screen shell
* typed pi, then pressed return key
* After which presented with some login prompts as below.
* Can't seem to get login credentials correct. 
```
Login timed
Raspbian GNU/Linux 12 raspberrypi ttyS0

raspberrypi login: pi
Password:

Login incorrect
raspberrypi login: pi
Password:

Login incorrect
raspberrypi login: pi
Password:
Login timed
Raspbian GNU/Linux 12 raspberrypi ttyS0

raspberrypi login: pi
Password:

Login incorrect
raspberrypi login:
Password:

Login incorrect
raspberrypi login: raspb
Login timed
Raspbian GNU/Linux 12 raspberrypi ttyS0

raspberrypi login: raspberrypi
Password:

Login incorrect
raspberrypi login: raspberrypi
Password:

Login incorrect
raspberrypi login: pi
Password:

Login incorrect
raspberrypi login:
Login time
Raspbian GNU/Linux 12 raspberrypi ttyS0

raspberrypi login: 

```
* Pressed x on terminal window to kill process. Which also terminate /dev/ttyACM0 serial port. Have to unplug and plug back in RPi Debug Probe to get new serial port /dev/ttyACM0 .


## Output - headless to RPi Zero 2 W with USB cable
First Process. Attempting to connect to the RPi Zero 2 W 'headless' with USB cable. Using RPi documentation, RPi Forum, Online tutorials. 
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

Raspberry Pi Zero - datasheets, user guides, documentation
* Getting started, [WS](https://www.raspberrypi.com/documentation/computers/getting-started.html), Raspberry Pi Documentation
* Raspberry Pi Zero 2 W Product Brief, [WS](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-product-brief.pdf), Raspberry Pi Datasheet
* Raspberry Pi Zero Pinout, [WS](https://forums.raspberrypi.com/viewtopic.php?t=378242), Raspberry Pi Forum
* Raspberry Pi Zero Pinout, [WS](https://pinout.xyz/), xyz
* Raspberry Pi Zero Schematic, [WS](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-reduced-schematics.pdf), Raspberry Pi Datasheet
* Raspberry Pi Zero Test Pads [WS](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-test-pads.pdf), Raspberry Pi Datasheet
* Raspberry Pi Zero Mechanical Drawing [WS](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-mechanical-drawing.pdf), Raspberry Pi Datasheet
* Raspberry Pi 3-pin Debug Connector Specification, [WS](https://datasheets.raspberrypi.com/debug/debug-connector-specification.pdf), Raspberry Pi Datasheet
* ...

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
* 

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

WiFi - Debian, RPi OS, Ubuntu
* WiFi, wpa_supplicant file, [WS](https://wiki.debian.org/WiFi/HowToUse#wpa_supplicant) , debian, 

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

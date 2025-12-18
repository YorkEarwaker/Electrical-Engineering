# Raspberry Pi Zero rpi-z

Single board computer, 

## Status

TODO
* <todo: consider, hello world project>
* <todo: consider, test USB device disconnection issue with RPi OS and RPi Pico, does RPi OS endlessly increment USB device number as Ubuntu does? >
* <todo: consider, use as platform for Bosch Paticlate Sensor for C code application sensor particulate value readings, >
* <todo: consider, ascii art, RPi Zero , GPIO pinout diagram and table with pin descriptors, for inclusion in code file comment headers for circuit diagrams, >

DONE
* <done: consider, intent to commit>
* <done: consider, as deployment option for Bosch BMV080 particulate matter sensor, >
* <done: consider, bill of materials for RPi Zero, compelted offline BoM in spreadsheet circa £64 inclusive 'useful' extras, >
* <done: consider, purchase of RPi Zero 2 W, and other items, completed, >

## Libs

Raspberry Pi
* raspberry-gcc10.2.1-r2, SYS GCC for Windows x32 bit Platforms,[WS](https://sysprogs.com/getfile/2076/raspberry-gcc10.2.1-r2.exe/)
* raspberry64-gcc10.2.1, SYS GCC for Windows x64 bit Platforms, [WS](https://sysprogs.com/getfile/1804/raspberry64-gcc10.2.1.exe)

## Hardware

Bill of materials
* Raspberry Pi Zero, [WS](https://www.raspberrypi.com/products/raspberry-pi-zero/), Raspberry Pi
* Power Supply, 12.75 Raspberry Pi
* Micro SD Card, with RPi OS preinstalled, Raspberry Pi
* 

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
      |      |    Mini    |                        |  Data   |   | PWR IN  |        |
      |      |    HDMI    |                        | USB 2.0 |   | USB 5V  |        |
       ------/____________\------------------------/_________\---/_________\--------
```

## Output

### Create SSH file on SD Card
Remote Access, Enable the SSH server, [WS](ttps://www.raspberrypi.com/documentation/computers/remote-access.html#enable-the-ssh-server), Raspberry Pi, docs
* placed RPi micro SD Card in SD Card holder, 
* put RPi SD Card holder into laptop
* created ssh file as per instructions in link above.
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
* Put SD Card into RPi Zero, using an extension cable for easier access and to improve life of micro SD Card
* Put power micro USB into PWR IN USB slot
* Plugged in 12.75 Raspberry Pi Power adapter into mains
* Led, green light flashed on and off for a while, assuming during RPi OS boot sequence,
* Led, green light is permanently on after a while
* probably a mistake without having made necessary changes to SD card RPi OS changes first, unlikely ssh file creation was sufficient see above, 

### Headless, connect to RPi Zero from Dell laptop, USB cable
* <todo: trying this, but encountering difficulties, no first contact yet,  >
* probably not set up the RPi Zero correctly beforehand
* RPi Zero on, green Led solid green, 
* Plug in USB cable (data and power), Dell A standard type USB port, RPi Zero micro USB port, Pi Hut website reports cable compatible with Zero and carries data, 
* RPi Zero powered from mains with micro USB PWR IN port
* Retarted Dell laptop with USB cable attached to 
* Can't access RPi OS file system, so can't shut it down powering off,
* Option 1. remove SD card and make changes likely harms SD card file system, and changes likely won't be recognized until reboot anyway, which currently can't be done gracefully
* Option 2. unplug RPi Zero from mains will likely also harm SD card file system, 
* Option 3. add power down button to RPi Zero GPIO pins for equivalent of hard shut down on PC by holding down power button? investigate if this is possible may be less harmful than; removing SD card (option 1), pulling the plug (option 2) 
* Option 4. explore Dell to do on Ubuntu LTS 24.04.3 via Gnome desktop or terminal cli
* Option 5. keep RPi Zero powered on and purchase keyboard and display

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

### 

## References

Raspberry Pi Zero - datasheets, user guides
* Getting started, [WS](https://www.raspberrypi.com/documentation/computers/getting-started.html), Raspberry Pi
* Raspberry Pi Zero 2 W Product Brief, [WS](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-product-brief.pdf), Raspberry Pi
* Raspberry Pi Zero Pinout, [WS](https://forums.raspberrypi.com/viewtopic.php?t=378242), Raspberry Pi
* Raspberry Pi Zero Pinout, [WS](https://pinout.xyz/), xyz
* Raspberry Pi Zero Schematic, [WS](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-reduced-schematics.pdf), Raspberry Pi
* Raspberry Pi Zero Test Pads [WS](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-test-pads.pdf), Raspberry Pi
* Raspberry Pi Zero Mechanical Drawing [WS](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-mechanical-drawing.pdf), Raspberry Pi
* ...

SSH
* How do I turn off the green LED on my RPI Zero 2 W? [WS](https://forums.raspberrypi.com/viewtopic.php?t=328550), Raspberry Pi Forums, 
* How to boot up & start using raspberry pi using laptop as a monitor, [WS](https://raspberrypi.stackexchange.com/questions/84349/how-to-boot-up-start-using-raspberry-pi-using-laptop-as-a-monitor), StackExchange, Raspberry Pi, 
* Add ssh and wpa_supplicant.conf Files, [WS](https://seengreat.com/wiki/123/raspberry-pi-zero-2-w?#toc6), SeenGreat, 
* Raspberry Pi Zero W headless using wpa_supplicant.conf not working, [WS](https://raspberrypi.stackexchange.com/questions/67649/raspberry-pi-zero-w-headless-using-wpa-supplicant-conf-not-working), StackExchange, Raspberry Pi, 
* Connect to a Raspberry Pi Zero over USB on Ubuntu, [WS](https://johnnymatthews.dev/blog/2021-02-06-connect-to-raspberry-pi-zero-over-usb-on-ubuntu/), Johnny Matthews
* Setting up Pi Zero OTG - The quick way (No USB keyboard, mouse, HDMI monitor needed), [WS](https://gist.github.com/gbaman/975e2db164b3ca2b51ae11e45e8fd40a), gbaman, github

Debian 
* WiFi, wpa_supplicant file, [WS](https://wiki.debian.org/WiFi/HowToUse#wpa_supplicant) , debian, 

Power down
* Turning off power on a PI Zero W, [WS](https://forums.raspberrypi.com/viewtopic.php?t=215796), 









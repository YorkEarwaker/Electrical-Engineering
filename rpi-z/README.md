# Raspberry Pi Zero rpi-z

Single board computer, 

## Status

TODO
* <todo: consider, hello world project>
* <todo: consider, test USB device disconnection issue with RPi OS and RPi Pico, does RPi OS endlessly increment USB device number as Ubuntu does? >
* <todo: consider, use as platform for Bosch Particlate Sensor for C code application sensor particulate value readings, >
* <todo: consider, ascii art, RPi Zero , GPIO pinout diagram and table with pin descriptors, for inclusion in code file comment headers for circuit diagrams, >
* <todo: consider, list prerequisits for headless RPi Zero access of various sorts, setup before powering on, ssh file, WiFi wpa_supplicant.conf, Ethernet USB On-The-Go, Bluetooth, other, and so on, >
* <todo: consider, RYO voltage down shift device, resistors? research and test, >
* <todo: consider, investigate Ethernet connection to RPi Zero, first order of priority, On-The-Go cable RPi Zero type micro USB B  peripheral Dell laptop standard USB A acts as host, seemed not to work, buy anther cable, probs not, likely RPI Zero config issue, in Ubuntu desktop open bootfs add modules-load=dwc2,g_ether after rootwait in cmdline.txt and add dtoverlay=dwc2 under all section in config.txt, from tutorial, source offical Raspberry Pi docs, >
* <todo: consider, investigate Ethernet connection to RPi Zero, first order of priority, USB cable RPi Zero type micro B USB peripheral Dell laptop USB C acts as host, >
* <todo: consider, RPi Zero as mountable flash device, see RPi Magaizine article in references below, >
* <todo: consider, reuse old laptop screen as second dispaly for Dell and/or display for RPi Zero SBC, see references below for example, >
* <todo: consider, investigate scavange old laptop keyboard as standalone keyboard, probs more difficult than screen dispaly reuse? >

DONE
* <done: consider, intent to commit>
* <done: consider, as deployment option for Bosch BMV080 particulate matter sensor, >
* <done: consider, bill of materials for RPi Zero, compelted offline BoM in spreadsheet circa £64 inclusive 'useful' extras, >
* <done: consider, purchase of RPi Zero 2 W, and other items, completed, >
* <done: consider, for future use, first pass at wpa_supplicat.conf file, a Debian configuration file for WiFi, see referrences below,  >

## Libs

Raspberry Pi
* raspberry-gcc10.2.1-r2, SYS GCC for Windows x32 bit Platforms,[WS](https://sysprogs.com/getfile/2076/raspberry-gcc10.2.1-r2.exe/)
* raspberry64-gcc10.2.1, SYS GCC for Windows x64 bit Platforms, [WS](https://sysprogs.com/getfile/1804/raspberry64-gcc10.2.1.exe)

## Hardware

Bill of materials, BoM
* Raspberry Pi Zero, [WS](https://www.raspberrypi.com/products/raspberry-pi-zero/), Raspberry Pi, acquired
* Power Supply, 12.75 Raspberry Pi, acquired
* Micro SD Card, with RPi OS preinstalled, Raspberry Pi, acquired
* Micro SD Card adapter, Raspberry Pi, acquired
* SD Card cable, acquired

BoM, To be considered --- to be purchased only if necessary, don't have one as intent was use headless from start, but may have to buy one
* HDMI cable, with Mini HDMI plug to display (screen) socket plug, 
* Display (screen), 
* Keyboard, 

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

## Output

### Create SSH file on SD Card
Remote Access, Enable the SSH server, [WS](ttps://www.raspberrypi.com/documentation/computers/remote-access.html#enable-the-ssh-server), Raspberry Pi, docs
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
* <note: ssh file had already been created see heading >
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


### Headless, connect to RPi Zero 2 W from Dell laptop, Wifi
<todo: try this, but will likely require changes to RPi OS config files, >
* MicroSD Card Adapter in laptop
* Navigate to rootfs/etc/wpa_supplicant found there an admin rights protected file wpa_supplicant.conf 
* Opened as Administrator edited with with following with local respective values for country=, ssid=, psk=, 
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
* Can't see RPi Zero in WiFi Router Hub control panel, 
* Can't see RPi Zero with nmcli connection show
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
* Can't see RPi Zero with $ usbip list -l, list only usual Dell laptop component parts on bus 001 
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

### 

## References

Terms
* USB On-The-Go, [WP](https://en.wikipedia.org/wiki/USB_On-The-Go), 

Raspberry Pi Zero - datasheets, user guides
* Getting started, [WS](https://www.raspberrypi.com/documentation/computers/getting-started.html), Raspberry Pi
* Raspberry Pi Zero 2 W Product Brief, [WS](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-product-brief.pdf), Raspberry Pi
* Raspberry Pi Zero Pinout, [WS](https://forums.raspberrypi.com/viewtopic.php?t=378242), Raspberry Pi
* Raspberry Pi Zero Pinout, [WS](https://pinout.xyz/), xyz
* Raspberry Pi Zero Schematic, [WS](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-reduced-schematics.pdf), Raspberry Pi
* Raspberry Pi Zero Test Pads [WS](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-test-pads.pdf), Raspberry Pi
* Raspberry Pi Zero Mechanical Drawing [WS](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-mechanical-drawing.pdf), Raspberry Pi
* ...

SSH - RPi Zero OTG USB Ethernet, 
* How do I turn off the green LED on my RPI Zero 2 W? [WS](https://forums.raspberrypi.com/viewtopic.php?t=328550), Raspberry Pi Forums, 
* How to boot up & start using raspberry pi using laptop as a monitor, [WS](https://raspberrypi.stackexchange.com/questions/84349/how-to-boot-up-start-using-raspberry-pi-using-laptop-as-a-monitor), StackExchange, Raspberry Pi, 
* Add ssh and wpa_supplicant.conf Files, [WS](https://seengreat.com/wiki/123/raspberry-pi-zero-2-w?#toc6), SeenGreat, 
* Raspberry Pi Zero W headless using wpa_supplicant.conf not working, [WS](https://raspberrypi.stackexchange.com/questions/67649/raspberry-pi-zero-w-headless-using-wpa-supplicant-conf-not-working), StackExchange, Raspberry Pi, 
* Connect to a Raspberry Pi Zero over USB on Ubuntu, [WS](https://johnnymatthews.dev/blog/2021-02-06-connect-to-raspberry-pi-zero-over-usb-on-ubuntu/), Johnny Matthews
* Setting up Pi Zero OTG - The quick way (No USB keyboard, mouse, HDMI monitor needed), [WS](https://gist.github.com/gbaman/975e2db164b3ca2b51ae11e45e8fd40a), gbaman, github
* How to Setup a Raspberry Pi Without a Monitor or Keyboard (Video Tutorial), [WS](https://www.reddit.com/r/raspberry_pi/comments/dzgke0/how_to_setup_a_raspberry_pi_without_a_monitor_or/), Reddit, 
* How To Set Up Raspberry Pi Zero 2 W - Headless Mode, [WS](https://albert-fit.com/how-to-set-up-raspberry-pi-zero-2-w-headless-mode/), 12/01/2024, Albert Fit 
* RPi Zero USB OTG (usb-ethernet device), [WS](https://forums.raspberrypi.com/viewtopic.php?t=221259), Raspberry Pi Forums, 

SSH - RPi Zero soft shut down
* How to do a soft shutdown on headless Pi? [WS](https://forums.raspberrypi.com/viewtopic.php?t=306320), Raspberry Pi Forums, 

Headless - RPi Zero hard shut down
* Shutting down the Pi safely without SSH or a monitor?, [WS](https://raspberrypi.stackexchange.com/questions/59529/shutting-down-the-pi-safely-without-ssh-or-a-monitor), StackExchange, Raspberry Pi, 

Headless - RPi Zero power on
* Using Both PWR and USB in OTG Mode on the Pi Zero [WS](https://forums.raspberrypi.com/viewtopic.php?t=223891)

Ethernet, connect via USB, ... 
* ... to source

WiFi - Debian, RPi OS, Ubuntu
* WiFi, wpa_supplicant file, [WS](https://wiki.debian.org/WiFi/HowToUse#wpa_supplicant) , debian, 

BlueTooth
* ... to source

Flash
* Make a Pi Zero W Smart USB flash drive , [WS](https://magazine.raspberrypi.com/articles/pi-zero-w-smart-usb-flash-drive), Russell Barnes. 

Screen
* Re-purposed Laptop Screen for Raspberry Pi, [WS](https://www.instructables.com/Re-purposed-Laptop-Screen-for-Raspberry-Pi/), AutoDesk Instructables, lerigsby12 in Circuits, Raspberry Pi
* Home Raspberry Pi Desktop With Old Laptop Screen, [WS](https://www.instructables.com/Home-Raspberry-Pi-Desktop-With-Old-Laptop-Screen/), AutoDesk Instructables, Ashu_d in Circuits, Raspberry Pi
* Connect Pi to an old laptop screen, [WS](https://raspberrypi.stackexchange.com/questions/848/connect-pi-to-an-old-laptop-screen), StackExchange, Raspberry Pi, 
* Old laptop display (40pins)how to use as a raspberry pi 4 B display(15pins), [WS](https://forums.raspberrypi.com/viewtopic.php?t=277682), Forums, Raspberry Pi, 
* Re-purposing old laptop LCD via Raspberry Pi, [WS](https://forums.raspberrypi.com/viewtopic.php?t=255727), Forums, Raspberry Pi, 
* Using laptop screen with RPI, [WS](https://forums.raspberrypi.com/viewtopic.php?t=234270), Forums, Raspberry Pi, 

Power down, power off, 
* Turning off power on a PI Zero W, [WS](https://forums.raspberrypi.com/viewtopic.php?t=215796), Forums, Raspberry Pi, 

SD Card, MicroSD card removal
* Can I temporarily remove the SD card while my device is turned on?, [WS](https://raspberrypi.stackexchange.com/questions/3759/can-i-temporarily-remove-the-sd-card-while-my-device-is-turned-on), StackExchange, Raspberry Pi, 

SSH file location
* Placing SSH File on New SDCard, [WS](https://forums.raspberrypi.com/viewtopic.php?t=314900), Forums, Raspberry Pi, 
* "Put an empty 'ssh' file in /boot/" trick not working anymore [WS](https://raspberrypi.stackexchange.com/questions/98719/put-an-empty-ssh-file-in-boot-trick-not-working-anymore), StackExchange, Raspberry Pi, 
* Enabling SSH by default on Raspbian Stretch [WS](https://raspberrypi.stackexchange.com/questions/73119/enabling-ssh-by-default-on-raspbian-stretch), StackExchange, Raspberry Pi, 

USB Ethernet - Ubuntu, RPi OS, debian, linux, 
* How to set up an usb/ethernet interface in Linux? [WS](https://unix.stackexchange.com/questions/386162/how-to-set-up-an-usb-ethernet-interface-in-linux), StackExchange, Unix Linux
* How to Share your USB Device in Ubuntu 24.04 over LAN, [WS](https://ubuntuhandbook.org/index.php/2024/09/share-usb-ubuntu-lan/), Ubuntu Handbook, **** Looks important generally, not sure it is relevant with USB RPi Zero connection to Dell laptop.
* RTL8125 2.5GbE Ethernet port not working in Ubuntu 24.04, [WS](https://discourse.ubuntu.com/t/rtl8125-2-5gbe-ethernet-port-not-working-in-ubuntu-24-04/55551/1), Discourse, Ubuntu, 
* No Network Connection with 24.04 and r8125 Ethernet, [WS](https://discourse.ubuntu.com/t/no-network-connection-with-24-04-and-r8125-ethernet/58589), Discourse, Ubuntu, 
* ...

USB OTG - Raspberry Pi 
* STICKY: USB device not working on Raspberry Pi Zero, 1, 2, 3? Click here!, [WS](https://forums.raspberrypi.com/viewtopic.php?t=53832&sid=e1f95c7352ca64da9a75c5c7d0b71f87), Forums, Raspberry Pi, 






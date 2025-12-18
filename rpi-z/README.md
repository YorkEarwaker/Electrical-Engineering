# Raspberry Pi Zero rpi-z

Single board computer, 

## Status

TODO
* <todo: consider, hello world project>
* <todo: consider, test USB device disconnection issue with RPi OS and RPi Pico, does RPi OS endlessly increment USB device number as Ubuntu does? >
* <todo: consider, use as platform for Bosch Paticlate Sensor for C code application sensor particulate value readings, >

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
* Power Supply, 
* Micro SD Card, 
* 

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

Pi0 - examples
* https://raspberrypi.stackexchange.com/questions/84349/how-to-boot-up-start-using-raspberry-pi-using-laptop-as-a-monitor





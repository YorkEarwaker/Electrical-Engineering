## SD Card sdc

RPi Pico SD Card SPI interface, memory extension for RPi Pico to extend life of Pico flash memory, eMMC and SD

## Status

TODO
* <todo: SD Card extension for RPi Pico, breakout board/ >
* <todo: consider, SDIO support rpi pico, not yet part of official SDK as of 06/05/2025? investigate prototype library that includes 1 and 4 bit SDIO support using PIO, up to 4 data pins at once,  SD Card use case, other use cases?, >

DONE
* <done: consider, SD Card storage project to increase total storage above onboard 2MB RPi Pico flash storage, MicroPython taking up to 600kB storage and available storage reduced to 1448kB, limiting ~20k flash writes/delete cycles lifetime, falsh is not replacable, SD Card extension is replaceable component, Weather station project \amn might benefit from this solution central data storage hub 'mother' Pico and spoke 'children' Pico's sensor control data logging to data hub 'mother' SD Card, good use of componentisation, loose coupling, high cohesion, . spoke 'child' low spec Pico or even lower spec MCU?  >
* <done: consider, MicroPython library support for, SD Cards, eMMC cards, SD vs eMMC,  sdcard.py mpy driver for SD Cards, FAT32 formatted best option for pico? >


## Libraries

Standards
* SD Specifications, Part 1, Physical Layer, Simplified Specification, Version 2.00, 25 September 2006 , [PDF](https://users.ece.utexas.edu/~valvano/EE345M/SD_Physical_Layer_Spec.pdf)

Libs
* SD, [WS](https://docs.arduino.cc/libraries/sd/), Arduino SD library, 
* SD, CircuitPython
* SD, [WS](https://os.mbed.com/cookbook/SD-Card-File-System), ARM, mbed, 
* SD, [GH](https://github.com/micropython/micropython-lib/tree/master/micropython/drivers/storage/sdcard), MicroPython, sdcard.py
* SD, [GH](https://github.com/raspberrypi/pico-extras/tree/master/src/rp2_common/pico_sd_card), Raspbery Pi, C/C++. pico_sd_card
* (e)MMC/SD card driver, 
* SDIO, driver, 

## References

Terms
* SD Card
* eMMC Card

News Papers - External storage, i.e. SD Card memmory extension to RPi Pico 
* SD Card Read Write,  [WS](https://www.digikey.com/en/maker/projects/raspberry-pi-pico-rp2040-sd-card-example-with-micropython-and-cc/e472c7f578734bfd96d437e68e670050), Maker . io,  
* Raspberry Pi Pico -- Micro SD Card Interface, [WS](https://www.instructables.com/Raspberry-Pi-Pico-Micro-SD-Card-Interface/), Autodesk, Instructables, 
* Initializing an SD Card, [WS](http://www.rjhcoding.com/avrc-sd-interface-1.php), RJH coding . com

News Papers - SD Cards, forum, Raspberry Pi, 
* SD card with a pico, [WS](https://forums.raspberrypi.com/viewtopic.php?t=344610), forums, Raspberry Pi, 
* Use SDCard with MicroPython on Raspberry Pi Pico, [WS](https://forums.raspberrypi.com/viewtopic.php?t=307275), forums, Raspberry Pi, 
* Pico w/4-bit SDIO interface example?, [WS](https://forums.raspberrypi.com/viewtopic.php?t=337143), forums, Raspberry Pi, 
* ...
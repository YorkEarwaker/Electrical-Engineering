## Secure Digital Card sdc

RPi Pico SD Card SPI interface, memory extension for RPi Pico to extend life of Pico flash memory, eMMC and SD

Primary use case in relation to \amn project for data logging time series data. 

## Status

TODO
* <todo: SD Card extension for RPi Pico, breakout board/shield/hat, candidate for first project roll your own PCB? perf board? >
* <todo: consider, SDIO support rpi pico, not yet part of official SDK as of 06/05/2025? investigate prototype library that includes 1 and 4 bit SDIO support using PIO, up to 4 data pins at once,  SD Card use case, other use cases?, >
* <todo: consider, I2C support RPi Pico, libraries to source, 3rd party projects to identify, >
* <todo: consider, determine if Pololu device can be wired to Pico for dual use, SPI and SDIO, using same pinout but different mpy code pin allocation? Pololu device has eleven (11) pins >
* <todo: consider, level shifters and voltage dividers, for devices/system integration with logic level signals above V3.3, further research required, components tobe identified, this should probably be part of a seperate PoC of mixed voltage systems integration, >
* <todo: consider, moving adc_thing.py files to a different sub project? or keep here due to ADC.CORE_TEMP datalogging example? perhaps seperate analogue to digital converter ADC direcory, >

DONE
* <done: consider, SD Card storage project to increase total storage above onboard 2MB RPi Pico flash storage, MicroPython taking up to 600kB storage and available storage reduced to 1448kB, limiting ~20k flash writes/delete cycles lifetime, falsh is not replacable, SD Card extension is replaceable component, Weather station project \amn might benefit from this solution central data storage hub 'mother' Pico and spoke 'children' Pico's sensor control data logging to data hub 'mother' SD Card, good use of componentisation, loose coupling, high cohesion, . spoke 'child' low spec Pico or even lower spec MCU?  >
* <done: consider, MicroPython library support for, SD Cards, eMMC cards, SD vs eMMC,  sdcard.py mpy driver for SD Cards, FAT32 formatted best option for pico? >
* <done: consider, extension cable, for micro SD Card, improve life of sd card, ability to move sd card between sd card breakout boaords, ability to use sd card in RPi 5 or laptop, >
* <done: consider, micro SD card 'pin out' map to SPI>
* <done: consider, micro SD card 'pin out' map to SD interface >
* <done: consider, candidate wiring for breadboard for Pololu SD Card reader, breadboard wired using Pojo>

## Readings

### Rotating Potentiometer, voltage divider, 0V to 3.3V
Potential data to log, in datalogger

>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot

 voltage: 3.3, raw 65535
 voltage: 3.3, raw 65535
 voltage: 3.042133, raw 60414
 voltage: 3.071137, raw 60990
 voltage: 2.571517, raw 51068
 voltage: 2.248341, raw 44650
 voltage: 2.11057, raw 41914
 voltage: 1.671376, raw 33192
 voltage: 1.543223, raw 30647
 voltage: 1.191041, raw 23653
 voltage: 1.144312, raw 22725
 voltage: 0.4730327, raw 9394
 voltage: 0.4730327, raw 9394
 voltage: 0.004834058, raw 96
 voltage: 0.004834058, raw 96
 voltage: 0.004834058, raw 96
 voltage: 0.002417029, raw 48
 voltage: 0.004834058, raw 96

## Libraries

Standards
* SD Association SDA, org [WS](https://www.sdcard.org/), SD Card org
* SD Standard Overview, [WS](https://www.sdcard.org/developers/sd-standard-overview/), SD Card org, 
* Simplified Specifications, [WS](https://www.sdcard.org/downloads/pls/), SD Card org
* Secure Digital Card upto 2GB, SD Specifications, Part 1, Physical Layer, Simplified Specification, Version 2.00, 25 September 2006, [PDF](https://users.ece.utexas.edu/~valvano/EE345M/SD_Physical_Layer_Spec.pdf)
* SDHC Secure Digital High Capacity upto 32GB
* SDXC Secure Digital eXtended Capacity upto 2TB
* SDUC Secure Digial Ultra Capacity upto 128TB

Libs
* SD, [WS](https://docs.arduino.cc/libraries/sd/), Arduino SD library, 
* SD, CircuitPython
* SD, [WS](https://os.mbed.com/cookbook/SD-Card-File-System), ARM, mbed, 
* SD, [GH](https://github.com/micropython/micropython-lib/tree/master/micropython/drivers/storage/sdcard), MicroPython, sdcard.py
* SD, [GH](https://github.com/raspberrypi/pico-extras/tree/master/src/rp2_common/pico_sd_card), Raspbery Pi, C/C++. pico_sd_card
* (e)MMC/SD card driver, 
* SDIO, driver, 
* FreeRTOS +FAT, the SD card driver, [GH](https://github.com/carlk3/FreeRTOS-FAT-CLI-for-RPi-Pico)

## Hardware

SD Card 'reader' boards - assessment, evaluation, RPi Pico 2 W, system/device voltage v3.3 
* Adafruit Micro SD SPI or SDIO Card Breakout Board, The Pi Hut suppler [WS](https://thepihut.com/products/adafruit-micro-sd-spi-or-sdio-card-breakout-board-3v-only)
* Pololu Breakout Board for MicroSD Cards, The Pi Hut suppler [WS](https://thepihut.com/products/pololu-breakout-board-for-microsd-cards), product [WS](https://www.pololu.com/product/2597), schematic [PDF](https://www.pololu.com/file/0J808/breakout-board-for-microsd-card-schematic.pdf), Not v3.3 shifted for use in v5 systems integration, 
* <todo: others to assess>

Level shifters, voltage dividers  - assessment, evaluation, , system/device voltage greater than V3.3, RPi Pico (also RPi 5?) operates at V3.3, SD Cards operate between V2.7 V3.6 ? 
* Pololu Logic Level Shifter, 4-Channel, Bidirectional, product [WS](https://www.pololu.com/product/2595), schematic [PDF](https://www.pololu.com/file/0J752/ls01a-logic-level-shifter-schematic.pdf), This logic level converter requires two supply voltages: the lower-voltage logic supply (1.5 V to 7 V) connects to the LV pin and the higher-voltage supply (LV to 18 V) connects to the HV pin. The HV supply must be higher than the LV supply for proper operation. Is this required for use with RPi Pico? probably not but an interesting solution for other dibirectional voltage high/low low/high. If RPi Pico has to integrate with higher voltage device/systems

SD Card 'reader' boards - assessment, evaluation, , for use with system/device voltage v5 +
* Pololu Breakout Board for microSD Card with 3.3V Regulator and Level Shifters, product [WS](https://www.pololu.com/product/2587), schematic [PDF](https://www.pololu.com/file/0J873/breakout-board-for-micro-sd-card-with-regulator-and-level-shifters-schematic.pdf), direct integrated into 5 V systems

## References

Terms
* SD Card, [WP](https://en.wikipedia.org/wiki/SD_card)
* eMMC , MultiMediaCard, precursor standard to SD Card, slower, less data, 
* Serial Periferal Interface SPI [WP](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface)
* Secure Digital Input Output SDIO, [WP](https://en.wikipedia.org/wiki/SD_card#SDIO_cards)

News Papers - External storage, i.e. SD Card memmory extension to RPi Pico 
* SD Card Read Write,  [WS](https://www.digikey.com/en/maker/projects/raspberry-pi-pico-rp2040-sd-card-example-with-micropython-and-cc/e472c7f578734bfd96d437e68e670050), Maker . io,  
* Raspberry Pi Pico -- Micro SD Card Interface, [WS](https://www.instructables.com/Raspberry-Pi-Pico-Micro-SD-Card-Interface/), Autodesk, Instructables, 
* Initializing an SD Card, [WS](http://www.rjhcoding.com/avrc-sd-interface-1.php), RJH coding . com
* Raspberry Pi Pico (RP2040) SD Card Example with MicroPython and C/C++, [WS](https://www.digikey.com/en/maker/projects/raspberry-pi-pico-rp2040-sd-card-example-with-micropython-and-cc/e472c7f578734bfd96d437e68e670050), 2021-07-26, ShawnHymel, 

News Papers - SD Cards, forum, Raspberry Pi, 
* SD card with a pico, [WS](https://forums.raspberrypi.com/viewtopic.php?t=344610), forums, Raspberry Pi, 
* Use SDCard with MicroPython on Raspberry Pi Pico, [WS](https://forums.raspberrypi.com/viewtopic.php?t=307275), forums, Raspberry Pi, 
* Pico w/4-bit SDIO interface example?, [WS](https://forums.raspberrypi.com/viewtopic.php?t=337143), forums, Raspberry Pi, 
* ...
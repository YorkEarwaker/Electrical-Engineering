## Secure Digital Card sdc (mpy)

RPi Pico SD Card SPI interface, memory extension for RPi Pico to extend life of Pico flash memory. Memory extention kinds inclusive of but not limited to; SD, MMC, eMMC . Other projects to deal with concern of memory extention via usb stick a similar use case, and vau external harddisk module, cloud, and so on. 

Format as FAT32 for SPI and MicroPython. 

Use Cases
* Primary use case 
	* for data logging time series data. in relation to Climate Model \amn project 
* Secondary use cases include;
	* to hold configuration files so as not to have to change code excuting on Rpi Pico
	* to hold static file like html files ...

## Status

TODO
* <todo: consider, SDIO support rpi pico, not yet part of official SDK as of 06/05/2025? investigate prototype library that includes 1 and 4 bit SDIO support using PIO, up to 4 data pins at once,  SD Card use case, other use cases?, >
* <todo: consider, I2C support RPi Pico, libraries to source, 3rd party projects to identify, >
* <todo: consider, determine if Pololu device can be wired to Pico for dual use, SPI and SDIO, using same pinout but different mpy code pin allocation? Pololu device has eleven (11) pins >
* <todo: consider, level shifters and voltage dividers, for devices/system integration with logic level signals above V3.3, further research required, components tobe identified, this should probably be part of a seperate PoC of mixed voltage systems integration, >
* <todo: consider, moving adc_thing.py files to a different sub project? or keep here due to ADC.CORE_TEMP datalogging example? perhaps seperate analogue to digital converter ADC direcory, >
* <todo: consider, bottom out licencing requirement for SDIO interface - dito for SDMMC protocols are they the same thing as SDIO - for SD Card modules, is there a fair use dev free to use licence opt out? >
* <todo: consider, is it possible to boot from an SD Card with Raspberry Pi Pico? >
* <todo: consider, differences of SD Card formatting for use cases;  SD Card for Raspbian OS (FAT32 and EXT4?) for RPi IV/V/B/Zero/..., SD Card for data logger (FAT32) for RPi Pico, other use case? >
* <todo: consider, is the SD Card required to be a formatted as a single partition for SD Card logging and Raspberry Pi Pico? >
* <todo: consider, for data logging on SD Card with Raspberry Pi Pico SD Card cannot be larger than 32Gig due to FAT32 or other SD Card formatting restrictions? >
* <todo: consider, allocation unit size aka cluster size for MVP data logger, which unit size/cluster size would be best? how large will data logs get for time series data between transfer eleswhere via wifi or other network option, will other file tpyes be used in in mixed use case for data logger sd card, or should it only be restricted to data logging use case, >
* <todo: cconsider, can a database to be used by RPi Pico be installed on and run from SD Carad? SQLlite or similar? >

DONE
* <done: consider, SD Card extension for RPi Pico, breakout board/shield/hat, candidate for first project roll your own PCB? perf board? intial two cadidates; Pololu Breakout Board for MicroSD Cards, Adafruit Micro SD SPI or SDIO Card Breakout Board, >
* <done: consider, SD Card storage project to increase total storage above onboard 2MB RPi Pico flash storage, MicroPython taking up to 600kB storage and available storage reduced to 1448kB, limiting ~20k flash writes/delete cycles lifetime, falsh is not replacable, SD Card extension is replaceable component, Weather station project \amn might benefit from this solution central data storage hub 'mother' Pico and spoke 'children' Pico's sensor control data logging to data hub 'mother' SD Card, good use of componentisation, loose coupling, high cohesion, . spoke 'child' low spec Pico or even lower spec MCU?  >
* <done: consider, MicroPython library support for, SD Cards, eMMC cards, SD vs eMMC,  sdcard.py mpy driver for SD Cards, FAT32 formatted best option for pico? >
* <done: consider, extension cable, for micro SD Card, improve life of sd card, ability to move sd card between sd card breakout boaords, ability to use sd card in RPi 5 or laptop, >
* <done: consider, micro SD card 'pin out' map to SPI>
* <done: consider, micro SD card 'pin out' map to SD interface >
* <done: consider, candidate wiring for breadboard for Pololu SD Card reader, breadboard wired using Pojo>
* <done: consider, does SPI require FAT32, SPI used for SD Card interface with Raspberry Pi Pico, Pico does not support SDMMC natively so SPI id only option as of 25/06/2025, third party SDMMC drivers are avialble, MicroPython supports FAT32, SPI with MicroPython, yes FAT32 required for this used case >
* <done: consider, quick format FAT32, volume lable 'Pico_Data', 32k allocation unit size, windows 10 mounts card and formats it, Rpi Pico & Thonny IDE  & sdcard.py still exception thrown 'no SD card'.  >
* <done: consider, full format FAT32, volume lable 'Pico_Data', 32k allocation unit size, windows 10 mounts card and formats it, Rpi Pico & Thonny IDE  & sdcard.py still exception thrown 'no SD card'.  >
* <done: consider, wiring on breadboard, success! There was a wiring issue, now resolved, proves Pongo pin clamp works, implies must test current setup without first formating SD Card to FAT32, >

## Readings

### Rotating Potentiometer, voltage divider, 0V to 3.3V
Potential sample test data to log, in datalogger

>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot

 voltage: 3.3, raw: 65535 . 
 voltage: 3.3, raw: 65535 . 
 voltage: 2.881753, raw: 57229 . 
 voltage: 2.524788, raw: 50140 . 
 voltage: 2.03398, raw: 40393 . 
 voltage: 1.512607, raw: 30039 . 
 voltage: 0.9146441, raw: 18164 . 
 voltage: 0.5205676, raw: 10338 . 
 voltage: 0.02658732, raw: 528 . 
 voltage: 0.004028382, raw: 80 . 
 voltage: 0.004834058, raw: 96 . 
 voltage: 0.004834058, raw: 96 . 
 voltage: 0.004028382, raw: 80 . 
 voltage: 0.004834058, raw: 96 . 

### RPi Pico internal core temperature - no heat added to CPU
Potential sample test data to log, in datalogger

>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot

PICO CPU temperature: 22.8311, converted raw reading: 0.7131746, raw reading: 14163 . 
PICO CPU temperature: 23.76739, converted raw reading: 0.7115633, raw reading: 14131 . 
PICO CPU temperature: 23.29925, converted raw reading: 0.712369, raw reading: 14147 . 
PICO CPU temperature: 22.8311, converted raw reading: 0.7131746, raw reading: 14163 . 
PICO CPU temperature: 23.29925, converted raw reading: 0.712369, raw reading: 14147 . 
PICO CPU temperature: 23.76739, converted raw reading: 0.7115633, raw reading: 14131 . 
PICO CPU temperature: 23.29925, converted raw reading: 0.712369, raw reading: 14147 . 
PICO CPU temperature: 23.76739, converted raw reading: 0.7115633, raw reading: 14131 . 
PICO CPU temperature: 22.8311, converted raw reading: 0.7131746, raw reading: 14163 . 
PICO CPU temperature: 23.29925, converted raw reading: 0.712369, raw reading: 14147 . 
PICO CPU temperature: 23.29925, converted raw reading: 0.712369, raw reading: 14147 . 

### RPi Pico internal core temperature - heat added to CPU, tip of finger placed on top of CPU
Potential sample test data to log, in datalogger

>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot

PICO CPU temperature: 22.8311, converted raw reading: 0.7131746, raw reading: 14163 . 
PICO CPU temperature: 23.76739, converted raw reading: 0.7115633, raw reading: 14131 . 
PICO CPU temperature: 23.29925, converted raw reading: 0.712369, raw reading: 14147 . 
PICO CPU temperature: 22.8311, converted raw reading: 0.7131746, raw reading: 14163 . 
PICO CPU temperature: 24.70368, converted raw reading: 0.7099519, raw reading: 14099 . 
PICO CPU temperature: 24.23554, converted raw reading: 0.7107576, raw reading: 14115 . 
PICO CPU temperature: 27.0444, converted raw reading: 0.7059236, raw reading: 14019 . 
PICO CPU temperature: 24.70368, converted raw reading: 0.7099519, raw reading: 14099 . 
PICO CPU temperature: 24.23554, converted raw reading: 0.7107576, raw reading: 14115 . 
PICO CPU temperature: 24.70368, converted raw reading: 0.7099519, raw reading: 14099 . 
PICO CPU temperature: 26.57626, converted raw reading: 0.7067292, raw reading: 14035 .

### RPi Pico recognises SD Card

>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot

sd_card_spi: SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, sck=10, mosi=11, miso=12)
micro sd card: <SDCard object at 20010940>
os mount point: None
sys vol info: ['System Volume Information']

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

## Disk Management
SD Card formatting and partitioning

Raspberry Pi Imager ? <todo: consider, investigate further>

SD Association - sdc format FAT32 and other file system kinds, what are the downsides using the SD Association 'official' formatter? - software product
* SD Card Formatter, FAQs [WS](https://www.sdcard.org/downloads/formatter/faq/), SD Association, 
* SD Card Formatter 5.0.3 for Windows/Mac User’s Manual, Version 1.11, December 13, 2024, [PDF](https://www.sdcard.org/pdf/SD_CardFormatterUserManualEN.pdf), SD Association, 

DiskGenius - sdc format FAT32, might offer misleading advice re Raspberry Pi and Raspberry Pi Pico - software product
* The 6 Best SD Card Format Tools to Format SD Cards in Windows 11/10, [WS](https://www.diskgenius.com/resource/sd-card-format-tools.html), Anne, 18 July 2020 last updated
* How to Format EXT4/3/2 in Windows 10/8/7/XP?, [WS](https://www.diskgenius.com/how-to/format-ext4-windows.php) ???? does RPi Pico require Ext4? for micro SD Card useage?

## References

Terms
* SD Card, [WP](https://en.wikipedia.org/wiki/SD_card)
* MMC , MultiMediaCard, precursor standard to SD Card, slower, less data,
* eMMC, embedded?
* Serial Periferal Interface SPI [WP](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface)
* Secure Digital Input Output SDIO, [WP](https://en.wikipedia.org/wiki/SD_card#SDIO_cards)

MicroPython
* Machine, SD Card class, docs, [WS](https://docs.micropython.org/en/latest/library/machine.SDCard.html), 
* sdcard, code, [GH](https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/storage/sdcard/sdcard.py), driver

MicroPython Forum
* Pico Mounting SD Card, [WS](https://forum.micropython.org/viewtopic.php?t=9700&start=20), MicroPython Forum (Archive), 
* SD card file write, [WS](https://forum.micropython.org/viewtopic.php?t=3100), MicroPython Forum (Archive), 

Raspberry Pi - github, error
* Raspberry Pi Pico SD Card Errors #11483, [GH](https://github.com/micropython/micropython/issues/11483)
* no SD card #627, [GH](https://github.com/micropython/micropython-lib/issues/627)
* Raspberry Pi Pico SD Card Errors #656, [GH](https://github.com/micropython/micropython-lib/issues/656)
* OSError: no SD card #871 [GH](https://github.com/micropython/micropython-lib/issues/871)

Pimoroni
* Pico Wireless - how to access SD card?, [WS](https://forums.pimoroni.com/t/pico-wireless-how-to-access-sd-card/17751/1)

News Papers - External storage, i.e. SD Card memmory extension to RPi Pico 
* Raspberry Pi Pico -- Micro SD Card Interface, [WS](https://www.instructables.com/Raspberry-Pi-Pico-Micro-SD-Card-Interface/), Autodesk, Instructables, 
* Initializing an SD Card, [WS](http://www.rjhcoding.com/avrc-sd-interface-1.php), RJH coding . com
* Raspberry Pi Pico (RP2040) SD Card Example with MicroPython and C/C++, [WS](https://www.digikey.com/en/maker/projects/raspberry-pi-pico-rp2040-sd-card-example-with-micropython-and-cc/e472c7f578734bfd96d437e68e670050), 2021-07-26, ShawnHymel, Maker . io,  
* Connecting an SD Card to a Raspberry Pi Pico [WS](http://www.d3noob.org/2022/10/connecting-sd-card-to-raspberry-pi-pico.html), 30 October 2022
* Raspberry Pi Pico: MicroSD Card Guide with Datalogging Example (MicroPython) [WS](https://randomnerdtutorials.com/raspberry-pi-pico-microsd-card-micropython/), random tutorials, 

News Papers - SD Cards, forum, Raspberry Pi, 
* SD card with a pico, [WS](https://forums.raspberrypi.com/viewtopic.php?t=344610), forums, Raspberry Pi, 
* Use SDCard with MicroPython on Raspberry Pi Pico, [WS](https://forums.raspberrypi.com/viewtopic.php?t=307275), forums, Raspberry Pi, 
* Pico w/4-bit SDIO interface example?, [WS](https://forums.raspberrypi.com/viewtopic.php?t=337143), forums, Raspberry Pi, 
* ...

News Papers - os, path, file
* How to Check if a File Exists in Python with isFile() and exists(), [WS](https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/), January 5, 2023, Dionysia Lemonaki

News Papers - sdc format FAT32
* Difference between quick format and slow format?, [WS](https://www.reddit.com/r/DataHoarder/comments/y58k35/difference_between_quick_format_and_slow_format/), Reddit, 
* The SD Association has an official SD card formatter (sdcard .org), [WS](https://news.ycombinator.com/item?id=41445898), Hacker News, 
* What is the standard file system that a SD card have to use before write Raspbian using dd command?, [WS](https://raspberrypi.stackexchange.com/questions/17110/what-is-the-standard-file-system-that-a-sd-card-have-to-use-before-write-raspbia), StackExchange, Raspberry Pi
* What format should my SD card be? [duplicate], [WS](https://raspberrypi.stackexchange.com/questions/23281/what-format-should-my-sd-card-be), StackExchange, Raspberry Pi
* Format SD Card from Console, [WS](https://forums.raspberrypi.com/viewtopic.php?t=329474), Raspberry Pi Forum, 
* fat32 sd card, [WS](https://forums.raspberrypi.com/viewtopic.php?t=261901), Raspberry Pi Forum, 
* Which Allocation Unit Size do I have to choose for my SDHC card?, [WS](https://superuser.com/questions/455098/which-allocation-unit-size-do-i-have-to-choose-for-my-sdhc-card), StackExchange, SuperUser
* Block size & lots of small files, [WS](https://forums.raspberrypi.com/viewtopic.php?t=133349), Raspberry Pi Forum, 



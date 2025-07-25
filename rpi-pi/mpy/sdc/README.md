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
* <todo: consider, retrieve file from sd card, file transfer via wifi, push and pull varients>

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
* <done: consider, Thonny, Tools, Manage packages, Manage packages for Raspberry Pi Pico @ COMS, create a package for BME280 driver, Install from local file Click here to locate and install the package file (usually with .whl, .tar.gz or .zip extension). Under the hood This dialog uses `pipkin`, a new command line tool for managing MicroPython and CircuitPython packages. See https://pypi.org/project/pipkin/ for more info. Note! this Tools menu item is only available after Stop/Restart (RPi Pico) backend, done for /snr-tsd project for import of bme280 driver into this project, how to do so steps in /hwd project,issues remain with use of snr_bme280_drv after import for use with this project in Thonny >

## Readings

### Rotating Potentiometer, voltage divider, 0V to 3.3V
Potential sample test data to log, in datalogger

```
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
```

### RPi Pico internal core temperature - no heat added to CPU
Potential sample test data to log, in datalogger

```
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
```

### RPi Pico internal core temperature - heat added to CPU, tip of finger placed on top of CPU
Potential sample test data to log, in datalogger

```
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
```

### RPi Pico recognises SD Card


```
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot

sd_card_spi: SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, sck=10, mosi=11, miso=12)
micro sd card: <SDCard object at 20010940>
os mount point: None>>> %Run -c $EDITOR_CONTENT
```

### Rpi Pico file io to SD Card
<todo: consider adding more verbose explanitory output, >

```
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
sd_card_spi: SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, sck=10, mosi=11, miso=12)
micro sd card: <SDCard object at 20010c20>
sys vol info: ['System Volume Information']
file access, exception: [Errno 2] ENOENT
file exists: False
file: new created, <io.TextIOWrapper 20011800>
file size: 0 unicode chars
file content: first line
second line

file content: first line
second line
third line

file content: 1st line
2nd line
3rd line

file exists: True
file size: 27 unicode chars
file access, exception: [Errno 2] ENOENT
file exists: False
file deleted os.remove: True
sys vol info: ['System Volume Information']
```

### Rpi Pico CPU internal temperature reading to file io to SD Card

```
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
sd_card_spi: SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, sck=10, mosi=11, miso=12)
micro sd card: <SDCard object at 20010cd0>
sys vol info: ['System Volume Information', 'pico-cpu-temp-log.txt']
file exists: True
temperature: 29.85327, at date & time: (2025, 6, 30, 0, 10, 10, 34, 0)

file exists: True
file size: 818 unicode chars
file content: 30.32141, (2025, 6, 27, 4, 17, 43, 21, 0), 
29.85327, (2025, 6, 27, 4, 17, 47, 46, 0), 
30.32141, (2025, 6, 27, 4, 17, 48, 1, 0), 
26.10811, (2025, 6, 30, 0, 9, 10, 14, 0), 
27.51254, (2025, 6, 30, 0, 9, 19, 39, 0), 
28.91698, (2025, 6, 30, 0, 9, 25, 33, 0), 
30.32141, (2025, 6, 30, 0, 9, 25, 48, 0), 
29.38512, (2025, 6, 30, 0, 9, 26, 3, 0), 
30.32141, (2025, 6, 30, 0, 9, 26, 18, 0), 
29.85327, (2025, 6, 30, 0, 9, 26, 33, 0), 
30.32141, (2025, 6, 30, 0, 9, 26, 48, 0), 
29.85327, (2025, 6, 30, 0, 9, 27, 3, 0), 
29.85327, (2025, 6, 30, 0, 9, 27, 18, 0), 
29.85327, (2025, 6, 30, 0, 9, 27, 21, 0), 
29.85327, (2025, 6, 30, 0, 9, 27, 36, 0), 
27.98069, (2025, 6, 30, 0, 9, 53, 55, 0), 
30.78955, (2025, 6, 30, 0, 9, 55, 17, 0), 
28.44883, (2025, 6, 30, 0, 10, 4, 57, 0), 
29.85327, (2025, 6, 30, 0, 10, 10, 34, 0), 

Logging interupt; keyboard
>>> 
```

### BME280 temperature humdity air pressure reading to file io to SD Card
Exits with success with package imported to Thonny IDE, 
* <info: see also build output in .../Snr-tsd, >
* <info: with package build with build-system section in pyproject.toml , >
* <info: with package build-system with PDM, >
* <info: circuit simplified, removal of rotating potentiometer, voltage divider, >
* <info: circuit simplified, removal of flat jumper wire bare ends, to jumper wire cable pin ends,  >
* <info: circuit defect fix, one of the errors was a wiring issue, scl and sda wires from sensor were set to wrong GPIO pins>
* <info: end run, 'stop/restart backend' >

```
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
sd_card_spi: SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, sck=10, mosi=11, miso=12)
micro sd card: <SDCard object at 20012b80>
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
sys vol info: ['System Volume Information', 'pico-cpu-temp-log.txt', 'bme280-thp-log.txt']
i2c.scan() address list: [119]
bme initialised: <BME280 object at 20013e30>
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
bme.temperature(): 25.92C
bme.humidity(): 40.-4146847%
bme.humidity(): 1006.12hPa
Temperature:  25.92C
Temperature:  78.62F
Humidity:  40.-4146847%
Pressure:  1006.12hPa
temperature C: 25.92C, temperature F: 78.62F, humidity: 40.-4146847%, pressure: 1006.12hPa, at date & time: (2025, 7, 11, 4, 10, 20, 48, 0)
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
bme.temperature(): 25.82C
bme.humidity(): 40.-4133360%
bme.humidity(): 1006.20hPa
Temperature:  25.82C
Temperature:  78.49F
Humidity:  40.-4133360%
Pressure:  1006.20hPa
temperature C: 25.82C, temperature F: 78.49F, humidity: 40.-4133360%, pressure: 1006.20hPa, at date & time: (2025, 7, 11, 4, 10, 21, 48, 0)
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
bme.temperature(): 25.77C
bme.humidity(): 40.-4123670%
bme.humidity(): 1006.33hPa
Temperature:  25.77C
Temperature:  78.39F
Humidity:  40.-4123670%
Pressure:  1006.33hPa
temperature C: 25.77C, temperature F: 78.39F, humidity: 40.-4123670%, pressure: 1006.33hPa, at date & time: (2025, 7, 11, 4, 10, 22, 48, 0)
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
bme.temperature(): 25.72C
bme.humidity(): 40.-4120872%
bme.humidity(): 1006.39hPa
Temperature:  25.72C
Temperature:  78.3F
Humidity:  40.-4120872%
Pressure:  1006.39hPa
temperature C: 25.72C, temperature F: 78.3F, humidity: 40.-4120872%, pressure: 1006.39hPa, at date & time: (2025, 7, 11, 4, 10, 23, 48, 0)
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
bme.temperature(): 25.65C
bme.humidity(): 40.-4119174%
bme.humidity(): 1006.52hPa
Temperature:  25.65C
Temperature:  78.17F
Humidity:  40.-4119174%
Pressure:  1006.52hPa
temperature C: 25.65C, temperature F: 78.17F, humidity: 40.-4119174%, pressure: 1006.52hPa, at date & time: (2025, 7, 11, 4, 10, 24, 48, 0)

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
file exists: True
file size: 379 unicode chars
file content: 25.92C, 78.62F, 40.-4146847%, 1006.12hPa, (2025, 7, 11, 4, 10, 20, 48, 0), 
25.82C, 78.49F, 40.-4133360%, 1006.20hPa, (2025, 7, 11, 4, 10, 21, 48, 0), 
25.77C, 78.39F, 40.-4123670%, 1006.33hPa, (2025, 7, 11, 4, 10, 22, 48, 0), 
25.72C, 78.3F, 40.-4120872%, 1006.39hPa, (2025, 7, 11, 4, 10, 23, 48, 0), 
25.65C, 78.17F, 40.-4119174%, 1006.52hPa, (2025, 7, 11, 4, 10, 24, 48, 0), 

Logging interupt; keyboard

MPY: soft reboot
MicroPython v1.25.0 on 2025-04-15; Raspberry Pi Pico 2 W with RP2350

Type "help()" for more information.

>>> 
```

Exits with error with package imported to Thonny IDE, Subsequent to first successful run.
* <info: start run, after 'stop/restart backend', likely correlation >
* <info: possibly a lose wire issue,  likely causation, >
* <info: end run, 'stop/restart backend' >

```
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
sd_card_spi: SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, sck=10, mosi=11, miso=12)
micro sd card: <SDCard object at 20012b80>
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
sys vol info: ['System Volume Information', 'pico-cpu-temp-log.txt', 'bme280-thp-log.txt']
i2c.scan() address list: []
sensor creation, exception: [Errno 110] ETIMEDOUT
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
file io, exception: 'NoneType' object has no attribute 'temperature'

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
file exists: True
file size: 379 unicode chars
file content: 25.92C, 78.62F, 40.-4146847%, 1006.12hPa, (2025, 7, 11, 4, 10, 20, 48, 0), 
25.82C, 78.49F, 40.-4133360%, 1006.20hPa, (2025, 7, 11, 4, 10, 21, 48, 0), 
25.77C, 78.39F, 40.-4123670%, 1006.33hPa, (2025, 7, 11, 4, 10, 22, 48, 0), 
25.72C, 78.3F, 40.-4120872%, 1006.39hPa, (2025, 7, 11, 4, 10, 23, 48, 0), 
25.65C, 78.17F, 40.-4119174%, 1006.52hPa, (2025, 7, 11, 4, 10, 24, 48, 0), 

Logging interupt; keyboard

MPY: soft reboot
MicroPython v1.25.0 on 2025-04-15; Raspberry Pi Pico 2 W with RP2350

Type "help()" for more information.

>>> 
```

Exits with success with package imported to Thonny IDE, 
* <info: wire check, to ensure all were securly connected, likely causation, >
* <info: the sd card was ejected and then reinserted into the sc card reader, tlikely corrolation, >
* <info: start run, after 'stop/restart backend', >
* <info: end run, 'stop/restart backend' >

```
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
sd_card_spi: SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, sck=10, mosi=11, miso=12)
micro sd card: <SDCard object at 20012b80>
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
sys vol info: ['System Volume Information', 'pico-cpu-temp-log.txt', 'bme280-thp-log.txt']
i2c.scan() address list: [119]
bme initialised: <BME280 object at 20013e30>
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
bme.temperature(): 26.88C
bme.humidity(): 38.-3930159%
bme.humidity(): 1004.02hPa
Temperature:  26.88C
Temperature:  80.33F
Humidity:  38.-3930159%
Pressure:  1004.02hPa
temperature C: 26.88C, temperature F: 80.33F, humidity: 38.-3930159%, pressure: 1004.02hPa, at date & time: (2025, 7, 11, 4, 11, 32, 10, 0)
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
bme.temperature(): 26.79C
bme.humidity(): 38.-3946543%
bme.humidity(): 1004.24hPa
Temperature:  26.79C
Temperature:  80.22F
Humidity:  38.-3946543%
Pressure:  1004.24hPa
temperature C: 26.79C, temperature F: 80.22F, humidity: 38.-3946543%, pressure: 1004.24hPa, at date & time: (2025, 7, 11, 4, 11, 33, 11, 0)
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
bme.temperature(): 26.73C
bme.humidity(): 38.-3927661%
bme.humidity(): 1004.35hPa
Temperature:  26.73C
Temperature:  80.11F
Humidity:  38.-3927661%
Pressure:  1004.35hPa
temperature C: 26.73C, temperature F: 80.11F, humidity: 38.-3927661%, pressure: 1004.35hPa, at date & time: (2025, 7, 11, 4, 11, 34, 11, 0)
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
bme.temperature(): 26.66C
bme.humidity(): 38.-3912176%
bme.humidity(): 1004.43hPa
Temperature:  26.66C
Temperature:  79.99F
Humidity:  38.-3912176%
Pressure:  1004.43hPa
temperature C: 26.66C, temperature F: 79.99F, humidity: 38.-3912176%, pressure: 1004.43hPa, at date & time: (2025, 7, 11, 4, 11, 35, 11, 0)
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
bme.temperature(): 26.60C
bme.humidity(): 38.-3904684%
bme.humidity(): 1004.51hPa
Temperature:  26.60C
Temperature:  79.88F
Humidity:  38.-3904684%
Pressure:  1004.51hPa
temperature C: 26.60C, temperature F: 79.88F, humidity: 38.-3904684%, pressure: 1004.51hPa, at date & time: (2025, 7, 11, 4, 11, 36, 11, 0)

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
file exists: True
file size: 759 unicode chars
file content: 25.92C, 78.62F, 40.-4146847%, 1006.12hPa, (2025, 7, 11, 4, 10, 20, 48, 0), 
25.82C, 78.49F, 40.-4133360%, 1006.20hPa, (2025, 7, 11, 4, 10, 21, 48, 0), 
25.77C, 78.39F, 40.-4123670%, 1006.33hPa, (2025, 7, 11, 4, 10, 22, 48, 0), 
25.72C, 78.3F, 40.-4120872%, 1006.39hPa, (2025, 7, 11, 4, 10, 23, 48, 0), 
25.65C, 78.17F, 40.-4119174%, 1006.52hPa, (2025, 7, 11, 4, 10, 24, 48, 0), 
26.88C, 80.33F, 38.-3930159%, 1004.02hPa, (2025, 7, 11, 4, 11, 32, 10, 0), 
26.79C, 80.22F, 38.-3946543%, 1004.24hPa, (2025, 7, 11, 4, 11, 33, 11, 0), 
26.73C, 80.11F, 38.-3927661%, 1004.35hPa, (2025, 7, 11, 4, 11, 34, 11, 0), 
26.66C, 79.99F, 38.-3912176%, 1004.43hPa, (2025, 7, 11, 4, 11, 35, 11, 0), 
26.60C, 79.88F, 38.-3904684%, 1004.51hPa, (2025, 7, 11, 4, 11, 36, 11, 0), 

Logging interupt; keyboard

MPY: soft reboot
MicroPython v1.25.0 on 2025-04-15; Raspberry Pi Pico 2 W with RP2350

Type "help()" for more information.

>>> 
```

Exits with success with package imported to Thonny IDE, 
* <info: start run, after 'stop/restart backend' >
* <info: end run, 'interupt execution Ctrl C' >

```
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
sd_card_spi: SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, sck=10, mosi=11, miso=12)
micro sd card: <SDCard object at 20012b80>
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
sys vol info: ['System Volume Information', 'pico-cpu-temp-log.txt', 'bme280-thp-log.txt']
i2c.scan() address list: [119]
bme initialised: <BME280 object at 20013c70>
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
bme.temperature(): 26.46C
bme.humidity(): 38.-3906981%
bme.humidity(): 1004.78hPa
Temperature:  26.46C
Temperature:  79.59F
Humidity:  38.-3906981%
Pressure:  1004.78hPa
temperature C: 26.46C, temperature F: 79.59F, humidity: 38.-3906981%, pressure: 1004.78hPa, at date & time: (2025, 7, 11, 4, 11, 39, 35, 0)
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
bme.temperature(): 26.39C
bme.humidity(): 38.-3910878%
bme.humidity(): 1004.89hPa
Temperature:  26.39C
Temperature:  79.48F
Humidity:  38.-3910878%
Pressure:  1004.89hPa
temperature C: 26.39C, temperature F: 79.48F, humidity: 38.-3910878%, pressure: 1004.89hPa, at date & time: (2025, 7, 11, 4, 11, 40, 35, 0)
file exists: True
file size: 911 unicode chars
file content: 25.92C, 78.62F, 40.-4146847%, 1006.12hPa, (2025, 7, 11, 4, 10, 20, 48, 0), 
25.82C, 78.49F, 40.-4133360%, 1006.20hPa, (2025, 7, 11, 4, 10, 21, 48, 0), 
25.77C, 78.39F, 40.-4123670%, 1006.33hPa, (2025, 7, 11, 4, 10, 22, 48, 0), 
25.72C, 78.3F, 40.-4120872%, 1006.39hPa, (2025, 7, 11, 4, 10, 23, 48, 0), 
25.65C, 78.17F, 40.-4119174%, 1006.52hPa, (2025, 7, 11, 4, 10, 24, 48, 0), 
26.88C, 80.33F, 38.-3930159%, 1004.02hPa, (2025, 7, 11, 4, 11, 32, 10, 0), 
26.79C, 80.22F, 38.-3946543%, 1004.24hPa, (2025, 7, 11, 4, 11, 33, 11, 0), 
26.73C, 80.11F, 38.-3927661%, 1004.35hPa, (2025, 7, 11, 4, 11, 34, 11, 0), 
26.66C, 79.99F, 38.-3912176%, 1004.43hPa, (2025, 7, 11, 4, 11, 35, 11, 0), 
26.60C, 79.88F, 38.-3904684%, 1004.51hPa, (2025, 7, 11, 4, 11, 36, 11, 0), 
26.46C, 79.59F, 38.-3906981%, 1004.78hPa, (2025, 7, 11, 4, 11, 39, 35, 0), 
26.39C, 79.48F, 38.-3910878%, 1004.89hPa, (2025, 7, 11, 4, 11, 40, 35, 0), 

Logging interupt; keyboard
>>> 
```

Exits with success with package imported to Thonny IDE, 
* <info: start run, after 'interupt execution Ctrl C' >
* <info: end run, 'stop/restart backend' >

```
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
sd_card_spi: SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, sck=10, mosi=11, miso=12)
micro sd card: <SDCard object at 20012b80>
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
sys vol info: ['System Volume Information', 'pico-cpu-temp-log.txt', 'bme280-thp-log.txt']
i2c.scan() address list: [119]
bme initialised: <BME280 object at 20013c70>
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
bme.temperature(): 26.30C
bme.humidity(): 38.-3925064%
bme.humidity(): 1005.00hPa
Temperature:  26.30C
Temperature:  79.3F
Humidity:  38.-3925064%
Pressure:  1005.00hPa
temperature C: 26.30C, temperature F: 79.3F, humidity: 38.-3925064%, pressure: 1005.00hPa, at date & time: (2025, 7, 11, 4, 11, 44, 9, 0)

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
file exists: True
file size: 1060 unicode chars
file content: 25.92C, 78.62F, 40.-4146847%, 1006.12hPa, (2025, 7, 11, 4, 10, 20, 48, 0), 
25.82C, 78.49F, 40.-4133360%, 1006.20hPa, (2025, 7, 11, 4, 10, 21, 48, 0), 
25.77C, 78.39F, 40.-4123670%, 1006.33hPa, (2025, 7, 11, 4, 10, 22, 48, 0), 
25.72C, 78.3F, 40.-4120872%, 1006.39hPa, (2025, 7, 11, 4, 10, 23, 48, 0), 
25.65C, 78.17F, 40.-4119174%, 1006.52hPa, (2025, 7, 11, 4, 10, 24, 48, 0), 
26.88C, 80.33F, 38.-3930159%, 1004.02hPa, (2025, 7, 11, 4, 11, 32, 10, 0), 
26.79C, 80.22F, 38.-3946543%, 1004.24hPa, (2025, 7, 11, 4, 11, 33, 11, 0), 
26.73C, 80.11F, 38.-3927661%, 1004.35hPa, (2025, 7, 11, 4, 11, 34, 11, 0), 
26.66C, 79.99F, 38.-3912176%, 1004.43hPa, (2025, 7, 11, 4, 11, 35, 11, 0), 
26.60C, 79.88F, 38.-3904684%, 1004.51hPa, (2025, 7, 11, 4, 11, 36, 11, 0), 
26.46C, 79.59F, 38.-3906981%, 1004.78hPa, (2025, 7, 11, 4, 11, 39, 35, 0), 
26.39C, 79.48F, 38.-3910878%, 1004.89hPa, (2025, 7, 11, 4, 11, 40, 35, 0), 
26.29C, 79.3F, 38.-3923865%, 1005.00hPa, (2025, 7, 11, 4, 11, 43, 58, 0), 
26.30C, 79.3F, 38.-3925064%, 1005.00hPa, (2025, 7, 11, 4, 11, 44, 9, 0), 

Logging interupt; keyboard

MPY: soft reboot
MicroPython v1.25.0 on 2025-04-15; Raspberry Pi Pico 2 W with RP2350

Type "help()" for more information.

>>>
```

### BME280 temperature humdity air pressure reading to file io to SD Card and to LCD screen
Successful run in QA1 env. sensor readings, the same in log file see end of output below, and LCD screen display images not included. Logging and dispaly of sensor readings interupt execution with Ctrl C.
* <todo: reconfirms requirement to troubleshoot BME280 sensor humidity readings, is BME280 properly calibrated, damaged, driver defective? >

```
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
display_i2c: I2C(0, freq=400000, scl=9, sda=8, timeout=50000)
display_i2c.scan() address list: [62, 96, 112]
sd_card_spi: SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, sck=10, mosi=11, miso=12)
micro sd card: <SDCard object at 20013e50>
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
sys vol info: ['System Volume Information', 'pico-cpu-temp-log.txt', 'bme280-thp-log.txt']
i2c.scan() address list: [119]
bme initialised: <BME280 object at 200170a0>
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
Temperature:  23.56C
Temperature:  74.37F
Humidity:  49.-5023890%
Pressure:  1007.15hPa
temperature C: 23.56C, temperature F: 74.37F, humidity: 49.-5023890%, pressure: 1007.15hPa, at date & time: (2025, 7, 25, 4, 15, 57, 53, 0)
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
Temperature:  23.56C
Temperature:  74.41F
Humidity:  49.-5013700%
Pressure:  1007.12hPa
temperature C: 23.56C, temperature F: 74.41F, humidity: 49.-5013700%, pressure: 1007.12hPa, at date & time: (2025, 7, 25, 4, 15, 58, 53, 0)
file exists: True
sensor_i2c: I2C(1, freq=1000, scl=19, sda=18, timeout=50000)
Temperature:  23.60C
Temperature:  74.46F
Humidity:  48.-4998115%
Pressure:  1007.04hPa
temperature C: 23.60C, temperature F: 74.46F, humidity: 48.-4998115%, pressure: 1007.04hPa, at date & time: (2025, 7, 25, 4, 15, 59, 53, 0)
file exists: True
file size: 1288 unicode chars
file content: 25.92C, 78.62F, 40.-4146847%, 1006.12hPa, (2025, 7, 11, 4, 10, 20, 48, 0), 
25.82C, 78.49F, 40.-4133360%, 1006.20hPa, (2025, 7, 11, 4, 10, 21, 48, 0), 
25.77C, 78.39F, 40.-4123670%, 1006.33hPa, (2025, 7, 11, 4, 10, 22, 48, 0), 
25.72C, 78.3F, 40.-4120872%, 1006.39hPa, (2025, 7, 11, 4, 10, 23, 48, 0), 
25.65C, 78.17F, 40.-4119174%, 1006.52hPa, (2025, 7, 11, 4, 10, 24, 48, 0), 
26.88C, 80.33F, 38.-3930159%, 1004.02hPa, (2025, 7, 11, 4, 11, 32, 10, 0), 
26.79C, 80.22F, 38.-3946543%, 1004.24hPa, (2025, 7, 11, 4, 11, 33, 11, 0), 
26.73C, 80.11F, 38.-3927661%, 1004.35hPa, (2025, 7, 11, 4, 11, 34, 11, 0), 
26.66C, 79.99F, 38.-3912176%, 1004.43hPa, (2025, 7, 11, 4, 11, 35, 11, 0), 
26.60C, 79.88F, 38.-3904684%, 1004.51hPa, (2025, 7, 11, 4, 11, 36, 11, 0), 
26.46C, 79.59F, 38.-3906981%, 1004.78hPa, (2025, 7, 11, 4, 11, 39, 35, 0), 
26.39C, 79.48F, 38.-3910878%, 1004.89hPa, (2025, 7, 11, 4, 11, 40, 35, 0), 
26.29C, 79.3F, 38.-3923865%, 1005.00hPa, (2025, 7, 11, 4, 11, 43, 58, 0), 
26.30C, 79.3F, 38.-3925064%, 1005.00hPa, (2025, 7, 11, 4, 11, 44, 9, 0), 
23.56C, 74.37F, 49.-5023890%, 1007.15hPa, (2025, 7, 25, 4, 15, 57, 53, 0), 
23.56C, 74.41F, 49.-5013700%, 1007.12hPa, (2025, 7, 25, 4, 15, 58, 53, 0), 
23.60C, 74.46F, 48.-4998115%, 1007.04hPa, (2025, 7, 25, 4, 15, 59, 53, 0), 

Logging interupt; keyboard
>>> 
```

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
* SD, [GH](https://github.com/micropython/micropython-lib/tree/master/micropython/drivers/storage/sdcard), MicroPython, sdcard.py - evaluating this driver, 2025/06/25
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

mS Windows FAT formatting
* <todo: sources> This is the option used for the micro SD Card in this project

Raspberry Pi Imager ? 
* <todo: consider, investigate further, only for RPi SBC not microbontrollers? Rasbian dependency? >

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

News Papers - os, path, file, micropython
* How to Check if a File Exists in Python with isFile() and exists(), [WS](https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/), January 5, 2023, Dionysia Lemonaki
* Implementing 'os.path.isfile()', [WS](https://forums.raspberrypi.com/viewtopic.php?t=321965), Raspberry Pi Forum, 

News Papers - sdc format FAT32
* Difference between quick format and slow format?, [WS](https://www.reddit.com/r/DataHoarder/comments/y58k35/difference_between_quick_format_and_slow_format/), Reddit, 
* The SD Association has an official SD card formatter (sdcard .org), [WS](https://news.ycombinator.com/item?id=41445898), Hacker News, 
* What is the standard file system that a SD card have to use before write Raspbian using dd command?, [WS](https://raspberrypi.stackexchange.com/questions/17110/what-is-the-standard-file-system-that-a-sd-card-have-to-use-before-write-raspbia), StackExchange, Raspberry Pi
* What format should my SD card be? [duplicate], [WS](https://raspberrypi.stackexchange.com/questions/23281/what-format-should-my-sd-card-be), StackExchange, Raspberry Pi
* Format SD Card from Console, [WS](https://forums.raspberrypi.com/viewtopic.php?t=329474), Raspberry Pi Forum, 
* fat32 sd card, [WS](https://forums.raspberrypi.com/viewtopic.php?t=261901), Raspberry Pi Forum, 
* Which Allocation Unit Size do I have to choose for my SDHC card?, [WS](https://superuser.com/questions/455098/which-allocation-unit-size-do-i-have-to-choose-for-my-sdhc-card), StackExchange, SuperUser
* Block size & lots of small files, [WS](https://forums.raspberrypi.com/viewtopic.php?t=133349), Raspberry Pi Forum, 

News Papers - sd card drivers, read/write, blockwrite, sdcard.py 
* drivers: sdcard.py should support multiple block read/write #1801, [WS](https://github.com/micropython/micropython/issues/1801)

News Papers - machine.Timer, python, micropython
* callback from a timer ?, [WS](https://forums.raspberrypi.com/viewtopic.php?t=363587), Raspberry Pi Forums, 

News Papers - error codes
* my raspberry pi pico oled display code is returning 'OSError: [Errno 5] EIO', [WS](https://raspberrypi.stackexchange.com/questions/140130/my-raspberry-pi-pico-oled-display-code-is-returning-oserror-errno-5-eio), StackExchange, Raspberry Pi,  
* I2C, OSError: [Errno 5] EIO, [WS](https://forums.raspberrypi.com/viewtopic.php?t=318848&sid=fa43e17e60a704520b003d3947ed6da7), Raspberry Pi Forums, 
* OSError: [Errno 5] EIO when accessing sensor data #9201, [GH](https://github.com/orgs/micropython/discussions/9201), MicroPython, GitHub







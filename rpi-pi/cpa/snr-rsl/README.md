# Aerosol sensor rsl (cpa)

See also Aerosol sensor rsl (mpy) [GH](https://github.com/YorkEarwaker/Electrical-Engineering/tree/main/rpi-pi/mpy/snr-rsl), first cut research, start of bare bones MicroPython driver, 

## Status
TODO
* <todo: consider, /doc BMV080 specific information, BMV080 Sparkfun breakout board information>
* <todo: consider, VSCodium and VSCode with Pico extension for build for Pico of Bosch BMV080 SDK, >
* <todo: consider, does the Sunspark breakout board BMV080 SDK have any dependencies on the Bosch BMV080 SDK, >
* <todo: consider, VSCodium and VSCode with Pico extension for build for Pico of Sunspark breakout board BMV080 SDK, modification of hello project, >
* <todo: consider, what is the bare minimum that must run on Pico MCU and what could be run from another host like an SCB, >
* <todo: consider, build for MS Windows 10, how to connect to laptop? Qwiik to USB? >
* <todo: consider, VS Code with Arduino CLI, two seperate installs?,  map Arduino CLI path to VS Code C/CMakelist project? is Arduino IDE extension depricated?  >
* <todo: consider, read Sunspark documentation for GitHub project code, for code BMV080 sensor and code generic SPI I2C connection, >
* <todo: consider, read Sunspark BMV080 code and connection code Arduino microcontroller specific?, If so how simple/complex to modify for RPi Pi 2350 W, >

DONE
* <done: intent to commit>
* <done: consider, BMV080 sensor ASCI diagram simplified top view, ZIF, Flex PCB, Passives, lens & lasor, >

## Libs

Bosch
* BMV080 SDK download, [WS](https://www.bosch-sensortec.com/software-tools/double-opt-in-forms/sdk-v11-2.html) 
* Supported platforms, [PDF](https://www.bosch-sensortec.com/media/boschsensortec/software_tools/software/bmv080_1/supported_platforms/bmv080_binary_size_information.pdf)

Sparkfun
* SparkFun Toolkit Arduino Library, [GH](https://github.com/sparkfun/SparkFun_Toolkit/tree/main), Toolkit of common functionality for use within SparkFun Libraries 
* SparkFun Air Quality PM1/PM2.5/PM10 Sensor - BMV080 (Qwiic) [GH](https://github.com/sparkfun/SparkFun_BMV080_Arduino_Library/tree/main), Arduino Library to support the Bosch BMV080 Particulate Matter Air Quality Sensor PM2.5 via I2C and SPI. 

IDE
* Arduino IDE, Sparkfun code, 
* VS Code with Arduino CLI, 

Build
* Make, Bosche code, Raspbery Pi
* PlatformIO, Bosch code, everything else not Raspberry Pi, 

Language 
* C standard library clib, [WP](https://en.wikipedia.org/wiki/C_standard_library)
* C reference, [WS](https://en.cppreference.com/w/c.html)

## References

Sparkfun BMV080 particulate matter sensor breakout board
* Schematic [PDF](https://docs.sparkfun.com/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080/assets/board_files/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080_v10_Schematic.pdf)
* ..


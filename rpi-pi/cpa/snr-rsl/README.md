# Aerosol sensor rsl (cpa)

See also Aerosol sensor rsl (mpy) [GH](https://github.com/YorkEarwaker/Electrical-Engineering/tree/main/rpi-pi/mpy/snr-rsl), first cut research, start of bare bones MicroPython driver, 

## Status
TODO
* <todo: consider, /doc BMV080 specific information, BMV080 Sparkfun breakout board information>
* <todo: consider, VSCodium and VSCode with Pico extension for build for Pico of Bosch BMV080 SDK, modification of hello world project?, >
* <todo: consider, VSCodium and VSCode with Pico extension for build for Pico of Sunspark breakout board BMV080 SDK, modification of hello world project?, >
* <todo: consider, what is the bare minimum that must run on Pico MCU and what could be run from another host like an SCB, >
* <todo: consider, build for MS Windows 10, how to connect to laptop? Qwiik to USB? >
* <todo: consider, VS Code with Arduino CLI, two seperate installs?,  map Arduino CLI path to VS Code C/CMakelist project? is Arduino IDE extension depricated?  >
* <todo: consider, read Sunspark documentation for GitHub project code, for code BMV080 sensor and code generic SPI I2C connection, >

DONE
* <done: intent to commit>
* <done: consider, BMV080 sensor ASCI diagram simplified top view, ZIF, Flex PCB, Passives, lens & lasor, >
* <done: consider, does the Sunspark breakout board BMV080 SDK have any dependencies on the Bosch BMV080 SDK, Yes it does!, requires download of MBV080 SDK and copy of some files to 'SparkFun Air Quality PM1/PM2.5/PM10 Sensor - BMV080 (Qwiic)' code base, >
* <done: consider, support for RP2350 for RPi Pico? Yes! the Bosch SDK v11.2.0 on July 12th, 2025 added support for the RP2350 processor (m33), >
* <done: consider, read Sunspark BMV080 code and connection code Arduino microcontroller specific?, If so how simple/complex to modify for RPi Pi 2350 W, . Yes need for refactoring, Sunspark RP2350 code is tailored to Sunspark RP2350 boards, there is a RP2350 example  for 'SparkFun IoT RedBoard - RP2350' on 'SparkFun Air Quality PM1/PM2.5/PM10 Sensor - BMV080 (Qwiic)' >

## Libs

Bosch
* BMV080 SDK download, [WS](https://www.bosch-sensortec.com/software-tools/double-opt-in-forms/sdk-v11-2.html) 
* Supported platforms, [PDF](https://www.bosch-sensortec.com/media/boschsensortec/software_tools/software/bmv080_1/supported_platforms/bmv080_binary_size_information.pdf)

Raspberry Pi
* Raspberry Pi Pico-series C/C++ SDK Libraries and tools for C/C++ development on Raspberry Pi microcontrollers. [PDF](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf), RPi Pico 2, C/C++ sdk-v11-2 , 2 0 2 5 - 0 7 - 3 0 : 3 0 0 3 1 8 4 - c l e a

Sparkfun
* SparkFun Toolkit Arduino Library, [GH](https://github.com/sparkfun/SparkFun_Toolkit/tree/main), Toolkit of common functionality for use within SparkFun Libraries 
* SparkFun Air Quality PM1/PM2.5/PM10 Sensor - BMV080 (Qwiic), [GH](https://github.com/sparkfun/SparkFun_BMV080_Arduino_Library/tree/main), Arduino Library to support the Bosch BMV080 Particulate Matter Air Quality Sensor PM2.5 via I2C and SPI. 

IDE
* Arduino IDE, Sparkfun code, with SparkFun_BMV_Arduino_Library v1.0.1 Bosch BMV080 SDK v11.2.0 Arduino IDE 2.3.5
* VS Code with Arduino CLI, 

Build
* Make, Bosche code, Raspbery Pi
* PlatformIO, Bosch code, everything else not Raspberry Pi, 

Language 
* C standard library clib, [WP](https://en.wikipedia.org/wiki/C_standard_library)
* C reference, [WS](https://en.cppreference.com/w/c.html)

## Hardware

MCU - microcontroller, RP2350
* Raspberry Pi Pico 2, [WS](https://www.raspberrypi.com/products/raspberry-pi-pico-2/), preferred option, RISC‑V architecture, dual core, dual architecture, a pair of Arm Cortex-M33 cores, and a pair of open-hardware Hazard3 cores 
* SparkFun IoT RedBoard - RP2350, [WS](https://www.sparkfun.com/sparkfun-iot-redboard-rp2350.html), Arduino R4 format (aka form factor?), 

## References

Sparkfun BMV080 particulate matter sensor breakout board
* Schematic [PDF](https://docs.sparkfun.com/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080/assets/board_files/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080_v10_Schematic.pdf)
* ..


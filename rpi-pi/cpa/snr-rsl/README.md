# Aerosol sensor rsl (cpa)

See also Aerosol sensor rsl (mpy) [GH](https://github.com/YorkEarwaker/Electrical-Engineering/tree/main/rpi-pi/mpy/snr-rsl), first cut research, start of bare bones MicroPython driver, 

## Notes

Bosch Sensortec Community BSC
* Posted on Bosch Sensortec Community regarding full integration of BMV080 with RPi universe. [WS](https://community.bosch-sensortec.com/mems-sensors-forum-jrmujtaw/post/bmv080---raspberry-pi-what-are-the-issues-that-prevent-full-integration-dHQvd8Fa2dvcmKb)

Raspberry Pi Forum
* <todo: await response from BSC before posting on RPi Forum re same. >

## Status
TODO
* <todo: consider, VSCodium and VSCode with Pico extension for build for Pico of Bosch BMV080 SDK, modification of hello world project?, >
* <todo: consider, VSCodium and VSCode with Pico extension for build for Pico of Sunspark breakout board BMV080 SDK, modification of hello world project?, >
* <todo: consider, what is the bare minimum that must run on Pico MCU and what could be run from another host like an SCB, >
* <todo: consider, VS Code with Arduino CLI, two seperate installs?,  map Arduino CLI path to VS Code C/CMakelist project? is Arduino IDE extension depricated?  >
* <todo: consider, read Sunspark documentation for GitHub project code, for code BMV080 sensor and code generic SPI I2C connection, >
* <todo: consider, - ```api_examples\raspberry_pi\*```	Example application project for Raspberry Pi platform as a CMake project. Bosch SDK README.md>
* <todo: consider, - ```api_examples\x86_x64\*```	Example application for x86 / x64 platform with Windows OS as a CMake project. Bosch SDK README.md>
* <todo: consider, sepearation of concern, purchase RPi Zero for BMV080 PoC not RPi V, for RPi Zero Bosch informs there is a compile and deployment option, Bosch SDK README.md>
* <todo: consider, raise question on Bosch Sensortec Community forum about any known limiting RPi integration concerns with Bosch Gas sensors, go ahead and purchase one in anycase while waiting for answers about BMV080 RPi compatibility? >

DONE
* <done: intent to commit>
* <done: consider, BMV080 sensor ASCI diagram simplified top view, ZIF, Flex PCB, Passives, lens & lasor, >
* <done: consider, does the Sunspark breakout board BMV080 SDK have any dependencies on the Bosch BMV080 SDK, Yes it does!, requires download of MBV080 SDK and copy of some files to 'SparkFun Air Quality PM1/PM2.5/PM10 Sensor - BMV080 (Qwiic)' code base, >
* <done: consider, support for RP2350 for RPi Pico? Unclear! the Bosch SDK v11.2.0 on July 12th, 2025 added support for the RP2350 processor (m33), But the BMV080 SDK README.md state no Pico compile option, and references Cortex-M33F not M33 so does that mean SDK requries hareware floating point support in the cores? >
* <done: consider, read Sunspark BMV080 code and connection code Arduino microcontroller specific?, If so how simple/complex to modify for RPi Pi 2350 W, . Yes need for refactoring, Sunspark RP2350 code is tailored to Sunspark RP2350 boards, there is a RP2350 example  for 'SparkFun IoT RedBoard - RP2350' on 'SparkFun Air Quality PM1/PM2.5/PM10 Sensor - BMV080 (Qwiic)' >
* <done: consider, formulate question re Bosch BMV080 concerns with RPi universe, e.g. limitations of ARM Cortex M33, for Bosch Sensortec Community, re compile and deployment to RPi Pico 2 W, see Notes above,  >
* <done: consider, /doc BMV080 specific information, BMV080 Sparkfun breakout board information, not at this time, >
* <done: consider, build for MS Windows 10, how to connect to Sparkfun BMV080 breakout to laptop? Qwiic to USB via breadboard? not acomplished but spawned another project PCEE /pcee under electrical engineering repsitory >
* <done: consider, - ```api\lib\arm_cortex_m33f\arm_none_eabi_gcc\release\*``` Library files of BMV080 sensor driver for ARM Cortex-M33F architecture with full hardware floating-point support, using the ARM GCC compiler Bosch SDK README.md, resolved? no point? Pico on Cortex-M33 not Cortex-M33F, 3.2.3 Using External Interrupt vs Polling>
* <done: consider, - ```api_examples\arm_cortex_m33f\*```	Example application project for ARM Cortex-M33F platform as a PlatformIO project. Bosch SDK README.md, resolved?  no point? Pico on Cortex-M33 not Cortex-M33F, 3.2.3 Using External Interrupt vs Polling>

## Libs

Bosch
* BMV080 SDK download, [WS](https://www.bosch-sensortec.com/software-tools/double-opt-in-forms/sdk-v11-2.html) 
* Bosch sensor(tec) comminity, [WS](https://community.bosch-sensortec.com/), 
* Supported platforms, [PDF](https://www.bosch-sensortec.com/media/boschsensortec/software_tools/software/bmv080_1/supported_platforms/bmv080_binary_size_information.pdf)

Raspberry Pi
* Raspberry Pi Pico-series C/C++ SDK Libraries and tools for C/C++ development on Raspberry Pi microcontrollers. [PDF](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf), RPi Pico 2, C/C++ sdk-v11-2 , 2 0 2 5 - 0 7 - 3 0 : 3 0 0 3 1 8 4 - c l e a

Sparkfun
* SparkFun Toolkit Arduino Library, [GH](https://github.com/sparkfun/SparkFun_Toolkit/tree/main), Toolkit of common functionality for use within SparkFun Libraries 
* SparkFun Air Quality PM1/PM2.5/PM10 Sensor - BMV080 (Qwiic), [GH](https://github.com/sparkfun/SparkFun_BMV080_Arduino_Library/tree/main), Arduino Library to support the Bosch BMV080 Particulate Matter Air Quality Sensor PM2.5 via I2C and SPI. ,  .ino Ardu'ino' C++ like source file examples

IDE
* Arduino IDE, Sparkfun code, with SparkFun_BMV_Arduino_Library v1.0.1 Bosch BMV080 SDK v11.2.0 Arduino IDE 2.3.5
* VS Code with Arduino CLI, 

Build
* CMake, Windows x64 [GH](https://github.com/Kitware/CMake/releases/download/v3.28.1/cmake-3.28.1-windows-x86_64.msi/), Bosche code, Raspbery Pi
* PlatformIO, Bosch code, everything else not Raspberry Pi, 

Language 
* C standard library clib, [WP](https://en.wikipedia.org/wiki/C_standard_library)
* C reference, [WS](https://en.cppreference.com/w/c.html)

## Hardware

MCU - microcontroller, RP2350
* Raspberry Pi Pico 2, [WS](https://www.raspberrypi.com/products/raspberry-pi-pico-2/), preferred option, RISC‑V architecture, dual core, dual architecture, a pair of Arm Cortex-M33 cores, and a pair of open-hardware Hazard3 cores 
* SparkFun IoT RedBoard - RP2350, [WS](https://www.sparkfun.com/sparkfun-iot-redboard-rp2350.html), Arduino R4 format (aka form factor?), Home Development Boards Microcontrollers Arduino Arduino Boards 

Systems - 
* Bosch Sensortec BMV080 Shuttle Board 3.1, [WS](https://www.bosch-sensortec.com/software-tools/tools/application-board-3-1/), with Web App, 
* BlackIoT Polverine, [WS](https://blackiot.swiss/polverine), ESP32 platform, 
* SparkFun Breakout Board, [WS](https://www.sparkfun.com/sparkfun-air-quality-pm1-pm2-5-pm10-sensor-bmv080-qwiic.html), Arduino centric? Home Sensors Environmental Sensors Air Quality 
* PurpleAir PIXEL

## References

Sparkfun BMV080 particulate matter sensor breakout board
* Schematic [PDF](https://docs.sparkfun.com/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080/assets/board_files/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080_v10_Schematic.pdf)
* SparkFun Air Quality PM1/PM2.5/PM10 Sensor - BMV080 (Qwiic) Hookup Guide, [WS](https://docs.sparkfun.com/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080/introduction/#), ESP32 centric, 
* ..

Arduino IDE .ino files
* .h and .cpp or .ino?[WS](https://community.arduboy.com/t/h-and-cpp-or-ino/10592), Aug 2022, Arduboy, 
* PlatformIO, )

Raspberry Pi - datasheets
* RP2350 Datasheet A microcontroller by Raspberry Pi, [PDF](https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf), the RP2350, an ARM Cortex-M33 chip, 
* Raspberry Pi Pico 2 Datasheet An RP2350-based microcontroller boardd [PDF](https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf), the RPi Pico PCB, 
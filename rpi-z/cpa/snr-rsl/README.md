# Aerosol sensor snr-rsl (cpa)

* Third attempt at making some progress with the Bosch BMV080 aerosol sensor. 
* First attempt with single board computer RPi Zero 2 W.

See also
* RPi Pico; Aerosol sensor rsl (mpy) [GH](https://github.com/YorkEarwaker/Electrical-Engineering/tree/main/rpi-pi/mpy/snr-rsl), first cut research, start of bare bones MicroPython driver, recognized on Pico I2C bus
* RPi Pico; Aerosol sensor rsl (cpa) [GH](https://github.com/YorkEarwaker/Electrical-Engineering/tree/main/rpi-pi/cpa/snr-rsl), first cut research, C/C++ 
* Air purifier, [WS](https://github.com/YorkEarwaker/Electrical-Engineering/tree/main/hap/arp), particulate matter sensor as component part of /arp project

## Notes

Assumption
* C/C++ on the RPi Zero 2 W might have less hurdles than on RPi Pico for BMV080 .
* C/C++ on Dell Ubuntu Laptop might have less hurdles than on Dell MS Win 10 Laptop
* MS Win 10 was end of life and out of support and patching
* Target operating systems on RPi Zero 2 W both Debian based distros; RaspiOS Lite Trixie, Ubuntu Core 24, 
* Integration on Dell Ubuntu Laptop to RPi Zero 2 W might has less hurdles as both use Debian Linux distros, 
* RPi Pico 2 W, or other Pico MCU, are not properly supported by Bosch for BMV080 
* RPi Pico 2 W, or other Pico MCU, are not adequately specked for use with Bosch BMV080
* Intent, as progress is made on C/C++ code for BMV080 on RPi Zero 2 W try and cross compile too for RPi Pico 2 W, or other Pico MCU .
* ...

## Status
TODO
* <todo: consider, review SparkFun code base, for SparkFun breakout board BMV080, >
* <todo: consider, other similar particulate matter sensors from other vendors, >
* <todo: consider, updating first and second attempts with RPi Pico with link to this third attempt with RPi Zero 2 W, >

DONE
* <done: consider, intent to commit, >

## Overview
Connection scenarios
* Two main connection scenarios to BMV080 breakout board; I2C, SPI . Using Sparkfun Arduino code base reconfigured for RPi Z.
* Third possible connection direct to BMV080 sensor?; FPC 13-pin 0.33mm Connector? Using Bosch SDK directly? TBD.

### I2C
* I2C is default connection mode for breakout board?
* Wifi connection to UI Device for MVP. Not PoC.
* Qwiic or I2C pin out should require no changes to code base?

Context Diagram -  RPi Z GPIO I2C to BMV080 breakout board Qwiic 
```                                   
            BMV080 Breakout                                  RPi Zero 2 W                                       UI Device (mobile, tablet, laptop, ...)
             -----------                 I2C                  -----------                      Wifi               -----------
            |        ___|             Connection         I2C |o o     ___| PWR IN           Connection           |           |
            |       |___  Qwiic ----------------------- GPIO |o o    |___  Micro USB B                           |           |
            |           |         Sink < Power < Source      |o o        | Sink < Source                         |           |
             -----------               < Data >               -----------                    < Data  >            -----------
                                                               
```

Circuit Diagram
``` 
     TBC
```

Context Diagram - RPi Z GPIO I2C to BMV080 breakout board I2C pin out
```                                   
            BMV080 Breakout                                  RPi Zero 2 W                                       UI Device (mobile, tablet, laptop, ...)
             -----------                 I2C                  -----------                      Wifi               -----------
            |         o | I2C         Connection         I2C |o o     ___| PWR IN           Connection           |           |
            |         o | PIN ------------------------- GPIO |o o    |___  Micro USB B                           |           |
            |         o | OUT     Sink < Power < Source      |o o        | Sink < Source                         |           |
             -----------               < Data >               -----------                    < Data  >            -----------
                                                            
```

Circuit Diagram
``` 
     TBC
```

### SPI
Similar to I2C . Unclear if SparkFun Arduino code supports this. If not will have to write SPI connection code in C. TBD

### FPC
Very different from either I2C or SPI and may not be viable for PoC. Consider if there are any advantages for a MVP? 

### Development environment
Two scenarios
* Dev env box UART serial bridge to RPi Z 2 W
* Dev env box SSH over Wifi to RPi Z 2 W

Assumptions - both scenarios
* Assume requirement for some serial communication with headless RPi Z from Laptop for development over UART serial bridge
* RPi Z running headless OS, either RPi Trixie Lite or Ubuntu Core 24
* The Bosch SDK and other code using it executes on the RPi Zero 2 W to interact with BMV080 sensor on breakout board,

Context Diagram - Dev env box UART serial bridge to RPi Z 2 W
* I2C to I2C context is shown 
* Likely identical or similar for contexts; I2C to Qwiic, SPI to SPI, SPI to Qwiic
* <todo: consider, reviewed once development has started and make changes accordingly, wip >
```                                   
            BMV080 Breakout                                  RPi Zero 2 W                         USB TTL to UART device                                   Dev env box
             -----------                 I2C                  ------------          Serial             -----------                Serial                   -----------
            |         o | I2C         Connection         I2C |o o      o o| UART  Connection     UART |o       ___| Some        Connection                |___        |
            |         o | PIN ------------------------- GPIO |o o  __  o o| GPIO ---------------- PIN |o  SBC |___  USB ------------------- standard USB A ___|       |
            |         o | OUT     Sink < Power < Source      |o o |  | o o|                       OUT |o          | A/B/C   Sink < Power < Source         |           |
             -----------               < Data >               ----    ----         < Data >            -----------               < Data >                  -----------
                                                                  Sink                            Serial Bridge Chip SBC
                                                                   ^   PWR IN Micro USB B         
                                                                 Source
                                                                
```

Circuit Diagram
``` 
     TBC
```

Context Diagram - Dev env box SSH over Wifi to RPi Z 2 W
* ? context is shown 
* Likely identical or similar for contexts; ?
* <todo: consider, reviewed once development has started and make changes accordingly, wip >
```                                   
     TBC
                                                                
```

Circuit Diagram
``` 
     TBC
```

## Hardware

Sensor - BMV080, Bosch
* Particulate matter sensor BMV080, [WS](https://www.bosch-sensortec.com/products/environmental-sensors/particulate-matter-sensor/bmv080/), Bosch, 
* Datasheet, [WS](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmv080-ds000.pdf), Bosch
* Bosch Sensortec Community [WS](https://community.bosch-sensortec.com/), Bosch

Device - SparkFun breakout board using BMV080, 
* SparkFun Air Quality PM1/PM2.5/PM10 Sensor - BMV080 (Qwiic) [WS](https://www.sparkfun.com/sparkfun-air-quality-pm1-pm2-5-pm10-sensor-bmv080-qwiic.html), SparkFun,
* Schematic, [WS](https://docs.sparkfun.com/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080/assets/board_files/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080_v10_Schematic.pdf), SparkFun
* Hookup Guide, [WS](https://docs.sparkfun.com/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080/introduction/#), SparkFun

Device - TBD thing using BMV080
* <todo: evaluaate other BMV080 candidate devices, >

Sensor - tbd
* ...

## References

Terms
* Aerosol, 
* CO, carbon monoxide
* PM, particulate matter
* VOCs, volatile organic compounds
* VSCs, volatile sulfer compounds

VOCs - propellants, compressed aerosols, vehicle exhausts, other sources, 
* Photochemical smog, toxic smog, 
* Ground ozone O3, 
* SOA, secondary organic aerosols
* Halocarbons, CFC's, banned under the Montreal Protocol 1987, due to depletion of and hole in stratospheric ozone layer, 
* Butane 
* Propane [WP](https://en.wikipedia.org/wiki/Propane)
* Toluene
* Ethylbenzene
* Xylene (p-xylene, o-xylene)
* Styrene
* Chlorobenzene
* ...

VSCs - industrial? mainly?
* ...

Papers
* Global emissions of VOCs from compressed aerosol products. [WS](https://online.ucpress.edu/elementa/article/9/1/00177/116770/Global-emissions-of-VOCs-from-compressed-aerosol) 2021. Yeoman, AM, Lewis, AC., Elementa: Science of Anthropocene 9(1). [DOI](https://doi.org/10.1525/elementa.2020.20.00177)

News Papers - VOCs
* Consumer aerosol products overtake cars as source of dangerous smog in UK, [WS](https://ncas.ac.uk/consumer-aerosol-products-overtake-cars-as-source-of-dangerous-smog-in-uk/), 27 April 2025, National Centre for Atmospheric Science, UK, 
* Effect Of Photochemical Smog, [WS](https://www.sciencing.com/effect-of-photochemical-smog-12328963), 24 March 2022 (updated), Mike Charmaine, Sciencing, 
* ...

News Papers - BMV080
* Sensors Converge 2025: Bosch boosts ecosystem around BMV080 particulate matter sensor, [WS](https://www.bosch-sensortec.com/news/sensors-converge-2025-bosch-boosts-ecosystem-around-bmv080-particulate-matter-sensor.html), Plug-and-play platforms simplify and accelerate development with Bosch environmental sensors








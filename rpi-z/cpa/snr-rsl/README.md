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
* Development is carried out on Dev env box in this instance Dell Ubuntu laptop
* Code is cross compiled by tool chain on Dev env box and compiled files deployed to RPi Z 2 W
* Once the dev env and dev ops are working for deployment to RPi Z 2 W create scripts delta for other platforms RPi Pico in the first instance

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
* Ubuntu Core 24 context is shown 
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
* Datasheet, [PDF](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmv080-ds000.pdf), Bosch
* Technical Specification Statement, [PDF](https://www.bosch-sensortec.com/media/boschsensortec/downloads/application_notes_1/bst-bmv080-an002.pdf), Bosch, readings
* Shipment & Packaging Details, [PDF](https://www.bosch-sensortec.com/media/boschsensortec/downloads/shipment_and_packaging_details/bst-bmv080-sp000.pdf), Bosch, bulk purchase of sensors
* Integration Guidelines, [PDF](https://www.bosch-sensortec.com/media/boschsensortec/downloads/handling_soldering_mounting_instructions/bst-bmv080-hs000.pdf), Bosch, integration to host PCB
* Bosch Sensortec Community [WS](https://community.bosch-sensortec.com/), Bosch

Device - SparkFun breakout board using BMV080, 
* SparkFun Air Quality PM1/PM2.5/PM10 Sensor - BMV080 (Qwiic) [WS](https://www.sparkfun.com/sparkfun-air-quality-pm1-pm2-5-pm10-sensor-bmv080-qwiic.html), SparkFun,
* Schematic, [WS](https://docs.sparkfun.com/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080/assets/board_files/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080_v10_Schematic.pdf), SparkFun
* Hookup Guide, [WS](https://docs.sparkfun.com/SparkFun_Particulate_Matter_Sensor_Breakout_BMV080/introduction/#), SparkFun

Device - TBD thing using BMV080
* <todo: evaluaate other BMV080 candidate devices, >

Sensor - tbd
* <todo: other particlate matter sensors, other manufacturer options, >
* ...

### Test

Particulate matter - standardized test materials 
* Some sample test materials and methods partly sourced from Bosch BMV080 sensor documentation, other found in search results on topic, 
* ISO 12103-1:2024, Road vehicles — Test contaminants for filter evaluation, Part 1: Arizona test dust, [WS](https://www.iso.org/standard/85949.html), ISO, Arizona Road Dust, four to five grades of test dust; A1 Ultrafine, A2 Fine, A3 Medium, A4 Course, sometimes also A5 Course. natural and synthetic can behave differently,
* ISO 16000-9:2024, Indoor air, Part 9: Determination of the emission of volatile organic compounds from samples of building products and furnishing — Emission test chamber method, [WS](https://www.iso.org/standard/79022.html), ISO, volatile organic compounds VOCs in indoor air, "incense smoke", 
* CSN EN 16738 Emission safety of combustible air fresheners - Test methods, [WS](https://www.en-standard.eu/csn-en-16738-emission-safety-of-combustible-air-fresheners-test-methods/),  determining combustible air fresheners in indoor air, 
* EN 16739 methodology for assessing test results, 
* <todo: others to source, which are relevant for this AGW sensor project, which scenarios to prioritise, >

Particulate matter - lists, catalogs, 
* Emissions analytics, [WS](https://www.emissionsanalytics.com/list-of-standards), list of standards, automotive, overlap with other sectors?
* <todo: others to source, for other contexts, >

### Tools

Spectrometer - aerosols
* To use as benchmark tests for aerosol sensors, comparisons, 
* LAP 322 Aerosol Spectrometer, [WS](https://www.topas-gmbh.de/en/products/particle-measurement/product/lap-322), TOPAS, for analysis of particle size distributions and particle number concentrations in aerosols, monochrome light, referenced in Bosch BMV080 technical specification statement
* <todo: other of a similar type to source, >

## References

Terms
* Aerosol, 
* AQI, air quality indices 
* PM, particulate matter

Particulate matter - kinds
* CO, carbon monoxide
* PAHs, polycyclic aromatic hydrocarbons
* VOCs, volatile organic compounds
* VSCs, volatile sulfur compounds

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








# Aerosol sensor snr-rsl (cpa)

* Third attempt at making some progress with the Bosch BMV080 aerosol sensor. 
* First attempt with single board computer RPi Zero 2 W.

See also
* RPi Pico; Aerosol sensor rsl (mpy) [GH](https://github.com/YorkEarwaker/Electrical-Engineering/tree/main/rpi-pi/mpy/snr-rsl), first cut research, start of bare bones MicroPython driver, recognized on Pico I2C bus
* RPi Pico; Aerosol sensor rsl (cpa) [GH](https://github.com/YorkEarwaker/Electrical-Engineering/tree/main/rpi-pi/cpa/snr-rsl), first cut research, C/C++ 

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

DONE
* <done: consider, intent to commit, >

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








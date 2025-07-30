# Aerosol sensor rsl (mpy)

Aerosol, molecules, particulate matter, air quality control, . The consequence of phase change. The likelyhood of wetbulb events increases. In a warming planet more seven percent more water vapor will be held in the atmosphere for each degree of warming. In a warming planet more volatile substance will evaporate. In a warming planet more fires wild and urban will occure and so more particulate matter. Area burned will at least double for every degree of warming. The water vapor will compbine with other volative vapor and particulate matter and gases. Each water droplet a miniature testtube in the sky heated by the Earths radiative energy and catalysed by the Suns radiative energy. In one giant chemical experiment in the sky. Each water droplet in the atmosphere also a miniature petri dish in the sky. The chemistry will interact with microorganisms in one giant biological experiment in the sky. Which will interact with the chemistry and biology in oceans and on land and cryosphere. So the atmopheric water droplets as micro testtube and micro petri dish interacting with the macro testtube and macro petri dish of the oceans. And so on with meso ecosystem niches and on. And the increased heat will speed chemical and biochemical molecular interactive process. In one giant biospheric and geospheric experment in Earths global systems of systems.

So sensors are needed to measure the aerosol things to at least know what is out there and where an in what concentrations and for how long and with what other things to be able to start to think of how to mitigate the possible consequences. CFC's and the hole in the ozone as one example.

Global health consequences. Not least with the possibility of novel microorganisms and the possiblity of global pandemics. Notwithstanding all of the other geospheric and biospheric consequences.

## Status
TODO
* <todo: consider, LEW-TOPS-19, NASA, Multi-Parameter Aerosol Scattering Sensor MPASS, nanometer particle scale detection, >
* <todo: consider, Bosch, BME688?, Gas + thp, sensor, cost circa: bare sensor £?, brakout board £20?>
* <todo: consider, other sensors, light based nanometer scale measurements, >
* <todo: consider, ocean system corollery to atmopherice aerosol measurements in water column and interaction with atmosphere and mixing >
* <todo: consider, find EU Copernicus studies on atmospheric chemisty effects on human health, longevity of substances, >
* <todo: consider, find JP KR IN AU NZ and so on studies on atmospheric chemisty effects on human health, longevity of substances, >
* <todo: consider, package nameing org.agw.een.rsl or org.agw.een.snr.rsl or org.agw.een.snr ?  >
* <todo: consider, creating a (cpa) project directory structure for C/C++ code as Sparkfund and Bosch examples are in C/C++, create a seperate docs folder for BMV080 and sparkfun board info, >

DONE
* <done: intent to commit>
* <done: consider, Bosch, BMV080, Air Quality, sensor, looks like a good candidate, cost circa: bare sensor £43, brakout board £63?, acquired, >

## Libs

* <todo: identify generic sensor libs, wrappers, standard like interoperabiity, api, ontology, message data formats, JSON, and so on, >

## Hardware

Sensor component part - the sensor, alone, environmeental sensors, particulate sensors, aerosl sensors, 
* BMV080, Bosch
* BME690, Bosch
* BME688, Bosch
* SPS30 [WS](https://sensirion.com/products/catalog/SPS30), Sensirion
* <todo: others to identify, particulate matter detection specifically, gas specifically, >

Independent component (stand alone device) - lose coupling, high cohesion, if limited to single device, i.e. a single sensor, better componentisation, better NFR's ilities, the sensor on a circuit board no resistors etc, likely supplied pinned 0.1 , 
* <todo: identify ones other than DHT22/DHT11 not a particle sensor, temperature only,  >

Breakout boards - lose coupling, high cohesion, if limited to single device, i.e. a single sensor, better componentisation, better NFR's ilities, the sensor on a circuit board likely resistors etc. may or may not be pinned 0.1, 
* SparkFun Air Quality PM1/PM2.5/PM10 Sensor - BMV080 (Qwiic), sparkfun com [WS](https://www.sparkfun.com/sparkfun-air-quality-pm1-pm2-5-pm10-sensor-bmv080-qwiic.html), Pi Hut [WS](https://thepihut.com/products/sparkfun-air-quality-pm1-pm2-5-pm10-sensor-bmv080-qwiic) , I2C default, SPI available, 
* Particulate Matter Sensor - SPS30, sparkfun com [WS](https://www.sparkfun.com/particulate-matter-sensor-sps30.html), Pi Hut 
* <todo: others to identify, see papers below, review of particulate sensors, >

Microcontroller board integrated solutions - tight coupling of sensor device to microcontroller, low cohesion, useful for end user product development with no electrical engineering, 
* <todo: consider moving this section elsewhere?, or leave here as imformative, >
* Polverine, Cutting-edge environmental sensing in a compact form factor, [WS](https://www.crowdsupply.com/blackiot/polverine), BlackIoT, ESP32-S3-MINI-1 Microcontroller, 2.4GHz WiFi, Bluetooth 5, BMV080, BME690, cost circa: $79, International Shipping $18.00 GB VAT 20.00% $19.40 Order Total (USD) $116.40
* Martinica, A powerful Bosch sensor development board with Wi-Fi and enhanced security in an Arduino MKR form factor, [WS](https://www.crowdsupply.com/blackiot/martinica), BlackIoT, WIP, <retrieved: 2025, 07, 21>

Manufacturers
* MCU, BlackIoT, Crowd Supply [WS](https://www.crowdsupply.com/blackiot), com [WS](https://www.blackiot.swiss/), multiple integrated devices, 
* Board, SparkFun, 
* Seosor, Bosch, 

## Readings

### Recognise BMV080 Sunspark breakout board on I2C bus
<info: successfully scan for BMV080 Sunspark breakout board on I2C bus in DE1 dev env. >
```
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
pm_sensor_i2c: I2C(0, freq=400000, scl=9, sda=8, timeout=50000)
pm_sensor_i2c.scan() address list: [87]
>>> 
```

## References

Terms
* Aerosol, a mixture of particles in the air, solid particle, liquid droplet, 
* Particle, matter in solid phase or liquid phase, 
* Particulate Matter, [WP](https://en.wikipedia.org/wiki/Particulate_matter) PM, PM1=1μm, PM2.5=2.5μm, PM10=10μm, ...

Technology
* Compact lasers
* Integrated photodiods
* ...

Particles
* Primary particle, precursor of secondary particle, 
* Secondary particle, oxidation of primary particles, sulfuric acid (liquid), nitric acid (gaseous), salts dry (solid) aqueous solution (liquid); amonimum sulfate, amonium nitrate, 

Meteorology
* climate
* precipitation

Health
* Stroke
* Heart disease
* Lung disease
* Preterm birth
* ...

Scale
* micormetre, micron, μm, μ symbol, [WP](https://en.wikipedia.org/wiki/Micrometre)
* Mu, Μμ, [WP](https://en.wikipedia.org/wiki/Mu_(letter)), Greek letter
* 90μ, fine beach sand
* 70μ-180μ, paper thickness, 
* 17μ-181μ, circa 50μ-70μ, human hair diameter, 
* 10μ, fungal hyphae,
* 10μ, fog, mist, cloud, water droplet
* 10μ, dust, pollen, mould
* 6μ-8μ, red blood cell
* 6μ, carbon fiber, 
* 3μ-8μ, spider silk
* 1μ-10μ, bacterium
* 2.5μ, combustion particles, organic compounds, metals, 

Types, and size distribution in micrometres (μm), of atmospheric particulate matter [WP](https://en.wikipedia.org/wiki/Particulate_matter#/media/File:Airborne-particulate-size-chart.svg)

Biological Contaminants
* Pollen, 10μm-100μm
* Mould Spores, 2-90
* House Dust Mite Allergens, 0.2-12
* Bacteria, 0.4-10
* Cat Allergens, 0.1-3.5
* Viruses, 0.005-0.08

Types of Dust
* Heavy Dust, 95-995
* Settling Dust, 0.95-95
* Suspended Atmospheric Dust, 0.0025-0.95

Particlate Contaminants
* Cement Dust, 4.5-100
* Fly Ash, 0.9-100
* Oil Smoke, 0.5-7.5
* Smog, 0.085-2
* Tobacco Smoke, 0.085-1.25
* Soot, 0.085-0.45

Gas Molecules - Gaseous Contaminants
* 0.085
* ...
* 0.0045

Journals
* Aerosol and Air Quality Research AAQR org [WS](https://aaqr.org/categories/low-cost-sensors), 
* Sensors com [WS](https://www.mdpi.com/journal/sensors), open access, 

Information packs - fact sheets
* The Impact of Wildfires on Climate and Air Quality, An emerging focus of the CSD, [WS](https://csl.noaa.gov/factsheets/csdWildfiresFIREX.pdf), NOAA, ESRL Chemical Sciences Division,

Papers
* A Review of Low-Cost Particulate Matter Sensors from the Developers’ Perspectives, PMC [WS](https://pmc.ncbi.nlm.nih.gov/articles/PMC7730878/), Sensors [DOI](https://www.mdpi.com/1424-8220/20/23/6819), 

Sensors - Instrumentation
* Multi-Parameter Aerosol Scattering Sensor (LEW-TOPS-19) [WS](https://technology.nasa.gov/patent/LEW-TOPS-19), NASA, Instrumentation, A highly accurate, lightweight, low-cost miniaturized environmental monitoring sensor system
* Particulate Matter Sensor, BMV080 [WS](https://www.bosch-sensortec.com/products/environmental-sensors/particulate-matter-sensor/bmv080/), Bosch, 
* BMV080 Ultra-mini Particulate Matter Sensor – Integration Guideline, [PDF](file:///C:/Users/yorke/Downloads/bst-bmv080-hs000.pdf), Bosch, Document revision 1.3, Document release date May 2025, Document number BST-BMV080-AN000-03, Sales part number 0273.017.054-1NV


# Linear power supply hello world lps-hwd

Learning about power suplies and linear power adapters. Basic electrical engineering using old technology.

## Notes

First attempt at an linear ac/dc power adapter 'hello world' simple example.

Objectives
* Basic electronic engineering, learning
* Build toward modern linear adapter for monitor, skills, capabilities
* Learn to use multimeter, learning
* Learn to Use a bench PSU for safety, to avoid direct mains power.
* Learn about galvanic separation, output is electrically separated from mains.

## Status
TODO
* <todo: consider, BoM for V5 @ !A ac/dc conversion, core experience for creating a power adapter >
* <todo: consider, BoM for V19 @ 1.7A ac/dc conversion, will require different component tollerances due to higher voltage and current requirements >
* <todo: consider, double component purchase, x1 for breadboard RnD, x1 for perboard, >
* <todo: consider, warning / disclaimer, working with mains electricity is extremely dangeouse, mains electricity can cause death or injury or loss of property. These are just notes to self not a recomendation for hobbist/maker projects. Always consider safety first. Comply with local safety regulatons and standards. Do not use this source as a guide it may lead to harm to persons or property and you do so at your own risk. >
* <todo: consider, peronal rider, this is a personal learning source, I am not a qualified electritian or electronics engineer or power engineer or mechanical engineer. Just tryig to learn as a means to better understanding of the world.  Bottom line, you or someone else may die or be permanently injured working with mains electricity and electrical components. There is a risk of; electricution, fire, explosion of component parts, . Safety first, in all instances. >
* <todo: consider, use of power supply unit psu instead of direct mains power for saftey, >

DONE
* <done: consider, intent to commit>

## Bill of Materials BoM
*  nominal uk 240 VAC, nominal eu 230 VAC, some eu nations 220 VAC, actual variability 207-253 VAC range, 

### BoM V5 @ 1A dc output, circuit components
Core set of components for bare bones build

* Transistor, x1, 9V - 12V 1A
* Diodes, x5, are 1N4001, 1N4004, 1N4007 suitable for uk? 
* Capacitors, x4, are 2 220-470uF electrolytic, 2 100nF ceramic disc suitable for uk?
* 78XX voltage regulator, x1, likely 7805 V5
* Wire, guage tbd

### BoM V19 @ 1.7A dc output, circuit components


## Calculations

```
rectified DC = ~1.414 x AC RMS voltate

```

## Output

Circuit diagram
```
tbd
```

## References

* AC RMS
* EMS

Tutorials - instructions, 
* AC to DC Conversion, [WS](https://www.instructables.com/AC-to-DC-Conversion/), Instructables, brmarcum
* AC-DC Regulator Kit Instructions, [WS](https://www.mitchelectronics.co.uk/resources/ac-dc-kit-instructions), Mitchel Electronics Ltd
* How to Convert AC to DC [WS](https://www.wikihow.com/Convert-AC-to-DC), wikiHow
* ...

News Papers - UK, EU mains
* What are the differences between 220VAC, 230VAC and 240VAC Mains Supplies and what voltage equipment should I use? [WS](https://www.se.com/uk/en/faqs/FA144717/)
* Mains voltage in the UK and the EU – and what it means for guitar amps, [WS](https://www.ampworks.co.uk/myth-busters/mains-voltages-in-the-uk-and-the-eu-and-what-it-means-for-guitar-amps/), 8 July 2020, rowan, Keld Ampworks, guitar amps

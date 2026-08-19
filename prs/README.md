# Power Supply prs

Comverting current, alternating current, dirct current, pulsed direct current, 

## Notes

Objectives
* build an ac/dc adapter
* ...

## Status
TODO
* <todo: consider, finalise BoM to raise purchase order of component parts >
* <todo: consider, require a multimeter for this project, find options>

DONE
* <done: consider, intent to commit>

## BoM

* Banana jack, black
* Banana jack, red
* Capacitors, various
* Filter capacitor
* Perf board
* 22 guage insulated wire
* AC line cord
* #6 hardware
* heat shrink tubbing
* heat gun/hair drier
* Rectifier, full wave bridge rectifier
* Transformer, step down, a few volts higher than needed, 
* Voltage regulator, 7800 series 5 to 24 volts, e.g. 7805 5V, 

## Output

Context diagram - current flow
```
Mains AC --------> AC/DC --------> DC Device
                  Adapter
```

Context diagram - adapter connector detail
* AC OUT  (out of mains source); UK three pin plug
* DC IN  (into the device sink); Coaxial power connector plug 'pin'
```
        Mains ---> Plug ---> Cable ----> Brick ----> Cable ---> Pin ---> Device
         
                     __               |         |             ______     |       Phone
Socket   |:|       =|__| ------------ |  AC/DC  | -----------(_____(·)   |  (·)  Monitor
                                      | Adapter |                        |       Laptop
                                      |         |                                 ...           

        AC OUT ---> AC IN ------------>  AC/DC -------------- DC OUT ---> DC IN 
                                       Conversion
```

Context diagram - coaxial power connector - plugs and recepticals
* barrel connector, concentric barrel connector, tip connector, barrel pin, pin tip, jack
* metal tubing outer diameter OD inner diameter ID, metal rod central pin diameter CPD
* Coaxial power connector 'pin'; outer diameter OD, inner diameter ID, central pin diameter CPD, length L
* <todo; consider, source difinitive reference to metal alloy tubing and rod, brass niclel plated? stainless steel? >
```
              Pin                   Pin
              Plug                  Receptical

              DC OUT                DC IN
           _________
 ---------(________(•)          |    (•)

              AC/DC Adaptor         DC Device
              Provider              Consumer 

              Power                 Power
              Source                Sink
```

Calculations
```
Theoretical voltage
AC Voltage / sqrt(2) = DC Voltage
230 / √2 ≈ 162.63, EU
240 / √2 ≈ 169.71, UK reality?, nominally 230
120 / √2 =  84.85, US

Supply frequency 
50Hz/60Hz

```


Circuit diagram - AC/DC adapter
* Circuit conversion process steps high level
* Voltage Transformation, transformer, to change voltage up or down to required level
* Rectification, diodes, to convert alternating current to pulsed direct current 
* Filtering and Regulation, capacitors and voltage regulators,to smooth output and maintain stable dc output voltage
```
Bread board - RnD, no solder
Perf Board - PoC, solder
Printed Circuit Board - Product, circuit certification

  Wire in ---> Transformer ---> Diodes ---> Capacitors & Voltage Regulators ---> Wire out


```


## References

Electrical terms
* Alternating current
* Direct current
* Direct current (pulsed)
* Mains electricity by country, [WP](https://en.wikipedia.org/wiki/Mains_electricity_by_country)

Metric
* Ampere, Amp, [WP](https://en.wikipedia.org/wiki/Ampere), si unit amps, A
* Electric current, [WP](https://en.wikipedia.org/wiki/Electric_current), si unit ampere
* Voltage, Volts, [WP](https://en.wikipedia.org/wiki/Voltage), si unit volts, V

Products
* AC Adapter [WP](https://en.wikipedia.org/wiki/AC_adapter)
* Linear adapter
* Switched mode power supply smps [WP](https://en.wikipedia.org/wiki/AC_adapter)

Components - consider part of larger bom
* Coaxial power connector [WP](https://en.wikipedia.org/wiki/Coaxial_power_connector)

News Papers - tutorials, AC 2 DC, build an adapter
* How to Build Your Own AC/DC Power Adapter, [WP](https://ourpastimes.com/sudoku.html), Our Pastimes, 12  April 2017, John Papiewski, 
* AC Power Design in 7 Steps, [WP](https://www.fsp-group.com/en/knowledge-tec-23.html), 22 10 2020
* AC to DC Conversion, [WP](https://www.instructables.com/AC-to-DC-Conversion/), Instructables
* How to Convert AC to DC, [WP](https://www.wikihow.com/Convert-AC-to-DC), 7 September 2024, Jesse Kuhlman, Hunter Rising, wikiHow, 

News Papers - tutorials, repair an adapter
* Notes on the Troubleshooting and Repair of AC Adapters, Power Supplies, and Battery Packs, and - Other Related Information, [WP](https://www.repairfaq.org/sam/aapsfaq.htm), Version 1.19 (14-Jan-13), Samuel M. Goldwasser, 



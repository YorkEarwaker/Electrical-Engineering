# Power Supply prs

Comverting current, alternating current, dirct current, pulsed direct current, 

## Notes

Objectives
* build an ac/dc adapter 5V, learning
* build ac/dc adaptor 19V for 24MP55HQ-P monitor, reuse
* build skils capabilities for heat pump project, upskilling
* switching power supply, advanced, next steps,

Projcet type
* RnD, bread board, no solder
* PoC, perf board, solder
* Prod, printed circuit board, circuit certification

## Status
TODO
* <todo: consider, finalise BoM to raise purchase order of component parts >
* <todo: consider, break items out into general keep here, ac/dc adapter project for monitor sub-project, switching power supply sub-project, >
* <todo: consider, two linear ac/dc adapter projects, first RnD hello world 5V, second RnD & PoC monitor 19V >

DONE
* <done: consider, intent to commit>
* <done: consider, require a multimeter for this project, find options, likely Brymen BM869s >

## BoM - circuit 

* Banana jack, black
* Banana jack, red
* Capacitors, various
* Filter capacitor
* Perf board, PoC
* 22 guage insulated wire
* AC line cord
* #6 hardware, what is this???
* heat shrink tubbing, PoC
* Rectifier, full wave bridge rectifier
* Transformer, step down, a few volts higher than needed, 
* Voltage regulator, [WP](https://en.wikipedia.org/wiki/Voltage_regulator), linear, switching
* Linear regulator, 7800 series [WP](https://en.wikipedia.org/wiki/78xx), 5 to 24 volts, e.g. 7805 5V, aka L78xx, LM78xx, MC78xx, . 78xx positive, 79xx negative, so 7824 + 7905 = 19V 

## BoM circuit - additional - specifically for LG 24MP55HQ-P monitor
* EIAJ_05, Philmore 214, Mating Jack: Philmore # 214, 265 & 365 or Equivalent
* EIAJ_05, CUI Inc. PJ-025, Mating Jack: ???
* EIAJ_05, Farnell, others
* <todo: consider, new normal addition plugs jacks, >

## BoM - tools
* Heat gun/hair drier, for heat shrink tubbing, RnD?, PoC, rationale; useful, cost 
* Multimeter, electric charge testing, RnD, PoC, Prod, likely Brymen MB896s and some add ons, rationale; cost, high metrology capability, 
* Multimeter, Brymen extras; BU-86X USB Interface Kit, second K-type thermocouple air temp and tech temp, Brymen BKB32 Adapter for third party standard mini-plug, Brymen BMH-01 Magnetic Hanger todo check not bundled first, Pomona 6275/6341/72902/
* Micrometer, [](), metrology, barrel pin measurements, nice to have?
* Pin guages, [](), metrology, barrel pin measurements, recpticales, jacks, RnD?, PoC, likely 6mm to 1mm or parts of
* Soldering iron, PoC
* helping hands, likely KOTTO LED Magnifying Third Hand Soldering Station, rationale; quality, cost bracket, 
* pcb board holder, likely not now, tbd depending of commitment going forward
* Solder, PoC
* Soldering mat, PoC
* Vernier scale caliper, [WP](https://en.wikipedia.org/wiki/Vernier_scale), metrology, barrel pin measurements, nice to have?

## Tool suppliers
* Engineering & Guage Ltd [WS](https://www.engineering-gauge.co.uk/), metrology, pin gauges
* Metrology Quality Services [WS](https://mqs.co.uk/), metrology, pin gauges, circa £18 per set, 6 x 18 = 108? is this necesarry for this project? not for ac/dc adaptor but for monitor element for which ac/dc is neceaary in first place
* Telonic Instruments, [WS](https://telonic.co.uk/), multimeter, Brymen BM869s, circa £210.00 (including 20% VAT), logging cable £40.80 (including 20% VAT), 
* Farnell (CPC Farnell), [WS](https://uk.farnell.com/), electrical components circa £100?, Pomona probes & clips circa £100?, 
* RS Components, see Farnell
* Mouser, see Farnell
* Ubuy? KOTTO LED Magnifying Third Hand Soldering Station, circa £44

Total cost 
* everything: circa £603? closer to £700, likely cut; BM869s extras, helping hands, other? 
* BM869s and electrical components; circa £350? likely way forward RnD no solder
* Helping hands (optional), soldering mat, solder iron, other solder stuff cleaning holder, perf board, heat gun, ; circa £250? total guess, dig out previuse work on this, likely way forward PoC solder

## Libs

Brymen BM869s - is the cable nesecarry at this point? 
* Sigrok, python native driver for BM869s
* hid, roll your own scripts, access USB HID device cable interface, more powerfull than driver?

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
         
             |        __                                       ______     |       Phone
Socket   |:| |      =|__| ------------ |  AC/DC  | -----------(_____(·)   |  (·)  Monitor
             |                         | Adapter |                        |       Laptop
                                                                                   ...           

         AC OUT ---> AC IN ------------>  AC/DC -------------- DC OUT ---> DC IN 
                                        Conversion
```

Context diagram - coaxial power connector - plugs and recepticals
* barrel connector, concentric barrel connector, tip connector, barrel pin, pin tip, jack
* metal tubing outer diameter OD inner diameter ID, metal rod central pin diameter CPD
* Coaxial power connector 'pin'; outer diameter OD, inner diameter ID, central pin diameter CPD, length L
* <todo; consider, source difinitive reference to metal alloy tubing and rod, brass niclel plated? stainless steel? >
```
              Pin male              Socket female
              Plug                  Receptical, jack

              DC OUT                DC IN
           _________
 ---------(________(•)          |    (•)

              AC/DC Adaptor         DC Device
              Provider              Consumer 

              Power                 Power
              Source                Sink
```

Polarity - plug pin
* Warning! Inverted polarity plugs can damage equipment devices when plugged in
* Checking polairity, tbc
* Outer contact, aka; barrel, sleeve, ring . Inner contact, aka; tip, .
* <todo: consider, research this further, find source for reference >
```
          barrel                   tip
              OD                    ID
                    Usual Polarity
              (-)---------(• -------(+)

                 Inverted Polarity
              (+)---------(• -------(-)

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

Linear power adapter
```
tbc
       ╲
    	╳
       ╱
```

Switching power adapter
```
tbc
```

## References

Power Enginnering, [WP](https://en.wikipedia.org/wiki/Power_engineering), subfield of electrical enginneering

Electrical terms
* Alternating current
* Direct current
* Direct current (pulsed)
* Electric current, [WP](https://en.wikipedia.org/wiki/Electric_current), si unit ampere
* Mains electricity by country, [WP](https://en.wikipedia.org/wiki/Mains_electricity_by_country)

Metrology - si units
* Ampere, Amp, [WP](https://en.wikipedia.org/wiki/Ampere), si unit amps, A
* Voltage, Volts, [WP](https://en.wikipedia.org/wiki/Voltage), si unit volts, V
* Watt?, necessary for this project calculations?

Products
* AC Adapter [WP](https://en.wikipedia.org/wiki/AC_adapter)
* Linear adapter
* Switched mode power supply smps [WP](https://en.wikipedia.org/wiki/AC_adapter)

Components - consider part of larger bom
* Coaxial power connector [WP](https://en.wikipedia.org/wiki/Coaxial_power_connector)
* DC connector [WP](https://en.wikipedia.org/wiki/DC_connector)
* Extra low voltage [](), rated at of below 120VDC
* AC power plugs and sockets,

Standards - dc connectors, barrel pins, plugs
* IEC 60130-10
* EIAJ Japan
* DIN Germany
* JSBP, some laptops
* ...

Text character symbols
* Box drawing characters, [WP](https://en.wikipedia.org/wiki/Box-drawing_characters), 
* ...

News Papers - tutorials, AC 2 DC, build an adapter
* How to Build Your Own AC/DC Power Adapter, [WP](https://ourpastimes.com/sudoku.html), Our Pastimes, 12  April 2017, John Papiewski, 
* AC Power Design in 7 Steps, [WP](https://www.fsp-group.com/en/knowledge-tec-23.html), 22 10 2020
* AC to DC Conversion, [WP](https://www.instructables.com/AC-to-DC-Conversion/), Instructables
* How to Convert AC to DC, [WP](https://www.wikihow.com/Convert-AC-to-DC), 7 September 2024, Jesse Kuhlman, Hunter Rising, wikiHow, 

News Papers - tutorials, repair an adapter
* Notes on the Troubleshooting and Repair of AC Adapters, Power Supplies, and Battery Packs, and - Other Related Information, [WP](https://www.repairfaq.org/sam/aapsfaq.htm), Version 1.19 (14-Jan-13), Samuel M. Goldwasser, 



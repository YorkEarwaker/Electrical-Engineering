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
* <todo: consider, itterative approach to assembling bench development and testing tools, requires some upfront research on cohsive and interoperable bench elecronic tools, otherwise risk not interoperable issues, jasper like end to end testing for example, consider no solcer first, >
* <todo: consider, no solder setups higher current higher voltage, research into current safty and use in prototyping poc necessary, no solder setups, avoid short cicuites, and so on current is important metric Ampres, nylon bolts standoffs for perfboard and breadboard, wire guards, heat shrink wrap, ... >
* <todo: consider, bench tools, psu, oscilloscope, dc loader, ..., Rigol and Siglent, both CN, appear to be at the right price point and capability for prototyping bench, Siglent overall appears a little better? SCIP, LAN, USB, ... >

DONE
* <done: consider, intent to commit>
* <done: consider, require a multimeter for this project, find options, likely Brymen BM869s >

## Bill of Materials BoM

### BoM - circuit first cut, adapter component candidate high level
* Banana jack, black, necessary?
* Banana jack, red, necessary?
* Capacitors, various
* Filter capacitor
* Perf board, PoC
* 22 guage insulated wire
* AC line cord
* #6 hardware, what is this???
* heat shrink tubbing, PoC
* Rectifier, full wave bridge rectifier, diodes component package, 
* Transformer, step down, a few volts higher than needed, 
* Voltage regulator, [WP](https://en.wikipedia.org/wiki/Voltage_regulator), linear, switching
* Linear regulator, 7800 series [WP](https://en.wikipedia.org/wiki/78xx), 5 to 24 volts, e.g. 7805 5V, aka L78xx, LM78xx, MC78xx, . 78xx positive, 79xx negative, so 7824 + 7905 = 19V 

### BoM circuit - additional - specifically for LG 24MP55HQ-P monitor
* EIAJ_05, Philmore 214, Mating Jack: Philmore # 214, 265 & 365 or Equivalent
* EIAJ_05, CUI Inc. PJ-025, Mating Jack: ???
* EIAJ_05, Farnell, others
* <todo: consider, new normal addition plugs jacks, >

### BoM - tools circuit design, circuit simulation, electrical engineering
* KiCad 8, design, laptop, Schematic + PCB layout + Gerber export., Free
* DesignSpark PCB, design, laptop
* Eagle, design, laptop
* Micro-Cap, simulation, laptop?, circuit virtual testing and component validation, before purchase order of components, validate physical assembly before the event 

### BoM - tools bench, circuit build, dev, test, QA, electrical engineering
* Heat gun/hair drier, bench, for heat shrink tubbing, RnD?, PoC, rationale; useful, cost 
* Multimeter, bench, electric charge testing, RnD, PoC, Prod, likely Brymen MB869s and some add ons, rationale; cost, high metrology capability, 
* Multimeter, bench, Brymen extras; BU-86X USB Interface Kit, second 'type-K temperature bead probe Bkp60' thermocouple air temp and tech temp, Brymen BKB32 Adapter for third party standard mini-plug, Brymen BMH-01 Magnetic Hanger todo check not bundled first, Pomona 6235 and 5325A sbc/mcu/pcb 10A 5V/12V/24V, also consider other use cases Pomona  6275/6341/72902/ 72902 + 72905
* Oscilloscope, bench, Rigol or Siglent, e.g. Rigol DS1054Z, ~£250, nice to have, for sbc/mcu/pcb and linear adapter project other projects wavefrom 
* Bench power supply, bench, source, Rigol or Siglent, e.g. Rigol DP832, ~£295, necessary, Clean, current-limited, multi-rail DC power, for heat pump
* DC load, bench, sink, Rigol or Siglent, e.g. Rigol DL3021. ~£378, expensive option, switching adapter, really necessary such a high spec?
* DC load, bench, sink, QX-100, ~£80, will do the job? 
* Functon generator, bench, Rigol or Siglent, Rigol DG1022Z ~£250, necessary?, Signal generation for testing, 
* LCR meter, bench, DE-5000, LCR / ESR / inductance, £90
* SLogic16U3, bench, Protocol debugging, £60
* ESD mat and strap + magnification + fume, bench, Practical bench hygiene, ~£85

### BoM - tools metrology, mechanical engineering
* Pin guages, bench, [](), metrology, barrel pin measurements, recpticales, jacks, RnD?, PoC, likely 6mm to 1mm or parts of
* Vernier scale caliper,bench, [WP](https://en.wikipedia.org/wiki/Vernier_scale), metrology, barrel pin measurements, nice to have?
* Micrometer, bench, [](), metrology, barrel pin measurements, nice to have?

### BoM - tools no solder, devices that require higher currents, where plastic breadboard might melt,  
* Screw terminal blocks (0.1″ pitch), power distribution, motor/relay wiring, plug into perfboard or standalone; 10–30 A per terminal;
* Snap-action wiring blocks (DF-15), quick splicing free-hanging wires, no crimping, reusable, rated 16 A; temporary power connections
* Binding posts / banana jacks, bench testing, power injection, Industrial-style, high current (15–30 A), very secure
* Crimp connectors + terminal strips, semi-permanent builds, crimp onto wire, insert into terminal block; no solder at either end
* Wire wrap, permanent?, gas-tight connections, 30 AWG, rated well beyond 24 V;
* nylon standoffs (M2 or #2-56), insulate breaboard or other items from short circuit 
* nylon nuts + standoffs, perboard, drill holes in corners of perfboard, 
* IC sockets, dip chips, swap chips and no harm to build, 
* blue tack, double sided tap, resistors, capacitors, small IC's
* foam tape (3m vhb, others, ...), heavier parts, not for heat generating component parts,
* cable ties, velcro cable straps, wire bundling
* wire loom/cable channel (flat plastic raceway, ~10-15mm wide) along board edge for main power runs,
* 30 AWG wire-wrap wire (spool)
* acrlyic board, aluminium board, mdf board, 3mm, to which to mount breadboards and perfboards
* breadboard with mounting holes, to take M2/M3 nylon standoffs
* perboard, 

### BoM - tools 3D priting, encasements, mechancical parts, 
* tbd ..

### BoM - tools soldering station, smd, through hole, 
* Soldering iron, bench, Hakko FX-888DX, Soldering, £125
* YIHUA 995D+, Hot air rework, £89, necessary?
* helping hands, bench, likely KOTTO LED Magnifying Third Hand Soldering Station, rationale; quality, cost bracket, 
* pcb board holder, bench, likely not now, tbd depending of commitment going forward* Solder, bench, PoC
* Soldering mat, bench, PoC
* SMD assembly, Stencil + squeegee + paste + toaster oven + temp controller + tweezers + flux + IPA	~£120
* Prototyping, Breadboard + perfboard, £10
* Stereo microscope, bench, inspection, (AmScope T340T), £100, solder joins, poor contact, bridging, ... 
* Thermal camera, bench, inspection, solder joins, heat spots, ...

### BoM - tools installation, building codes, saftey, 
* Clamp meter, installation, Brymen BM089, ~£130, for heat pump project, not necessary for bench work, must have for installation work 
* MFT (IR/Zs/RCD/3φ), installation, MI3125BT, ~£570, for heat pump project not necessary for bench work, must have for installation work 
* ...

### Tool suppliers
* Engineering & Guage Ltd [WS](https://www.engineering-gauge.co.uk/), metrology, pin gauges
* Metrology Quality Services [WS](https://mqs.co.uk/), metrology, pin gauges, circa £18 per set, 6 x 18 = 108? is this necesarry for this project? not for ac/dc adaptor but for monitor element for which ac/dc is neceaary in first place
* Telonic Instruments, [WS](https://telonic.co.uk/), multimeter, Brymen BM869s, circa £210.00 (including 20% VAT), logging cable £40.80 (including 20% VAT), 
* Farnell (CPC Farnell), [WS](https://uk.farnell.com/), electrical components circa £100?, Pomona probes & clips circa £100?, 
* RS Components, see Farnell
* Mouser, see Farnell
* Ubuy? KOTTO LED Magnifying Third Hand Soldering Station, circa £44

Total cost 
* everything: circa £2k? closer to £2.5k-3k?, bench development and testing kit all in? 
* Brymen BM869s multimeter, purchsed, now owned, 
* Brymen BM869s extras, purchased, now owned; BU-86X USB Interface Kit, Brymen BKB32 Adapter for third party probes, Brymen BMH-01 Magnetic Hanger, others tbc
* Brymen BM869s extras, pending, not owned, second type-K temperature bead probe Bkp60, Pomona 6235 & 5325A test probes, second Brymen BKB32 Adapter for third party probes, 
* Bench dev test tools, Class C, Rigol and Siglent CN appear to be good enough maker/prototyping, Siglent possibly better all round? need to qualify this? 
* Bench dev test tools, Class C, which are absolutley necessary, need more research, get some advice, 
* Bench dev test tools, Class C only, delta Class B software standard, delta Class A hardware trigger standard, Class B and Class A order much more expensive unafordable at this time due to quality of product, standards delta is not the main diffirentiator quality is,
* Electrical components; circa £80? linear adapter only, likely way forward RnD no solder
* Electrical components; circa £130? switching adapter only, PoC, pcb, RnD no solder impossible? 
* Helping hands (optional), ? keep seperate from magnifying lens + stand? likely as pcb holder would require magnification capability too
* Magnifying lens + stand necessary! and/or magnifying head set too? which to prioritise?
* Soldering mat, solder iron, other solder stuff cleaning holder, perf board, heat gun, ; circa £250? total guess, dig out previuse work on this, likely way forward PoC solder

## Workflow process method
Safty first, 

### Workflow no solder - no shorts, safety humans, safety equipment
* Isnuation, heat shrink all wire joints, krapton tape or heat shrink over individual wires that pass near other components
* Barriers, separate power section and signal section on dev build board, cardboard, acrylic, 3d printed divider, 
* Separate power and signal wires, power wires bundle and other bundles of signal cables, power wires to one side of board signal wires to other side of board
* Trim bare wires flush, avoid wire tails hanging free, bare copper, wire wrap tails,

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

Circuit diagram - Linear power adapter
```
tbc - see relevant sub project 
```

Circuit diagram - Switching power adapter
```
tbc - see relevant sub project
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
* Surface mount device SMD, chips, SOC's, 

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

News Papers - no solder higher current 
* Permanent Solderless Breadboard Example, [WS](https://runtimemicro.com/construction/permanent-solderless-breadboard-projects), 26 July 2016, update 17 December 2025, Runtime Micro
* <todo: consider, find other examples, >

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
* <todo: consider, BoM for V19 @ 1.6A ac/dc conversion, will require different component tollerances due to higher voltage and current requirements >
* <todo: consider, double component purchase, x1 for breadboard RnD, x1 for perboard, >
* <todo: consider, warning / disclaimer, working with mains electricity is extremely dangeouse, mains electricity can cause death or injury or loss of property. These are just notes to self not a recomendation for hobbist/maker projects. Always consider safety first. Comply with local safety regulatons and standards. Do not use this source as a guide it may lead to harm to persons or property and you do so at your own risk. >
* <todo: consider, peronal rider, this is a personal learning source, I am not a qualified electritian or electronics engineer or power engineer or mechanical engineer. Just tryig to learn as a means to better understanding of the world.  Bottom line, you or someone else may die or be permanently injured working with mains electricity and electrical components. There is a risk of; electricution, fire, explosion of component parts, . Safety first, in all instances. >
* <todo: consider, use of power supply unit psu instead of direct mains power for saftey, >

DONE
* <done: consider, intent to commit>
* <todo: consider, reformulate the numbers below based on 1.6A, likely fine but must be done, completed and sufficient head room remained nonetheless after recalculation, >

## Bill of Materials BoM
*  nominal uk 240 VAC, nominal eu 230 VAC, some eu nations 220 VAC, actual variability 207-253 VAC range, 

### BoM V5 @ 1A dc output, circuit components

Assumptions
* After rectification require ~7-8V DC for 5V DC output
* 12 x 1.414 = 16.968 ~17 DC
* 1A / (2 x 100 Hz x 2200 µF) ≈ 2.3V peak to peak, ripple check
* 5V + 2V = 7V dropout requirement
* 15.6V - 2.3V = 13.3V minimum input, above the 7V dropout threshold

Materials
* Transformer, x1, 9V - 12V, drop down transformer
* Diodes, x5, 14000 series (1A), 1N4001 (50V, 1A), 1N4004, 1N4007, x4 for full wave bridge rectifier, x1 for reversed current protection Schottky prefferred over silicon diode
* Capacitors (electrolytic), x2, x1 2200 µF input bulk (smoothing), 100 µF output bulk (transient), bulk energy storage, frequency ripple
* Capacitors (ceramic MLCC), x2, x1 0.33 µF (or 100 nF) input bypass (stability), x1 0.1 µF (or 100 nF) output bypass (high frequency HF), high bypass, regulator stability 
* Voltage regulator (fixed) 78XX, x1 LM7805, V5, 
* Wire, guage tbd

Ignore - workings out, <todo; consider, delete when no longer needed, >
* Capacitors, x4, are 2 220-470uF electrolytic, 2 100nF ceramic disc suitable for uk?

### BoM V19 @ 1.6A dc output, circuit components
* <todo: consider, verify the transformer and rectifier diodes can handle 1.6A withoug overheating, >

Assumptions
* After rectification require ~22-23V DC for 19V DC output
* 18 * 1.414 = 25.452 ~25.5 DC
* 1.6A / (2 x 100 Hz x 4700 µF) ≈ 1.7V peak to peak, ripple check 
* 19V + 2V = 21V dropout requirement
* 24.1V - 1.7V = 22.4V minimum input
* 1.6A / (2 x 100 Hz x 10,000 µF) ≈ 0.8V peak to peak, ripple check, 
* 24.1V - 0.8V = 23.3V minimum input, with ripple drop to 0.8V, more margin

Materials
* Transformer, x1 15V - 18V 2.0A/2.5A, drop down transformer
* Diodes, x5 1N5400 series, 1N5819 (40V, 1A), 1N5822 (40V, 3A), 1N5408 (1000V, 3A), x4 for full wave bridge rectifier, x1 for reversed current protection, SB340 drop in equivalent for 1N5822, SS34 SMC (SMD) version of 1N5822, - what is a freewheeling diode?
* Capacitors (electrolytic), x2, x1 2200 µF/4700 µF 35V rating (or 10,000 µF) input bulk (smoothing), x1 220 µF (or 47 µF) output bulk (transient),  bulk energy storage, frequency ripple
* Capacitors (ceramic MLCC), x2, x1 0.33 µF (or 100 nF) input bypass (stability), x1 0.1 µF (100 nF),  high bypass, regulator stability 
* Voltage regulator (fixed) 78XX, LM7819, 19V if one can be sourced,  or  LM7818, 18V, with diode boost, x2 1N4007 diodes in series between the ground pin and actual ground, less accurate than an adujustable regulator, 
* Wire, guage tbd
* Heatsink, x1, 

## BoM expanded
Additoinal things to consider outside bare bones

Materials
* Voltage regulator (adjustible), LM317, requires a sixth diode place on the ADJ pin, note LM337 is a negative version
* Heatsink, x1, 

## Calculations
* <todo: consider, find source for all the calculation that have to be made.>

Rectified DC = ~1.414 x AC RMS voltage, sqrt(2) ~1.414, peak voltage, <todo: consider, is this capacitor filtered rectifier? true? confirm>

$V_{\text{DC}} \approx \sqrt{2} \times V_{\text{RMS}} \approx V_{\text{peak}}$

Average DC output of an unfiltered full-wave rectifier, <todo: consider, true? confirm>

$V_{\text{DC}} \approx {0.9} \times V_{\text{RMS}}$

Electrical power which becomes heat, P is power, V is voltage, I is current, Power is rate of heat generated in Watts

$P = V \times I$

Total heat produced, where t is time, V is voltage, I is current, P is power, E is energy, E as Energy is total heat in Joules

$E = P \times t = V \times I \times t$

Voltage drop, large heat dissipation for a linear device

$P_(\text{dissipated)} = (V_(\text(in)) \minus V_(\text(out))) \times I_(\text{load})$

$P_(\text{dissipated)} \approx (24V \minus 19V) \times 1.6A =  8W$

Winding Losses, current squared x resistance

$I^{2} \times R$


## Output
* Development and testing environments, 

### Rules, development, testing, 
* Critical Rule: 230VAC stays off board. Never put 230VAC on a breadboard or perfboard. Breadboard contacts are not rated for 230VAC. Breadboard/perfboard, creepage distance is insufficient, shock and fire hazard with loose connection at mains voltage

Two options are
* Critical Rule: 230VAC stays off board. Bench power supply unit PSU, Mains Front End Module. Safest. More contol. 
* Critical Rule: 230VAC stays off board. Bespoke build, Mains Front End Module. Least ripple.

Context diagram - high level galvanic isolation
```
     Mains ----> Front End Module ----> Project Board Module
                 Mains isloation        Project 1, 12VAC (~17V peak), V5 @ 1A, comfortably within breadboard & perfboard voltage limits
                 240VAC or 230VAC       Project 2, 18VAC (~25.5 peak), V19 @ 1.6A, remains within breadboard & perfboard voltage limits
                                        Project N, ...
```

Circuit diagram
* the ascii distorts when displyed in GitHub due to unusual Unicode characters . The ascii below is purposely 'out of alignment' in the raw to try to overcome GitHub rendering distortion of not often used character sets. 
* <todo; consider, find alternative characters to stop rendering distortion, difficult for 45 deg edges, replace diode squares with DN ltters, replace 'mathematical falling/rising diagonal' with forward back slash, replace unicode froun C1 with something else, replace black circle with zero 0 or cap O >
```
                ___________________
                |                 |
                |                 ●
 ~______    ____|               ⟋   ⟍
        )||(               D3 □       □  D1                            _________
 AC     )||(        neg -   ⟋           ⟍   + pos                     |       |
        )||(           ---●               ●----------●---------●-------|IN  OUT|--------●---- + pos ⎓
 ~ _____)||(____       |    ⟍           ⟋        C1 | + pos   | C2    |  GND  |     C3 |           
                |      |   D2 □       □  D4          --        --      |_______|        --           
                |      |        ⟍   ⟋               ⌢         --          |            --          DC
                |      |          ●                  |         |           |            |          
                |______|__________|                  |         |           |            |           
                       |_____________________________●_________●___________●____________●____ - neg ⎓
                                                                                    
    Transformer                Rectifier         Capacitor  Capacitor   Regulator    Capacitor
     Drop down                  Diodes
```


## References

Terms
* AC RMS
* EMS

?
* Galvanic separation
* Power supply unit, bench
* Power supply unit, computer [WP](https://en.wikipedia.org/wiki/Power_supply_unit_(computer))

Tutorials - instructions, 
* AC to DC Conversion, [WS](https://www.instructables.com/AC-to-DC-Conversion/), Instructables, brmarcum
* AC-DC Regulator Kit Instructions, [WS](https://www.mitchelectronics.co.uk/resources/ac-dc-kit-instructions), Mitchel Electronics Ltd
* How to Convert AC to DC [WS](https://www.wikihow.com/Convert-AC-to-DC), wikiHow
* How to Build a DC Linear Power Supply [WS](https://www.build-electronic-circuits.com/linear-power-supply/), 12 July  2023, Omar Muñoz Urias, build electronic circuits
* ...

News Papers - UK, EU mains
* What are the differences between 220VAC, 230VAC and 240VAC Mains Supplies and what voltage equipment should I use? [WS](https://www.se.com/uk/en/faqs/FA144717/)
* Mains voltage in the UK and the EU – and what it means for guitar amps, [WS](https://www.ampworks.co.uk/myth-busters/mains-voltages-in-the-uk-and-the-eu-and-what-it-means-for-guitar-amps/), 8 July 2020, rowan, Keld Ampworks, guitar amps

Symbols
* box drawing, [WS](https://www.w3.org/TR/xml-entity-names/023.html), W3Schools
* box drawing characters, [WP](https://en.wikipedia.org/wiki/Box-drawing_characters)
* geometric shapes, [WP](https://en.wikipedia.org/wiki/Geometric_Shapes_(Unicode_block))
* ascii arrows, [WS](Unicode / ASCII arrows in 8 directions?), Stack Overflow
* dingbats, [WP](https://en.wikipedia.org/wiki/Dingbat)
* Glossary of mathematical symbols [WP](https://en.wikipedia.org/wiki/Glossary_of_mathematical_symbols)
* Miscellaneous Technical [WP](https://en.wikipedia.org/wiki/Miscellaneous_Technical)
* Miscellaneous Symbols A [WP](https://en.wikipedia.org/wiki/Miscellaneous_Mathematical_Symbols-A)
* Miscellanious Symbols B [WP](https://en.wikipedia.org/wiki/Miscellaneous_Mathematical_Symbols-B)
* Arrow Symbols [WP](https://en.wikipedia.org/wiki/Arrow_(symbol))
* Are there unicode symbols for entering basic electrical symbols from multimeter? [WS](https://stackoverflow.com/questions/74578021/are-there-unicode-symbols-for-entering-basic-electrical-symbols-from-multimeter), Stack Overflow

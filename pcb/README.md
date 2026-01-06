# Printed circuit board pcb

Electical circuit, electronic design automation, 

## Status

TODO
* <todo: consider, create hello world pcb, >
* <todo: consider, prerequisit investment in tools start listing as BoM for MVP, source actual items and actual material costs, find supplier('s), wip >
* <todo: consider, circuit board repair, >

DONE
* <done: intent to commit>

## Libraries

Desgin
* EagleCAD
* Fritzing

## Standards

Flamability - electrical devices, ...
* IEC 60695-11-10 
* IEC 60695-11-20 
* ISO 9772 
* ISO 9773
* UL 94, [WS](https://en.wikipedia.org/wiki/UL_94), flamability standard, platics and other products, e.g. UL 94 V-0 highest rating
* UL 1581, electrical; wires, cables, chords, 

## Hardware

### Tools

Solderless, no solder
* Pogo Pin Probe Clip, connect to breakout board header pins, e.g. Pogo Pin Probe Clip - 6 Pins with 2.54mm/0.1" Pitch, 
* Pogo Pin Probe Clip SWD, connect to a PCB with classic 'SWD' pad holes, debug, programming
* Pogo Pins,  

Working surfaces, workbench
* anti static mat, antistat seems to be main UK merchant in non exhuastive search
* magnetic mat, many retailers, Maplins low cost option
* soldering mat, many retailers, Maplins low cost option

Merchants - 
* <todo: find other merchants sources, >
* Antistat, co.uk, UK [WS](https://www.antistat.co.uk/), anti static mats, ...
* Complema, com, FR [WS](https://www.compelma.com/en/emi-shielding-thermal-dissipation/), emi shielding, thermal disipation
* Magnosphere, co.uk, UK [WS](https://www.magnosphere.co.uk/), magnetic mat, magenets, ...

## References

Terms
* Printed Circuit Board [WP](https://en.wikipedia.org/wiki/Printed_circuit_board), aka printed wire board PWB, 
* Electronic design automation, EDA, ECAD, produce layout file
* Printed electrionics, related

PCB - Flamability, see standards above
* Flamability
* Flamability diagram
* Fire test

PCB - protection, longer life, critical failure mitigation, risk mitigation, 
* thermal disipation, 
* emi shielding, 
* ...

PCB - kinds
* Mother board
* Microcontroller
* Single computer board SCB

PCB - manufacture
* Reflow soldering, [WP](https://en.wikipedia.org/wiki/Reflow_soldering)
* Surface mount technology smt, planar mounting
* Surface mount device, integrated circuit
* Printed circuit board milling, isolation milling, from layout file
* Production PCB, pre engineered copper connection pathways acting as wires in circuit, copper laid down in phenolic or fiberglass substrate material, likely from layout file
* via, 
* through hole technology, through hole plating
* ...

PCB - prototyping
* Perf board, [WP](https://en.wikipedia.org/wiki/Perfboard), hobbiest PCB, RAD, PoC, prototyping component connection pathways with wire
* Stripboard, [WP](https://en.wikipedia.org/wiki/Stripboard), veroboard, DIP IC's, solder
* Breadboard, no solder
* Terminal strip, barrier strip, terminal block, no solder
* Wire wrapping, no solder, light guage tightly wound for mechancial end electrical bonding, 
* Pogo-pin clamps, no solder, 
* Programming test clip, no solder, 

PCB - component kinds, materials
* component kind, resistor
* component kind, capacitor
* component kind, integrated circuit
* component kind, wire
* component kind, electrical connector, [WP](https://en.wikipedia.org/wiki/Electrical_connector)
* ...

Kind - electrical connector
* JST connector, [WP](https://en.wikipedia.org/wiki/JST_connector), com [WS](https://www.jst-mfg.com/product/) 
* Jumper, [WP](https://en.wikipedia.org/wiki/Jumper_(computing)), 
* Jumper block , 
* Jumper shunt, 
* SPDT (Single Pole Double Throw) switch, jumper

Kind - of what? semiconductor, superconductor
* Field effect transistors FETs
* Metal oxide semiconductor field effect transistor MOSFETs, 
* Tunnel field effect transistors TFETs, see Silicene, 

Kind - of chip, integrated circuit in silicon
* Bridge chip, e.g. USB to UART, ...

Kind? - semiconductor device - diode, transistor, ...
* kind, diode
* kind, transistor
* Schottky diode, [WP](https://en.wikipedia.org/wiki/Schottky_diode)
* Shockley diode, 
* p-n diode, 

Periodic table
* copper
* silicon, semiconductor, integrated circuits, solar cells, 
* lead, soldering
* ...

News Papers - components
* How To Identify Components on Printed Circuit Boards, [WS](https://www.axcontrol.com/blog/2021/how-to-identify-components-on-printed-circuit-boards/06/07/), 2021 July 06, AX Control, Inc.

News Papers - jumpers
* FAQ: What can Printed Circuit Board (PCB) jumpers do?, [WS](https://www.componentscorp.com/pcb-jumpers-faq.html), 2016 February 29, 
* Navigating the Challenges of Jumper Wire Work, [WS](https://www.circuitrework.com/blogs/165.html), Circuit Technology Centre, 
* What is a PCB Jumper in a Circuit Board?, [WS](https://www.fscircuits.com/pcb-jumper/), FS Circuits, 
* ...

News Papers - soldering
* Introduction to Soldering Wires on Circuit Boards, [WS](https://morepcb.com/how-to-solder-wire-on-circuit-board/), MorePCB, 
* ...
* ...

News Papers - solderless, no solder
* Who Needs Pin Headers?, [WS](https://hackaday.com/2021/08/12/who-needs-pin-headers/), Hackaday, chris lott, 2021
* Review: Hammer-Installed Solderless Raspberry Pi Pin Headers, [WS](https://hackaday.com/2017/01/16/review-hammer-installed-solderless-raspberry-pi-pin-headers/), Hackaday, Jenny List, 2017
* Is there such a thing as a pin (or pogo pin) clamp for testing?, [WS](https://electronics.stackexchange.com/questions/163550/is-there-such-a-thing-as-a-pin-or-pogo-pin-clamp-for-testing), StackExchange, Electrical Engineering
* Identification of SWD header for footprint, [WS](https://electronics.stackexchange.com/questions/491487/identification-of-swd-header-for-footprint), StackExchange, Electrical Engineering, 2020?

News Papers - prototyping
* Building Resistor Circuits Using Breadboards, Perfboards, and Terminal Strips, [WS](https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/building-simple-resistor-circuits/), All About Electrontics, 

News Paper - cables, beadboard power supply, 
* USB Cable to Breadboard Power Supply Using a Power Bank, [WS](https://www.instructables.com/USB-Cable-to-Breadboard-Power-Supply-Using-a-Power/), TheLeftyMaker, Instructables, 
* Power Your Breadboard With USB, [WS](https://www.instructables.com/Power-your-breadboard-with-USB/), janw, Instructables


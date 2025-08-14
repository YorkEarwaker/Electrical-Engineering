# Personal computing electrical engnineering pcee

Electrical engineering with a laptop or desktop or similar. Interconnection between PC (connector comms host) and diverse hardware devices and systems.

## Notes

Rationale - Two different use cases emerging
* create a pc on a breadboard
* get a pc to interact with breadboard

Question
* Is this reinventing the microcontroller?

PC direct to breadboard
* PC to breadboard power supply, i.e. via connector 'plug' power adaptor
* PC to breadboard comms, i.e. I2C, UART, SPI, GPIO? ...

Access from personal computer PC to breadboard BB by adaptor examples
* USB tranceiver to USB breadboard adapter. 
* UART port with USB to UART converter chip adapter. FTDI FT232RL USB to serial IC
* ...

## Status
TODO
* <todo: consider, BreadBoarding with MS Windows, .exe on Windows interacts with devices attached to breadboard, via USB? >
* <todo: consider, construct a PC on a breadboard, >

DONE
* <done: intent to commit>

## Libs

MS Win 10/11
* ... <todo: find the magic code base, >

## Hardware

To consider using
* Micro-USB Breakout - Horizontal, [WS](https://thepihut.com/products/micro-usb-breakout-horizontal), The Pi Hut, use with Pogo clip?
* ...

## References

Terms
* COM port
* Virtual COM port (VCP) , 

move elsewhere
* Field Programmable Gate Array FPGA 
* DIP, Dual in-line package, [WP](https://en.wikipedia.org/wiki/Dual_in-line_package)
* small outline integreated cicuit SOIC
* plastic leaded chip carrier PLCC
* surface mount technology SMT 

MacOsX
* LapTop BreadBoarding, [WS](https://www.instructables.com/LapTop-BreadBoarding/), instructables, By dsauer in Living>Music

MSWin
* ...

News Papers - get pc to interact with a breadboard
* Can I program a Breadboard with a laptop? [WS](https://electronics.stackexchange.com/questions/360521/can-i-program-a-breadboard-with-a-laptop), Mar 8, 2018 
* How can I easily connect to my breadboard circuit using USB? [WS](https://electronics.stackexchange.com/questions/34281/how-can-i-easily-connect-to-my-breadboard-circuit-using-usb/34285), Jun 21, 2012 
* PC controlled Breadboard, [WS](https://forum.allaboutcircuits.com/threads/pc-controlled-breadboard.49481/), 

News Papers - create a pc on a breadboard
* 8-bit Breadboard Computer [WS](https://www.instructables.com/8-bit-Breadboard-Computer/), instructables, GilDev in CircuitsElectronics
* ... several others to consider, 

News Pappers - I2C
* https://electronics.stackexchange.com/questions/39244/what-is-the-simplest-way-to-interact-with-an-i2c-peripheral
* Bus Pirate I2C http://dangerousprototypes.com/docs/I2C
* https://superuser.com/questions/1578355/how-to-communicate-over-i2c-in-windows

Hardware - examples, retail COTS connector 
* Breadboard Prototype Adapters, [WS](https://www.winford.com/products/cat_pbc.php), 
* SparkFun FTDI Basic Breakout - 5V, [WS](https://www.sparkfun.com/sparkfun-ftdi-basic-breakout-5v.html), see similar items on page, 
* FTDI VCP drivers, [WS](https://ftdichip.com/drivers/vcp-drivers/), ...
* SUB-20 Multi Interface USB Adapter [WS](http://www.xdimax.com/sub20/sub20.html), USB-I2C, USB-SPI, USB-GPIO, RS232, RS485, MDIO, Ir, LCD, PWM
* UMFT201XA-02, Development Module, FT201XQ, USB to I2C, Interface [WS](https://uk.farnell.com/ftdi/umft201xa-02/development-module-usb-to-i2c/dp/4048086)
* Mouser, list of, Interface development tools, USB to I2C, [WS](https://www.mouser.co.uk/c/embedded-solutions/engineering-tools/analog-digital-ic-development-tools/interface-development-tools/?type=USB%20to%20I2C)
* FT201XQ, USB Full Speed to I2C IC with USB Charger Detection, QFN-16 [WS](https://ftdichip.com/products/ft201xq/)
* USB I2C Click, [WS](https://www.mikroe.com/usb-i2c-click), USB to I2C/UART

Hardware - pcb design
* https://github.com/harbaum/I2C-Tiny-USB

Hardware - example, DIP, 
* SOIC-To-DIP Breadboard Adapters, 

Software - MS, discovery, move to libs when solid solution found? 
* An overview of Windows for IoT, [WS](https://learn.microsoft.com/en-gb/windows/iot/product-family/windows-iot)
* Inter-Integrated Circuit (I2C) sample, [WS](https://learn.microsoft.com/en-us/samples/microsoft/windows-universal-samples/iot-i2c/), 06/21/2023
* Human Interface Devices HID, over I2C, [WS](https://learn.microsoft.com/en-us/windows-hardware/drivers/hid/hid-over-i2c-guide)
* Skeleton I2C Sample Driver, [WS](https://learn.microsoft.com/en-us/samples/microsoft/windows-driver-samples/skeleton-i2c-sample-driver/), 07/02/2024
* Windows-universal-samples/Samples/IoT-I2C/ [GH](https://github.com/microsoft/Windows-universal-samples/blob/main/Samples/IoT-I2C/)



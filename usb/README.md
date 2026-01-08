# Universal serial bus usb

Inter device communication at a local systems level.

## Notes

See concerns on USB Device Number count issue here, possible Linux kernel defect
* Raspberry Pi Pico USB disconnect issue on Linux, [WS](https://forums.raspberrypi.com/viewtopic.php?t=394718), Raspberry Pi Forum, 

## Status

### TODO
* <todo: consider, what are the minimum requirements to start development, >
* <todo: consider, as a real world project, serial communication with a RPi Zero as 'headless' >
* <todo: consider, ethenet over usb, use RPi Zero as test bed, does RPi Zero have contraits that would disallow this? >
* <todo: consider, experiment, plug and unplug the same usb flash disk, thumb drive, to see if Device Number increments, see if unmounting before unplugging changes Device Number count, that is decriments devnum >

### DONE
* <done: consider, intent to commit>

## Software

ARM IDE's - move to embedded?
* ARM, developer, com, [WS](https://developer.arm.com/)
* Kiel MDK, com, [WS](https://www.arm.com/products/development-tools/embedded-and-software/keil-mdk), ARM, products, MCU software development, embedded, 
* <todo: list other ARM tools for development, >
* Kiel MDK, com, [WS](https://www.keil.arm.com/), Kiel, ARM, VS Code extension, 
* ...


## References

Terms
* Serial Communication, 
* Ethernet over USB, [WP](https://en.wikipedia.org/wiki/Ethernet_over_USB)

Hardware - plug and cable standards
* Universal Serial Bus USB, org, [WS](https://www.usb.org/), USB Implementers Forum, Inc., USB specifications, 
* USB Communication Device Class CDC (NCM), [WP](https://en.wikipedia.org/wiki/USB_communications_device_class)
* USB CDC list, [WP](https://en.wikipedia.org/wiki/USB#Device_classes)
* ... 

Serial Standards - controller GPIO pins to target (peripheral device) GPIO pins, GPIO to USB, chipset to motherboard bus, 
* Note, Yes Y No N, High H Medium M Low L, 
* Inter-Integrated Circuit I2C, OSI model; physical layer (Y, H), data link layer (Y, M), . embedded systems, also PC's, 
* Mircowire, μWire, subset of SPI, half duplex, MicrowirePlus full duplex, 
* System Management Bus SMBus, OSI model; physical layer (Y, H), data link layer (Y, H), .stricter variant of I2C, use in PC bus, 
* Serial Peripheral Interface SPI, OSI model; physical layer (Y, H), data link layer (Y, L), . full duplex, 
* Universal Asynchronous Receiver Transmitter UART, [WP](https://en.wikipedia.org/wiki/USB_communications_device_class), OSI model; physical layer (N, _), data link layer (Y, H), . chips may be; UART, dual UART DUART, quadruple UART QUART, octal UART OCTART, ... others? 
* Universal Synchronous Asynchronous Receiver Transmitter USART
* ...

Hardware other - USB to other hardware connector
* Controller Area Network CAN, automotive 
* FireWire, 
* JTAG, testing, 
* Low Voltage Differential Signaling LVDS
* RS 232
* RS 422 , of particular interest?
* RS 485, UART based, 
* ...

Documentation
* Linux USB API, [WS](https://www.kernel.org/doc/html/v4.14/driver-api/usb/index.html), The Linux Kernel, 

Ethernet over USB
* How to set up an usb/ethernet interface in Linux? [WS](https://unix.stackexchange.com/questions/386162/how-to-set-up-an-usb-ethernet-interface-in-linux)

Microwire
* National Semiconductor Microwire frame format, [WS](https://developer.arm.com/documentation/ddi0194/h/functional-overview/primecell-ssp-operation/national-semiconductor-microwire-frame-format), ARM, 

UART
* Lesson 9: UART, [WS](http://www.simplyembedded.org/tutorials/msp430-uart/), Simply Embedded, 

# Raspberry Pi Pico rpi-pi

Microcontroller, IoT, physical computing

## Status

TODO
* <todo: consider, preparetory work for Climate-Model \amn project PoC, >
* <todo: consider, wifi connection to RPi Pico 2 W , see datasheet below, >
* <todo: consider, bluetooth project, RPi Pico >
* <todo: consider, try both MicroPython and C/C++ versions, can a Pico flashed with MPY execute c/c++ code too? >
* <todo: consider, research Core 0 core0 Core 1 core1 RPi Pico ARM chip, threading, asysnc, two executables running at the same time one on each core, one executable accessing both cores, >
* <todo: consider, testing the sku 19328 RPi Pico M micorcontroller product included in the Waveshare MicroPython learning kit, supplied by The Pi Hut, This microcontroller is not a W wireless, manufactured in CN, part of Waveshare Micropython Learning Kit, >
* <todo: consider, purchase one RPi Pico with debug connector already onboard the microcontroller, so as not to have to solder one on. 18/04/2025 difficulty sourcing Pico with onbaord debug connector,>
* <todo: consider, fritzing diagrams for cicuit board designs, start with current solutions uploaded to GitHub, >

DONE
* <done: intent to commit>
* <done: consider, \cpp or \cee dirctory for c++ and standard c code, likely seperate sub projects, C and Cpp and assembly \cpa, C and C++ and ASM \cpa >
* <done: consider, as it appears Micropython only allows access to a single core of RPi Pico Arm chip, C/C++ allows access to both cores of RPi Pico Arm chip, confirm this is the case! likely both core can be used by use of threading? Also MicroPython and C/C++ SDK side by side might be possible, call C/C++ SDK from MicroPython? conclusion difficult to do, but not impossible, likely future versions of RPi Pico N will make this easier, There may be a CircuitPython work around but also not clear on longevity of CircuitPython fork, >
* <done: consider, secondary languages on RPi Pico, two core languages MicroPython for DEV/QA and RAD and PoC, C/C++/asm for PROD and MVP, secondary languages only for specific use case where mpy and cpa won't work, concentrate on RPi and Ubuntu ecosystem,  >
* <done: consider, source pico-jvm for java project on RPi Pico, does on exist? would it be worth the effort? probably not worth the effort at this point, wait for market to mature further, Oracle or Eclipse Foundation focus on IoT and embedded systems, RPi ecosystem, Ubuntu ecosystem, >
* <done: consider, purchase a few more, one or two or three, additional RPi Pico breadboards, Allows for multiple cicuit design and testing with different versions of the RPi Pico microcontrollers, purchased 17/04/2025 1xfull size 1xhalf size bradboard, >
* <done: consider, purchase one or two more RPi Pico 2 W to run parallel projects with different tool sets mpy and cpa in parallel; wifi, bluethooth, assorted sensors, . To allow for incremental change to circuit design, to allow for identical circuit design in mpy and cpa, ... dev, qa, prod, 1xRPi Pico 2 W, battery holder, >

## Libraries

Languages - primary
* C/C++/asm, Note_02
* CircuitPython, Ardfruit specific, 
* MicroPython, microcontroller agnostic, Note_01

Languages - secondary 
* Arduino?, C like, 
* Java?, pico-jvm?
* Rust?
* Basic?
* Javascript? 
* ...

IDE
* Thonny [WS](https://thonny.org/), Python IDE for beginners, MicroPython, Note_01
* VSCode, C/C++/asm, MicroPython, works
* VSCodium, C/C++/asm, MicroPython, evaluating for C/C++/asm for PRi Pico 2, Note_02
* Arduino, [WS](https://www.arduino.cc/en/software), C/C++/Arduino, does not appear to support RP2030 i.e. RPi Pico 2, only RP2040 i.e. RPi Pico 1, uninstalled for now.

Tools
* PuTTY, 0rg [WS](https://www.putty.org/), download [WS](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), use as serial monitor for RPi Pico 2 device, USB COM output, 

Libs
* libusb, [WS](https://libusb.info/), cross-platform user library to access USB devices, C lib, Note_02

Note
* Note_01, recommended by Raspberry Pi Pico, Getting Started Guide, The Pi Hut, see link below
* Note_02, recommended by Raspberry Pi Pico, Getting started with Raspberry Pi Pico-series C/C++ development with Raspberry Pi Pico-series and other Raspberry Pi microcontroller-based boards

## References

Getting started stuff - 101
* Raspberry Pi Pico, MicroPython Learning Kit (Pico Included) [WS](https://thepihut.com/products/raspberry-pi-pico-micropython-learning-kit-pico-included), The Pi Hut, 
* Raspberry Pi Pico, Getting Started Guide, [WS](https://thepihut.com/blogs/raspberry-pi-tutorials/raspberry-pi-pico-getting-started-guide), 19 Dec 2022, The Pi Hut
* Raspberry Pi Pico, Pinout [PDF](https://cdn.shopify.com/s/files/1/0176/3274/files/Pico-R3-A4-Pinout_f22e6644-b3e4-4997-a192-961c55fc8cae.pdf?v=1664490511), full fat pinout
* Raspberry Pi Pico, Pinout [WS](https://cdn.shopify.com/s/files/1/0176/3274/files/simplified_pico_pinout.jpg), simplified pico pinout
* Micropython, [WS](https://www.waveshare.com/wiki/File:Raspberry_Pi_Pico_MicroPython_Demo_Code.7z), Waveshare, for kit, code samples, 

MicroPython
* MicroPython, RPi Pico, bootsel, docs [WS](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython), Drag-and-Drop MicroPython
* MicroPython, RPi Pico, bootsel, [WS](https://micropython.org/download/RPI_PICO/), Flashing via UF2 bootloader, 
* MicroPython, [WS](https://github.com/micropython/micropython), 
* MicroPython, RP2 port, [WS](https://github.com/micropython/micropython/tree/master/ports/rp2)
* ...

Books
* Get Started with MicroPython on Raspberry Pi Pico, 2nd Edition, [GH](https://github.com/raspberrypipress/gsw-micropython-on-raspberry-pi-pico-2e),
* See also, C and Cpp and ASM cpa, in RPi Pico directory structure, for books C/C++/asm books, 

Documentation
* Raspberry Pi, docs [WS](https://www.raspberrypi.com/documentation/)
* Raspberry Pi, tutorials [WS](https://www.raspberrypi.com/tutorials/)
* Raspberry Pi, datasheets [WS](https://datasheets.raspberrypi.com/)
* Raspberry Pi, forums [WS](https://forums.raspberrypi.com/)

Datasheet - Raspberry Pi Pico
* Raspberry Pi Pico, datasheet [PDF](https://datasheets.raspberrypi.com/picow/pico-2-w-datasheet.pdf), Raspberry Pi Pico 2 W Datasheet, schematics, power, pinout, 
* Raspberry Pi Pico, datasheet [PDF](https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf), RP2350 Datasheet
* Raspberry Pi Pico, datasheet [PDF](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf), Getting started with Raspberry Pi Pico-series C/C++ development with Raspberry Pi Pico-series and other Raspberry Pi microcontroller-based boards
* Raspberry Pi Pico, datasheet [PDF](https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf), Connecting to the Internet with Raspberry Pi Pico W-series. Getting online with C/C++ or MicroPython on W-series devices.

Datasheet - Component parts of RPi Pico
* CYW43439 [WS](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-4-802.11n/cyw43439/), Single-band Wi-Fi 4 (802.11n) + Bluetooth® 5.4 combo

News Papers - wireless, wifi <todo: move to separate directory structure for sbc RPi 5/4, >
* Host a Wi-Fi hotspot with a Raspberry Pi, [WS](https://www.raspberrypi.com/tutorials/host-a-hotel-wifi-hotspot/), 
* ...

News Papers - antenna, wireless, wifi, bluetooth, 
* Raspberry Pi Pico W - how to connect an external antenna, [WS](https://raspberrypi.stackexchange.com/questions/141136/raspberry-pi-pico-w-how-to-connect-an-external-antenna), Raspbery Pi, StackExchange, 
* Can I add external anthena on pi pico w? The two screw mount holes are actually plated and connected to the anthena., [WS](https://www.reddit.com/r/raspberrypipico/comments/12ifx14/can_i_add_external_anthena_on_pi_pico_w_the_two/), reddit, Raspberry Pi Pico
* Pi Pico W external antenna, [WS](https://forums.raspberrypi.com/viewtopic.php?t=348928), Raspberry Pi, forums, 
* ...

News Papers - MicroPython and C/C++ SDK side by side on RPi Pico 
* Possible to run MicroPython on one core and C SDK code on the other?, [WS](https://forums.raspberrypi.com/viewtopic.php?t=325167), Raspberry Pi, forums, yes?

New Papers - daisy chain breadboards, power supply, 
* Voltage is reduced across chained breadboards, [WS](https://electronics.stackexchange.com/questions/85599/voltage-is-reduced-across-chained-breadboards), 

News Papers - power pico
* How to Power the Raspberry Pi Pico? 6 Different ways, [WS](https://randomnerdtutorials.com/power-raspberry-pi-pico-6-different-ways/), Random Tutorials, 

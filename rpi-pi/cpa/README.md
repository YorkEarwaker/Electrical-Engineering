# C and Cpp and ASM cpa 

RPi Pico SDK, C and C++ and ARM assembly language, RPi Pico 2 W 

## Notes

Use one of the recommneded IDE's for fast initial C/Cpp interaction with Pico series.
* Getting started with Raspberry Pi Pico-series C/C++ development with Raspberry Pi Pico-series and otherRaspberry Pi microcontroller-based boards. 2 0 2 4 - 1 0 - 1 5 : 2 b 6 0 1 8 e - c l e a 

Windows tool chain - low level understanding of dependencies
* Install Git for Windows, allows use of Git bash env, user@DESKTOP-PERD8MS MINGW64 ~
* Manually Configure your Environment, Appendix C: Manual toolchain setup, Getting started with Raspberry Pi Pico-series C/C++ development with Raspberry Pi Pico-series and otherRaspberry Pi microcontroller-based boards. 2 0 2 4 - 1 0 - 1 5 : 2 b 6 0 1 8 e - c l e a 

## Status

TODO
* <todo: consider, wifi connection to internet, >
* <todo: consider, wifi connection to laptop, >

DONE
* <done: intent to commit>
* <done: consider, evaluation, install VSCodium for SDK \cpa projets, wip >
* <done: consider, evaluation, VSCodium extension Raspberry Pi Pico for SDK \cpa development >
* <done: consider, hello world, attempt to replicate MicroPython \hwd examples with SDK?  success, >
* <done: consider, C/C++ book for raspberry pi pico , ARM chips, source, see I/O Press, >
* <done: consider, contact I/O Press for publication date, Master the Raspberry Pi Pico, Harry Fairhead, email sent 14/04/2025, response from I/O Press, first edition in print, second edition unclear at this point but possible in 2026? >
* <done: consider, purchase of Programming The Raspberry Pi Pico/W In C, Second Edition, find reveiws, paperback circa £36.00, I/O Press, response from I/O Press, wait till june/july 2025 when third edition is expected out. >

## Libraries
<todo: where is Eclipse in all of this? >

Languages
* Assembly language asm, [WP](https://en.wikipedia.org/wiki/Assembly_language) 
* C, 
* Cpp, 

Build tools - meta build tools
* CMake, CMakeLists.txt files, used by Bosch for BMV080 SDK, for Raspberry Pi things, but Pico seems excluded
* PlatformIO, docs, [WS](https://docs.platformio.org/en/latest/integration/ide/pioide.html), extension for VSCode, for CLion experimental, used by Bosch for BMV080 SDK, not for Raspberry Pi though, Python CLI, install into Python venv or similar, build system for C/C++ code stack, 
* ...

Build tools - native build tools, generators, command runners
* Ninja

Rpi SDK
* Raspberry Pi, Microcontrollers, The C/C++ SDK, [GH](https://github.com/raspberrypi/pico-sdk) [WS](https://www.raspberrypi.com/documentation/microcontrollers/c_sdk.html)
* Getting started with Raspberry Pi Pico-series C/C++ development with Raspberry Pi Pico-series and other Raspberry Pi microcontroller-based boards. 2 0 2 4 - 1 0 - 1 5 : 2 b 6 0 1 8 e - c l e a  [PDF](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)
* Raspberry Pi Pico-series C/C++ SDK Libraries and tools for C/C++ development on Raspberry Pi microcontrollers. [PDF](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf)
* RP2350 Datasheet a microcontroller by Raspberry Pi [PDF](https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf)
* 

IDE/Code editor
* CLion, <todo: assess CLion as IDE, >
* PlatformIO, [WS](https://docs.platformio.org/en/latest/what-is-platformio.html), VSCode, written in Python, 
* Raspberry Pi Pico, extension, VSCode, VSCodium
* VSCodium, [GH](https://github.com/VSCodium), com [WS](https://vscodium.com/) FOSS, VSCode binaries with no telemetry to Microsoft, see Note_01, evaluation for C/C++/asm RPi Pico, wip
* VSCode, Microsoft, see Note_01, ongoing RAD for Python and Java 

Notes
* Note_01, as recomended by Raspberry Pi Pico, datasheet, Getting started with Raspberry Pi Pico-series C/C++ development with Raspberry Pi Pico-series and other Raspberry Pi microcontroller-based boards, datasheet see below

## References

Documentation
* Pico C, SDK, [WS](https://www.raspberrypi.com/documentation/pico-sdk/), C and C++, 
* Pico C, SDK, Examples, [GH](https://github.com/raspberrypi/pico-examples), docs [WS](https://www.raspberrypi.com/documentation/pico-sdk/examples_page.html#examples_page), Raspberry Pi Pico, code samples, example code, 
* ...

Datasheet
* Raspberry Pi Pico, datasheet [PDF](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf), Getting started with Raspberry Pi Pico-series C/C++ development with Raspberry Pi Pico-series and other Raspberry Pi microcontroller-based boards
* Raspberry Pi Pico, datasheet [PDF](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf), Raspberry Pi Pico-series C/C++ SDK Libraries and tools for C/C++ development on Raspberry Pi microcontrollers. 
* ...
* ...

News Papers - IDE/Code editor
* VSCode or VSCodium; Which do you use?, [WS](https://www.reddit.com/r/learnprogramming/comments/u2m5di/vscode_or_vscodium_which_do_you_use/)
* VS Code vs VS Codium: What's the Difference? [WS](https://itsfoss.com/vs-code-vs-codium/)
* ...

Books
* Programming The Raspberry Pi Pico/W In C, Second Edition, [WS](https://www.iopress.info/index.php/books/pico/programming-the-raspberry-pi-pico-w-in-c-2ed), Harry Fairhead, (Paperback), I/O Press, <todo: more research! > circa £36.00 
* Master the Raspberry Pi Pico in C: WiFi with lwIP & mbedtls [WS](https://www.iopress.info/index.php/books/pico/master-the-raspberry-pi-pico-in-c-wifi-with-lwip-mbedtls), Harry Fairhead, in print, I/O Press, circa £30.00

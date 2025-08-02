# Rust rst

Is this a good idea? Doin' stuff with RPi Pico in the Rust programming language.


## Status

TODO
* <todo: consider, a first simple project to understand this space better, evaluate need, tools, ecosystem, >
* <todo: consider, What does rust have to offer that cannot be done with MicroPython or C/C++/asm ? >
* <todo: consider, That is what is the value proposition? MVP but not PoC? >
* <todo: consider, what are the down sides? >
* <todo: consider, does the particulat matter aerosol /snr-rsl project offer a good opportunity to create first Rust project, or would it be too complex, or is Rust for RPi and Pico not yet mature/rich enough? >
* <todo: consider, hello world /hwd project for Rust on RPi Pico, >

DONE
* <done: intent to commit,>

## Libraries

Languages
* Rust, [WS](https://www.rust-lang.org/), fast, low resource, no runtime, no carbage collection, typed, compiled, embedded part of roadmap, binary executable deployment,  

IDE
* First class editor support, [WS](https://www.rust-lang.org/tools), Rust recomended IDE list

Tools
* rustup, [WS](https://rustup.rs/), rust installer for dev PC, manage rust installs on dev env

Libs
* rp-rs, [GH](https://github.com/rp-rs), Rust on the RP series of microcontrollers. 
* embassy-rs, [GH](https://github.com/embassy-rs), dev [WS](https://embassy.dev/), Rust async for embedded
* Rust Embedded, [GH](https://github.com/rust-embedded), org [WS](https://www.rust-lang.org/governance/wgs/embedded), Enabling usage of Rust on Embedded Platforms (Embedded Linux / RTOS / Bare Metal)
* rp-hal, [GH](https://github.com/rp-rs/rp-hal), Rust support for the "Raspberry Silicon" family of microcontrollers
* crates, rp2040-hal v0.11.0 [WS](https://crates.io/crates/rp2040-hal), A Rust Embedded-HAL impl for the rp2040 microcontroller #embedded #embedded-hal #hal #raspberry-pi #rp2040
* crates, rp-hal-common v0.1.0 [WS](https://crates.io/crates/rp-hal-common), Shared HAL code for the Raspberry Pi microcontrollers, Code and types useful to both rp2040-hal and rp235x-hal.

## References

Terms - hardware
* Hardware Abstraction Layer, HAL, 
* Single Cycle IO, SIO, 

Terms - rust
* Executable and Linkable File, ElF, elf2uf2
* Board Support Package BSP, 
* Toms Obvious Markup Language TOML, markup language used by Rust, rust project meta configuration, 

News Papers - rust projects, RPi Pico
* Controlling an Output: Programming a Raspberry Pi Pico with Rust, [WS](https://www.alexdwilson.dev/learning-in-public/controlling-an-output-how-to-program-a-raspberry-pi-pico-in-rust), 18 Januray? 2025?, Alex Wilson, hardware abstraction layer HAL, 
* Quick Start: How to Program a Raspberry Pi Pico in Rust, [WS](https://www.alexdwilson.dev/learning-in-public/how-to-program-a-raspberry-pi-pico), 17 Januray 2025?, Alex Wilson
* Rust on RP2350, [WS](https://www.raspberrypi.com/news/rust-on-rp2350/), 6 Sep 2024, Ashley Whittaker, News, Raspberry Pi, 





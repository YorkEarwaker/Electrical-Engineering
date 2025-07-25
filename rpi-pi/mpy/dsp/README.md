# Display dsp (mpy)

Display things on a screen, wired to RPi Pico using I2C and SPI interfaces, 

## Status

TODO
* <todo: consider, oled display, wired on breadboard to RPi Pico, discovery, understaing ecosystm, >
* <todo: consider, BME280 temperature readings to screen in QA environment QA1, both LCD screen and BME sensor are use I2C work around is have each be on seperate bus, BME280 on bus 1 and LCD on bus 0, LCD bus 0 probably simplest work around for now,  >
* <todo: consider, there are still issues to fully understand with Hatch build options in pyproject.toml, further research necessary, >
* <todo: consider, refactor LCD1602 dirver so that it is passed an I2C object as argument, currently the driver has a hard coded option internal, allow bus variability 0 or 1 allow GPIO pin variability allow frequence variablity, instead of all being hard coded values, allow daisy chaining of LCD driver with other I2C devices on same contraller with same GPIO pins>
* <todo: consider, after LCD1602 driver refatord to take an i2c controller as argument daisy chain BME280 and LCD screen, as test, >

DONE
* <done: intent to commit>
* <done: consider, lcd dispaly, wired on breadboard to RPi Pico, discovery , understaing ecosystm, driver and code as use cases, driver completed needs testing, >
* <done: consider, lcd dispaly, wired on breadboard to RPi Pico, discovery , understaing ecosystm, initial user testing to be code as use case, 'Hello, World!' to screen, success, >
* <done: consider, DHT22 temperature readings to screen in development environment DE1, >
* <done: consider, build distribution archive for use in Thonny IDE, as step toward systems testing in QA environment QA1, which build tool used: Hatch, >

## Output

### build package distribution
<info: successful build distribtuion package with Hatch for to import driver 'dsp_lcd1602_dvr.py' into QA1 env. >
```
(venv) C:\Users\yorke\Documents\dev\repo\electrical-engineering\rpi-pi\mpy\dsp>hatch build
──────────────────────────────────────────────────────── sdist ────────────────────────────────────────────────────────
dist\display_org_agw_een_dsp-0.0.1.tar.gz
──────────────────────────────────────────────────────── wheel ────────────────────────────────────────────────────────
dist\display_org_agw_een_dsp-0.0.1-py3-none-any.whl

(venv) C:\Users\yorke\Documents\dev\repo\electrical-engineering\rpi-pi\mpy\dsp>
```

### test package distribution
<info: successful run of script 'dsp_lcd1602_hwd.py' to display Hello World on LCD screen in QA1 env after importing 
       display_org_agw_een_dsp-0.0.1-py3-none-any.whl in Thonny IDE.  >
```
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
display_i2c: I2C(1, freq=400000, scl=7, sda=6, timeout=50000)
display_i2c.scan() address list: [62, 96, 112]
>>> 
```

### integrate LCD and DHT22 readings

Success in DE1 dev env. Only LCD screen device on I2C bus 1. Successully display temperature and humidity and air pressure readings from DHT22 on LCD screen.

### integrate LCD and BME280 readings

Failure in QA1 env. Two devices on I2C bus 1; LCD screen and BME280 sensor. Both work independently but require disconnect of USB cable power down of RPi Pico for respective successful run.
* <todo: consider, troubleshoot two devices on same I2C bus, likely an I2C conflict issue. >
* <todo: consider, addressing issue on I2C, >
* <todo: consider, rebuild bme280 package distribution in Hatch, current versoin is pd was built in PMD, likely correlation not causation, >


## Hardware

LCD
* LCD1602 RGB backlight character LCD, Waveshare, [WS](https://www.waveshare.com/LCD1602-RGB-Module.htm), Waveshare wiki [WS](https://www.waveshare.com/wiki/LCD1602_RGB_Module), datasheet [PDF](https://www.waveshare.com/w/upload/2/2e/LCD1602_RGB_Module.pdf), 16x2 characters LCD, RGB Backlight, 3.3V/5V, I2C bususing I2C bus to display text or adjust RGB backlight, (Raspberry Pi/Jetson Nano/Arduino examples)
* 1.3" IPS LCD Display Module (240x240), The Pi Hut [WS](https://thepihut.com/products/1-3-ips-lcd-display-module-240x240), Waveshare wiki, [WS](https://www.waveshare.com/wiki/1.3inch_LCD_Module), 
* <todo: other tbd evaluation, >

OLED
* tbd

## References

Terms
* I2C, I2C Bus org [WS](https://www.i2c-bus.org/), 
* SPI

Books
* Get Started with MicroPython on Raspberry Pi Pico, The Official Raspberry Pi Pico Guide, Gareth Halfacree, Ben Everard, 2nd Edition, Chapter 10 Digital Communication Protocols: I2C and SPI
* Raspberry Pi Pico Tips and Tricks, Inter-Integrated Circuit I2C, [WS](https://leanpub.com/rpitandt/read#leanpub-auto-inter-integrated-circuit-i2c), Last updated on 2024-03-02, Malcolm Maclean, Learnpub, retrieved 2025-07-25, 

Datasheets
* ...

News Papers - LCD dispaly
* Raspberry Pi Pico with I2C LCD Display (MicroPython), [WS](https://randomnerdtutorials.com/raspberry-pi-pico-i2c-lcd-display-micropython/), Randomtutorials, 

News Papers - I2C
* Using I2C devices with Raspberry PI Pico and MicroPython, [WS](https://peppe8o.com/using-i2c-devices-with-raspberry-pi-pico-and-micropython/), Last Updated on 19th April 2024, peppe8o


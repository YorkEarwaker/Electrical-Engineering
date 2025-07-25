# Display dsp (mpy)

Display things on a screen, wired to RPi Pico using I2C and SPI interfaces, 

## Status

TODO
* <todo: consider, oled display, wired on breadboard to RPi Pico, discovery, understaing ecosystm, >
* <todo: consider, there are still issues to fully understand with Hatch build options in pyproject.toml, further research necessary, >
* <todo: consider, refactor LCD1602 dirver so that it is passed an I2C object as argument, currently the driver has a hard coded option internal, allow bus variability 0 or 1 allow GPIO pin variability allow frequence variablity, instead of all being hard coded values, allow daisy chaining of LCD driver with other I2C devices on same contraller with same GPIO pins>
* <todo: consider, after LCD1602 driver refatord to take an i2c controller as argument daisy chain BME280 and LCD screen, as test, >
* <todo: consider, rebuild bme280 package distribution in Hatch, current versoin is pd was built in PMD, likely correlation not causation, >

DONE
* <done: intent to commit>
* <done: consider, lcd dispaly, wired on breadboard to RPi Pico, discovery , understaing ecosystm, driver and code as use cases, driver completed needs testing, >
* <done: consider, lcd dispaly, wired on breadboard to RPi Pico, discovery , understaing ecosystm, initial user testing to be code as use case, 'Hello, World!' to screen, success, >
* <done: consider, DHT22 temperature readings to screen in development environment DE1, >
* <done: consider, build distribution archive for use in Thonny IDE, as step toward systems testing in QA environment QA1, which build tool used: Hatch, >
* <done: consider, troubleshoot two devices on same I2C bus, likely an I2C conflict issue. >
* <done: consider, addressing issue on I2C, >
* <done: consider, BME280 temperature readings to screen in QA environment QA1, both LCD screen and BME sensor are use I2C work around is have each be on seperate bus, BME280 on bus 1 and LCD on bus 0, LCD bus 0 probably simplest work around for now,  >


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

Success in QA1 env. Two devices I2C, one I2C bus 0 and second on I2C bus 1; LCD screen on bus 0 and BME280 sensor on bus 1. Successully display temperature and humidity and air pressure readings from BME280 on LCD screen.
* <todo: consider, contact Bosch re humidity reading, it appears incorrect, is this a calibrtion issue? or is it sensor damaged, or are registries compromised via driver? >
* <todo: consider, refine display of values, to better understand values returned from BME280 registers, and conversion of values for display,  >

```
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
display_i2c: I2C(0, freq=400000, scl=9, sda=8, timeout=50000)
devices: [119]
display_i2c.scan() address list: [62, 96]
current date & time: (2025, 7, 25, 4, 11, 52, 56, 0)
Temperature:  24.60C
Temperature:  75.88F
Humidity:  47.-4896214%
Pressure:  1006.33hPa
current date & time: (2025, 7, 25, 4, 11, 53, 2, 0)
Temperature:  24.12C
Temperature:  75.42F
Humidity:  48.-4912598%
Pressure:  1007.14hPa
current date & time: (2025, 7, 25, 4, 11, 53, 7, 0)
Temperature:  24.11C
Temperature:  75.4F
Humidity:  48.-4919392%
Pressure:  1007.17hPa
current date & time: (2025, 7, 25, 4, 11, 53, 12, 0)
Temperature:  24.12C
Temperature:  75.4F
Humidity:  48.-4921789%
Pressure:  1007.17hPa
current date & time: (2025, 7, 25, 4, 11, 53, 18, 0)
Temperature:  24.11C
Temperature:  75.4F
Humidity:  48.-4927384%
Pressure:  1007.14hPa
current date & time: (2025, 7, 25, 4, 11, 53, 23, 0)
Temperature:  24.12C
Temperature:  75.4F
Humidity:  48.-4927484%
Pressure:  1007.14hPa
current date & time: (2025, 7, 25, 4, 11, 53, 28, 0)
Temperature:  24.12C
Temperature:  75.4F
Humidity:  48.-4922888%
Pressure:  1007.22hPa
current date & time: (2025, 7, 25, 4, 11, 53, 34, 0)
Temperature:  24.12C
Temperature:  75.42F
Humidity:  48.-4918393%
Pressure:  1007.20hPa

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Traceback (most recent call last):
  File "<stdin>", line 292, in <module>
KeyboardInterrupt: 

MPY: soft reboot
MicroPython v1.25.0 on 2025-04-15; Raspberry Pi Pico 2 W with RP2350

Type "help()" for more information.

>>> 
Connection lost -- EOF

Use Stop/Restart to reconnect.

Process ended with exit code 1.
```
### integrate LCD and BME280 readings and sd card
BME280 temperature humdity air pressure reading to file io to SD Card and to LCD screen, in rpi-pi/sdc (mpy) project [GH](https://github.com/YorkEarwaker/Electrical-Engineering/tree/main/rpi-pi/mpy/sdc#bme280-temperature-humdity-air-pressure-reading-to-file-io-to-sd-card-and-to-lcd-screen)

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


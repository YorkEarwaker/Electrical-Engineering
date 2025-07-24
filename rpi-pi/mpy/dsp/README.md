# Display dsp (mpy)

Display things on a screen, wired to RPi Pico using I2C and SPI interfaces, 

## Status

TODO
* <todo: consider, oled display, wired on breadboard to RPi Pico, discovery, understaing ecosystm, >
* <todo: consider, BME280 temperature readings to screen in QA environment QA1, >
* <todo: consider, there are still issues to fully understand with Hatch build options in pyproject.toml, further research necessary, >

DONE
* <done: intent to commit>
* <done: consider, lcd dispaly, wired on breadboard to RPi Pico, discovery , understaing ecosystm, driver and code as use cases, driver completed needs testing, >
* <done: consider, lcd dispaly, wired on breadboard to RPi Pico, discovery , understaing ecosystm, initial user testing to be code as use case, 'Hello, World!' to screen, success, >
* <done: consider, DHT22 temperature readings to screen in development environment DE1, >
* <done: consider, build distribution archive for use in Thonny IDE, as step toward systems testing in QA environment QA1, which build tool used: Hatch, >

## Output

<info: successful build distribtuion package with Hatch for to import driver 'dsp_lcd1602_dvr.py' into QA1 env. >
```
(venv) C:\Users\yorke\Documents\dev\repo\electrical-engineering\rpi-pi\mpy\dsp>hatch build
──────────────────────────────────────────────────────── sdist ────────────────────────────────────────────────────────
dist\display_org_agw_een_dsp-0.0.1.tar.gz
──────────────────────────────────────────────────────── wheel ────────────────────────────────────────────────────────
dist\display_org_agw_een_dsp-0.0.1-py3-none-any.whl

(venv) C:\Users\yorke\Documents\dev\repo\electrical-engineering\rpi-pi\mpy\dsp>
```

<info: successful run of script 'dsp_lcd1602_hwd.py' to display Hello World on LCD screen in QA1 env after importing 
       display_org_agw_een_dsp-0.0.1-py3-none-any.whl in Thonny IDE.  >
```
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
display_i2c: I2C(1, freq=400000, scl=7, sda=6, timeout=50000)
display_i2c.scan() address list: [62, 96, 112]
>>> 
```

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

Datasheets
* ...

News Papers - LCD dispaly
* Raspberry Pi Pico with I2C LCD Display (MicroPython), [WS](https://randomnerdtutorials.com/raspberry-pi-pico-i2c-lcd-display-micropython/), Randomtutorials, 
* ...
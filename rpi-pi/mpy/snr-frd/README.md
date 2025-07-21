# Infrared sensor frd (mpy)

Infrared sensor capability. Radiative energy, heat detection, the likelyhood of phase change. In a warming planet everything will be getting hotter. The gap to biological heat stesss decreases. The likelyhood of wetbulb invents increases. The gap to ignition decreases. The gap to engineering tolernce failure decreases. The gap to vaporisation of volatile substances decreases. The gap to meltinig point decresses. ...

May be use case that requires purchse of SBC like RPi 5. But would a lower end SBC RPi Zero 2 be sufficient speced. 

## Status
TODO
* <todo: consider, select infrared sensor to start with, >
* <todo: consider, what are the infrared sensor options, >
* <todo: consider, thermal imaging camera options, >
* <todo: consider, identify infrared spectrum high low, before purchase of high end compoent, >
* <todo: consider, low end compoennt for intial PoC, >
* <todo: consider, field of view, standard 45°, 55°, wide angle 90°, enumerate use cases for each, >
* <todo: consider, does this require purchase of RPi 5 SBC, likely MCU like pico under speced for processig and display, >
* <todo: consider, could Pico MCU be used to capture and transfer stream circa 250fps? probs not, >
* <todo: consider, temperature? heat? measurement ranage, cold to hot, >

DONE
* <done: intent to commit>

## Libs

Drivers?
* SparkFun MLX90640 Arduino Example [GH](https://github.com/sparkfun/SparkFun_MLX90640_Arduino_Example), 

VNC - mobile phone integration
* 

## Hardware

Sensor
* MLX90640
* MLX90641
* <todo: identify others, >

Boards - which of these could be used with MCU like Pico? 
* Thermal Camera HAT, Thermal Camera USB, wiki [WS](https://www.waveshare.com/wiki/Thermal_Camera_HAT), Waveshare, USB Pi Hut [WS](https://thepihut.com/products/long-wave-ir-thermal-imaging-camera-module) cost circa: £115, HAT Pi Hut [WS](https://thepihut.com/products/long-wave-ir-thermal-imaging-camera-hat-for-raspberry-pi) cost circa: £86
* Grove - Thermal Imaging Camera / IR Array MLX90640 - 55°, Pi Hut [WS](https://thepihut.com/products/grove-thermal-imaging-camera-ir-array-mlx90640-55), Grove, cost circa: £55
* MLX90641 IR Array Thermal Imaging Camera, Pi Hut [WS](https://thepihut.com/products/mlx90641-ir-array-thermal-imaging-camera), Waveshare, cost circa: £45
* Standard (55°) – MLX90640 Thermal Camera Breakout, Pi Hut [WS](https://thepihut.com/products/standard-55-mlx90640-thermal-camera-breakout), Pimori, cost circa: £60
* SparkFun IR Array Breakout - 55 Degree FOV, MLX90640 (Qwiic) Sparkfun [WS](https://www.sparkfun.com/sparkfun-ir-array-breakout-55-degree-fov-mlx90640-qwiic.html), Sparkfun, cost circa: $70
* <todo: identify others, >

# References

Terms
* Thermal Imaging, 
* Infrared long Wavelenth, IR lW
* microbolometer pixels
* thermopile pixels

News Papers - nhw to
* Building a Raspberry Pi Thermal Imaging Camera - MLX90640 guide, [WS](https://everythingsmarthome.co.uk/building-a-raspberry-pi-thermal-imaging-camera-mlx90640-guide/), Lewis Barclay, 


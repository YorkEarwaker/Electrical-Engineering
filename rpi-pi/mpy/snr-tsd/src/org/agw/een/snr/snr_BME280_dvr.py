#        _ _   _ _ _      _
#       /   ) / _ _ )  _ \ )
#      / (| |/ /  _ _ \ ) \ \
#     /  _    (  (_  ) \ \ \ \
#    / /  | |\ \ _ )  \_) \_) \
#   (_/   |_| \ _ _ /\ _ _ _ _ )
#   Anthropogenic Global Warming
# --------------------------------
# 
# Code Sources
#
# MicroPython,
# RP2 module, quick reference
# https://docs.micropython.org/en/latest/rp2/quickref.html # module
# 
# machine module
# https://docs.micropython.org/en/latest/library/machine.html # modul# machine module I2C class, i2c.scan(), 
# https://docs.micropython.org/en/latest/library/machine.I2C.html # class
#
# Waveshare CN web site,
# https://files.waveshare.com/upload/9/91/BME280_datasheet.pdf
# Related, Bosch datasheet
# https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/
# https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf
# 
# Tutorials 
# https://randomnerdtutorials.com/raspberry-pi-pico-bme280-micropython/
# https://github.com/RuiSantosdotme/ESP-MicroPython/blob/master/code/WiFi/HTTP_Client_IFTTT_BME280/BME280.py
# https://microcontrollerslab.com/raspberry-pi-pico-w-wireless-bme280-web-server/
#
# Context diagram
# Assuming only the microcontroller interacts with the device.
#  ___________________________________________  ____________________________________
# |            Electrical Engineering         ||        Internet of Things          | 
#                   In Scope                               Out of Scope
#  ___________________________________________  _________________  _________________
# |                                           ||                 ||                 |
#  Device                  Microcontroller          SomeThing-M^J     SomeThing′-N^K 
#  ______   do x      ________________________    do p     ______    do p′    ______ 
# |      |<----------| CPU  Mpy  Drvr Prog    |<----------|      |<----------|      |
# |      |  get y    | |_|<-|_|<-|_|<-|_|     |   get q   |      |   get q′  |      |
# |______|<----------|________________________|<----------|______|<----------|______|
#
# A device is any external hardware component wired (integrated) to and programatically controlled by
# the hardware microcontroller. The microcontroller executes programme software which use driver software,
# both of which might be installed on the microcontroller, to issue commands to the device to do something
# or get information the device has saved in the device memory banks. The device driver software is specialist
# software that has been written to communicate specifically with a particular external device.
# The device might do some activity, as a result of a command received from a programme using the device driver
# running on the microcontroller, and save information about the activity to specific address locations
# in the device memory bank registers. The first programme that issued the do activity command, or second programme,
# might then get the information from the memory bank registers of the device and return the information to the
# microcontroller.
# 
# Another thing, hardware or software, might issue commands to the microcontroller to do something
# and get information from the microcontroller memory bank. The internet of things is out of scope
# in this context. But this electrical engineering context A might be used in as part of a larger
# systme of systems IoT context B.
# <todo: context text work in progress, last reviewed 01/05/2025, wip>
#
# Sensor
# Pin sequence numbers, left to right, 1 2 3 4 5 6, with circuit board and BME sensor forward facing
#
#       [.] BME280 sensor device, circa factor larger than actual size
#   ___________ 
#  |    [.]    | Simplified       | --- | --------- | Circuit board 
#  |           | Front of         | 1   | VCC       | pins functions
#  |           | BME280           | 2   | GND       |
#  |___________| sensor           | 3   | SDA/MOSI  |
#  |___________| Waveshare, CN    | 4   | SCL/SCK   |
#   | | | | | |  Circuit board    | 5   | ADDR/MISO |     
#   1 2 3 4 5 6                   | 6   | CS        |
#                                 | --- | --------- | 
#
# 4.2.2 Trimming parameter readout,
# Bosch Sensortec,  BME280 Data sheet, BST-BME280-DS001-23 Revision_1.23_012022
# | ------------------------------------------------------------ |
# | Compensation parameter storage, naming and data type         |
# | -- | ---------------- | ------------------- | -------------- |
# | ID | Register Address | Register content    | Data type      |
# | -- | ---------------- | ------------------- | -------------- |
# | 1  | 0x88 / 0x89      | dig_T1 [7:0]/[15:8] | unsigned short |
# | 2  | 0x8A / 0x8B      | dig_T2 [7:0]/[15:8] | signed short   |
# | 3  | 0x8C / 0x8D      | dig_T3 [7:0]/[15:8] | signed short   |
# | 4  | 0x8E / 0x8F      | dig_P1 [7:0]/[15:8] | unsigned short |
# | 5  | 0x90 / 0x91      | dig_P2 [7:0]/[15:8] | signed short   |
# | 6  | 0x92 / 0x93      | dig_P3 [7:0]/[15:8] | signed short   |
# | 7  | 0x94 / 0x95      | dig_P4 [7:0]/[15:8] | signed short   |
# | 8  | 0x96 / 0x97      | dig_P5 [7:0]/[15:8] | singed short   |
# | 9  | 0x98 / 0x99      | dig_P6 [7:0]/[15:8] | singed short   |
# | 10 | 0x9A / 0x9B      | dig_P7 [7:0]/[15:8] | singed short   |
# | 11 | 0x9C / 0x9D      | dig_P8 [7:0]/[15:8] | singed short   |
# | 12 | 0x9E / 0x9F      | dig_P9 [7:0]/[15:8] | singed short   |
# | 13 | 0xA1             | dig_H1 [7:0]        | unsigned char  |
# | 14 | 0xE1 / 0xE2      | dig_H2 [7:0]/[15:8] | signed short   |
# | 15 | 0xE3             | dig_H3 [7:0]        | unsigned char  |
# | 16 | 0xE4 / 0xE5[3:0] | dig_H4 [11:4]/[3:0] | signed short   |
# | 17 | 0xE5[7:4] / 0xE6 | dig_H5 [3:0]/[11:4] | signed short   |
# | 18 | 0xE7             | dig_H6              | signed char    |
# | -- | ---------------- | ------------------- | -------------- |
# 
# Compensation words, words are 16 bit signed or unsigned integer stored in two's complement, 
# dig_T* = temperature compensation related values
# dig_P* = pressure related values
# dig_H* = humidity related values
# 
# Table 18: Memory map
# Bosch Sensortec,  BME280 Data sheet, BST-BME280-DS001-23 Revision_1.23_012022
# |----------------- | --------- | --------------------------------------------------------------------- | ------------|
# | Register Name    | Address   | bit7 | bit6 | bit5 | bit4 |     bit3     | bit2 | bit1 |     bit0     | Reset state |
# |----------------- | --------- | DR ------------------------------------------------------------------ | ------------|
# | hum_lsb          | 0xFE      |                             hum_lsb<7:0>                              | 0x00        |
# |----------------- | --------- | DR ------------------------------------------------------------------ | ------------|
# | hum_msb          | 0xFD      |                             hum_msb<7:0>                              | 0x80        |
# |----------------- | --------- | DR ------------------------------------------------------------------ | ------------|
# | temp_xlsb        | 0xFC      |       temp_xlsb<7:4>      |       0      |   0  |   0  |       0      | 0x00        |
# |----------------- | --------- | DR ------------------------------------------------------------------ | ------------|
# | temp_lsb         | 0xFB      |                             temp_lsb<7:0>                             | 0x00        |
# |----------------- | --------- | DR ------------------------------------------------------------------ | ------------|
# | temp_msb         | 0xFA      |                             temp_msb<7:0>                             | 0x80        |
# |----------------- | --------- | DR ------------------------------------------------------------------ | ------------|
# | press_xlsb       | 0xF9      |       press_xlsb<7:4>     |       0      |   0  |   0  |       0      | 0x00        |
# |----------------- | --------- | DR ------------------------------------------------------------------ | ------------|
# | press_lsb        | 0xF8      |                            press_lsb<7:0>                             | 0x00        |
# |----------------- | --------- | DR ------------------------------------------------------------------ | ------------|
# | press_msb        | 0xF7      |                            press_msb<7:0>                             | 0x80        |
# |----------------- | --------- | CR --------------- | CR ----------------------- | RR - | CR --------- | ------------|
# | config           | 0xF5      |      t_sb[2:0]     |         filter[2:0]        |      | spi3w_en[0]  | 0x00        |
# |----------------- | --------- | CR --------------- | CR ----------------------- | CR ---------------- | ------------|
# | ctrl_meas        | 0xF4      |      osrs_t[2:0]   |         osrs_p[2:0]        |      mode[1:0]      | 0x00        |
# |----------------- | --------- | RR ---------------------- | SR --------- | RR -------- | SR --------- | ------------|
# | status           | 0xF3      |                           | measuring[0] |             | im_update[0] | 0x00        |
# |----------------- | --------- | RR ------------------------------------- | CR ----------------------- | ------------|
# | ctrl_hum         | 0xF2      |                                          |         osrs_h[2:0]        | 0x00        |
# |----------------- | --------- | CD ------------------------------------------------------------------ | ------------|
# | calib26..calib41 | 0xE1…0xF0 |                           calibration data                            | individual  |
# |----------------- | --------- | RS ------------------------------------------------------------------ | ------------|
# | reset            | 0xE0      |                              reset[7:0]                               | 0x00        |
# |----------------- | --------- | ID ------------------------------------------------------------------ | ------------|
# | id               | 0xD0      |                             chip_id[7:0]                              | 0x60        |
# |----------------- | --------- | CD ------------------------------------------------------------------ | ------------|
# | calib00..calib25 | 0x88…0xA1 |                           calibration data                            | individual  |
# |----------------- | --------- | --------------------------------------------------------------------- | ------------|
#
# | ----------- | --------- | ----------- | --------- |  -------- | --------- | ---- | ------ |
# | Registers   | Reserved  | Calibration | Control   | Data      | Status    | Chip | ReSet  |
# |             | Registers | Data        | Registers | Registers | Registers | ID   | (Soft) |
# | ----------- | --------- | ----------- | --------- |  -------- | --------- | ---- | ------ |
# | Type        | do not    | read        | read /    | read      | read      | read | write  | 
# |             | change    | only        | write     | only      | only      | only | only   |
# | ----------- | --------- | ----------- | --------- |  -------- | --------- | ---- | ------ |
# | Abreviation | RR        | CD          | CR        | DR        | SR        | ID   | RS     |
# | ----------- | --------- | ----------- | --------- |  -------- | --------- | ---- | ------ |
#
# 10.2 Function return codes
# Bosch Sensortec,  BME280 Data sheet, BST-BME280-DS001-23 Revision_1.23_012022
# A list of the possible function return codes can be found below.
# | ------ | ---------------------------------------------------- |
# | Return | Function return code, meaning description,           |        
# | code   | state of sensor, error, exception, message           |
# | ------ | ---------------------------------------------------- |
# |  0     | Sensor OK                                            |
# | 10     | Communication error or wrong device found            |
# | 20     | Trimming data out of bound                           |
# | 30     | Temperature bond wire failure or MEMS defect         |
# | 31     | Pressure bond wire failure or MEMS defect            |
# | 40     | Implausible temperature (default limits: 0…40°C)     |
# | 41     | Implausible pressure (default limits: 900…1100 hPa)  |
# | 42     | Implausible humidity (default limits: 20...80 %rH    |
# | ------ | ---------------------------------------------------- |
#
# 7. Pin-out and connection diagram
# Bosch Sensortec,  BME280 Data sheet, BST-BME280-DS001-23 Revision_1.23_012022
#
# [.] BME280 sensor device, circa factor larger than actual size
#
# BME280 sensor device, enlarged with pads
# Botton view with pads visible.
# Note the vent hole is visible only in Top view.
#  ______________________________________
# |   _______                  _______   |                
# |  |   1   |                |   8   |  |
# |  |  GND  |                |  VDD  |  |
# |  |_______|                |_______|  |
# |                                      |
# |   _______                  _______   |                
# |  |   2   |                |   7   |  |
# |  |  CSB  |     Bottom     |  GND  |  |
# |  |_______|      View      |_______|  |
# |            (pads visible)            |
# |   _______                  _______   |                
# |  |   3   |                |   6   |  |
# |  |  SDI  |                | VDDIO |  |
# |  |_______|                |_______|  |
# |                 Vent                 |
# |   _______       hole       _______   |  The vent hole is shown to indicate its          
# |  |   4   |       ◯       |   5   |  |  ralative position on the top view.
# |  |  SCK  |      (not      |  SDO  |  |  The vent hole would not be visible in
# |  |_______|    visible)    |_______|  |  the bottom view when the device pads are visible.
# |______________________________________|  The device pads are integrated into the circuit board.
#
# 
# Table 35: Pin description
# Bosch Sensortec,  BME280 Data sheet, BST-BME280-DS001-23 Revision_1.23_012022
# | --- | ----- | -------- | ------------------- | -------------------------- |
# | Pin | Name  | I/O Type | Description         |        Connect to          |
# |     |       |          |                     | SPI 4W | SPI 3W  | I²C     |
# | --- | ----- | -------- | ------------------- | ------ | ------- | ------- |
# | 1   | GND   | Supply   | Ground              |            GND             |
# | 2   | CSB   | In       | Chip select         | CSB    | CSB     | VDDIO   |
# | 3   | SDI   | In/Out   | Serial data input   | SDI    | SDI/SDO | SDA     |
# | 4   | SCK   | In       | Serial clock input  | SCK    | SCK     | SCL     |
# | 5   | SDO   | In/Out   | Serial data output  | SDO    | DNC     | GND for |
# |     |       |          |                     |        |         | default |
# |     |       |          |                     |        |         | address |
# | 6   | VDDIO | Supply   | Digital / Interface |           VDDIO            |
# |     |       |          |      supply         |                            |
# | 7   | GND   | Supply   | Ground              |            GND             |
# | 8   | VDD   | Supply   | Analog supply       |            VDD             |
# | --- | ----- | -------- | ------------------- | -------------------------- |
# 
#
# 

# #
# import libraries to use in this programme
from machine import I2C
import time

# I2C registry address default for BME280 is 0 x 77
# if ADDR is grounded the registry address is 0 x 76
reg_addr_i2c_bme280_prime = 0x77 # default
reg_addr_i2c_bme280_secondary = 0x76 # 

reg_addr_i2c_bme280 = reg_addr_i2c_bme280_prime

# #
# oversampling modes
# filter modes
# data rates

# Sensor oversampling mode settings for BME280
oversampling_mode_one = 1 # 1
oversampling_mode_two = 2 # 2
oversampling_mode_four = 3 # 4
oversampling_mode_eight = 4 # 8
oversampling_mode_sixteen = 5 # 16

# compensation parameter register address
# each is stored in 16 bit word signed or unsigned integer stored in two' complement
# trimming parameter readout, trimming parameters are stored in sensor device non volative memory NVM
# readings are taken uncompensated ut up uh . compensation is applied to values after reading.
# compensation code is provided by Bosch in the BME280 datasheet
# compensation code logic equations use the trimming paramters stored in NVM. 

# Temperature
# Compensating parameter, register address
# Trimming parameter readout
# Calibration data, register
reg_addr_compensation_trim_param_dig_t1 = 0x88 
reg_addr_compensation_trim_param_dig_t2 = 0x8A
reg_addr_compensation_trim_param_dig_t3 = 0x8C

# Pressure
# Compensating parameter, register address
# Trimming parameter readout
# Calibration data, register
reg_addr_compensation_trim_param_dig_p1 = 0x8E
reg_addr_compensation_trim_param_dig_p2 = 0x90
reg_addr_compensation_trim_param_dig_p3 = 0x92
reg_addr_compensation_trim_param_dig_p4 = 0x94
reg_addr_compensation_trim_param_dig_p5 = 0x96
reg_addr_compensation_trim_param_dig_p6 = 0x98
reg_addr_compensation_trim_param_dig_p7 = 0x9A
reg_addr_compensation_trim_param_dig_p8 = 0x9C
reg_addr_compensation_trim_param_dig_p9 = 0x9E

# Humidity
# Compensating parameter, register address
# Trimming parameter readout
# Calibration data, register
reg_addr_compensation_trim_param_dig_h1 = 0xA1
reg_addr_compensation_trim_param_dig_h2 = 0xE1
reg_addr_compensation_trim_param_dig_h3 = 0xE3
reg_addr_compensation_trim_param_dig_h4 = 0xE4
reg_addr_compensation_trim_param_dig_h5 = 0xE5
reg_addr_compensation_trim_param_dig_h6 = 0xE7

# Memory map, sensor identifiction
# ID, register
reg_addr_chip_id = 0xD0 # 
reg_addr_version = 0xD1 # verify this is true, can't seem to find it in the BME280 datasheet

# Memory map, sensor administration
# Reset, register
reg_addr_reset = 0xE0 # readout value always 0x00
# Status, register
reg_addr_status = 0xF3 # measuring, im_update

# Memory map, sensor operations, device data acquisition options
# Control, register('s)
reg_addr_config = 0xF5 # time? other two? to list
reg_addr_ctrl_hum = 0xF2 # humidity data aquisition options for device, depencency on ctrl_meas wirte for changes to take effect
reg_addr_ctrl_meas = 0xF4 # temperature and pressure data acquisition options for device

# Memory map, raw sensor data
# Data, register('s)
reg_addr_temperature_data = 0xFA #  0xFA…0xFC “temp” (_msb, _lsb, _xlsb)
reg_addr_pressure_data = 0xF7 #  0xF7…0xF9 “press” (_msb, _lsb, _xlsb)
reg_addr_humidity_data = 0xFD #  0xFD…0xFE “hum” (_msb, _lsb)

# I2C device comms
# 8bit, 16bit, byte array, read write
# to registers of a I2C device
class Device:
    
    # Create an instance of an I2C device
    # using the provided address and I2C interface object 
    def __init__(self, address, i2c):
        self._address = address
        self._i2c = i2c
    
    # Write an 8bit value on the bus (without register)
    def write_raw_eight_bit(self, bits_val):
        value = bits_val & 0xFF
        self.i2c.writeto(self._address, bits_val)
        
    # Write 8bit value to provided register
    def write_eight_bit(self, register, bits_val):
        b=bytearray(1)
        b[0] = bits_val & 0xFF
        self._i2c.writeto_mem(self._address, register, b)
        
    # Write 16bit value to provided register
    def write_sixteen_bit(self, register, bits_val):
        bits_val = bits_val & 0xFFF
        b=bytearray(2)
        b[0] = bits_val & 0xFF
        b[1] = (bits_val>>8) & 0xFF
        self._i2c.writeto_mem(self._address, register, bits_val)
    
    # Read 8bit value on the but (without register)
    def read_raw_eight_bit(self):
        return int.from_bytes(self._i2c.readfrom(self._address, 1), 'little') & 0xFF
    
    # Read unsigned byte from provided register
    def read_unsigned_eight(self, register):
        return int.from_bytes(self._i2c.readfrom_mem(self._address, register, 1), 'little') & 0xFF
    
    # Read signed byte from provided register
    def read_signed_eight(self, register):
        reg_rtn_val = self.read_unsigned_eight(register)
        if reg_rtn_val > 127:
            reg_rtn_val -= 256
        return reg_rtn_val
    
    # Read unsigned 16bit value from the provided register
    # with provided endian, default little endian,
    # or least significant byte first
    def read_unsigned_sixteen(self, register, little_endian = True):
        reg_rtn_val = int.from_bytes(self._i2c.readfrom_mem(self._address, register, 2), 'little') & 0xFFFF
        
        if not little_endian: 
            reg_rtn_val = ((reg_rtn_val << 8) & 0xFF00) + (reg_rtn_val >> 8)
        return reg_rtn_val
    
    # Read signed 16bit value from the provided register
    # with provided endian, default little endian
    # or least significant byte
    def read_signed_sixteen(self, register, little_endian =  True):
        reg_rtn_val = self.read_unsigned_sixteen(register, little_endian)
        
        if reg_rtn_val > 32767:
            reg_rtn_val -= 65536
        return reg_rtn_val
    
    # Read unsigned 16bit value from the provided register,
    # in little endian byte order
    def read_unsigned_sixteen_little_endian(self, register):
        return self.read_unsigned_sixteen(register, little_endian = True)
       
    # Read unsigned 16bit value from provided register
    # in big endian byte order
    def read_unsigned_sixteen_big_endian(self, register):
        return self.read_unsigned_sixteen(register, little_endian = False)
    
    # Read signed 16bit value from provided register
    # in little endian bytes order
    def read_signed_sixteen_little_endian(self, register):
        return self.read_signed_sixteen(register, little_endian = True)
    
    # Read signed 16bit value from provided register,
    # in big endian byte order
    def read_signed_sixteen_big_endian(self, register):
        return self.read_signed_sixteen(register, little_endian =  False)

# The BME280 sensor device,
# BMP280 and other Bosche sensors could be added in a similar way
# 
# RPi Pico does not have a floating point unit hardware
# so all floating piont calculations must be carried out in software
# floating point calculation are emulated in software
class BME280:
    
    # initialize the class instance
    def __init__(self, mode=oversampling_mode_one, address=reg_addr_i2c_bme280, i2c=None, **kwargs):
        
        # check the mode is valid
        if mode not in [oversampling_mode_one, oversampling_mode_two,
                        oversampling_mode_four, oversampling_mode_eight,
                        oversampling_mode_sixteen]:
            raise ValueError('Unexpected mode value {0}. Set mode to one of'
                             'BME280_ULTRALOWPOWER, BME280_STNADARD, BME280_HIGHRES, or'
                             'BME280_ULTRAHIGHRES'.format(mode))
        self._mode = mode
        # create ic2 device
        if i2c is None:
            raise ValueError('An I2C object is required.')
        self._device = Device(address, i2c)
        # load calibrated values.
        self._load_calibration()
        self._device.write_eight_bit(reg_addr_ctrl_meas, 0x3F)
        self.t_fine = 0
    
    # 
    def _load_calibration(self):
        
        # temperature, compensation
        self.dig_T1 = self._device.read_unsigned_sixteen_little_endian(
            reg_addr_compensation_trim_param_dig_t1)
        self.dig_T2 = self._device.read_signed_sixteen_little_endian(
            reg_addr_compensation_trim_param_dig_t2)
        self.dig_T3 = self._device.read_signed_sixteen_little_endian(
            reg_addr_compensation_trim_param_dig_t3)
        
        # pressure, compensation
        self.dig_P1 = self._device.read_unsigned_sixteen_little_endian(
            reg_addr_compensation_trim_param_dig_p1)
        self.dig_P2 = self._device.read_signed_sixteen_little_endian(
            reg_addr_compensation_trim_param_dig_p2)
        self.dig_P3 = self._device.read_signed_sixteen_little_endian(
            reg_addr_compensation_trim_param_dig_p3)
        self.dig_P4 = self._device.read_signed_sixteen_little_endian(
            reg_addr_compensation_trim_param_dig_p4)
        self.dig_P5 = self._device.read_signed_sixteen_little_endian(
            reg_addr_compensation_trim_param_dig_p5)
        self.dig_P6 = self._device.read_signed_sixteen_little_endian(
            reg_addr_compensation_trim_param_dig_p6)
        self.dig_P7 = self._device.read_signed_sixteen_little_endian(
            reg_addr_compensation_trim_param_dig_p7)
        self.dig_P8 = self._device.read_signed_sixteen_little_endian(
            reg_addr_compensation_trim_param_dig_p8)
        self.dig_P9 = self._device.read_signed_sixteen_little_endian(
            reg_addr_compensation_trim_param_dig_p9)
        
        # humidity, compensation
        self.dig_H1 = self._device.read_unsigned_eight(
            reg_addr_compensation_trim_param_dig_h1)
        self.dig_H2 = self._device.read_signed_sixteen_little_endian(
            reg_addr_compensation_trim_param_dig_h2)
        self.dig_H3 = self._device.read_unsigned_eight(
            reg_addr_compensation_trim_param_dig_h3)
        self.dig_H6 = self._device.read_signed_eight(
            reg_addr_compensation_trim_param_dig_h7)
        
        h4 = self._device.read_signed_eight(
            reg_addr_compensation_trim_param_dig_h4)
        h4 = (h4 << 24) >> 20
        self.dig_H4 = h4 | (
            self._device.read_unsigned_eight(
                reg_addr_compensation_trim_param_dig_h5) & 0x0F)
        
        h5 = self._device.read_signed_eight(
            reg_addr_compensation_trim_param_dig_h6)
        h5 = (h5 << 24) >> 20
        self._H5 = h5 | (
            self._device.read_unsigned_eight(
                reg_addr_compensation_trim_param_dig_h5) >> 4 & 0x0F)
        
    # Temperature
    # Read the raw, uncompensated, temperature from the sensor
    def read_raw_temp(self):
        meas = self._mode
        self._device.write_eight_bit(reg_addr_ctrl_hum, meas)
        meas = self._mode << 5 | self._mode << 2 | 1
        self._device.write_eight_bit(reg_addr_ctrl_meas, meas)
        sleep_time = 1250 + 2300 * (1 << self._mode)
        
        # allow suffient elapsed time before other readings
        # pressure level and humidity
        sleep_time = sleep_time + 2300 * (1 << self._mode) + 575
        sleep_time = sleep_time + 2300 * (1 << self._mode) + 575 # why twice
        time.sleep_us(sleep_time) # Pause for sufficient time
        msb = self._device.read_unsigned_eight(reg_addr_temperature_data)
        lsb = self._device.read_unsigned_eight(reg_addr_temperature_data + 1)
        xlsb = self._device.read_unsigned_eight(reg_addr_temperature_data + 2)
        raw = ((msb << 16) | (lsb << 8) | xlsb) >> 4
        return raw
        
    # Pressure
    # Read the raw, uncompensated, pressure level from the sensor
    # Assume the temperature has been read beforehand
    # That is, sufficient time has elapsed, delay provided
    def read_raw_pressure(self):
        
        msb = self._device.read_unsigned_eight(reg_addr_pressure_data)
        lsb = self._device.read_unsigned_eight(reg_addr_pressure_data + 1)
        xlsb = self._device.read_unsigned_eight(reg_addr_pressure_data + 2)
        raw = ((msb << 16) | (lsb << 8) | xlsb) >> 4
        return raw
    
    # Humidity
    # Read the raw, uncompensated, temperature from the sensor
    # Assume the temperature has been read beforehand
    # That is, sufficient time has elapsed, delay provided
    def read_raw_humidity(self):
        
        msb = self._device.read_unsigned_eight(reg_addr_humidity_data)
        lsb = self._device.read_unsigned_eight(reg_addr_humidity_data + 1)
        raw = (msb << 8) | lsb
        return raw
    
    # Temperature
    # Calculate the compensated temperature in celsius
    # with presision 0.01 of a degree celsius
    def read_temperature(self):
        adc = self.read_raw_temp()
        var1 = ((adc >> 3) - (self.dig_T1 << 1)) * (self.dig_T2 >> 11)
        var2 == ((
            (((adc >> 4) - self.deg_T1) * ((adc >> 4) - self.dig_T1)) >> 12)
            self.dig_T3) >> 14
        self.t_fine = var1 + var2
        return (self.t_fine * 5 + 128) >> 8
    
    # Pressure
    # Calculate the compensated pressure in Pascals
    def read_pressure(self):
        adc = self.read_raw_pressure()
        var1 = self.t_fine - 128000
        var2 = var1 * var1 * self.dig_P6
        var2 = var2 + ((var1 * self.dig_P5) << 17)
        var2 = var2 + (self.dig_P4 << 35)
        var1 = (((var1 * var1 * self.dig_P3) >> 8) +
                ((var1 * self.dig_P2) >> 12))
        var1 = (((1 << 47) + var1) * self.dig_P1) >> 33
        if var1 == 0:
            return 0
        p = 1048576 - adc
        p = (((p << 31) - var2) * 3125) // var1
        var1 = (self.dig_P9 * (p >> 13) * (p >> 13)) >> 25
        var2 = (self.dig_P8 * p) >> 19
        return ((p + var1 + var2) >> 8) + (self.dig_P7 << 4)
    
    # Humidity
    def read_humidity(self):
        adc = self.read_raw_humidity()
        # print 'Raw humidity = {0:d}'.format (adc) # debug?
        h = self.t_fine - 76800
        h = (((((adc << 14) - (self.dig_H4 << 20) - (self.dig_H5 * h)) +
               16384) >> 15) * (((((((h * self.dig_H6) >> 10) * (((h *
                                self.dig_H3) >> 11) + 32768)) >> 10) + 2097152) *
                                self.dig_H2 + 8192) >> 14))
        h = h - (((((h >> 15) * (h >> 15)) >> 7) * self.dig_H1) >> 4)
        h = 0 if h < 0 else h
        h = 419430400 if h > 419430400 else h
        return h >> 12
    
    # Return the temperature in degress
    @property
    def temperature(self):
        t = self.read_temperature()
        ti = t // 100
        td = t - ti * 100
        return "{}.{:02d}C".format(ti, td)
    
    
    # Return pressure in hPa
    @property
    def pressure(self):
        p = self.read_pressure() // 256
        pi = p // 100
        pd = p - pi * 100
        return "{}.{:02d}hPa".format(pi, pd)
        
    # Return the humidity in percent
    @property
    def humidity(self):
        h = self.read_humidity()
        hi = h // 1024
        hd = h * 100 // 1024 - h * 100
        return "{}.{:02d}%".format(hi, hd)
    
    
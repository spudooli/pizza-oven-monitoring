#!/usr/bin/python

# https://learn.adafruit.com/max31855-thermocouple-python-library/hardware
# https://github.com/adafruit/Adafruit_Python_MAX31855
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855

# https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code
from Adafruit_7Segment import SevenSegment

import urllib2

pizzaapi = "https://www.spudooli.com/track/"

segment = SevenSegment(address=0x70)


# Raspberry Pi software SPI configuration.
CLK = 25
CS  = 24
DO  = 18
sensor = MAX31855.MAX31855(CLK, CS, DO)

pizza-oven-temperature = sensor.readTempC()
internal = sensor.readInternalC()
print 'Thermocouple Temperature: {0:0.3F}*C'.format(pizza-oven-temperature)
print '    Internal Temperature: {0:0.3F}*C'.format(internal)




segment.writeDigit(0, int(str(pizza-oven-temperature)[0]) 
segment.writeDigit(1, int(str(pizza-oven-temperature)[1]) 
segment.writeDigit(3, int(str(pizza-oven-temperature)[2])
segment.writeDigit(4, int(str(pizza-oven-temperature)[3])

pizzaapi = pizzaapi + "?insidetemp=" + pizza-oven-temperature + "&outsidetemp=" + internal

urllib2.urlopen(pizzaapi)

#!/usr/bin/python

# https://learn.adafruit.com/max31855-thermocouple-python-library/hardware
# https://github.com/adafruit/Adafruit_Python_MAX31855
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855

# http://www.derekscholten.com/2013/09/02/raspberry-pi-sparkfun-7-segment-display-clock/

import seven_segment_display
import seven_segment_i2c
import time
import urllib2

#pizzaapi = "https://www.spudooli.com/track/"

# Raspberry Pi software SPI configuration.
CLK = 25
CS  = 24
DO  = 18
sensor = MAX31855.MAX31855(CLK, CS, DO)

def main():
    try:
		bus = seven_segment_i2c.SevenSegmentI2c(1)
		display = seven_segment_display.SevenSegmentDisplay(bus)
		display.clear_display()
		while True:
			pizzaoventemperature = sensor.readTempC()
			internal = sensor.readInternalC()
			print 'Thermocouple Temperature: {0:0.3F}*C'.format(pizzaoventemperature)
			print '    Internal Temperature: {0:0.3F}*C'.format(internal)
			print pizzaoventemperature
			display.write_int(6666)


			#pizzaapi = pizzaapi + "?insidetemp=" + pizzaoventemperature + "&outsidetemp=" + internal

			#urllib2.urlopen(pizzaapi)
			time.sleep(3.0)
    except IOError as ex:
        print ex

        
if  __name__ =='__main__':
    main()
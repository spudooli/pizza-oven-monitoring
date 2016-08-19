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

global pizzaapi

pizzaapi = "http://www.spudooli.com/track/pizza.php"

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
		enable_colon = True
		senddatacounter = 1
		while True:
			senddatacounter += 1
			pizzaoventemperature = sensor.readTempC()
			internal = sensor.readInternalC()
			
			print 'Thermocouple Temperature: {:.0f}*C'.format(pizzaoventemperature)
			print '    Internal Temperature: {:.0f}*C'.format(internal)
			
			pizzaoventemperature = int(pizzaoventemperature)
			internal - int(internal)
			display.write_int(pizzaoventemperature)

			#make the colon blink every other cycle
			enable_colon = not enable_colon
			nondigits = []
			if enable_colon:
				nondigits.append(seven_segment_display.DotEnum.DECIMAL_4)
			display.set_nondigits(nondigits)
			
			if senddatacounter > 20:
				senddatacounter = 1
				senddata(pizzaoventemperature, internal)

			time.sleep(3.0)

    except IOError as ex:
        print ex

def senddata(pizzaoventemperature, internal):
	global pizzaapi
	pizzaapi = pizzaapi + "?insidetemp=" + str(pizzaoventemperature) + "&outsidetemp=" + str(internal)
	urllib2.urlopen(pizzaapi)
        print pizzaapi
if  __name__ =='__main__':
    main()

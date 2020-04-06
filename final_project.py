#!/usr/bin/env python

# GrovePi Example for using the Grove Temperature & Humidity Sensor Pro
# (http://www.seedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor_Pro)
#
# The GrovePi connects the Raspberry Pi and Grove sensors
# You can learn more about GrovePi here: http://www.dexterindustries.com/GrovePi
#
# Have a question about this example? Ask on the forums here:
# http://forum.dexterindustries.com/c/grovepi
#
'''

## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove
Sensors to the Raspberry Pi.
Copyright (C) 2017 Dexter Industries

Permission is herby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software') to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, soblicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERSBE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import grovepi
import math
import json # import JSON library
import time # to set frequency

from grove_rgb_lcd import *

#Connect the Grove Temperature & Humidity Sensor Pro to digitl port D4
# This example uses the blue colord sensor
# SIG, NC, VCC, GND
temp_hum_sensor = 4 # The Sensor goes on digitl port 4

# Connect the Grove Light Sensor to analog port A0
light_sensor = 0

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor
blue = 0 # The Blue colored sensor
white = 1 # The White colored sensor

# set backlight color to blue
setRGB(0,0,255)

# set LEDs to digital ports D8, D7, and D3
led_b = 8
led_g = 7
led_r = 3

# Set threshold so sensor only records during daytime hours
threshold = 65

grovepi.pinMode(light_sensor, "INPUT")
grovepi.pinMode(temp_hum_sensor, "INPUT")
grovepi.pinMode(led_b, "OUTPUT")
grovepi.pinMode(led_g, "OUTPUT")
grovepi.pinMode(led_r, "OUTPUT")

# list for temp storage of data
data_list = []

while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(light_sensor)

        # set if statement so data only collects during daylight
        if sensor_value > threshold:
            # This example uses the blue colored sensor
            # The first parameter is the port, the second parameter is the type of sensor
            [temp,humidity] = grovepi.dht(temp_hum_sensor,blue)
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                temp = (temp * 9/5) + 32 # convert to F
                print("temp = %.02f F humidity = %.02f%%"%(temp, humidity))

                t = str(temp)
                h = str(humidity)

                # insert a \n to seperate the lines
                setText("Temp: " + t + "F\n" + "Humidity: " + h + "%")

                data_list.append([temp, humidity])

                with open("data.json", "w") as write_file:
                    json.dump(data_list, write_file)

                if temp > 60 and temp < 85 and humidity < 80:
                    grovepi.digitalWrite(led_g,1)
                    grovepi.digitalWrite(led_r,0)
                    grovepi.digitalWrite(led_b,0)

                elif temp > 85 and temp < 95 and humidity < 80:
                    grovepi.digitalWrite(led_g,0)
                    grovepi.digitalWrite(led_r,0)
                    grovepi.digitalWrite(led_b,1)

                elif temp >= 95 and humidity < 80:
                    grovepi.digitalWrite(led_r,1)
                    grovepi.digitalWrite(led_g,0)
                    grovepi.digitalWrite(led_b,0)

                elif humidity >= 80 and temp < 95:
                    grovepi.digitalWrite(led_b,1)
                    grovepi.digitalWrite(led_g,1)

                elif temp >= 95 and humidity >= 80:
                    grovepi.digitalWrite(led_b,1)
                    grovepi.digitalWrite(led_g,1)
                    grovepi.digitalWrite(led_r,1)

                elif temp <= 60 and humidity < 80:
                    grovepi.digitalWrite(led_b,1)
                    grovepi.digitalWrite(led_g,0)
                    grovepi.digitalWrite(led_r,0)
                    time.sleep(2)
                    grovepi.digitalWrite(led_b,0)
                    grovepi.digitalWrite(led_r,1)
                    time.sleep(2)
                    grovepi.digitalWrite(led_b,1)

                elif temp <= 60 and humidity >=80:
                    grovepi.digitalWrite(led_b,1)
                    grovepi.digitalWrite(led_g,1)
                    grovepi.digitalWrite(led_r,0)
                    time.sleep(2)
                    grovepi.digitalWrite(led_b,0)
                    grovepi.digitalWrite(led_r,1)
                    time.sleep(2)
                    grovepi.digitalWrite(led_b,1)

                # wait 10 minutes (600 seconds)
                time.sleep(600)

        else:
            grovepi.digitalWrite(led_g,0)
            grovepi.digitalWrite(led_b,0)
            grovepi.digitalWrite(led_r,0)

    except IOError:
        print ("Error")
        setText("") # clear text from LCD

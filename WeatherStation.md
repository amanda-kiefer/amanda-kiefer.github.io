# **Weather Station Project**

## Weather Station Program in Python:

```
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

```



## View Video of Working Weather Station [Here](https://youtu.be/dbO3AOFffKA)



## HTML Dashboard Images Derived From Weather Station Data 
![StaticCanvas](https://user-images.githubusercontent.com/61916035/78588828-48d44400-780d-11ea-96f1-b6501150cc08.PNG)
![Humidity](https://user-images.githubusercontent.com/61916035/78588794-3ce88200-780d-11ea-9135-6aa8bd620eaf.PNG)
![image](https://user-images.githubusercontent.com/61916035/78588532-d3687380-780c-11ea-8905-ff0e10b4be4c.png)

# **Weather Station Project**

This project was completed in 2019 for a course at SNHU. The weather station device utilizes a temperature and humidity sensor as well as a light sensor to read in input through the GrovePi system. Output is sent to three colored LED lights; one red, one green, and one blue. The device also utilizes an LCD screen which has been set up to display the latest temperature and humidity reading. The program, written in Python, is written to record the temperature and humidity data and save it to a JSON file during daylight hours. Therefore, the program is set up with a condition to only run if the light sensor does not fall below the set light threshold. During daylight hours, the program will record the data at set intervals and illuminate select LED lights based on temperature and humidity conditions. This project displays my ability not only to develop a functioning program, but to set up a real-world device which can utilize the program and provide usable data as a result. 
	I have made improvements to the Python program code to make the code easier to understand when viewed. The purpose of some variables has been made more evident with clearer naming practices. I also have removed some redundant variables I found when completing the code review. I had the temperature and humidity readings transferred to a new set of variables before being saved to the JSON file, which was unnecessary. This portion of the code was reworked, and the redundant variables removed. These modifications have made the code better structured and more readable when viewed by someone unfamiliar with the program.
	Enhancements were also made to the functionality to the program. I have added a portion of code to initiate LED indication for when the temperature drops below 60 degrees. Other aspects of the various LED indication conditions have also been improved. For instance, I created additional statements so that all combinations of circumstances are covered. Previously, the program would illuminate the red LED if the temperature reads over 95 degrees, but no other instructions were provided for the other LEDs within this condition. I have included additional instructions ensuring the other LEDs are set to off in this condition. I then added an additional condition for if the humidity is over 80 percent and the temperature is over 95 degrees, which results in both all three LEDs being illuminated. Additionally, I have decreased the time between readings to 10 minutes apart, as this is more conducive my needs for the device. 
	The HTML graph which was a part of the project has had minor enhancements. I have updated the x-axis to coordinate with the new 10-minute time frame. I have also created two additional HTML files, one for only temperature data and one for only humidity data. This makes the details easier to read and understand for the user, and the client would likely want access to multiple graphs to view and utilize the results from the weather station.


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

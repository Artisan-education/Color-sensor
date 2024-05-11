# PiicoDev VEML6040 minimal example code
# This program reads light data from the PiicoDev VEML6040 Colour Sensor
# Displays Raw Data, and classifies colours as fruits

from colorsensor import ColorSensor
from time import sleep_ms # cross-platform compatible sleep function

# Associate a hue value with a fruit name
fruitList = {
    "apple":0,
    "carrot":60,
    "lime":120
    }

cs = ColorSensor(bus=0, sda=0, scl=1) # initialise the sensor
sleep_ms(100)
while True:
#     ### Example 1: Print Raw RGB Data
#     data = colourSensor.readRGB() # Read the sensor (Colour space: Red Green Blue)
#     red = data['red'] # extract the RGB information from data
#     grn = data['green']
#     blu = data['blue']
#     
#     print(str(blu) + " Blue  " + str(grn) + " Green  " + str(red) + " Red") # Print the data. Printing as BGR so the Thonny plot-colours match nicely :)

    ### Example 2: Classify the colour being shown - eg. a fruit sorting machine
    data = cs.readHSV() # Read the sensor (Colour space: Hue Saturation Value)
    hue = data['hue'] # extract the Hue information from data

    label = cs.classifyHue() # Read the sensor again, this time classify the colour
    print(str(label) + " Hue: " + str(hue)) # Show the label and the corresponding hue

    sleep_ms(100)
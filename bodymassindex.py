# Asha Blewett
# calculate a persons BMI

import os
os.system ('cls')

weight = int(input("your weight in kg: ")) 
weight2= weight * weight 
height = int(input("your height in meters: "))
BMI= weight2/height 

print ("Your BMI is: ", BMI) 

if (BMI < 14.5):
    print ("you're underweight")

if (BMI > 40):
    print ("you're overweight")

if (BMI > 14.5) and (BMI < 40):
    print ("you're healthy")

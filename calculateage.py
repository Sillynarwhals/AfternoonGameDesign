# Asha Blewett
# calculate age

import os
os.system("cls")

number1 = int(input("the current year"))
number2 = int(input("year of birth"))

subtract=number1 - number2
print(subtract) #display age from two numbers

if (subtract > 50):
    print ("you are old")
if (subtract < 50):
    print ("you are young")

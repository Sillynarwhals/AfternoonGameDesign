# Asha Blewett
# find if number is even or odd

import os
os.system ('cls')

number= int(input("any number between 1-100"))
Modulus= number%2
if (Modulus==0):
    print ("number is even")
if (Modulus==1):
    print ("number is odd")
Multiple= number%5
if (Multiple==0):
    print ("number is a multiple of 5")
if (Multiple>0):
    print ("number is not a multiple of 5")
Multiple2= number%3
if (Multiple2==0):
    print ("number is a multiple of 3")
if (Multiple2>0):
    print ("number is not a multiple of 3")

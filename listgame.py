# Asha Blewett
# 
import os
import random
os.system ('cls')

for i in range (74):
    print ("*", end = "")
print ()
print ( "|----------------------- Color Wheel ------------------------------------|")
print ("| The goal of this game is to guess the random color chosen from a list  |")
print ("|If you guess correct you win. If you guess incorrect reset and try again|")
print ("|                         good luck ^v^                                  |")
for i in range (74):
    print ("*", end = "")
MyColors= ["pink", "red", "orange", "yellow", "green", "blue", "purple", "brown", "black", "white"]
print ()
for i in range (1):
    element= random.choice(MyColors)



for i in range (10):
    guess= input ("input a color:")

    if guess== element:
        print ("Congrats! You won :)")
        break
    else:
        print ("f Try again!")
        continue


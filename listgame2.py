# Asha Blewett
# guessing game for colors
#my colors= pink, red, orange, yellow, green, blue, purple, brown, black, white
from ast import Break
from audioop import add
import os
import random
from unicodedata import name
os.system ('cls')

for i in range (74):
    print ("*", end = "")
print ()
print ( "|----------------------- Color Wheel ------------------------------------|")
print ("| 1. Color                                                                |")
print ("| 2. Fruit                                                                |")
print ("| 3. Animal                                                               |")
print ("|If you guess correct you win. If you guess incorrect reset and try again |")
print ("|                         good luck ^v^                                   |")
for i in range (74):
    print ("*", end = "")
MyColors= ["pink", "red", "orange", "yellow", "green", "blue", "purple", "brown", "black", "white"]
MyFruit= ["apple", "banana", "orange", "grapefruit", "blueberry", "mango", "strawberry", "rasberry", "watermelon","blackberry"]
MyAnimal= ["dog", "cat", "snake", "cow", "pig", "chicken", "fish","bear", "ant", "turtle"]
print ()
count=0
Game=True

name = input("What is your name? ")
print(name, end = ", ")
answer = input("would you like to play the game? ")
answer = answer.lower()
if 'n' in answer:
    Game = False
    
    

while True:
    choice= input("What game would you like to play 1, 2, or 3? ")
    try:
        choice=int(choice)
        if choice > 0 and choice < 4:
            break
        else:
            print("give me 1,2, or 3")
    except:
        print("Please enter a number")   
    
def selectWord(choice):
    global element
    if choice==1: 
        element= random.choice(MyColors)
    if choice==2:
        element=random.choice(MyFruit)
    if choice==3:
        element=random.choice(MyAnimal)
    
for i in range (30):
    guess= input ("Please put your guess here:")

    if guess== random.choice(MyColors):
        print ("Congrats! You won :)")
        break
    if guess== random.choice(MyFruit):
        print ("Congrats! You won :)")
        break
    if guess== random.choice(MyAnimal):
        print ("Congrats! You won :)")
        break
    else:
        print ("f Try again!")
        continue


score = 200-40*(count-1) 
high=0
if score > high:
    score=high
    scrLine=str(high)+"\t"+ name +"\n"
    myFile = open("scre.txt", 'a')
    myFile.write(scrLine)
    myFile.close()
else:
    print ("Your Highest score is"+ str(high))
    input("Please press enter ")

    #os.system('cls')
    answer = input("Do you want to play again? ")
    if ('n' or 'N') in answer:
        Game = False
        print("Thank you for playing")
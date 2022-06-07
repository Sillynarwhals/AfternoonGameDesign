# Daniel Walker
# from ctypes.wintypes import WORD
from ast import While
import random
import os 

os.system ('cls')
from time import sleep
seconds=.5

list = ["coral","scallop","sea urchin","oyster","mussel","cockle","clam","geoduck","abelone","ostrea"]
theword=random.choice(list)
count= 0
Game= True
theword=""
def hint():
    global count
    if count==0:
        print("|*************************************|")
        print("|         Here is a new hint          |")
        print("|These creatures all have a hard shell|")
        print("|        only 2 shells in fact        |")
        print("|*************************************|")
        

    elif count==1:
        print("|**************************************|")
        print("|       Here is your final hint        |")
        print("|  These creatures almost never move   |")
        print("|**************************************|")      
        print("|***************************************|")
    
    else:
        print ("You are horrible at guessing")

    while Game:
        print("|         Guess The Animal!!!           |")
        print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
        print("| 1. Animals                            |")
        print("| 2. Fruits                             |")
        print("| 3. Colors                             |")
        print("|   There are 10 animals in this game   |")
        print("|     You must guess one of them        |")
        print("|First we will provide you with one hint|")
        print("|           !Your Hint Is!              |")
        print("|  These animals are big fans of water  |")
        print("|***************************************|")

name= input("What is your name?")
print(name, end= ",")
answer= input("would you like to play the game?")
answer= answer.lower()
if 'n' in answer:
    Game= False
 
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

os.system('cls')
check= True
while check and count <5:
    guess1=input("plese put your guess here: ")

    if guess1 == theword:
        print("Congrats, You got it")
        check= False
    else:
        hint()
    count+= 1
    
    os.system ('cls')    
    answer= input ("Do you want to play again?")
    if ('n'or 'N') in answer:
        Game= False
        print ("Thanks for playing")


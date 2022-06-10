#Asha Blewett
#We are going to learn basic pygame functions


import pygame, os, time
pygame.init()
os.system('cls')

WIDTH = 700#amount of pixels
HEIGHT = 700
colors={"white":(255,255,255),"pink":(255,0,255),"purple":(125,0,125),"dark green":(0,153,0),"orange":(255,128,0),"yellow":(255,255,0),"grey":(128,128,128),"light blue":(0,255,255),"dark blue":(0,0,153),"cyan":(0,255,177)}
clr=colors.get("white")
#create a display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")# title of window
blueClr = (0,0,255) #represents pixels of r,g and b
redClr= (255,0,0)
cyanClr= (0,255,177)
screen.fill(cyanClr)
pygame.display.update() #have to do this after any change that the user can see
pygame.time.delay(3000)

hb= 50
wb= 50
xb= 325
yb= 325
square = (xb,yb,wb,hb) #create the object to draw


run = True
background = clr
while run:
    screen.fill(background)#loop that prevents the window from automatically closing
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #code to quit window without any error
            run = False
            print ("you quit")
    #rect(surface, color, object)        
    pygame.draw.rect(screen, cyanClr, square)
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, blueClr, (200, 200),25)
    pygame.display.update()
    
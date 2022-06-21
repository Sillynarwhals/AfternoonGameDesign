# Asha Blewett
# Final game code: Froggy

import pygame, time,os,random, math, datetime, sys


date=datetime.datetime.now()
pygame.init()#initialize the pygame package
TITLE_FONT = pygame.font.SysFont('comicsans', 40) #font for Title
MENU_FONT = pygame.font.SysFont('comicsans', 20) #font for words 
os.system('cls')
#dimensions
WIDTH=700
HEIGHT=700
#list of colors
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), "red": (255,0,0), "black": (0,0,0), "yellow": (255,255,0)}
#Images
man = pygame.image.load('PygameFile\images\player.png')
man = pygame.transform.scale(man, (50, 50))
treasure = pygame.image.load('PygameFile\images\\treasure.png')
treasure = pygame.transform.scale(treasure, (50, 50))
#car1= pygame.image.load('PygameFile\images\car2.png')
#car1= pygame.transform.rotate(car1, 90)
#car1= pygame.transform.scale(car1,(500,550) )
bg= pygame.image.load('PygameFile\images\\road bg.png')
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
#create screen window
screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Road")
pygame.display.update()

clock = pygame.time.Clock()
#Sprite Variables 
x = 50
y = HEIGHT//6
tx = 600
ty = 300
cx = 100
cy= 10
vel = 4
twidth = 14
theight = 12
width = 12
height = 18.5
left=False
right=False
walkCount = 0
def redrawGameWindow():
    global walkCount
    screen.blit(bg, (0,0))
    screen.blit(treasure,(tx,ty))
    #screen.blit(car1, (cx, cy))
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        screen.blit(man, (x,y))
        walkCount += 1
    elif right:
        screen.blit(man, (x,y))
        walkCount +=1
    else:
        screen.blit(man, (x,y))
    
    pygame.display.update()

run= True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("you quit")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        left= True
        right=False
    
    elif keys[pygame.K_RIGHT] and x < WIDTH-width - 50:
        x += vel
        right= True
        left= False

    if keys[pygame.K_UP] and y > 0:
        y -= vel
        left=False
        right= False
    
    if keys [pygame.K_DOWN] and y < HEIGHT-height-50:
        y += vel
        left=False
        right=False
    
    redrawGameWindow()

    




    




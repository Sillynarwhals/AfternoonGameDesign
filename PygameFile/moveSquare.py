# Asha Blewett
#We are going to be learning basic pygame functions
#creating screens,clrs, shape
# K_UP                  up circle

import pygame, os, time,random,math
pygame.init()
os.system('cls')

WIDTH = 900#amount of pixels
HEIGHT = 700
colors = {"white":(255,255,255), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
clr = colors.get("white")
#create a display window 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game") # title of the window
#images
bg=pygame.image.load("PygameFile\images\bgSmaller.jpg")
char = pygame.transform.scale
screen.blit(bg, (0,0))
pygame.display.update
# pygame.display.update() #have to do after any change that the user can see
pygame.time.delay(5000)

blueClr = (0,0,255)
redClr = (255,0,0)
cyanClr = (0, 255, 177)


#var for the square
hb = 50
wb = 50
xb = 325
yb = 325
square = pygame.Rect(xb,yb,wb,hb) #create the object to draw
squareClr=colors.get("purple")

#char var
charx= xb
chary= yb


#var for the circle
cx=350
cy=350
rad=25
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)
insSquare=pygame.Rect(xig,yig,ibox,ibox)
#bounce
mountainSquare = pygame.Rect(250,300,180,250)

speed=2

circleClr=colors.get("green")
background = redClr
run = True
while run:
    # screen.fill(background)
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("you quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            print(mousePos)
    keys=pygame.key.get_pressed() #provide a list of all keys 

    if keys[pygame.K_a] and square.x> speed:
        square.x -=speed
        charx -=speed
    if keys[pygame.K_d] and square.x < WIDTH-(wb+speed):
        square.x +=speed
        charx +=speed
    if keys[pygame.K_w] and square.y> speed:
        square.y -=speed
        chary -=speed
    if keys[pygame.K_s] and square.y < HEIGHT-(hb+speed):
        square.y +=speed
        chary +=speed
    if keys[pygame.K_LEFT] and cx> (speed+rad):
        cx -=speed
        insSquare.x -=speed
    if keys[pygame.K_RIGHT] and cx < WIDTH-(rad+speed):
        cx +=speed
        insSquare.x +=speed
    if keys[pygame.K_UP] and cy> (speed+rad):
        cy -=speed
        insSquare.y -=speed
    if keys[pygame.K_DOWN] and cy < HEIGHT-(rad+speed):
        cy +=speed
        insSquare.y +=speed
    #rect(surface, color, rect)-> Rect
    #if square.collidepoint((cx,cy)):
    if square.colliderect(insSquare):
        print("BOOM")
        cx=random.randint(rad,WIDTH-rad)
        cy=random.randint(rad,HEIGHT-rad)
        rad +=5
        ibox = rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        insSquare=pygame.Rect(xig,yig,ibox,ibox)
        #mountain collide
        if square.colliderect(mountainSquare):
            square.x = 10
            square.y = 10
            charx = 10
            chary = 10
    #rect(surface,background,rect)
    pygame.draw.rect(screen, squareClr, square)
    pygame.draw.rect(screen,background,insSquare)
    pygame.blit(char, (charx,chary))

    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, circleClr, (cx, cy), rad)
    pygame.draw.rect(screen, colors.get("white"), mountainSquare)


    pygame.display.update()
    pygame.time.delay(20)
# Asha Blewett
#We are going to be learning basic pygame functions
#creating screens,clrs, shape

import pygame, os, time,random,math
pygame.init()


#print(pygame.font.get_fonts())
#pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans',40)
MENU_FONT =pygame.font.SysFont('comicsans', 20)

os.system('cls')
WIDTH = 700 #amount of pixels
HEIGHT = 700 #like constant
colors = {"white":(255,255,255), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
clr = colors.get("white")
message = ['Instructions', 'Settings', 'Game 1', 'Game2', 'Scoreboard', 'Exit']
#create a display window 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game") # title of the window
#images
bg=pygame.image.load('PygameFile\images\bgSmaller.jpg')
screen.blit(bg)
dude=pygame.image('PygameFile\images\PixelArtTutorial.png')
dude = pygame.transform.scale(dude, (1200,720))

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

#var for the circle
cx=350
cy=350
rad=25
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse variables
mx = 0
my = 0

insSquare=pygame.Rect(xig,yig,ibox,ibox)

speed=2

circleClr=colors.get("green")
background = redClr
run = True
Game = False

def menu():
    Title = TITLE_FONT.render("Circle eats Square", 1, colors.get("blue"))
    screen.fill(colors.get('white'))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    yMenu= 155
    for item in message:
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        screen.blit(text, (40, yMenu))

        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
    pygame.time.delay(5000)
def Instructions():
    #rendering text objects
    Title = TITLE_FONT.render("Instructions", 1, colors.get("blue"))
    text1 = MENU_FONT.render("Yes", 1, colors.get("blue"))
    text2 = MENU_FONT.render("No", 1, colors.get("blue"))

    #fills screen with white
    screen.fill(colors.get("white"))

    #creating button options
    Button_1 = pygame.Rect(200, 400, 100, 50)
    Button_2 = pygame.Rect(400, 400, 100, 50)
    pygame.draw.rect(screen, colors.get("green"), Button_1 )
    pygame.draw.rect(screen, colors.get("green"), Button_2 )

    #Instructions
    myFile = open("PygameFile\instructions.txt", "r")
    content = myFile.readlines()
    
    #var to control change of line
    yi = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi += 40

    myFile.close()

    #rendering fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    screen.blit(text1, (225, 410))
    screen.blit(text2, (425, 410))
    
    pygame.display.update()
    while True:
        mousePos = pygame.mouse.get_pos()
        mx = mousePos [0]
        my = mousePos [1]
        if Button_1.collidepoint((mx, my)):
            return True
        if Button_2.collidepoint((mx, my)):
            return False
menu()
run = Instructions()

while run:
    # screen.fill(background)
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("you quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            mx = mousePos[0]
            my = mousePos [1]
            Instructions()

        screen.blit(bg, (0,0))
        keys=pygame.key.get_pressed() # this is a list of all keys 
        if keys[pygame.K_a] and square.x> speed:
            square.x -=speed
        if keys[pygame.K_d] and square.x < WIDTH-(wb+speed):
            square.x +=speed
        if keys[pygame.K_w] and square.y> speed:
            square.y -=speed
        if keys[pygame.K_s] and square.y < HEIGHT-(hb+speed):
            square.y +=speed
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
        if square.colliderect(cx,cy):
            cx=random.randint(rad,WIDTH-rad)
            cy=random.randint(rad,HEIGHT-rad)
            print("BOOM")
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
            #rect(surface,background,rect)
            pygame.draw.rect(screen, squareClr, square)
            pygame.blit/dude
            #circle(surface, color, center, radius)
            pygame.draw.circle(screen, circleClr, (cx, cy), rad)
            pygame.draw.rect(screen, squareClr, insSquare)
            pygame.display.update()
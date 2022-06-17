# Asha Blewett
#06/09/2022
# #We are learning pygame basic functins, 
# # creating screens, clrs, shape ,move 
# # move  the square
# # K_UP                  up arrow
# # K_DOWN                down arrow
# # K_RIGHT               right arrow
# # K_LEFT                left arrow
# #picture = pygame. image. load(filename)
# #picture = pygame. transform. scale(picture, (1280, 720))
# #bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')


import pygame, time,os,random, math, datetime, sys
date=datetime.datetime.now()
pygame.init()#initialize the pygame package

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), "red": (255,0,0), "black": (0,0,0), "yellow": (255,255,0)}
clr=colors.get("limeGreen")
message=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window
clock=pygame.time.Clock()
#boxes for menu
Bx=WIDTH//3
By= HEIGHT//20
Button_menu=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_instruct=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_settings=pygame.Rect(Bx, 200, WIDTH//4, 40)
Button_Game1=pygame.Rect(Bx, 250, WIDTH//4, 40)
Button_Game2=pygame.Rect(Bx, 300, WIDTH//4, 40)
Button_score=pygame.Rect(Bx, 350, WIDTH//4, 40)
Button_exit=pygame.Rect(Bx, 400, WIDTH//4, 40)
Button_colors=pygame.Rect(Bx, 400, WIDTH//4, 40)
Button_size=pygame.Rect(Bx, 400, WIDTH//4, 40)
Button_sound=pygame.Rect(Bx, 400, WIDTH//4, 40)

#images
bg=pygame.image.load('PygameFile\images\\bgSmaller.jpg')
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
char = pygame.image.load('PygameFile\images\PixelArtTutorial.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)


#square Var
hb=50
wb=50
xb=100
rad=25
yb=300

charx = xb
chary = yb
#circle Var
cx=350
cy=350
speed=2
# insSquare Var
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse varuables
mx = 0
my = 0

square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
insSquare=pygame.Rect(xig,yig,ibox,ibox)
squareClr=colors.get("pink")
#keep running create a lp
mountainSquare=pygame.Rect(250,320,180,250)
circleClr=colors.get("blue")
backgrnd=colors.get("limeGreen")
run = True
Game = False

def mainMenu():
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_settings)
    Title = TITLE_FONT.render("Circle eats Square Menu", 1, colors.get("blue"))
    screen.fill(colors.get('white'))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    yMenu=150
    
    for item in message:
        Button_menu=pygame.Rect(274, yMenu, 125, 40)
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        pygame.draw.rect(screen, colors.get('limeGreen'), Button_menu)
        screen.blit(text, (280, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
    MENU=True
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("You quit")
                pygame.display.quit()
                MENU=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_instruct.collidepoint((mx, my)):
                    Instructions()
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_Game1.collidepoint((mx, my)):
                    GameOne()
                if Button_score.collidepoint((mx, my)):
                    scoreboard()
                if Button_exit.collidepoint((mx, my)):
                    exit()
                if Button_Game2.collidepoint((mx, my)):
                    GameTwo()
    
def Instructions():
    #rendering text objects
    Title = TITLE_FONT.render("Instructions", 1, colors.get("blue"))

    #fills screen with white
    screen.fill(colors.get("white"))

    #creating button options
    Button_1 = pygame.Rect(25, 350, 200, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)

    #Instructions
    myFile = open("PygameFile\instructions.txt", "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))

    pygame.display.update()
    Instructions = True
    while Instructions:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Instructions=False
                pygame.display.quit()
                print("You quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    mainMenu() 


def settings():
    TITLE_FONT = pygame.font.SysFont('comicsans', 40)
    MENU_FONT = pygame.font.SysFont('comicsans', 20)
    title=TITLE_FONT.render('Settings', 1, colors.get('black'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('black'))
    colort=MENU_FONT.render('Change colors', 1, colors.get('black'))
    sizet= MENU_FONT.render('Change text size', 1, colors.get('black'))
    soundt= MENU_FONT.render('Change screen size', 1, colors.get('black'))

    Bolor= (colors.get("red"))
    size= (colors.get("pink"))
    Sound= (colors.get("blue"))
    menu= (colors.get("limeGreen"))
    screen.fill(colors.get('white'))
    

    Button_3 = pygame.Rect(Bx, 400, WIDTH//4, 40)
    Button_colors=pygame.Rect(Bx, 120, WIDTH//4, 40)
    Button_size=pygame.Rect(Bx, 200, WIDTH//4, 40)
    Button_sound=pygame.Rect(Bx, 300, WIDTH//4, 40)
    pygame.draw.rect(screen, Bolor, Button_3)
    pygame.draw.rect(screen, size, Button_colors)
    pygame.draw.rect(screen, Sound, Button_size)
    pygame.draw.rect(screen, menu, Button_sound)
    screen.blit(title, (Bx,50))
    screen.blit(colort, (Bx,120))
    screen.blit(sizet, (Bx,200))
    screen.blit(soundt, (Bx,300))
    screen.blit(text, (Bx,400))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                sys.exit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()
                if Button_colors.collidepoint((mx, my)):
                    print("Change background")
                    screen.fill(colors.get('yellow'))
                    Button_3 = pygame.Rect(Bx, 400, WIDTH//4, 40)
                    Button_colors=pygame.Rect(Bx, 120, WIDTH//4, 40)
                    Button_size=pygame.Rect(Bx, 200, WIDTH//4, 40)
                    Button_sound=pygame.Rect(Bx, 300, WIDTH//4, 40)
                    pygame.draw.rect(screen, Bolor, Button_3)
                    pygame.draw.rect(screen, size, Button_colors)
                    pygame.draw.rect(screen, Sound, Button_size)
                    pygame.draw.rect(screen, menu, Button_sound)
                    screen.blit(title, (Bx,50))
                    screen.blit(colort, (Bx,120))
                    screen.blit(sizet, (Bx,200))
                    screen.blit(soundt, (Bx,300))
                    screen.blit(text, (Bx,400))
                    pygame.display.update()
                elif Button_size.collidepoint((mx, my)):
                    print ("Change Background and Increase Text Size")
                    screen.fill(colors.get('yellow'))
                    Button_3 = pygame.Rect(Bx, 400, WIDTH//4, 40)
                    Button_colors=pygame.Rect(Bx, 120, WIDTH//4, 40)
                    Button_size=pygame.Rect(Bx, 200, WIDTH//4, 40)
                    Button_sound=pygame.Rect(Bx, 300, WIDTH//4, 40)
                    pygame.draw.rect(screen, Bolor, Button_3)
                    pygame.draw.rect(screen, size, Button_colors)
                    pygame.draw.rect(screen, Sound, Button_size)
                    pygame.draw.rect(screen, menu, Button_sound)
                    TITLE_FONT= pygame.font.SysFont('comicsans', 60)
                    MENU_FONT= pygame.font.SysFont('comicsans', 40)
                    img = TITLE_FONT.render('Settings', True, colors.get("black"))
                    img2 = MENU_FONT.render('Change colors', True, colors.get("black"))
                    img3 = MENU_FONT.render('Change size', True, colors.get("black"))
                    img4 = MENU_FONT.render('Change sound', True, colors.get("black"))
                    img5 = MENU_FONT.render('Return to Menu', True, colors.get("black"))
                    screen.blit(img2, (Bx, 105))
                    screen.blit(img3, (Bx, 185))
                    screen.blit(img4, (Bx, 285))
                    screen.blit(img, (Bx, 35))
                    screen.blit(img5, (Bx, 385))
                    pygame.display.update()

                if Button_size.collidepoint((mx, my)):
                    print ("Increase Text Size")
                    screen.fill(colors.get('white'))
                    Button_3 = pygame.Rect(Bx, 400, WIDTH//4, 40)
                    Button_colors=pygame.Rect(Bx, 120, WIDTH//4, 40)
                    Button_size=pygame.Rect(Bx, 200, WIDTH//4, 40)
                    Button_sound=pygame.Rect(Bx, 300, WIDTH//4, 40)
                    pygame.draw.rect(screen, Bolor, Button_3)
                    pygame.draw.rect(screen, size, Button_colors)
                    pygame.draw.rect(screen, Sound, Button_size)
                    pygame.draw.rect(screen, menu, Button_sound)
                    TITLE_FONT= pygame.font.SysFont('comicsans', 60)
                    MENU_FONT= pygame.font.SysFont('comicsans', 40)
                    img = TITLE_FONT.render('Settings', True, colors.get("black"))
                    img2 = MENU_FONT.render('Change colors', True, colors.get("black"))
                    img3 = MENU_FONT.render('Change size', True, colors.get("black"))
                    img4 = MENU_FONT.render('Change sound', True, colors.get("black"))
                    img5 = MENU_FONT.render('Return to Menu', True, colors.get("black"))
                    screen.blit(img2, (Bx, 105))
                    screen.blit(img3, (Bx, 185))
                    screen.blit(img4, (Bx, 285))
                    screen.blit(img, (Bx, 35))
                    screen.blit(img5, (Bx, 385))
                    pygame.display.update()
                elif Button_colors.collidepoint((mx, my)):
                    print("Increase Text Size and Background")
                    screen.fill(colors.get('yellow'))
                    Button_3 = pygame.Rect(Bx, 400, WIDTH//4, 40)
                    Button_colors=pygame.Rect(Bx, 120, WIDTH//4, 40)
                    Button_size=pygame.Rect(Bx, 200, WIDTH//4, 40)
                    Button_sound=pygame.Rect(Bx, 300, WIDTH//4, 40)
                    pygame.draw.rect(screen, Bolor, Button_3)
                    pygame.draw.rect(screen, size, Button_colors)
                    pygame.draw.rect(screen, Sound, Button_size)
                    pygame.draw.rect(screen, menu, Button_sound)
                    TITLE_FONT= pygame.font.SysFont('comicsans', 60)
                    MENU_FONT= pygame.font.SysFont('comicsans', 40)
                    img = TITLE_FONT.render('Settings', True, colors.get("black"))
                    img2 = MENU_FONT.render('Change colors', True, colors.get("black"))
                    img3 = MENU_FONT.render('Change size', True, colors.get("black"))
                    img4 = MENU_FONT.render('Change sound', True, colors.get("black"))
                    img5 = MENU_FONT.render('Return to Menu', True, colors.get("black"))
                    screen.blit(img2, (Bx, 105))
                    screen.blit(img3, (Bx, 185))
                    screen.blit(img4, (Bx, 285))
                    screen.blit(img, (Bx, 35))
                    screen.blit(img5, (Bx, 385))
                    pygame.display.update()

                if Button_sound.collidepoint((mx, my)):
                    WIDTH=500
                    HEIGHT=500
                    screen2=pygame.display.set_mode((WIDTH,HEIGHT)) 
                    pygame.display.update()

                    



def scoreboard():
    name= input("Asha")
    high=0
    count=0
    score = 200+40*(count-1) 
    title=TITLE_FONT.render('Scoreboard', 1, colors.get('blue'))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("blue"))

    screen.fill(colors.get('white'))
    Button_3 = pygame.Rect(25, 350, 200, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    
    screen.blit(title, (250,50))
    screen.blit(text3, (30, 355))
    pygame.display.update()

    print(score)
    File=open('PygameFile\PygameScore.txt', 'a')
    File.write(str(score))
    File.close()

    myFile = open("PygameFile\PygameScore.txt", 'r')
    stuff=myFile.readlines()
    myFile.close()
    for line in stuff:
        screen.blit(line, (200,50))
        pygame.display.update()
        print(line)
        

    with open('PygameFile\PygameScore.txt') as f:
        if score > high:
            score=high
            scrLine=str(high)+"\t"+name +"\n"
            myFile = open("PygameFile\PygameScore.txt", 'a')
            myFile.write(scrLine)
            myFile.close()
            


    scoreboard=True
    while scoreboard:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()

def exit():
    title=TITLE_FONT.render('Bye-Bye', 1, colors.get('blue'))
    screen.fill(colors.get('white'))
    screen.blit(title, (275, 100))
    sys.exit()
    pygame.display.update()

def Game_2():
    global score, cx, cy, rad, run, Game, count, score, charx, chary, mx, my, square, insSquare
    score=0
    count=0
    score=200+40*(count-1)
    #squarevar
    xb=100
    yb=300
    charx = xb
    chary = yb
    #circle var
    cx=350
    cy=350
    rad=25
    speed=2
    ibox = rad*math.sqrt(2)
    xig = cx-(ibox/2)
    yig = cy-(ibox/2)
    bg=pygame.image.load('PygameFile\images\\bg.png')
    run= Game
    Game=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
                print(score)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
        screen.blit(bg, (0,0))
        char.blit()
        #image 1
        char=pygame.image.load('PygameFile\images\PixelArtTutorial.png')
        char=pygame.transform.scale(char, (WIDTH//7, WIDTH//7))
        #image 2
        char2=pygame.image.load('PygameFile\images\standing.png')
        char2=pygame.transform.scale(char2, (WIDTH//10,WIDTH//10 )) 
        pygame.display.update()

        keys= pygame.key.get_pressed() #this is a list
         #char movement
        if keys[pygame.K_d] and charx < WIDTH-wb:
            charx += speed
        if keys[pygame.K_a] and charx > 0:
            charx -= speed
        if keys[pygame.K_s] and chary < HEIGHT-hb:
            chary += speed
        if keys[pygame.K_w] and chary > 0:
            chary -= speed
        #circle and inscribed square movement
        if keys[pygame.K_RIGHT] and cx < WIDTH-rad:
            cx += speed
        if keys[pygame.K_LEFT] and cx > 0+rad:
            cx -= speed
        if keys[pygame.K_DOWN] and cy < HEIGHT-rad:
            cy += speed
        if keys[pygame.K_UP] and cy > 0+rad:
            cy -= speed
            
        if square.colliderect(insSquare): 
            print("BOOM")
            count+=1
            charx = random.randint(rad, WIDTH-rad)
            chary = random.randint(rad, HEIGHT-rad)
            rad += 5
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        if count==5:
            print("you lose")
            print (score)
            run=False
            pygame.display.quit()
        pygame.display.update()






def Game_1():
    global mx, my, insSquare, charx, chary, cx, cy, rad, run, Game, count, score
    count=0
    score=200-40*(count-1) 
    run= Game
    Game=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
                print(score)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
        screen.blit(bg, (0,0))
        #rect(surface, color, object)
        pygame.draw.rect(screen, colors.get("blue"), square)
        pygame.draw.rect(screen, colors.get("blue"), insSquare)
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, colors.get("red"), (cx, cy), rad)
        pygame.display.update()

        keys= pygame.key.get_pressed() #this is a list
         #square movement
        if keys[pygame.K_d] and square.x < WIDTH-wb:
            square.x += speed
            charx += speed
        if keys[pygame.K_a] and square.x > 0:
            square.x -= speed
            charx -= speed
        if keys[pygame.K_s] and square.y < HEIGHT-hb:
            square.y += speed
            chary += speed
        if keys[pygame.K_w] and square.y > 0:
            square.y -= speed
            chary -= speed
        #circle and inscribed square movement
        if keys[pygame.K_RIGHT] and cx < WIDTH-rad:
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_LEFT] and cx > 0+rad:
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_DOWN] and cy < HEIGHT-rad:
            cy += speed
            insSquare.y += speed
        if keys[pygame.K_UP] and cy > 0+rad:
            cy -= speed
            insSquare.y -= speed
        #circle square collide
        if square.colliderect(insSquare): 
            print("BOOM")
            count+=1
            cx = random.randint(rad, WIDTH-rad)
            cy = random.randint(rad, HEIGHT-rad)
            rad += 5
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        if count==5:
            print("you lose")
            print (score)
            run=False
            pygame.display.quit()
        pygame.display.update()


def GameOne():
    title=TITLE_FONT.render('Game Level 1', 1, colors.get('blue'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
    text2=MENU_FONT.render('Play the Game', 1, colors.get('blue'))

    screen.fill(colors.get('white'))

    Button_3 = pygame.Rect(25, 350, 175, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    Button_4=pygame.Rect(325, 350, 175, 50)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_4)

    screen.blit(title, (275,50))
    screen.blit(text, (30,355))
    screen.blit(text2, (330, 355))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()
                if Button_4.collidepoint((mx, my)):
                    Game_1()



def GameTwo():
        title=TITLE_FONT.render('Game Level 2', 1, colors.get('blue'))
        text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
        text2=MENU_FONT.render('Play the Game', 1, colors.get('blue'))

        screen.fill(colors.get('white'))

        Button_3 = pygame.Rect(25, 350, 175, 50)
        pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
        Button_4=pygame.Rect(325, 350, 175, 50)
        pygame.draw.rect(screen, colors.get('limeGreen'), Button_4)

        screen.blit(title, (275,50))
        screen.blit(text, (30,355))
        screen.blit(text2, (330, 355))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    pygame.display.quit()
                    print("You quit")
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    mx=mousePos[0]
                    my=mousePos[1]
                    if Button_3.collidepoint((mx, my)):
                        mainMenu()
                    if Button_4.collidepoint((mx, my)):
                        Game_2()

mainMenu()
Instructions()
pygame.display.update()
clock.tick(60)
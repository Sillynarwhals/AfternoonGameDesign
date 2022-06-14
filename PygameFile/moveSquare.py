# Asha Blewett
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


import pygame, time,os,random, math, datetime
date=datetime.datetime.now()
pygame.init()#initialize the pygame package

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
clr=colors.get("limeGreen")
message=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window

#boxes for menu
Button_menu=pygame.Rect(274, 125, 125, 40)
Button_instruct=pygame.Rect(274, 150, 125, 40)
Button_settings=pygame.Rect(274, 200, 125, 40)
Button_Game1=pygame.Rect(274, 250, 125, 40)
Button_Game2=pygame.Rect(274, 300, 125, 40)
Button_score=pygame.Rect(274, 350, 125, 40)
Button_exit=pygame.Rect(274, 400, 125, 40)
#images
bg=pygame.image.load('PygameFile\images\\bgSmaller.jpg')
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
cx=350
cy=350
speed=2
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)




#mouse varuables
mx = 0
my = 0

square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
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
    title=TITLE_FONT.render('Settings', 1, colors.get('blue'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))

    screen.fill(colors.get('white'))

    Button_3 = pygame.Rect(25, 350, 200, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)

    screen.blit(title, (275,50))
    screen.blit(text, (30,355))
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


def scoreboard():
    score=0
    high=0
    title=TITLE_FONT.render('Scoreboard', 1, colors.get('blue'))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("blue"))

    screen.fill(colors.get('white'))
    Button_3 = pygame.Rect(25, 350, 200, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    
    screen.blit(title, (250,50))
    screen.blit(text3, (30, 355))
    pygame.display.update()
    
    print(score)
    File=open('pygameFiles\scoreboard.txt', 'a')
    File.write(str(score))
    File.close()

    with open('pygameFiles\scoreboard') as f:
        if score>high:
            high=score
    File.write(str(score)) + '\t' + '\t'+ date.strftime('%m/%d/%Y')
    File.close()

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
    pygame.display.update()

def Level_1():
    Game=True
    while Game:
        global score,hb, wb, xb, rad, yb, charx, chary, cx, cy, speed, ibox, xig, yig
        hb=50
        wb=50
        xb=100
        rad=25
        yb=300
        charx = xb
        chary = yb
        cx=350
        cy=350
        speed=2
        ibox = rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        pygame.draw.rect(screen, colors.get("white"), mountainSquare)
        screen.blit(bg, (0,0))
        pygame.display.update()
        keys = pygame.key.get_pressed() #allow us to see what key was pressed
        #square movement
        if keys[pygame.K_d] and square.x < WIDTH-wb:
            square.x += speed
            charx+=speed
        if keys[pygame.K_a] and square.x > 0:
            square.x -= speed
            charx-= speed
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
        score=0
        insSquare=pygame.Rect(xig,yig,ibox,ibox)
    #circle square collide
        if square.colliderect(insSquare): 
            print("BOOM")
            score+=1
            cx = random.randint(rad, WIDTH-rad)
            cy = random.randint(rad, HEIGHT-rad)
            rad = 5
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

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
                print (score)
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()
                if Button_4.collidepoint((mx, my)):
                    Level_1()


Instructions()


win = pygame.display.set_mode((500,480))
clock = pygame.time.Clock()
walkRight = [pygame.image.load('PygameFile\images\R1.png'), pygame.image.load('PygameFile\images\R2.png'), pygame.image.load('PygameFile\images\R3.png'), pygame.image.load('PygameFile\images\R4.png'), pygame.image.load('PygameFile\images\R5.png'), pygame.image.load('PygameFile\images\R6.png'), pygame.image.load('PygameFile\images\R7.png'), pygame.image.load('PygameFile\images\R8.png'), pygame.image.load('PygameFile\images\R9.png')]
walkLeft = [pygame.image.load('PygameFile\images\L1.png'), pygame.image.load('PygameFile\images\L2.png'), pygame.image.load('PygameFile\images\L3.png'), pygame.image.load('PygameFile\images\L4.png'), pygame.image.load('PygameFile\images\L5.png'), pygame.image.load('PygameFile\images\L6.png'), pygame.image.load('PygameFile\images\L7.png'), pygame.image.load('PygameFile\images\L8.png'), pygame.image.load('PygameFile\images\L9.png')]
stand = pygame.image.load('PygameFile\images\standing.png')



def redrawGameWindow():
    left = False
    right = False
    x = 50
    y = 400
    width = 64
    height = 64
    vel = 5
    isJump = False
    jumpCount = 10
    global walkCount
    win.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        win.blit(char, (x,y))
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT] and x > vel:
            x -= vel
            left = True
            right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
            x += vel
            right = True
            left = False
    else:
            right = False
            left = False
            walkCount = 0
            
    if not(isJump):
        if keys[pygame.K_SPACE]:
                isJump = True
                right = False
                left = False
                walkCount = 0
    else:
        if jumpCount >= -10:
                neg = 1
        if jumpCount < 0:
            neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    
    pygame.display.update()


#mainloop
run = True

def Level_2():
    Game=True
    run = True
    while Game:
        screen.blit(bg, (0,0))
        clock.tick(27)
        walkCount = 0       
        redrawGameWindow()




def GameTwo():
    title=TITLE_FONT.render('Game Level 1', 1, colors.get('blue'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
    text2=MENU_FONT.render('Play the Game', 1, colors.get('blue'))

    screen.fill(colors.get('white'))

    Button_3 = pygame.Rect(25, 350, 175, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    Button_4=pygame.Rect(325, 350, 175, 50)
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_4)

    screen.blit(title, (275,50))
    screen.blit(text,  (30,355))
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
                    Level_2()
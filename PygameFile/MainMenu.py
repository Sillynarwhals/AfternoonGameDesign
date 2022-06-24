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

#Main Font
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
os.system('cls')
#Screen Dimensions
WIDTH=700 #like constant
HEIGHT=700
#colors
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), "red": (255,0,0), "black": (0,0,0), "yellow": (255,255,0)}
clr=colors.get("limeGreen")
#Main Menu list
message=['Instructions', 'Settings', 'Level 1', 'Level 2','Level 3', 'Scoreboard', 'Exit']
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Crossy Road")  #change the title of my window
clock=pygame.time.Clock()
#boxes for menu
Bx=WIDTH//3
By= HEIGHT//20
Button_menu=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_instruct=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_settings=pygame.Rect(Bx, 200, WIDTH//4, 40)
Button_Game1=pygame.Rect(Bx, 250, WIDTH//4, 40)
Button_Game2=pygame.Rect(Bx, 300, WIDTH//4, 40)
Button_Game3=pygame.Rect(Bx, 350,WIDTH//4, 40)
Button_score=pygame.Rect(Bx, 400, WIDTH//4, 40)
Button_exit=pygame.Rect(Bx, 450, WIDTH//4, 40)
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

#more variables
backgrnd=colors.get("limeGreen")
run = True
Game = False

#Main Menu Window function
def mainMenu():
    #screen setup
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_settings)
    Title = TITLE_FONT.render("Crossy Road", 1, colors.get("blue"))
    screen.fill(colors.get('white'))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    yMenu=150
    #Menu setup 
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
        #Quit Loop
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
                if Button_Game2.collidepoint((mx, my)):
                    GameTwo()
                if Button_Game3.collidepoint((mx, my)):
                    GameThree()
                if Button_score.collidepoint((mx, my)):
                    scoreboard()
                if Button_exit.collidepoint((mx, my)):
                    exit()

#Instructions function
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
    #File with Instructions
    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    #Quit Loop and return to Menu Loop
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

#Settings function
def settings():
    #Global variables
    global WIDTH, HEIGHT, screen
    #Fonts
    TITLE_FONT = pygame.font.SysFont('comicsans', 40)
    MENU_FONT = pygame.font.SysFont('comicsans', 20)
    title=TITLE_FONT.render('Settings', 1, colors.get('black'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('black'))
    colort=MENU_FONT.render('Change colors', 1, colors.get('black'))
    sizet= MENU_FONT.render('Change text size', 1, colors.get('black'))
    soundt= MENU_FONT.render('Change screen size', 1, colors.get('black'))
    #colors
    Bolor= (colors.get("red"))
    size= (colors.get("pink"))
    Sound= (colors.get("blue"))
    menu= (colors.get("limeGreen"))
    screen.fill(colors.get('white'))
    
    #Display Buttons
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
        #Quit Function
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
                #Return to Main Menu Button
                if Button_3.collidepoint((mx, my)):
                    mainMenu()
                #Change Background to Yellow 
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
                #Change Background to yellow and Increase Text Size
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
                #Increase Text Size
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
                #Increase Text Size and Background
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
                #Decrease Screen Size to 500*500 pixels
                if Button_sound.collidepoint((mx, my)):
                    WIDTH=500
                    HEIGHT=500
                    screen = pygame.display.set_mode((500, 500), 
                                 pygame.RESIZABLE)

                    


#scoreboard Function
def scoreboard():
    name= input("Asha")
    score=300
    high=0
    #Texts with Font
    title=TITLE_FONT.render('Scoreboard', 1, colors.get('blue'))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("blue"))
    #Create Screen
    screen.fill(colors.get('white'))
    Button_3 = pygame.Rect(25, 350, 200, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    #Display Text
    screen.blit(title, (250,50))
    screen.blit(text3, (30, 355))
    pygame.display.update()
    #Reads score from file
    myFile = open("PygameFile\PygameScore.txt", 'r')
    stuff=myFile.readlines()
    myFile.close()
    for line in stuff:
        screen.blit(line, (200,50))
        pygame.display.update()
        print(line)
    #adds highscore to game 
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
            #Quit loop
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            #Return to Menu loop
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()
#Exit Screen loop
def exit():
    title=TITLE_FONT.render('Bye-Bye', 1, colors.get('blue'))
    screen.fill(colors.get('white'))
    screen.blit(title, (275, 100))
    sys.exit()
pygame.display.update()
#Level 2 of Crossy Road (with increased velocity of cars)
def Game_2():
    #Font for words and stuff
    TITLE_FONT = pygame.font.SysFont('comicsans', 40) #font for Title
    MENU_FONT = pygame.font.SysFont('comicsans', 20) #font for words 
    win=TITLE_FONT.render('YOU WIN!!!', 1, colors.get('black'))
    Button_menu=pygame.Rect(274, 150, 125, 40)
    text=MENU_FONT.render('Return to Menu', 1, colors.get('black'))
    lose=TITLE_FONT.render("YOU LOSE :( Try Again", 1, colors.get('black'))
    #Images
    man = pygame.image.load('PygameFile\images\player.png')
    man = pygame.transform.scale(man, (50, 50))
    manBox= man.get_rect()
    treasure = pygame.image.load('PygameFile\images\\treasure.png')
    treasure = pygame.transform.scale(treasure, (50, 50))
    treasureBox= treasure.get_rect()
    car1= pygame.image.load('PygameFile\images\car2.png')
    car1= pygame.transform.rotate(car1, 270)
    car1= pygame.transform.scale(car1,(100,150))
    car2= pygame.image.load('PygameFile\images\car3.png')
    car2= pygame.transform.rotate(car2,270)
    car2= pygame.transform.scale(car2,(100,150))
    car3= pygame.image.load('PygameFile\images\car4.png')
    car3= pygame.transform.rotate(car3, 90)
    car3= pygame.transform.scale(car3, (100,150))
    car4= pygame.image.load('PygameFile\images\car1.png')
    car4= pygame.transform.rotate(car4, 270)
    car4= pygame.transform.scale(car4, (100, 150))
    car1Box= car1.get_rect()
    car2Box= car2.get_rect()
    car3Box= car3.get_rect()
    car4Box= car4.get_rect()
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
    #ect for chest variables
    xb= 605
    yb= 305
    treasureBox.x=xb
    treasureBox.y=yb
    #rect2 for man variables
    xc= 60
    yc= HEIGHT//6
    wc= 40
    hc= 40
    manBox.x=xc
    manBox.y=yc
    #red car on far right
    cx = 460
    cy= -125
    car1Box.x= cx
    car1Box.y=cy
    #bluecar on right
    dx = 350
    dy= 480
    car2Box.x=dx
    car2Box.y=dy
    # grey beetle on left
    bx = 250
    by= -10
    car3Box.x=bx
    car3Box.y=by
    #grey car on far left 
    ex= 150
    ey= 580
    car4Box.x=ex
    car4Box.y=ey
    #mouse variables
    mx = 0
    my = 0
    #movement variables
    vel = 4
    UP=True
    DOWN=True
    count=0
    score=300



    pygame.display.update()
    #function to create screen display
    def redrawGameWindow():
        screen.blit(bg, (0,0))
        screen.blit(treasure,treasureBox)
        screen.blit(car2, car2Box)
        screen.blit(car1, car1Box)
        screen.blit(car3, car3Box)
        screen.blit(car4, car4Box)
        screen.blit(man, manBox)
        pygame.display.update()



    #main loop
    run= True
    while run:
        clock.tick(60)
        
        #exit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("you quit")  
        #keys to move characters
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and manBox.x > 0:
            manBox.x -= vel
        
        if keys[pygame.K_RIGHT] and manBox.x < WIDTH- 50:
            manBox.x += vel

        if keys[pygame.K_UP] and manBox.y > 0:
            manBox.y -= vel

        if keys [pygame.K_DOWN] and manBox.y < HEIGHT-50:
            manBox.y += vel
        #loop to start car movement 
        if UP:
            car2Box.y-=4
            car4Box.y-=4
            if car2Box.y< -50:
                UP=False
        else:
            car2Box.y+=4
            car4Box.y+=4
            if car2Box.y> HEIGHT-200:
                UP=True
        if DOWN:
            car1Box.y+=4
            car3Box.y+=4
            if car1Box.y>470:
                DOWN=False
        else:
            car1Box.y-=4
            car3Box.y-=4
            if car1Box.y< -70:
                DOWN=True
        
        redrawGameWindow()
        #man collide chest
        if manBox.colliderect(treasureBox):
            screen.fill(colors.get("white"))
            screen.blit(win, (WIDTH//3, 50))
            pygame.draw.rect(screen, colors.get('limeGreen'), Button_menu)
            screen.blit(text, (240, 150))
            print("Your score is:", score)
            File=open('PygameFile\PygameScore.txt', 'a')
            File.write(str(score))
            File.close()
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
                    if Button_menu.collidepoint((mx, my)):
                        mainMenu()
        
        #man collide with car
        if manBox.colliderect(car1Box):
            manBox.x=x
            manBox.y=y
            score-=100
        if manBox.colliderect(car2Box):
            manBox.x=x
            manBox.y=y
            score-=100
        if manBox.colliderect(car3Box):
            manBox.x=x
            manBox.y=y
            score-=100
        if manBox.colliderect(car4Box):
            manBox.x=x
            manBox.y=y
            score-=100
        if score==0:
            screen.fill(colors.get("white"))
            screen.blit(lose, (WIDTH//3, 50))
            pygame.draw.rect(screen, colors.get('limeGreen'), Button_menu)
            screen.blit(text, (240, 150))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        run=False
                        print("You quit")
                        pygame.display.quit()
                        sys.exit()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        mousePos=pygame.mouse.get_pos()
                        mx=mousePos[0]
                        my=mousePos[1]
                    if Button_menu.collidepoint((mx, my)):
                        mainMenu()

#Level 1 of Crossy Road (with slower cars)
def Game_1():
    #Crossy Road Level 1
    #text 
    win=TITLE_FONT.render('YOU WIN!!!', 1, colors.get('black'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('black'))
    lose=TITLE_FONT.render("YOU LOSE :( Try Again", 1, colors.get('black'))
    #buttons
    Button_menu=pygame.Rect(274, 150, 125, 40)
    #Images
    man = pygame.image.load('PygameFile\images\player.png')
    man = pygame.transform.scale(man, (50, 50))
    manBox= man.get_rect()
    treasure = pygame.image.load('PygameFile\images\\treasure.png')
    treasure = pygame.transform.scale(treasure, (50, 50))
    treasureBox= treasure.get_rect()
    car1= pygame.image.load('PygameFile\images\car2.png')
    car1= pygame.transform.rotate(car1, 270)
    car1= pygame.transform.scale(car1,(100,150))
    car2= pygame.image.load('PygameFile\images\car3.png')
    car2= pygame.transform.rotate(car2,270)
    car2= pygame.transform.scale(car2,(100,150))
    car3= pygame.image.load('PygameFile\images\car4.png')
    car3= pygame.transform.rotate(car3, 90)
    car3= pygame.transform.scale(car3, (100,150))
    car4= pygame.image.load('PygameFile\images\car1.png')
    car4= pygame.transform.rotate(car4, 270)
    car4= pygame.transform.scale(car4, (100, 150))
    car1Box= car1.get_rect()
    car2Box= car2.get_rect()
    car3Box= car3.get_rect()
    car4Box= car4.get_rect()
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
    #ect for chest variables
    xb= 605
    yb= 305
    treasureBox.x=xb
    treasureBox.y=yb
    #rect2 for man variables
    xc= 60
    yc= HEIGHT//6
    wc= 40
    hc= 40
    manBox.x=xc
    manBox.y=yc
    #red car on far right
    cx = 460
    cy= -125
    car1Box.x= cx
    car1Box.y=cy
    #bluecar on right
    dx = 350
    dy= 480
    car2Box.x=dx
    car2Box.y=dy
    # grey beetle on left
    bx = 250
    by= -10
    car3Box.x=bx
    car3Box.y=by
    #grey car on far left 
    ex= 150
    ey= 580
    car4Box.x=ex
    car4Box.y=ey
    #mouse variables
    mx = 0
    my = 0
    #movement variables
    vel = 4
    UP=True
    DOWN=True
    score=300




    pygame.display.update()
    #function to create screen display
    def redrawGameWindow():
        screen.blit(bg, (0,0))
        screen.blit(treasure,treasureBox)
        screen.blit(car2, car2Box)
        screen.blit(car1, car1Box)
        screen.blit(car3, car3Box)
        screen.blit(car4, car4Box)
        screen.blit(man, manBox)
        pygame.display.update()



    #main loop
    run= True
    while run:
        clock.tick(60)
        
        #exit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("you quit")  
        #keys to move characters
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and manBox.x > 0:
            manBox.x -= vel
        
        if keys[pygame.K_RIGHT] and manBox.x < WIDTH- 50:
            manBox.x += vel

        if keys[pygame.K_UP] and manBox.y > 0:
            manBox.y -= vel

        if keys [pygame.K_DOWN] and manBox.y < HEIGHT-50:
            manBox.y += vel
        #loop to start car movement 
        if UP:
            car2Box.y-=1
            car4Box.y-=1
            if car2Box.y< -50:
                UP=False
        else:
            car2Box.y+=1
            car4Box.y+=1
            if car2Box.y> HEIGHT-200:
                UP=True
        if DOWN:
            car1Box.y+=1
            car3Box.y+=1
            if car1Box.y>470:
                DOWN=False
        else:
            car1Box.y-=1
            car3Box.y-=1
            if car1Box.y< -70:
                DOWN=True
        
        redrawGameWindow()
        #man collide chest
        if manBox.colliderect(treasureBox):
            screen.fill(colors.get("white"))
            screen.blit(win, (WIDTH//3, 50))
            pygame.draw.rect(screen, colors.get('limeGreen'), Button_menu)
            screen.blit(text, (240, 150))
            print("Your score is:", score)
            File=open('PygameFile\PygameScore.txt', 'a')
            File.write(str(score))
            File.close()
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
                    if Button_menu.collidepoint((mx, my)):
                        mainMenu()
        
        #man collide with car
        if manBox.colliderect(car1Box):
            manBox.x=x
            manBox.y=y
            score-=100
        if manBox.colliderect(car2Box):
            manBox.x=x
            manBox.y=y
            score-=100
        if manBox.colliderect(car3Box):
            manBox.x=x
            manBox.y=y
            score-=100
        if manBox.colliderect(car4Box):
            manBox.x=x
            manBox.y=y
            score-=100
        if score==0:
            screen.fill(colors.get("white"))
            screen.blit(lose, (WIDTH//3, 50))
            pygame.draw.rect(screen, colors.get('limeGreen'), Button_menu)
            screen.blit(text, (240, 150))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        run=False
                        print("You quit")
                        pygame.display.quit()
                        sys.exit()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        mousePos=pygame.mouse.get_pos()
                        mx=mousePos[0]
                        my=mousePos[1]
                    if Button_menu.collidepoint((mx, my)):
                        mainMenu()

#Level 3 of Crossy Road with even faster cars and slower player
def Game_3():
    #Font for words and stuff
    TITLE_FONT = pygame.font.SysFont('comicsans', 40) #font for Title
    MENU_FONT = pygame.font.SysFont('comicsans', 20) #font for words 
    win=TITLE_FONT.render('YOU WIN!!!', 1, colors.get('black'))
    Button_menu=pygame.Rect(274, 150, 125, 40)
    text=MENU_FONT.render('Return to Menu', 1, colors.get('black'))
    lose=TITLE_FONT.render("YOU LOSE :( Try Again", 1, colors.get('black'))
    #Images
    man = pygame.image.load('PygameFile\images\player.png')
    man = pygame.transform.scale(man, (50, 50))
    manBox= man.get_rect()
    treasure = pygame.image.load('PygameFile\images\\treasure.png')
    treasure = pygame.transform.scale(treasure, (50, 50))
    treasureBox= treasure.get_rect()
    car1= pygame.image.load('PygameFile\images\car2.png')
    car1= pygame.transform.rotate(car1, 270)
    car1= pygame.transform.scale(car1,(100,150))
    car2= pygame.image.load('PygameFile\images\car3.png')
    car2= pygame.transform.rotate(car2,270)
    car2= pygame.transform.scale(car2,(100,150))
    car3= pygame.image.load('PygameFile\images\car4.png')
    car3= pygame.transform.rotate(car3, 90)
    car3= pygame.transform.scale(car3, (100,150))
    car4= pygame.image.load('PygameFile\images\car1.png')
    car4= pygame.transform.rotate(car4, 270)
    car4= pygame.transform.scale(car4, (100, 150))
    car1Box= car1.get_rect()
    car2Box= car2.get_rect()
    car3Box= car3.get_rect()
    car4Box= car4.get_rect()
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
    #ect for chest variables
    xb= 605
    yb= 305
    treasureBox.x=xb
    treasureBox.y=yb
    #rect2 for man variables
    xc= 60
    yc= HEIGHT//6
    wc= 40
    hc= 40
    manBox.x=xc
    manBox.y=yc
    #red car on far right
    cx = 460
    cy= -125
    car1Box.x= cx
    car1Box.y=cy
    #bluecar on right
    dx = 350
    dy= 480
    car2Box.x=dx
    car2Box.y=dy
    # grey beetle on left
    bx = 250
    by= -10
    car3Box.x=bx
    car3Box.y=by
    #grey car on far left 
    ex= 150
    ey= 580
    car4Box.x=ex
    car4Box.y=ey
    #mouse variables
    mx = 0
    my = 0
    #movement variables
    vel = 2
    UP=True
    DOWN=True
    count=0
    score=300



    pygame.display.update()
    #function to create screen display
    def redrawGameWindow():
        screen.blit(bg, (0,0))
        screen.blit(treasure,treasureBox)
        screen.blit(car2, car2Box)
        screen.blit(car1, car1Box)
        screen.blit(car3, car3Box)
        screen.blit(car4, car4Box)
        screen.blit(man, manBox)
        pygame.display.update()



    #main loop
    run= True
    while run:
        clock.tick(60)
        
        #exit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("you quit")  
        #keys to move characters
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and manBox.x > 0:
            manBox.x -= vel
        
        if keys[pygame.K_RIGHT] and manBox.x < WIDTH- 50:
            manBox.x += vel

        if keys[pygame.K_UP] and manBox.y > 0:
            manBox.y -= vel

        if keys [pygame.K_DOWN] and manBox.y < HEIGHT-50:
            manBox.y += vel
        #loop to start car movement 
        if UP:
            car2Box.y-=8
            car4Box.y-=8
            if car2Box.y< -50:
                UP=False
        else:
            car2Box.y+=8
            car4Box.y+=8
            if car2Box.y> HEIGHT-200:
                UP=True
        if DOWN:
            car1Box.y+=8
            car3Box.y+=8
            if car1Box.y>470:
                DOWN=False
        else:
            car1Box.y-=8
            car3Box.y-=8
            if car1Box.y< -70:
                DOWN=True
        
        redrawGameWindow()
        #man collide chest
        if manBox.colliderect(treasureBox):
            screen.fill(colors.get("white"))
            screen.blit(win, (WIDTH//3, 50))
            pygame.draw.rect(screen, colors.get('limeGreen'), Button_menu)
            screen.blit(text, (240, 150))
            print("Your score is:", score)
            File=open('PygameFile\PygameScore.txt', 'a')
            File.write(str(score))
            File.close()
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
                    if Button_menu.collidepoint((mx, my)):
                        mainMenu()
        
        #man collide with car
        if manBox.colliderect(car1Box):
            manBox.x=x
            manBox.y=y
            score-=100
        if manBox.colliderect(car2Box):
            manBox.x=x
            manBox.y=y
            score-=100
        if manBox.colliderect(car3Box):
            manBox.x=x
            manBox.y=y
            score-=100
        if manBox.colliderect(car4Box):
            manBox.x=x
            manBox.y=y
            score-=100
        if score==0:
            screen.fill(colors.get("white"))
            screen.blit(lose, (WIDTH//3, 50))
            pygame.draw.rect(screen, colors.get('limeGreen'), Button_menu)
            screen.blit(text, (240, 150))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        run=False
                        print("You quit")
                        pygame.display.quit()
                        sys.exit()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        mousePos=pygame.mouse.get_pos()
                        mx=mousePos[0]
                        my=mousePos[1]
                    if Button_menu.collidepoint((mx, my)):
                        mainMenu()
#Function for screen to play Level 1
def GameOne():
    #different texts 
    title=TITLE_FONT.render('Game Level 1', 1, colors.get('blue'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
    text2=MENU_FONT.render('Play the Game', 1, colors.get('blue'))
    #create screen
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
            #Quit loop
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                #return to main menu
                if Button_3.collidepoint((mx, my)):
                    mainMenu()
                #play Level 1 of crossy road
                if Button_4.collidepoint((mx, my)):
                    Game_1()


#Function for screen to play Level 2
def GameTwo():
        #Texts used
        title=TITLE_FONT.render('Game Level 2', 1, colors.get('blue'))
        text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
        text2=MENU_FONT.render('Play the Game', 1, colors.get('blue'))
        #create screen and display
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
                #Quit loop
                if event.type==pygame.QUIT:
                    run=False
                    pygame.display.quit()
                    print("You quit")
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    mx=mousePos[0]
                    my=mousePos[1]
                    #Return to Menu loop
                    if Button_3.collidepoint((mx, my)):
                        mainMenu()
                    #Play Level 2 of Crossy Road
                    if Button_4.collidepoint((mx, my)):
                        Game_2()


#Function for screen to play Level 3 
def GameThree():
    #Texts used
    title=TITLE_FONT.render('Game Level 3', 1, colors.get('blue'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
    text2=MENU_FONT.render('Play the Game', 1, colors.get('blue'))
    #screen displayed 
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
            #Quit loop
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                #Return to Menu Loop
                if Button_3.collidepoint((mx, my)):
                    mainMenu()
                #Play Level 3 Loop
                if Button_4.collidepoint((mx, my)):
                    Game_3()
#Function that asks for Username
def Username():
    #Variables 
    clock=pygame.time.Clock()
    backgrnd=(255,255,255)
    WIDTH=700
    HEIGHT=700
    screen=pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Crossy Road')
    screen.fill(backgrnd)
    run = True 
    userName=''
    nameClr=(1, 125, 125) #for text for name
    bxClr=(200, 200, 200) #text box 
    #Texts and rectangles used
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//30)

    title=TITLE_FONT.render('Enter Name', 1, bxClr)
    screen.blit(title, (WIDTH/2.5, HEIGHT//7))
    pygame.display.update()

    nameBox=pygame.Rect(WIDTH//4, HEIGHT//3, WIDTH//2, HEIGHT//10)
    pygame.draw.rect(screen, bxClr, nameBox)
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            #Quit loop
            if event.type==pygame.QUIT:
                #Menu(mainTitle,messageMenu)
                pygame.quit()
                sys.exit()
                print("You quit")
            #Print name 
            if event.type == pygame.MOUSEBUTTONDOWN:
                print()
            if event.type == pygame.KEYDOWN:
                #Goes to Main Menu after printing
                if event.key == pygame.K_RETURN:
                    print(userName)
                    mainMenu()
                    #run main menu - if in main program
                if event.key ==pygame.K_BACKSPACE: #not working 
                    userName=userName[:-1]
                    print('back')
                else:
                    userName += event.unicode
            pygame.draw.rect(screen, bxClr, nameBox)
            textSurface=MENU_FONT.render(userName, True, nameClr)
            #use rect x and y to  allign the text 
            screen.blit(textSurface, (nameBox.x+5, nameBox.y+5))

            pygame.display.flip()
            clock.tick(60)
Username()
mainMenu()
Instructions()
pygame.display.update()
clock.tick(60) #Frame rate 
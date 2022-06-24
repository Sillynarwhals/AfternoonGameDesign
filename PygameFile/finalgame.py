# Asha Blewett
# Final game code: Froggy

from cmath import rect
import pygame, time,os,random, math, datetime, sys


date=datetime.datetime.now()
pygame.init()#initialize the pygame package

os.system('cls')
#dimensions
WIDTH=700
HEIGHT=700
score=300
#list of colors
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), "red": (255,0,0), "black": (0,0,0), "yellow": (255,255,0), "brown": (150, 75, 0)}
#Font for words and stuff
TITLE_FONT = pygame.font.SysFont('comicsans', 40) #font for Title
MENU_FONT = pygame.font.SysFont('comicsans', 20) #font for words 
win=TITLE_FONT.render('YOU WIN!!!', 1, colors.get('black'))
Button_menu=pygame.Rect(274, 150, 125, 40)
text=MENU_FONT.render('Return to Menu', 1, colors.get('black'))
lose=TITLE_FONT.render("YOU LOSE :( Try Again", 1, colors.get('black'))
Score=MENU_FONT.render("Your score is:" + str(score), 1, colors.get("black"))
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
        screen.blit(Score, (240, 300))
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
                    #if Button_menu.collidepoint((mx, my)):
                        #mainMenu()
    
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
                    #if Button_menu.collidepoint((mx, my)):
                        #mainMenu()









    




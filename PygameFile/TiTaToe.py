# Asha Blewett
# TICTACTOE 
# draw_grid() 
# zero_Array() 
# draw_markers() 
# checkWinner() 
# Game_end()


import os, random, time, pygame, math, datetime, sys
os.system('cls')

pygame.init()


WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), "red": (255,0,0), "black": (0,0,0), "yellow": (255,255,0)}
clr=colors.get("limeGreen")
messageMenu=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
messageSettings=["Background Colors", "Screen Size", "Sound On/Off"]
mainTitle="Circle eats Square Menu"
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Tic Tac Te")  #change the title of my window
backgrnd=colors.get("pink")
GAME_FONT= pygame.font.SysFont("comicsans", 20)
size = 3
#game Variable
gameOver=False #Check if the game is over
winner=0        #who won the game
xscore=0        #score count for x
oscore=0        #score count for o
player=1        #CONTROL players 1 is x and -1 is o
markers=[]      #Array to control the plays 
lineWidth=10    #Line thickness
Game=True       #Control Main Game
MxMy=(0,0)      #Checks click

cirClr=colors.get("blue")    #Color for the circle
xClr=colors.get("black")     #color for the X
linecolor = colors.get("blue")   #color for grid line
#Function to set our array to zeros
def zero_Array(): 
    for x in range(3):
        row= [0] *3
        markers.append(row)


def draw_grid():
    lineClr=colors.get("white")
    for x in range(1,3):
        pygame.draw.line(screen,lineClr,(0,HEIGHT//3*x),(WIDTH,HEIGHT//3*x),lineWidth)  #Hztal line
        pygame.draw.line(screen,lineClr,(WIDTH//3*x, 0),(WIDTH//3*x,HEIGHT),lineWidth)  #Vert line
    pygame.time.delay(100)

def draw_Markers():
    xValue=0
    for x in markers:   # getting a rw
        yValue=0
        for y in x:  #each elem fthe rw
            if y ==1:
                pygame.draw.line(screen,xClr,(xValue * WIDTH//3 + 15, yValue * HEIGHT//3 + 15), (xValue * WIDTH//3 + WIDTH//3-15, yValue * WIDTH//3 + WIDTH//3-15),lineWidth)
                pygame.draw.line(screen, xClr,(xValue*WIDTH//3 +WIDTH//3-15, yValue*HEIGHT//3+15),(xValue *WIDTH//3+15,yValue*HEIGHT//3+HEIGHT//3-15),lineWidth)
            if y==-1:
                pygame.draw.circle(screen,cirClr,(xValue*WIDTH//3+WIDTH//6,yValue*HEIGHT//3 +HEIGHT//6),WIDTH//6-15, lineWidth)
            yValue +=1
        xValue +=1
    pygame.display.update() 


def agn():
    global Game, backgrnd
    Game = False
    screen.fill(backgrnd)
    textagn=GAME_FONT.render('Want to play again?', 1, (linecolor))
    Buttony=pygame.Rect(WIDTH//4, HEIGHT//2, 100, 50)
    Button_n=pygame.Rect(3*WIDTH//4, HEIGHT//2, 100, 50)
    textyes=GAME_FONT.render('Yes', 1, (linecolor))
    textno=GAME_FONT.render('No', 1, (linecolor))
    xd = WIDTH//2 - (textagn.get_width()//2)
    screen.blit(textagn, (xd, 50))
    pygame.draw.rect(screen, colors.get('white'), Buttony)
    pygame.draw.rect(screen, colors.get('white'), Button_n)
    screen.blit(textyes, (WIDTH//4, HEIGHT//2))
    screen.blit(textno, (3*WIDTH//4, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(10000)
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousePos=pygame.mouse.get_pos()
            mx=mousePos[0]
            my=mousePos[1]
            if Buttony.collidepoint((mx, my)):
                cnt==0
                markers.clear()
                markers=[]
                zero_Array()
                Game = True
                pygame.display.update()
            if Button_n.collidepoint((mx, my)):
                screen.fill(backgrnd)
                textbye=GAME_FONT.render('Bye!', 1, (linecolor))
                screen.blit(textbye, (xd, HEIGHT//2))
                pygame.display.update()
                pygame.time.delay(2000)


def gameEnd():
    global markers, Game
    markers=[]
    textsce=GAME_FONT.render('Final Score', 1,(linecolor))
    texto=GAME_FONT.render('O score:'(xscore), 1, (linecolor))
    textx=GAME_FONT.render('X score:'(oscore), 1, (linecolor))
    xd = WIDTH//2 - (textsce.get_width()//2)
    screen.blit(textsce, (xd, 50))
    screen.blit(texto, (WIDTH//4, HEIGHT//2))
    screen.blit(textx, (3*WIDTH//4, HEIGHT//2))
    pygame.display.update()
    if xscore>oscore:
        print ("Player X is the winner")
    if oscore>xscore:
        print("Player O is the winner")
    if xscore==oscore:
        print("it is a tie")



def checkWinner():
    global Game, gameOver, winner, xscore, oscore
    x_POS=0
    for ROW in markers:
        #check collumns
        if sum(ROW)==3:
            winner =1
            xscore+=1
            gameOver=True
        if sum(ROW)==-3:
            winner=-1
            oscore+=1
            gameOver=True
        #check ROWs
        if markers[0][x_POS] +markers[1][x_POS]+markers[2][x_POS]==3:
            winner=1
            xscore+=1
            gameOver=True
        if markers[0][x_POS] +markers[1][x_POS]+markers[2][x_POS]==-3:
            winner=-1
            oscore+=1
            gameOver=True
        x_POS+=1
        #Check diagonals
        if markers[0][0]+markers[1][1]+markers[2][2]==3 or markers[2][0]+markers[1][1]+markers[0][2]==3:
            winner=1
            xscore+=1
            gameOver=True
        if markers[0][0]+markers[1][1]+markers[2][2]==-3 or markers[2][0]+markers[1][1]+markers[0][2]==-3:
            winner=-1
            oscore+=1
            gameOver=True
        if winner==1:
            screen.fill(xClr)
            print('X won!')
            os.system('cls')
            agn()
        if winner==-1:
            screen.fill(cirClr)
            print('O won!')
            os.system('cls')
            agn()
        if winner==0:
            screen.fill(backgrnd)
            print('Tie')
            cnttext = GAME_FONT.render('Nobody won.', 1, (backgrnd))
            screen.blit(cnttext, (10, HEIGHT//2))
            pygame.display.update()
            pygame.time.delay(2000)
            agn()
        #Check if game is tie
        if gameOver==False: #BOOLEAN == not gameOver
            tie= True
            for ROW in markers:
                for COL in ROW:
                    if COL==0:
                        tie=False
            if tie:
                xscore+=1
                oscore+=1
                gameOver=True
                winner=0



    # add all ROWS if markers[0][]+markers[0][]+markers[0][]==3 Or markers[1][]+markers[1][]+markers[1][]==3 OR
    #winner =1

zero_Array()
Game = True  
cnt=0
run=True
while run and cnt<9:
    screen.fill(backgrnd)
    draw_grid()
    draw_Markers()
    pygame.display.update()
    checkWinner()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            print("You quit")
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            cnt+=1
            MxMy = pygame.mouse.get_pos()
            cellx=MxMy[0]//(WIDTH//3)
            celly=MxMy[1]//(HEIGHT//3)
            print(markers)
            if markers[cellx][celly]==0:
                markers[cellx][celly]=player
                player *=-1
                checkWinner()
                print(winner)
                if gameOver: 
                    gameEnd()


#Asha Blewett
#Get User name:
#create screen,
#Title= enter yr name(FONTS)
#create BOX
#create name var:
#       add the letter
#       if press Backspace, delete last character
#       if press return they are d

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
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("User Name")  #change the title of my window
# framming your game
clock=pygame.time.Clock()
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), "red": (255,0,0), "black": (0,0,0), "yellow": (255,255,0)}
backgrnd=(255,255,255)
screen.fill(backgrnd)
pygame.display.update()
pygame.time.delay(500)
#local variables for game
#boxes for menu
Bx=WIDTH//3
By= HEIGHT//20
user_name=input(" ")
#create title
nametitle = TITLE_FONT.render("Input User Name",1, colors.get("blue"))
screen.blit(nametitle,(200,50))

input_rect=pygame.Rect(WIDTH//3, HEIGHT//3, 140, 50)
userName = MENU_FONT.render(user_name, 1, colors.get("black"))
screen.blit(userName, (WIDTH//3, HEIGHT//2))
pygame.display.update()
#create your box related to your width and height
run=True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print(user_name)
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            print()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                #main menu
                print(user_name)
                pygame.quit()
                sys.exit()
            if event.key==pygame.K_BACKSPACE:
                user_name=user_name[:-1]
            else:
                userName += event.unicode #gives you all characters
        screen.fill(colors.get("white"))

        
        screen.blit(nametitle,(200,50))
        screen.blit(nametitle, (50,10))
        # in ref to width  
        #draw rect      
        pygame.draw.rect(screen,colors.get("white"), input_rect)
        #update the name user
        name=MENU_FONT.render(userName, 1, colors.get("blue"))
        screen.blit(name,(input_rect.x+5, input_rect.y+5))
        pygame.display.flip()

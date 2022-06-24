#Asha Blewett
#Get User name:
#create screen,
#Title= enter yr name(FONTS)
#create BOX
#create name var:
#       add the letter
#       if press Backspace, delete last character
#       if press return they are d
import pygame, os, sys
pygame.init()
os.system('cls')

clock=pygame.time.Clock()
backgrnd=(255,255,255)
WIDTH=700
HEIGHT=700
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Get Name')
screen.fill(backgrnd)
run = True 
userName=''
nameClr=(1, 125, 125) #for text for name
bxClr=(200, 200, 200) #text box 

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
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            pygame.quit()
            sys.exit()
            print("You quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            print()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(userName)
                #run main menu - if in main program
                pygame.quit()
                sys.exit()
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

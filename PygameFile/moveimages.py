# Asha Blewett
# trying to make moving images

import pygame,os
pygame.init()
os.system('cls')

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("Practice Game")

walkRight = [pygame.image.load('PygameFile\images\R1.png'), pygame.image.load('PygameFile\images\R2.png'), pygame.image.load('PygameFile\images\R3.png'), pygame.image.load('PygameFile\images\R4.png'), pygame.image.load('PygameFile\images\R5.png'), pygame.image.load('PygameFile\images\R6.png'), pygame.image.load('PygameFile\images\R7.png'), pygame.image.load('PygameFile\images\R8.png'), pygame.image.load('PygameFile\images\R9.png')]
walkLeft = [pygame.image.load('PygameFile\images\L1.png'), pygame.image.load('PygameFile\images\L2.png'), pygame.image.load('PygameFile\images\L3.png'), pygame.image.load('PygameFile\images\L4.png'), pygame.image.load('PygameFile\images\L5.png'), pygame.image.load('PygameFile\images\L6.png'), pygame.image.load('PygameFile\images\L7.png'), pygame.image.load('PygameFile\images\L8.png'), pygame.image.load('PygameFile\images\L9.png')]
bg = pygame.image.load('PygameFile\images\\bg.png')
char = pygame.image.load('PygameFile\images\standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


def redrawGameWindow():
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
    
    pygame.display.update()


#mainloop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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
            
    redrawGameWindow()

pygame.quit()
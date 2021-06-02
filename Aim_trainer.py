import pygame, random

#initialize
pygame.init()

#create screen
win = pygame.display.set_mode((500, 500))

#set window name
pygame.display.set_caption("Aim trainer")

light_grey = (180, 180, 180)
rand1 = random.randint(50, 450)
rand2 = random.randint(50, 450)

width = 20
height = 20
score = 0

#enemy and player
def enemy():
    enem = pygame.draw.rect(win, (255, 0, 0), (rand1, rand2, width, height))
    return enem
def player():
    play = pygame.draw.ellipse(win, (255, 255, 255), (x, y, width/2, height/2))
    return play

pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

#indicates that run is true
run = True

#Game loop
while run:
    x, y = pygame.mouse.get_pos()
    #create a time delay
    pygame.time.delay(10)
    #collision detection
    if player().colliderect(enemy()):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                rand1 = random.randint(50,450)
                rand2 = random.randint(50,450)
                score = (score + 1)
                print("Your score: ", str(score))
    #iterate over the list of event objects
    #that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        #is user pressing X
        if event.type == pygame.QUIT:
            #exit program
            run = False

    win.fill((light_grey))
    player()
    enemy()
    pygame.display.update()
import pygame
import random


pygame.init()

blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game")


game_over = False


clock = pygame.time.Clock()

prevx = [0]
prevy = [0]
xlist = [400]
ylist = [300]
foodx = round(random.randint(0,790)/10)*10
foody = round(random.randint(0,590)/10)*10
xchange = 0
ychange = 0
snakesize = 1


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xchange = 10
                ychange = 0
            if event.key == pygame.K_LEFT:
                xchange = -10
                ychange = 0
            if event.key == pygame.K_UP:
                xchange = 0
                ychange = -10
            if event.key == pygame.K_DOWN:
                xchange = 0
                ychange = 10
            
    screen.fill(black)

    pygame.draw.rect(screen, blue, [xlist[0], ylist[0], 10,10])
    xlist[0] += xchange
    ylist[0] += ychange
    playercoord = (xlist[0], ylist[0])
    print(playercoord)
    pygame.draw.rect(screen, red, [foodx, foody, 10,10])
    if xlist[0] == foodx and ylist[0] == foody:
        screen.fill(black)
        foodx = round(random.randint(0,790)/10)*10
        foody = round(random.randint(0,590)/10)*10
        pygame.draw.rect(screen, red, [foodx, foody, 10, 10])
        snakesize += 1
    pygame.display.update()
    clock.tick(20)

    
    


pygame.quit()
quit()

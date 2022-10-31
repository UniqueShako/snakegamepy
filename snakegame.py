import pygame
import random
from collections import deque


pygame.init()

blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game")


game_over = False


clock = pygame.time.Clock()

xlist = [400]
ylist = [300]
savex = deque([])
savey = deque([])
foodx = round(random.randint(0,790)/10)*10
foody = round(random.randint(0,590)/10)*10
xchange = 0
ychange = 0
snakesize = 0


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
            


    pygame.draw.rect(screen, red, [foodx, foody, 10,10])
    if xlist[0] == foodx and ylist[0] == foody:
        foodx = round(random.randint(0,790)/10)*10
        foody = round(random.randint(0,590)/10)*10
        pygame.draw.rect(screen, red, [foodx, foody, 10, 10])
        snakesize += 1
        #xlist.append([0])
        #ylist.append([0])
        savex.append(0)
        savey.append(0)
    if snakesize > 0:
        savex.pop()
        savey.pop()
        savex.append(xlist[0])
        savey.append(ylist[0])
        savex.rotate(1)
        savey.rotate(1)
    for piece in range(snakesize):
        pygame.draw.rect(screen, blue, [savex[piece], savey[piece], 10, 10])
    xlist[0] += xchange
    ylist[0] += ychange
    pygame.draw.rect(screen, blue, [xlist[0], ylist[0], 10,10])
    pygame.display.update()
    print(savex, savey)
    clock.tick(15)

pygame.quit()
quit()

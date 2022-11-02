import pygame
import random
from collections import deque


pygame.init()

blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)

screenx = 800
screeny = 600

screen=pygame.display.set_mode((screenx,screeny))
pygame.display.set_caption("Snake Game")


game_over = False


clock = pygame.time.Clock()

xpos = 400
ypos = 300
playercoords = (xpos, ypos)
savex = deque([])
savey = deque([])
savecoords = []
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
                if xchange != -10:
                    xchange = 10
                    ychange = 0
            if event.key == pygame.K_LEFT:
                if xchange != 10:
                    xchange = -10
                    ychange = 0
            if event.key == pygame.K_UP:
                if ychange != 10:
                    xchange = 0
                    ychange = -10
            if event.key == pygame.K_DOWN:
                if ychange != -10:
                    xchange = 0
                    ychange = 10
            
    screen.fill(black)
            


    pygame.draw.rect(screen, red, [foodx, foody, 10,10])
    if xpos == foodx and ypos == foody:
        foodx = round(random.randint(0,790)/10)*10
        foody = round(random.randint(0,590)/10)*10
        pygame.draw.rect(screen, red, [foodx, foody, 10, 10])
        snakesize += 1
        savex.append(0)
        savey.append(0)
    if snakesize > 0:
        savex.pop()
        savey.pop()
        savex.append(xpos)
        savey.append(ypos)
        savex.rotate(1)
        savey.rotate(1)
    for piece in range(snakesize):
        pygame.draw.rect(screen, blue, [savex[piece], savey[piece], 10, 10])
    xpos += xchange
    ypos += ychange
    playercoords = (xpos, ypos)
    pygame.draw.rect(screen, blue, [xpos, ypos, 10,10])
    pygame.display.update()
    savecoords = [(savex[i], savey[i]) for i in range(0, len(savex))]
    for coord in savecoords:
        if playercoords == coord:
            game_over = True
            print(coord)
            print("Game Over!")
    if xpos >= screenx or xpos < 0 or ypos >= screeny or ypos < 0:
        game_over = True
        print("Game Over!")
    #print(savex, savey)
    print(playercoords)
    clock.tick(20)

pygame.quit()
quit()

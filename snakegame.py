import pygame


pygame.init()

blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game")


game_over = False


clock = pygame.time.Clock()


playerx = 400
playery = 300
xchange = 0
ychange = 0
playerpos = (playerx, playery)


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
    playerx += xchange
    playery += ychange
    pygame.draw.rect(screen, blue, [playerx, playery, 10,10])
    pygame.display.update()
    clock.tick(30)

    
    


pygame.quit()
quit()

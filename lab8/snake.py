import pygame # type: ignore
import random

pygame.init()

screen=pygame.display.set_mode((600,600))
clock=pygame.time.Clock()
x=300
y=300
coin_x=random.uniform(40,560)
coin_y=random.uniform(40,560)
right=up=down=False
left=True
length = 1

run=True
while run:
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            pygame.quit() 
        if event.type == pygame.KEYDOWN:
            if left or right:
                if event.key == pygame.K_UP:
                    up=True
                    right=left=down=False
                if event.key == pygame.K_DOWN:
                    down=True
                    right=up=left=False
            if up or down:
                if event.key == pygame.K_RIGHT:
                    right=True
                    left=up=down=False
                if event.key == pygame.K_LEFT:
                    left=True
                    right=up=down=False

    if left:
        x-=2
    if right:
        x+=2
    if up:
        y-=2
    if down:
        y+=2
    if x==0 or y==0 or x==600 or y==600:
        screen.fill((255,0,0))
        pygame.display.update()
        pygame.time.wait(3000)
        exit()
    
    if (x<=coin_x<=(x+20) and y<=coin_y<=(y+20)):
        coin_x=random.uniform(40,560)
        coin_y=random.uniform(40,560)
        length += 1


    screen.fill((0,0,0))
    coin = pygame.draw.circle(screen, (0, 0, 255), (int(coin_x), int(coin_y)), 20)
    # Рисуем каждый сегмент змеи
    for i in range(length):
        pygame.draw.rect(screen, (255, 255, 0), (x - i * 20, y, 20, 20))
    clock.tick(60)
    pygame.display.update()
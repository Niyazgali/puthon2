import pygame
import random

pygame.init()

SCREEN_WIDTH = 400
screen = pygame.display.set_mode((400, 600))
road = pygame.image.load("AnimatedStreet.png")
road_scale = pygame.transform.scale(road, (400, 600))
my_car = pygame.image.load("Player.png")
cars = pygame.image.load("Enemy.png")
coin = pygame.image.load("b.png")


# Создание цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()
x = 185
y = 500
cars_x = 60
cars_y = 0
sp = 5
number = 0
coin_x = 60
coin_y = 0
SPEED = 4
num_font = pygame.font.Font(None, 36)

run = True
collision = False  # Флаг для отслеживания столкновений

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Измените флаг run для завершения игры

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += 10
    if keys[pygame.K_LEFT]:
        x -= 10

    if cars_y == 600:
        cars_y = 0
        cars_x = random.randint(40, 320)
    else:
        cars_y += sp
        
    if coin_y < 600:                      #coin
        coin_y += SPEED
    else: 
        coin_y = 0
        coin_x = random.randint(40,320)
    if (y<=coin_y<=(y+80) and x<=coin_x<=(x+42)) or (y<=(coin_y+40)<=(y+80) and x<=(coin_x+40)<=(x+42)):
        number +=1
        sp += 1
        coin_y=0
        
    
    
        
    # Проверка на столкновение
    if (cars_x <= x <= (cars_x + 40) or cars_x <= (x + 40) <= (cars_x + 40)) and (cars_y + 90) == y:
        collision = True

    if x < 0:
        x = 0
    elif x > SCREEN_WIDTH - 60:
        x = SCREEN_WIDTH - 60


    num_f = num_font.render(str(number), True, (0, 0, 0))
    
    
    
    screen.blit(road_scale, (0, 0))
    screen.blit(num_f, (20, 20))
    screen.blit(my_car, (x, y))
    screen.blit(cars, (cars_x, cars_y))
    screen.blit(coin, (coin_x, coin_y))


    if collision:
        # Отобразите экран "Game Over"
        screen.fill(RED)
        game_over_font = pygame.font.Font(None, 48)
        game_over_text = game_over_font.render("Game Over", True, BLUE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_WIDTH // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Подождите 2 секунды
        run = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


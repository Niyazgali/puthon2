import pygame # type: ignore
import random

pygame.init()

screen=pygame.display.set_mode((400,600))           #все параметры и ресурсы
road=pygame.image.load("AnimatedStreet.png")
my_car=pygame.image.load("Player.png")
cars=pygame.image.load("Enemy.png")
clock=pygame.time.Clock()
coin_x=random.uniform(60,240)
coin_y=0

x=185
y=500
cars_x=60
cars_y=0
speed=6
number=0

pygame.mixer.music.load("background.wav")           #music
pygame.mixer.music.play(20)

num_font = pygame.font.Font(None, 36)

run=True
while run:
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            pygame.quit()                   #управление
                                                
    qimyl=pygame.key.get_pressed()
    if qimyl[pygame.K_RIGHT]:x+=5
    if qimyl[pygame.K_LEFT]:x-=5

    if cars_y==600:                     #рандомные дбижение обекты
        cars_y=0
        cars_x=random.uniform(60,240)
    else:
        cars_y+=speed

    if ( cars_x<=x<=(cars_x+40) or cars_x<=(x+40)<=(cars_x+40) ) and ( cars_y<=y<=(cars_y+80) or cars_y<=(y+80)<=(cars_y+80) ):             #авария
        screen.fill((255,0,0))
        pygame.mixer.music.stop()
        pygame.mixer.music.load("crash.wav")
        pygame.mixer.music.play()
        font = pygame.font.Font(None, 75)
        game_over = font.render("GAME OVER!", True, (0,0,0))
        screen.blit(game_over,(30,300))
        pygame.display.update()
        pygame.time.wait(4000)
        exit()

    if coin_y<600:                      #coin
        coin_y+=2
    else: 
        coin_y=0
        coin_x=random.uniform(60,240)
    if (y<=coin_y<=(y+80) and x<=coin_x<=(x+42)) or (y<=(coin_y+40)<=(y+80) and x<=(coin_x+40)<=(x+42)):
        number+=1
        coin_y=0


    num_f = num_font.render(str(number), True, (0,0,0))         #счетчик
    screen.blit(road,(0,0))                                     #перевернуть и обнавит скрин
    screen.blit(num_f,(20,20))             
    screen.blit(cars,(cars_x,cars_y))
    coin=pygame.draw.circle(screen,(255,255,0),(coin_x,coin_y),20)
    screen.blit(my_car,(x,y))
    pygame.display.flip()
    clock.tick(60)



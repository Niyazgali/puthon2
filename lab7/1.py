import pygame # type: ignore
from datetime import datetime

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200, 750))
mick = pygame.transform.scale(pygame.image.load("mainclock.png"), (1200, 750))
min = pygame.transform.scale(pygame.image.load("rightarm.png"), (1200, 750))
sec = pygame.transform.scale(pygame.image.load("leftarm.png"), (63, 750))

def rot_center(surf, image, angle, x, y):
    image = pygame.transform.rotate(image, angle)
    rect = image.get_rect(center=image.get_rect(center=(x, y)).center)
    surf.blit(image, rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(mick, (0, 0))
    t = datetime.now()
    rot_center(screen, min, -t.second * (6), 600, 375)
    rot_center(screen, sec, -t.minute * (6), 600, 375)

    pygame.display.flip()
    clock.tick(30)
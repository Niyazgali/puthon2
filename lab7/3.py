import pygame # type: ignore

pygame.init()
screen = pygame.display.set_mode((1200, 800))
done = False
blue1=True
x=600
y=400

clok=pygame.time.Clock()
a=1
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        blue1= not blue1

        screen.fill((0,0,0))
        if blue1:color=(0,128,255)
        else:color=(255,0,0)

        pygame.draw.circle(screen,color,(x,y),40)

        qimyl=pygame.key.get_pressed()
        if qimyl[pygame.K_UP]:y-=a
        if qimyl[pygame.K_DOWN]:y+=a
        if qimyl[pygame.K_RIGHT]:x+=a
        if qimyl[pygame.K_LEFT]:x-=a
        if (x+40)>1200:
                x=1200-40
        if (x-40)<0:
                x=0+40
        if (y+40) >800:
                y=800-40
        if (y-40) <0:
                y=0+40

        pygame.display.flip()

 



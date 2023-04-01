import  pygame
from balls import *
from pygame.draw import *
from random import randint

pygame.init()
pygame.font.init()

score  = 0
FPS = 60
size = Vector(1200, 900)
screen = pygame.display.set_mode(size.get())
balls = [Ball(screen) for i in range(5)]
rectangle = [Rectangl(screen) for i in range(1)]
elipses = [Ellipse(screen) for i in range(1)]

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        welcome_text = pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 30), 'Счет: '+ str(score), True, (200, 0, 0))
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cor = event.pos
            print(*cor)
            for fig in balls + rectangle + elipses:
                score += fig.check(*cor)
                
    for fig in balls:
        fig.draw()
        fig.move()

    for figers in rectangle:
        figers.draw()
        figers.move()

    for figerses in elipses:
        figerses.draw()
        figerses.move()

    screen.blit(welcome_text, (1000, 800))
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
import  pygame
from balls import *
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
size = Vector(1200, 900)
screen = pygame.display.set_mode(size.get())
score = 0
balls = [Ball(screen) for i in range(5)]

def new_ball():
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    
def click(event):
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cor = event.pos
            flag = False
            for ball in balls:
                flag = ball.check(*cor) or flag
            if flag:
                score += 1
                print('Click!')
                # click(event)
                print(score)
    for ball in balls:
        ball.draw()
        ball.move()
        
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
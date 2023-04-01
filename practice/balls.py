from pygame import Rect
from random import randint
from pygame.draw import *
from pygame.surface import Surface

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Vector:
    x : int
    y : int
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def get(self):
        return (self.x,self.y)
    
    def add(self, v):
        self.x += v.x
        self.y += v.y


class Ellipse:
    screen: Surface
    color: tuple
    rect: Rect
    size: Vector
    point: Vector
    speed: Vector
    score: int
    r1: int
    r2: int

    def __init__(self, screen):
        self.score = 15
        self.color = COLORS[randint(0,len(COLORS)-1)]
        self.screen = screen
        self.size = Vector(*self.screen.get_size())
        width = randint(20,120)
        height = randint(20,120)
        self.r1 = height // 2
        self.r2 = width // 2
        self.rect = Rect(0,0,width,height)
        x = randint(self.r1, self.size.x- self.r1)
        y = randint(self.r2, self.size.y - self.r2)
        self.point = Vector(x,y)
        speedx = randint(1,5)
        speedy = randint(1,5) 
        self.speed = Vector(speedx,speedy)

    def draw(self):
        self.rect.center = self.point.get()
        ellipse(self.screen, self.color, self.rect)

    def move(self):
        self.point.add(self.speed)
        if not self.r1 < self.point.y < self.size.y - self.r1:
            self.speed.y = -self.speed.y
        if not self.r2 < self.point.x < self.size.x - self.r2:
            self.speed.x = -self.speed.x

    def check(self,x,y):
        form = (x - self.point.x)**2//self.r2**2 + (y - self.point.y)**2//self.r1**2 <= 1
        return self.score if form else 0

class Rectangl():
    color: tuple
    rect: Rect
    width: int
    screen: Surface
    speed: int
    point: Vector
    size: Vector
    score:int


    def __init__(self, screen):
        self.score = 5
        self.width = randint(60, 100)
        self.color = COLORS[randint(0,len(COLORS)-1)]
        self.screen = screen
        radx = self.width//2
        self.size = Vector(*self.screen.get_size())
        x = randint(radx, self.size.x- radx)
        y = randint(radx, self.size.y - radx)
        self.point = Vector(x,y)
        speedx = randint(1,5)
        speedy = randint(1,5) 
        self.speed = Vector(speedx,speedy)
        self.rect = Rect(0,0, self.width, self.width)


    def draw(self):
        self.rect.center = self.point.get()
        rect(self.screen,self.color,self.rect)


    def move(self):
        radx = self.width//2
        self.point.add(self.speed)
        if not radx < self.point.x < self.size.x - radx:
             self.speed.x = -self.speed.x
        if not radx < self.point.y < self.size.y - radx:
             self.speed.y = -self.speed.y
    
    def check(self,x,y):
        top, right = self.rect.topright
        bottom, left = self.rect.bottomleft 
        form1 = top > x > bottom and left > y > right
        print('X',top,'>',x,'>',bottom)
        print('Y ',left,'>',y,'>',right)
        return self.score if form1 else 0

class Ball():
    rad: int
    point: Vector
    color: tuple
    screen: Surface
    speed : Vector
    size : Vector
    score: int

    def __init__(self,screen) -> None:
        self.score = 10
        self.rad = randint(30,50)
        self.color = COLORS[randint(0,len(COLORS)-1)]
        self.screen = screen
        self.size = Vector(*self.screen.get_size())
        x = randint(self.rad, self.size.x- self.rad)
        y = randint(self.rad, self.size.y - self.rad)
        self.point = Vector(x ,y)
        speedx = randint(1,5)
        speedy = randint(1,5) 
        self.speed = Vector(speedx,speedy)


    def draw(self):
        circle(self.screen, self.color, self.point.get(), self.rad)


    def move(self):
        self.point.add(self.speed)
        if not self.rad < self.point.x < self.size.x - self.rad:
            self.speed.x = -self.speed.x
        if not self.rad < self.point.y < self.size.y - self.rad:
            self.speed.y = -self.speed.y


    def check(self,x,y):
        formule1 = ((self.point.x - x) ** 2 + (self.point.y - y) ** 2) ** 0.5
        return self.score if formule1 <= self.rad else 0


class Score:
    screen: Surface
    point: Vector
    color: tuple

    def __init__(self,screen):
        pass

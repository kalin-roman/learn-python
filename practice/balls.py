import pygame
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

class Vector():
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

        
# class polygon():
#     point : Vector
#     color : list
#     screen : Surface
#     speed : Vector
#     size : Vector

#     def __init__(self,screen) -> None:

        
class Ball:
    rad: int
    point: Vector
    color: tuple
    screen: Surface
    speed : Vector
    size : Vector
    
    def __init__(self,screen) -> None:
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
        return formule1 <= self.rad
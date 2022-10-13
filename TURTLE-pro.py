from ctypes.wintypes import SIZE
from http.client import FORBIDDEN
from os import sep
from re import L
import turtle
import math
from random import *

from numpy import size

from Turtle import move

SIZE = 50

def mathik_lines():
    for i in range(100):
        turtle.right(180 * random())
        turtle.forward(randint(6,100))


def join_fun():
    A = ['red', 'green', 'blue']
    print(' '.join(A))
    print(''.join(A))
    print('***'.join(A))


def lists():
    A = [-1,8,0,3,-5]
    B = [x for x in A if x >= 0]
    print(B)


def zero(x,y):
    turtle.penup()
    turtle.goto


x = -400
y = 0

x += Vx*dt
y += Vy*dt + ay*dt**2/2
Vy += ay*dt
from importlib.resources import path
import turtle
import math
from numpy import angle

WIDTH = 50
HIGH = WIDTH * 2
DIG = math.floor((WIDTH ** 2 + WIDTH **2) ** 0.5)

def move(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def forward(A):
    for lenght,angle,fn in A:
        turtle.forward(lenght)
        if fn == 'right':
            turtle.right(angle)
        else:
            turtle.left(angle)


def draw(x,y,numbers):
    for d in numbers:
        dx,dy = d['start']
        move(x + dx, y + dy)
        forward(d['path'])
        x += WIDTH // 2 * 3




numbers = [
    { # ZERO
        'start': (0,0),
        'path': [
            (WIDTH,90,'right'),
            (HIGH,90,'right'),
            (WIDTH,90,'right'),
            (HIGH,45,'right')
        ]
    }, { # ONE
        'start':(0,-WIDTH),
        'path': [
            (DIG,135, 'right'),
            (HIGH,90,'left')
        ]
    }, { # TWO
        'start':(0,0),
        'path':[
            (WIDTH,90,'right'),
            (WIDTH,45,'right'),
            (DIG,135,'left'),
            (WIDTH,0,'right')
        ]
    }, { # THREE
        'start':(0,0),
        'path':[
            (WIDTH, 135, 'right'),
            (DIG, 135, 'left'),
            (WIDTH, 135, 'right'),
            (DIG, 45 , 'left'),
        ]
    }, { # FOUR
        'start':(0,0),
        'path':[
            (WIDTH,270,'right'),
            (WIDTH,90,'left'),
            (WIDTH,180,'left'),
            (HIGH, 90,'right')
        ]
    },{ # FIVE
        'start':(WIDTH,0),
        'path':[
            (WIDTH,90,'left'),
            (WIDTH,90,'left'),
            (WIDTH,90,'right'),
            (WIDTH, 90,'right'),
            (WIDTH, 45,'left')
        ]
    },{ # SIX
        'start':(WIDTH,0),
        'path':[
            (DIG,45,'left'),
            (WIDTH,90,'left'),
            (WIDTH,90,'left'),
            (WIDTH, 90,'left'),
            (WIDTH, 180,'left')
        ]
    },{ # SEVEN
        'start':(0,0),
        'path':[
            (WIDTH,135,'right'),
            (DIG,45,'left'),
            (WIDTH,90,'left')

        ]
    },{ # EIGHT
        'start': (0,0),
        'path': [
            (WIDTH,90,'right'),
            (HIGH,90,'right'),
            (WIDTH,90,'right'),
            (HIGH,180,'right'),
            (WIDTH,90,'left'),
            (WIDTH,45,'left')
        ]
    },{ # nine
        'start':(0,-HIGH),
        'path':[
            (DIG,45,'left'),
            (WIDTH,90,'left'),
            (WIDTH,90,'left'),
            (WIDTH, 90,'left'),
            (WIDTH, 180,'left')
        ]
    }
]
y = []
with open('input.txt') as f:
    for n in f:
        g = int (n)
        if 10 > g >= 0 :
            y.append(numbers[g])
draw(-400,100, y)

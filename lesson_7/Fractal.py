from cmath import cos
from shutil import move
import turtle
turtle.speed('fastest')
# turtle.penup()
# turtle.goto(-500,0)
# turtle.pendown()


def draw(l, n):
    if n == 0:
        turtle.left(180)
        return

    x = l / (n + 1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.left(90)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(l)


def Coha(l,n):
    x = l/3
    if n == 0:
        turtle.forward(x)
        return
    else:
        Coha(x, n - 1)
        turtle.left(60)
        Coha(x, n - 1)
        turtle.right(120)
        Coha(x, n - 1)
        turtle.left(60)
        Coha(x, n - 1)

def star(l,n):
        Coha(l,n)
        turtle.right(120)
        Coha(l,n)
        turtle.right(120)
        Coha(l,n)
        turtle.right(120)
        Coha(l,n)
        turtle.right(120)


def Minkovski(l,n):
    x = l/4
    if n == 0:
        turtle.forward(x)
        return
    else:
        Minkovski(x,n - 1)
        turtle.left(90)
        Minkovski(x,n - 1)
        turtle.right(90)
        Minkovski(x,n - 1)
        turtle.right(90)
        Minkovski(x  ,n - 1)
        Minkovski(x  ,n - 1)
        turtle.left(90)
        Minkovski(x,n - 1)
        turtle.left(90)
        Minkovski(x,n - 1)
        turtle.right(90)
        Minkovski(x,n - 1)


def Levi(l,n):
    
    x = l/2**0.5
    if n == 0:
        turtle.forward(x)
        return
    else:
        Levi(x,n - 1)
        turtle.right(90)
        Levi(x,n - 1)
        turtle.left(90)


def WIKI():


    turtle.hideturtle()
    turtle.tracer(0)
    turtle.penup()
    turtle.setposition(-100, 0)
    turtle.pendown()

    axiom, tempAx, logic, iterations = 'F', '', {'F': '-F++F-'}, 20

    for i in range(iterations):
        for j in axiom:
            tempAx += logic[j] if j in logic else j
        axiom, tempAx = tempAx, ''

    for k in axiom:
        if k == '+':
            turtle.right(45)
        elif k == '-':
            turtle.left(45)
        else:
            turtle.forward(1)

    turtle.update()
    turtle.mainloop()


def dragon():
    axiom, tmp, rule, count = 'FX', '', {'X': 'X+YF+', 'Y': '-FX-Y'}, 15
    for i in range(count):
        for j in axiom:
            tmp += rule[j] if j in rule else j
        axiom, tmp = tmp, '' 
        
    for k in axiom:
        if k == 'F':
            turtle.forward(2.5)
        elif k == '+':
            turtle.right(90)
        elif k == '-':
            turtle.left(90)
        

def poligon():
    axiom, tmp, rule, count = 'A', '',{ 'A': 'B-A-B', 'B': 'A+B+A'}, 8
    for i in range(count):
        for j in axiom:
            tmp += rule[j] if j in rule else j
        axiom, tmp = tmp, '' 

    for i in axiom:
        if i == 'A' or i == 'B':
            turtle.forward(2.5)
        elif i == '+':
            turtle.left(60)
        elif i == '-':
            turtle.right(60)

l = 1000
n = 6
turtle.penup()
turtle.setposition(-300, -300)
turtle.pendown()
poligon()


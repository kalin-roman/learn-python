from http.client import FORBIDDEN
from re import L
import turtle
import math


turtle.shape('turtle')

def move(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

#Упражнение №4: окружность
def circle(n):
    angle = 360/n
    for i in range(64):
        turtle.left(angle)
        turtle.forward(10)




#Упражнение №5: больше квадратов
def several_squears():
    x = 0
    y = 0
    f = 100
    n = 20
    for req in range(10):
        print('x=',x, 'y=',y)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()

        for i in range(4):
            turtle.forward(f)
            turtle.left(90)
        y -= n
        x -= n
        f += 2*n


# Упражнение №6: паук       
def spider(n,x,y):
    angle = 360/n
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for line in range(n):
        turtle.left(angle)
        turtle.forward(100)
        turtle.stamp()
        turtle.goto(x,y)

# Упражнение №7: спираль
def spiral():
    k=1
    fi_rad=0.1
    fi_degr=fi_rad*(180/3.14)
    for i in range (0,1000):
        ro=k*fi_rad
        turtle.forward(ro)
        turtle.left(fi_degr)
        fi_rad+=0.1
        ro+=ro



def sq_spiral():
    n = 10
    for i in range(100):
        turtle.forward(n)
        turtle.left(90)
        n += 5

#circle()
#several_squears()
# spider(5,-50,-50)

# spider(8,50,50)


# spider(10,100,100)
#sq_spiral()


def polygons_old():
    x = 0
    y = 0
    f = 100
    n = 20
    g = 3
    
    for req in range(10):
        print('x=',x, 'y=',y)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        #angle = ((g-2)*180/g)-180
        angle = 360/n-180
        for i in range(g):
            turtle.left(angle)
            turtle.forward(f)
            
        g += 1
        x += n
        f += 2*n
               



def flower():
    angle = 360/64
    angle2 = 360/3
    for k in range(3):   
        for i in range(64):
            turtle.left(angle)
            turtle.forward(5)
        for k in range(64):
            turtle.right(angle)
            turtle.forward(5)
        turtle.left(angle2) 


def binocle():

    turtle.speed(1000*10)
    turtle.width(2)
    
    angle = 360/64
    n = 5 
    turtle.left(90)
    for l in range(9):

        for i in range(64):
            turtle.left(angle)
            turtle.forward(n)
        for k in range(64):
            turtle.right(angle)
            turtle.forward(n)
        n *= 1.2

def arc():
    
    turtle.speed(1000)

    angle = 180/64
    n = 3
    d = n/6

    turtle.left(90)
    for g in range(6):
        for i in range(64):
            turtle.right(angle)
            turtle.forward(3)
        for j in range(64):
            turtle.right(angle)
            turtle.forward(d)

def smile():
    angle = 360/64
    angle2 = 180/64
    n = 3
    d = n/6
    turtle.penup()
    turtle.goto(0,-60)
    turtle.pendown()
    turtle.fillcolor('#FFFF00')
    turtle.begin_fill()
    for i in range(64):
        turtle.left(angle)
        turtle.forward(20)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0,200)
    turtle.pendown()
    turtle.right(90)  
    turtle.fillcolor('#0000FF')
    turtle.begin_fill()
    for l in range(64):
        turtle.left(angle)
        turtle.forward(5)
    for o in range(64):
        turtle.right(angle)
        turtle.forward(5)
    turtle.end_fill()
    turtle.left(90)
    turtle.color('#FF0000')
    turtle.penup()
    turtle.goto(60,60)
    turtle.pendown()
    turtle.width(8)
    turtle.right(90)
    for g in range(1):
        for q in range(64):
            turtle.right(angle2)
            turtle.forward(3)
    turtle.penup()
    turtle.goto(0,160)
    turtle.pendown()
    turtle.color('#000000')
    turtle.right(180)
    turtle.forward(80)


def star(n):
    angle = 180.0 - 180.0 / n
    for g in range(n):
    #     print('x=',x, 'y=',y)]\
        turtle.forward(100)
        turtle.left(angle)#145
        
             
def polygon(n ,lenght):
    a = 360/n
    r = a/(2*math.sin(360/(2*n)))
    move(r,0)
    l = j = (180-a)/2       
    for i in range(n):
        turtle.left(l)
        turtle.forward(lenght)
        l = 180+j*2
    move(r,0)             

def polygons():
    for i in range(3, 9):
        polygon(i, 50)

polygon(4, 100)
from calendar import c
from re import X

inX = input('x : ')
inY = input('y : ')
if inX and inY:
    x = int(inX)
    y = int(inY)
    if  x == 0 or y == 0:
        if x == 0:
            print("Точка принадлежит оси Y")
        elif y == 0:
            print("Точка принадлежит оси X")
        else:
            print("Zero")
    else:
        if x <= -10 or y <= -10:
            print("Alarm!!!!")
        if x > 0 and y > 0:               # x>0, y>0
            print("Первая четверть")
        elif x > 0 and y < 0:
            print('Четвертая четверть')
        elif y > 0:              # x<0, y>0
            print("Вторая четверть")
        else:                   # x<0, y<0    
            print("Третья четверть")
else:
    print('Enter the numbers, please')







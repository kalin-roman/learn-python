from calendar import c
from re import X


inX = input('x = ')
inY = input('y = ')

if inX and inY:
    x = int(inX)
    y = int(inY)
    isZero = x == 0 and y == 0 
    print(type(isZero), isZero)
    if isZero:
        print("Zero")
    else:
        if x > 0:
            if y > 0:               # x>0, y>0
                print("Первая четверть")
            else:                   # x>0, y<0
                if y <= -10:
                    print("Alarm y is low!!")
                print("Четвертая четверть")
        else:

            if x <= -10:
                print("Alarm x is low!!!!!!!")    
            if y > 0:               # x<0, y>0
                print("Вторая четверть")
            else:                   # x<0, y<0
                if y <= -10:
                    print("Alarm y is low!!")
                print("Третья четверть")
else:
    print('Enter the numbers!!!')







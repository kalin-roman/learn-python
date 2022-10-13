from re import S
from tkinter import Y

def f(symbols):
    s = 0
    for x in symbols:
        s += int(x)
    return s
def  f2(symbols):
    p = 1
    for x in symbols:
        p *=  x
    return p
data = input("Enter a number ")
s = list(data)
y = f(s)
print(y)

y = f(['1','2','3','4','5'])
print(y)

a = []
y = f(a)
print(y)

k = [5,3,4,1,2]
y = f2(k)
print(y)

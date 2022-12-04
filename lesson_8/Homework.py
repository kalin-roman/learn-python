from calendar import week
from html.entities import name2codepoint
from re import X

from numpy import append, true_divide


# z = bin(int('0F',16))

# a = list(map(int, z[2:len(z)]))

# print(a)

def sixteenth(n1, n2):
    c = []
    x = bin(n1)
    y = bin(n2)

    a = list(map(int, x[2:len(x)]))
    b = list(map(int, y[2:len(y)]))

    while len(a) < 8:
        a.insert(0,0)
    while len(b) < 8:
        b.insert(0,0)

    for i in range(len(a)):
            c.append(a[i] ^ b[i])
    l = ''.join(list(map(str,c)))
    pr = hex(int(l,2))

    return  pr[2:len(pr)]



def units(k):
    x = 0
    j = bin(k)
    a = list(map(int, j[2:len(j)]))

    for i in a:
        if i == 1:
            x += 1
    return x

# print(sixteenth(0xf0,0x0f))

def money_1(price,delts,m):
    day = 1
    week = 1
    money = 0
    while week <= m:
        money += price
        price += delts
        day += 1
        if day == 8:
            week += 1
            day = 1
    return money


def skob_vir(x):
    a = []
    for i in x:
        if i == '(':
            a.append('(')
        elif i == ')' and  len(a) > 0:
            a.pop()
        else:
            return 'NO'
    return 'YES' if len(a) == 0 else 'NO'
# print(money_1(10,1,1))


def search(n,M):
    x = 0
    for i in M:
        if n == i:
            x += 1
    return x


def bubles(A):
    x = []
    for k in A:
        if k != '.':
            x.append(k)
        else:
            break
    
    for i in range(1,len(x)):
        for j in range(len(x) - i):
            if ord(x[j + 1]) <  ord(x[j]):
                x[j],x[j + 1] = x[j + 1],x[j]
    
    return ''.join(x)


def 
a = input('Введите последовательность чисел:  ')

# print(search(str(input('Enter the number:')),x))
print(bubles(a))
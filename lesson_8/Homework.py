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


def slovar_poryadok(b):
        l = b
        max = 0
        for i in l:
            if len(i)> max:
                max = len(i)
        for k in range(len(l)):
            if len(l[k]) < max:
                while len(l[k]) != max:
                    l[k] = '0' + l[k]
        return l


def recurtion(k, l = 1):
        if l == len(k[0]):
            return 
        else:
            k.sort(key = lambda n : n[len(n)-l])    
            e = k[0][len(k) - 1]
            s = []
            for u in k:   
                if e == u[len(k) - 1]:
                    s.append(u)
  
                    recurtion(k ,  l + 1)
        return k 

def r_sort(A, n = 1):
    fn = lambda x : int(str(x // n)[-1])
    A.sort(key = fn)
    if len(A) <= 1:
        return A
    j = 0
    for i in range(len(A) - 1):
       if (fn(A[i]) != fn(A[i + 1])):
            A[j:i+1] = r_sort(A[j:i+1], n * 10)
            j = i + 1
    A[j:len(A)] = r_sort(A[j:len(A)], n * 10)
    return A


def task_r_sort():   
    b = input('Enter the numbers with space between them: ').split()
    nums = [int(x) for x in b]

    r_sort(nums)
    print(nums)


def matpomosh(A, n = 1):
    r = False if n == 1 else True 
    A.sort(key= lambda x :  x[n], reverse = r)
    if len(A) <= 1:
        return A
    j = 0
    for i in range(len(A)-1):
        if A[i][n] != A[i+1][n]:
            A[j:i+1] = matpomosh(A[j:i+1], 0)
            j = i + 1
    A[j:len(A)] = matpomosh(A[j:len(A)], 0)
    return A



def tests():
    k = int(input('Enter the amount of student: '))
    L = []
    for i in range(k):
        l = input('Enter the Lenght and weight: ').split()
        if len(l) == 2:
            L.append((float(l[0]),float(l[1])))
    print(len(L))
    print(*matpomosh(L), sep='\n')


def find(A,n):
    for i,ar in A:
        if n == i:
            return ar
    a = []
    A.append((n,a))
    return a

def sort_str(A,n = 0):
    A.sort(key= lambda x : x[0][n])
    if len(A)<=1:
        return A
    j = 0
    for i in range(len(A)-1):
        if A[i][n] != A[i+1][n]:
            A[j:i+1] = matpomosh(A[j:i+1], n + 1)
            j = i + 1


d = int(input('Enter the amount of words: '))
L = []
for i in range(d):
    w = input('Enter a word: ')
    L.append(w)
L.sort(key = len)
H = []
for i in range(len(L)):
    pL = len(L[i])
    a = find(H,pL)
    a.append(L[i][::-1])

H.sort(key= lambda x : x[0])
for i in range(len(H)):
    print(H[i][0])
    sort_str(H[i][1])
    for i in H[i][1]:
        print(i,i[::-1])
# print(H)  
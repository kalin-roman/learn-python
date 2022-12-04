from audioop import reverse

from numpy import False_


def col_a(N):   
    m = [0] * 100 
    for c in N:
        m[c] += 1
    return m.index(max(m))


def col_d(N):
    d = {}
    for x in N:
        a = d.get(x,0) 
        d[x] = a + 1
    y = list(d.items())
    y.sort(key = lambda v : v[1], reverse=True)
    return y[0][0]
N = []
l = int(input('Enter the length of array: '))

def fn(N):
    return len(N['car_name'])

for i in range(l):
    x = int(input('Enter the numbers: '))
    if x > 0 and x < 100:
        N.append(x)
    else:
        print('wrong numbers')

c = col_d(N)
print(c)
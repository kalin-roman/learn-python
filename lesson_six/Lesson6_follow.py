
from numpy import append

N = []
l = int(input("Колл: "))
k = 0
max = 0


for i in range(l):
    N.append(int(input('number: ')))


for i in range(len(N)):
    if N[i] == 1:
        k += 1
    elif N[i] == 0:
        if k > max:
            max = k
        k = 0
print(max)
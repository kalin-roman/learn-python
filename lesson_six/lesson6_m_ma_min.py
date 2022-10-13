from os import sep
from tkinter.ttk import Separator


N = []
x = 0




while x != "#":
    x = input('Enter the number: ') 
    if x != '#':
        N.append(int(x))


max = 0
min = 9999
mid1 = 0
mid2 = 0
k = 0
m = 0
c = 0
j = 0
l = 0

for i in range(len(N)):
    mid1 += N[i]
    k += 1
    m += N[i] 
    if N[i] > max:
        max = N[i] 
    if N[i] < min:
        min = N[i]
    if k == 3:
        c = m % k
        m = 0
    if k == 6:
        j = m % k
        l = j + c


mid2 = mid1 / len(N)

print(mid2,max,min, l ,sep = " ")

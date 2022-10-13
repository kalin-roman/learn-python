
from enum import Flag


s = input("Enter the string: ")
k = int(input("Enter k: "))
d = len(s) // k
x =  s[0:d]
flag = True

for i in range(k):
    y = s[i * d: i * d + d]
    flag = (flag and x == y)
    x = y
if flag :
    print(x)
else:
    print("NO SOLUTION")
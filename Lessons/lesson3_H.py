from re import L


k = []
n = 100
l = 0
while n != 0:
    n = int(input("Enter the number: "))
    if n > 0:
        k.append(n)
for i in k:
    if i % 2 == 0:
        l += 1
print(l)
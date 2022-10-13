n = 1
max = -1000
l = 0
while n != 0:
    n = int(input("Enter the numbers: "))
    if n > max:
        max = n
        l = 1
    elif n == max:
        l += 1

print(l)
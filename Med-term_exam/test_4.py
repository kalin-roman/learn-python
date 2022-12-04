max_n = 0

while True:
    x = int(input("Enter the numbers: "))
    if x == 0:
        break
    else:
        if x%2 == 0 and x > max_n:
            max_n = x

print(max_n)
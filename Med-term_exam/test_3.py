
sum_n = 0
col = 0

while True:
    x = int(input("Enter the numbers: "))
    if x == 0:
        break
    else:
        col += 1
        sum_n += x

mid = sum_n/col

print(round(mid,2))
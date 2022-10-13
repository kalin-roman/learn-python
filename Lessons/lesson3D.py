
def infun(x):
    i = 0
    d = 0
    num = []
    while d <= x:
        i += 1
        d = i ** 2
        if d <= x:
            num.append(d)
    return num
n = int(input("Введите число. "))
m = ""
for i in infun(n):
    m += str(i) + ' '
print(m)
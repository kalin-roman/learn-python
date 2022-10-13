
def c(x):
    return 0 < x < 9

i1 = int(input("Введите координаты ферязя строка i1: "))
j1 = int(input("Введите координаты ферязя столбик j1: "))
i2 = int(input("Введите координаты движения ферязя i2: "))
j2 = int(input("Введите координаты движения ферязя j2: "))

if c(i1) and c(j1) and c(i2) and c(j2):
    isRow = i1 == i2
    isColl = j1 == j2
    isCross = i1 + j1 == j1 + j2 
    isRCross = i1 + (8 - j1) == i2 + (8 - j2)
    if isRow or isColl or isCross or isRCross:
        print("Yes")
    else:
        print ("No")
else:
    print ("Введите цифры от 1 до 8!!!!!!")



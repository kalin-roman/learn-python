par = [
    int(input("Вес грузовика: ")),
    int(input("Высота груза: ")),
    int(input("Вес пианино: ")),
    int(input("Высота пианино: ")),
    int(input("Вес холодильника: ")),
    int(input("Высота холодильника: ")),
    int(input("Максимальный допустимый вес на мосту: ")),
    int(input("Максимальная допустимая высота в туннеле: "))
]


weight = par[0] + par[2] + par[4]
height = par[3] + par[5]

if par[6] <= weight and par[7] <= height :
    print('YES')
else:
    print('NO')

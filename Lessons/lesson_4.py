a = range(1,10)
print(*a) 

s = "max"
print(*s)

for i in s:
    print(i)


name = "Roma"
a,b,*rest = name
print(a,b,)
print(rest)


a = [(3,30),(4,10),(5,19)]
for angle,lenght in a:
    print('angle = ', angle,"lenght = ",lenght)
abc = [
    int(input('Enter the length')),
    int(input('Enter the length')),
    int(input('Enter the length'))
]

c = max(abc)
ab = [x for x in abc if x != c]
sumKv = ab[0]**2 + ab[1]**2

if c**2 == sumKv:
    print('right')
elif c**2 < sumKv:
    print('acute')
elif c**2 > sumKv:
    print('obtuse')
else:
    print("impossible")
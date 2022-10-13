
x = float(input('Enter x: '))
y = float(input('Enter y: '))
r = float(input('Enter r: '))


l = (x**2 + y**2)**0.5


if r < l:
    print("No")
else:
    print("Yes")
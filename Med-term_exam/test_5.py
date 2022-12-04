
z = int(input("Nummero: "))

def recurtion(x,n = 0):
    if n == z:
        return x
    else:
        x.append(x[n] + x[n + 1] + x[n + 2])
        recurtion(x,n + 1)
        return x
t = recurtion([0,0,1])
print(t)
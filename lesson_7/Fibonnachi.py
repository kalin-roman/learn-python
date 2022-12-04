x = int(input('Nummero: '))

def fib(n, i = 0):
    if x - 1 == i:
        return n
    else:
        n.append(n[i] + n[i + 1])
        return fib(n,i + 1)


z = fib([0,1])

print(z[len(z) - 1])
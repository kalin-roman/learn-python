def foo(*args):
    x,y,z = args
    return 100 * x + 10 * y + 1 * z


def bar( *args , op = '*' ):
    v = 1 if op == "*" or op == "//" else 0
    for arg in args:    
        if op == '*':
            v *= arg
        elif op == "+":
            v += arg
        elif op == "//":
            v //= arg
        else:
            v -= arg
    return v


T = 2,3,5
f = bar(1, 2, 3, 4, op = "+")
print(f,T, sep = '-')
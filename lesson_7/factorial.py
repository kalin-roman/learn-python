import sys


def fac(n, i = 1):
    if n == 0:
        return 1,i
    else:
        n_1, i_1 = fac(n-1, i + 1)
        return n * n_1, i_1


n, i = fac(5)
print(n, i, sys.getrecursionlimit())
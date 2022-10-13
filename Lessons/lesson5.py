from math import ceil, radians

def invert(A:list):
    j = len(A) - 1
    for i in range(len(A) // 2):
        A[i], A[j - i] = A[j - i], A[i]


def shift_left(a):
    tmp = a[0]
    prevI = len(a) - 1
    for k in range(prevI):
        a[k] = a[k + 1]
    a[prevI] = tmp


def shift_right(a):
    tmp = a[len(a) - 1]
    for k in  range(len(a)-2,-1,-1):
        a[k + 1] = a[k]
    a[0] = tmp


def Eratosphen():
    N = 15
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2,N):
        if A[k]:
            for m in range(2*k,N,k):
                A[m] = False
    for k in range(N):
        print(k,'-', 'simple'if A[k] else "sostavnie" )


def foo(x):
    
    return len(x) - 1



tmp = 2
a = [1,2,3,4,5,22,57]

b = foo(a) 

print(a[b])




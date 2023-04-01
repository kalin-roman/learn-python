
def cuts():
    A = [(0,1),(2,4),(5,1),(0,0)]
    for i,(x,y) in enumerate(A):
        print('i = ',i ,'xy = ',x,y)

    B = [0,1,2,3,4,5,6,7,8,8,9,]
    C = [10,11,12]

    B[7:7] = C

    print(B)

def Factor(n):
    assert n >=0, 'Factorial can not be defined'
    if n == 0:
        return 1
    return Factor(n-1) * n


print(6%8)

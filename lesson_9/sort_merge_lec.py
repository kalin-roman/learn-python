def merge (A:list,B:list):
    C = [0] * (len(A)+len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i]<= B[k]:
            C[n]= A[i]
            i += 1
        else:
            C[n] = B[k]
            k += 1
        n += 1
    while i < len(A):
        C[n]=A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


def merge_sort(A):
        if len(A) <= 1:
            return
        middle = len(A)//2
        L = A[0:middle]
        R = A[middle:len(A)]
        merge_sort(L)
        merge_sort(R)
        C = merge(L,R)
        for i in range(len(A)):
            A[i] = C[i]
        return A


def hoars_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for i in A:
        if i < barrier:
            L.append(i)
        elif i == barrier:
            M.append(i)
        else:
            R.append(i)
    hoars_sort(L)
    hoars_sort(R)
    k = 0
    for g in L+M+R:
        A[k] = g
        k += 1
    return A 


def check_sortED(A, asc = True):
    flag = True
    s = 2 * int(asc) - 1
    for i in range(0,len(A)-1):
        if  s*A[i] > s*A[i + 1]:
            flag = False
            break
    return flag


def search(A,n):
    middle =  len(A)//2
    if A[middle] == n:
        return middle
    elif middle == 0:
        return -1
    elif A[middle] < n:
        return  -1 if search(A[middle:len(A)],n) == -1 else middle + search(A[middle:len(A)],n)
    elif A[middle] > n:
        return search(A[0: middle],n)
    

A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(search(A, int(input())))
# flag = True
# N=int(input('Ввод N =',))
# for i in range(N):
#     x = int(input('Ввод Х =',))
#     flag = x%10==0 and flag
# print(flag)
def merge(a, b):
    c = []
    iA = 0
    iB = 0
    while iA < len(a) and iB < len(b):
        if a[iA] < b[iB]:
            c.append(a[iA])
            iA +=1
        else:
            c.append(a[iB])
            iB += 1
    while iA < len(a):
        c.append(a[iA])
    while iB < len(b[iB]):
        c.append(b[iB])
    return c

def merge_sort(a):
    if len(a) <= 1:
        return
    middle = len(a)//2 
    L = a[0 : middle]
    R = a[middle : len(a)]
    merge_sort(L)
    merge_sort(R)
    C = merge(L,R)
    for i in range(len(a)):
        a[i] = C[i]
    return a

a = [5, 4, 3, 2, 1]
print(merge_sort(a))

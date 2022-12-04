def merge_sort(A):
    for i in range(len(A)):
        A[i] = 0
    return A


A = [1,4,3,1]
merge_sort(A)
print(A)

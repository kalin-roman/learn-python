from re import I


def insert_sort(A):
    ''' insert sorting'''
    for i in range(len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j],A[j - 1] = A[j - 1],A[j]
            j -= 1


def choice_sort(A):
    '''choice sorting'''
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[j] < A[i]:
                A[i],A[j] = A[j], A[i]


def bubble_sort(A):
    '''bubble sorting'''    
    for i in range(1,len(A)):
        for j in range(len(A) - i):
            if A[j + 1] < A[j]:
                A[j],A[j + 1] = A[j + 1],A[j]
    print('module = ',__name__)


def count_sort(A):
    '''count sorting'''
    F = [0] * 20
    for x in A:
        F[x] += 1
    x = 0
    for i, n in enumerate(F):
        y = x + n
        for j in range(x, y):
            A[j] = i
        x = y
            

def test_sort(fnSort):
    print('Testing: ',fnSort.__doc__)
    print('testcase #1: ', end ='')
    A = [4,3,8,1,2]
    A_sorted = [1,2,3,4,8]
    fnSort(A)
    print('Ok'if A == A_sorted else 'Fail')

    print('testcase #2: ', end ='')
    A = list(range(10,20)) + list(range(0,10))
    A_sorted = list(range(20))
    fnSort(A)
    print('Ok'if A == A_sorted else 'Fail')

    print('testcase #3: ', end ='')
    A = [4,2,4,2,1]
    A_sorted = [1,2,2,4,4]
    fnSort(A)
    print('Ok'if A == A_sorted else 'Fail')

    print('testcase #4: ', end ='')
    A = [1,2,3,5,2,7,6,0,9,9,2,8,6,3,4,1,5,2,3,7,6,6,1,3,5,2]
    A_sorted = [0,1,1,1,2,2,2,2,2,3,3,3,3,4,5,5,5,6,6,6,6,7,7,8,9,9]
    fnSort(A)
    print('Ok'if A == A_sorted else 'Fail')


# if __name__=='__main__':
#     test_sort(insert_sort)
#     test_sort(choice_sort)
#     test_sort(bubble_sort)
#     test_sort(count_sort)
a = [3,4,5,6,1,6,4,53,0]

if __name__ == '__main__':
    bubble_sort(a)
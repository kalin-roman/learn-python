
def fn():
    n = 1000
    k = []
    sum = 0 
    while n != 0:
        n = int(input("Enter the numbers: "))
        k.append(n)
        
    for j in k:
        sum += j
    print(sum)


def  fn2():
    sum = 0 
    n = 1000
    while n != 0:
        n = int(input("Enter the numbers: "))
        sum += n
    print(sum)
    
fn2()
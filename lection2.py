flag = True
N=int(input('Ввод N =',))
for i in range(N):
    x = int(input('Ввод Х =',))
    flag = x%10==0 and flag
print(flag)
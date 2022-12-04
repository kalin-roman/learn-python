
def gen_bin(M,prifix = ''):
    if M == 0:
        print(prifix)
        return
    for digit in '0','1':
        gen_bin(M-1,prifix + digit)

def generate_numbers(N:int,M:int,prefix = None):
    if M == 0:
        print(''.join(map(str,prefix)))
        return
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N,M-1,prefix)
        prefix.pop()


def gennerate_permentations(N:int,M:int = -1,prefix = None):
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(*prefix,end = ', ', sep = '')
        return
    for number in range(1,N+1):
        if number in prefix:
            continue
        prefix.append(number)
        gennerate_permentations(N,M-1,prefix)
        prefix.pop()
# gennerate_permentations(3)

# generate_numbers(10,8)
# gen_bin(4)

print(bin(127))
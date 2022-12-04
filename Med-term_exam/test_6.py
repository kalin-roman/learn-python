a = int(input('Enter the number1: '))
b = int(input('Enter the number2: ')) 


def gcd(a,b):
    return(a if b == 0 else gcd(b,a%b))

print(gcd(a,b))

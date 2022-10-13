import math


x = float(input('Enter x: '))
p = float(input('Enter %: '))
y = float(input('Enter y: '))


years = 0
sum = 0 

while sum <= y:
        sum = x + x * p / 100 
        years += 1
        x = math.floor(sum * 100)/100.0 
print(years)
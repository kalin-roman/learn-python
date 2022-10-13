def highYear(x):
    return  x % 100 == 0 and x % 400 == 0 or  x % 100 != 0 and x % 4 == 0 



years = [1700, 1800, 1900, 2100, 
     2200, 2300, 2500, 2600, 
     1600, 2000, 2400, 1, 
     2000, -4 , -100, 1000000001 
    ]
for n in years:
    if 0 < n < 100000:
        if highYear(n):
            print(n, "Yes")
        else:
            print(n, "No")
    else:
        print(n," Error")

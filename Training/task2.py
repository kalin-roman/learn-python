strs = ["flower","flow","flight"]

def roma_s(strs):
    first = strs[0]
    array = ""
    d = 0
    check = 1


    while True:
        for g in range(0, len(strs)):
            if first[d] == strs[g][d]:
                check += 1
        if check == len(strs):
            check = 1
            array += first[d]
            d += 1
        else:
            break
    return array

def max_s(strs):
    i = 0
    next = 1 <= len(strs) <= 200 
    for s in strs:
        next = next and 0 < len(s) <= 200
    result = ''
    while next:
        for line in range(len(strs)):
            next = next and i < len(strs[line]) and strs[line][0:i + 1] == strs[0][0:i + 1]
        if next:
            result = strs[0][0:i + 1]
        i += 1
    return result

def best_s(strs):
    prefix = min(strs, key = len)
    next = False
    while not next:
        next = True
        for elem in strs:
            if elem[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                next = False
    return prefix
print(best_s(strs))
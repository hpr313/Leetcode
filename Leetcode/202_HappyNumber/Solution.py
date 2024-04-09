def isHappy(n):
    result = [n]
    while result[-1] != 1:
        a = 0
        for s in str(result[len(result)-1]):
            a += int(s) ** 2
        if a in result:
            return False
        else:
            result.append(a)
    return True

print(isHappy(2))
def integerReplacement(n):
    i = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        elif n == 3:
            i += 2
            break
        else:
            k = ((n + 1) / 2) % 2
            if ((n + 1) / 2) % 2 == 0:
                n += 1
            else:
                n -= 1
        i += 1
    return i

# print(618/2%2)
print(integerReplacement(3))
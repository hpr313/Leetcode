def findFactor(n):
    factor = [1, n]
    a = int(n ** 0.5)
    for i in range(2, a + 1):
        if n % i == 0:
            factor.append(i)
            break
    return factor

# def countPrimes(n):
#     primes = [2]
#     ans = 1
#     if n <= 2:
#         return 0
#     else:
#         for i in range(3, n, 2):
#             if str(n)[-1] == 5:
#                 pass
#             else:
#                 if len(findFactor(i)) == 2:
#                     primes.append(i)
#                     ans += 1
#         print(primes)
#         return ans

def countPrimes(n):
    primes = [2]
    ans = 1
    if n <= 2:
        return 0
    else:
        for i in range(3, n, 2):
            if str(i)[-1] == 5:
                pass
            else:
                j = 0
                while j < len(primes):
                    if i % primes[j] == 0:
                        break
                    else:
                        j += 1
                    if j == len(primes):
                        primes.append(i)
                        ans += 1
                        break
                    # primes.append(i)
        print(primes)
        return len(primes)
# def eratosthenes(n):
#     is_prime = [True] * (n + 1)
#     for i in range(2, int(n ** 0.5) + 1):
#         if is_prime[i]:
#             for j in range(i * i, n + 1, i):
#                 is_prime[j] = False
#     primes = [x for x in range(2, n + 1) if is_prime[x]]
#     if n in primes:
#         return len(primes)-1
#     else:
#         return len(primes)
# print(eratosthenes(3))
print(countPrimes(10))

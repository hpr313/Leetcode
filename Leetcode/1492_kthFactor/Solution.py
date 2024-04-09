def kthFactor(n, k):

    def findFactor(n):
        factor = [1, n]
        a = int(n ** 0.5)
        for i in range(2, a + 1):
            if n % i == 0:
                factor.append(i)
                if i != n // i:
                    factor.append(n // i)
        factor.sort()
        return factor

    if k > len(findFactor(n)):
        return -1
    elif k == 1:
        return 1
    else:
        return findFactor(n)[k - 1]
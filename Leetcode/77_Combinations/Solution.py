def combine(n, k):
    if k == 1:
        return [[i] for i in range(1, n+1)]
    else:
        result = []
        for i in range(1, n+1):
            result += [[i, j] for j in range(i+1, n+1)]
        return result

n = 4
k = 1

print(combine(n,k))
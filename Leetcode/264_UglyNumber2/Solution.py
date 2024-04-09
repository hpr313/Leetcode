def nthUglyNumber(n):

    if n <= 6:
        return n
    else:
        ans = [i for i in range(1,7)]
        i = 7
        while len(ans) < n:
            j = i
            while j % 2 == 0:
                j //= 2
            while j % 3 == 0:
                j //= 3
            while j % 5 == 0:
                j //= 5
            if j == 1:
                ans.append(i)
                i += 1
            else:
                i += 1
        print(ans)
        return ans[-1]

print(nthUglyNumber(456))
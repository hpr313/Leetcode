def tribonacci(n):
    nums = [0,1,1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return sum(nums)
    else:
        i = 4
        while i < n + 1:
            nums.append(sum(nums))
            nums.pop(0)
            i += 1
        return sum(nums)

print(tribonacci(25))


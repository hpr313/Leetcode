def maxRotateFunction(nums):
    initial = 0
    if len(nums) == 1:
        return initial
    else:

        for i in range(len(nums)):
            initial += i * nums[i]
        maxValue = initial
        i = 1
        while i < len(nums)+1:
            weight = initial + sum(nums) - len(nums) * nums[len(nums) - i]
            initial = weight
            maxValue = max(maxValue, weight)
            i += 1
        return maxValue

nums = [4,3,2,6, 1]
maxRotateFunction(nums)
print(maxRotateFunction(nums))
print(reversed(nums))
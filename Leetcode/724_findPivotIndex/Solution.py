
def pivotIndex(nums):
    if len(nums) == 0:
        return -1
    elif len(nums) == 1:
        return 0
    else:
        rightSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum -= nums[i]
            # print(rightSum)
            if i != 0:
                leftSum += nums[i - 1]
            if leftSum == rightSum:
                return i
        return -1
nums = [1,7,3,6,5,6]

print(pivotIndex(nums))
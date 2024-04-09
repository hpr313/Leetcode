def findDuplicates(nums):
    # result = [False] * len(nums)
    ans = []

    for num in nums:
        nums[abs(num) - 1] *= -1
        if nums[abs(num) - 1] > 0:
            ans.append(abs(num))
    return ans

nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))
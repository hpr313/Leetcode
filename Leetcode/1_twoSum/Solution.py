def twoSum(nums, target):
    i = 0
    ans = []
    while i < len(nums):
        a = nums.index(nums[i])
        if target-nums[i] in nums[i+1:]:
           ans.append(a)
           ans.append(nums[i+1:].index(target-nums[i])+i+1)
           break
        else:
            i += 1
    return ans

nums = [3,2,4]
# for i in range(len(nums)):
#     print(nums[i:])
target = 5

print(twoSum(nums,target))
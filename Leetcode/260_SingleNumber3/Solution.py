# def singleNumber(nums):
#     ans = []
#     set_nums = set(nums)
#     if len(nums) <= 2:
#         return nums
#     else:
#         for num in set_nums:
#             if nums.count(num) == 1:
#                 ans.append(num)
#             if len(ans) == 2:
#                 break
#         return ans
def singleNumber(nums):
    ans = []
    if len(nums) <= 2:
        return nums
    else:
        while len(ans) < 2 and len(nums) > 2:
            a = nums[0]
            if nums.count(a) == 2:
                nums.remove(a)
                nums.remove(a)
            else:
                ans.append(a)
                nums.remove(a)
        if len(ans) == 2:
            return ans
        elif len(nums) == 2:
            return nums
        else:
            return ans + nums
nums = [4,3,4,1,2,1,2,5]
print(singleNumber(nums))
print([1] + [2])


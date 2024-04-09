def singleNumber(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        i = 1
        while i < len(nums):
            a = nums[0]
            if nums.count(a) == 2:
                nums.remove(a)
                nums.remove(a)
            else:
                return nums[0]
        return nums[0]


nums = [-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354]

print(singleNumber(nums))
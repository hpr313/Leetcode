def singleNonDuplicate(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] != nums[i+1]:
            return nums[i]
        else:
            i += 2
    return nums[-1]
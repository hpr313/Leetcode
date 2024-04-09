
def Solution(nums):
    if len(nums) < 3:
        return False
    i = float('inf')
    j = float('inf')
    for num in nums:
        # print(num)
        if num <= i:
            i = num
        elif num <= j:
            j = num
        else:
            return True
    return False

nums = [2,1,5,0,4,6]
print(Solution(nums))
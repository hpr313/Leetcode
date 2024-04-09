def longestSubarray(nums):
    if len(nums) == 0:
        return 0
    elif nums.count(0) <= 1:
        return len(nums) - 1
    elif nums.count(0) == len(nums)-1:
        return 1
    else:
        indices = getZeroIndicies(nums)
        oneArray = getOneArray(nums, indices)
        return getResult(oneArray)

def getZeroIndicies(nums):
    indices = []
    for i in range(len(nums)):
        if nums[i] == 0:
            indices.append(i)
    return indices
def getOneArray(nums, indicies):
    ones = []
    if 0 not in indicies:
        ones.append(indicies[0])
    for i in range(len(indicies)-1):
        ones.append(indicies[i+1]-indicies[i]-1)
    if len(nums)-1 not in indicies:
        ones.append(len(nums)-1-indicies[-1])
    return ones

def getResult(ones):
    if len(ones) == 1:
        return ones[0]
    else:
        a = -float('inf')
        for i in range(len(ones)-1):
            if ones[i]+ones[i+1] > a:
                a = ones[i]+ones[i+1]
        return a

# nums = [0,1,1,1,0,1,1,1,0,1,1,0,1]
nums = [0,1,0]
print(getZeroIndicies(nums))
print(getOneArray(nums, getZeroIndicies(nums)))
print(getResult(getOneArray(nums, getZeroIndicies(nums))))
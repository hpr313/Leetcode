nums = [[1,2,3]]

def getSubsets(nums):
    subsets = []
    if len(nums) == 1:
        return [[], nums]

print(getSubsets(nums))
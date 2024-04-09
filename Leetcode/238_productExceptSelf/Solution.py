def Solution(nums):
  result = []
  if nums.count(0) >= 2:
    return [0] * len(nums)
  elif nums.count(0) == 1:
    result = [0] * len(nums)
    zeroIndex = nums.index(0)
    nums[zeroIndex] = 1
    product = 1
    for i in range(len(nums)):
        product *= nums[i]
    result[zeroIndex] = product
    return result
  else:
    return getResult(nums, result)

def getLeftArray(nums):
  leftArray = []
  leftArray.append(1)
  for i in range(1, len(nums)):
    leftArray.append(leftArray[i-1] * nums[i-1])

  return leftArray

def getRightArray(nums):
  rightArray = []
  rightArray.append(1)
  for i in range(len(nums)-1,0,-1):
    rightArray.insert(0, rightArray[i-len(nums)] * nums[i])
  return rightArray

def getResult(nums, result):

  left = getLeftArray(nums)
  right = getRightArray(nums)
  for i in range(len(nums)):
    result.append(left[i] * right[i])
  return result
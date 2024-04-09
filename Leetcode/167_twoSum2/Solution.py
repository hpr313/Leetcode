def twoSum(numbers, target):
    i = 0
    ans = []

    while i < len(numbers):
        if i >= 1 and numbers[i] == numbers[i-1]:
            i += 1
        else:
            a = numbers.index(numbers[i])+1
            if target-numbers[i] in numbers[i + 1:]:
               ans.append(a)
               ans.append(numbers[i + 1:].index(target - numbers[i]) + i + 2)
               break
            else:
                i += 1
    return ans

# for i in range(len(nums)):
#     print(nums[i:])
# print(list(set(nums)))
nums = [0,0,0,0,0,2,7,11,15]
target = 9
print(twoSum(nums, target))
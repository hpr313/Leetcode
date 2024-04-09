
def moveZeros(nums):
    cnt = nums.count(0)
    if cnt == len(nums):
        return nums
    else:
        i = 1
        while i <= cnt:
            nums.remove(0)
            i += 1
        while cnt > 0:
            nums.append(0)
            cnt -= 1
        return nums

arr = [0]
print(arr)
print(moveZeros(arr))
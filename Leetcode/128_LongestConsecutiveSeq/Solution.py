def longestConsecutive(nums):
    initial = min(nums)
    times = 1
    ans = 0
    while len(nums) != 0:

        if initial + 1 in nums:
            times += 1
            initial += 1
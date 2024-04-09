def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    ans = 0
    l = 0
    r = len(height) - 1
    hmax = max(height)

    while l < r:
        if height[l] == hmax and height[r] == hmax:
            ans = max(ans, hmax * (r-1))
            return ans
        else:
            minHeight = min(height[l], height[r])
            ans = max(ans, minHeight * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

    return ans

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
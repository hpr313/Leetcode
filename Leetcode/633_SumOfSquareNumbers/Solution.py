import math


def judgeSquareSum(c):
    l = 0
    r = int(sqrt(c))

    while l <= r:
      summ = l * l + r * r
      if summ == c:
        return True
      if summ < c:
        l += 1
      else:
        r -= 1

    return False

print(math.sqrt(4))
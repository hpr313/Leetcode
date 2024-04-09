
def asteroidCollision(asteroids):
  result = []
  for ast in asteroids:
    if len(result) == 0:
      result.append(ast)
    else:
      if ast > 0:
        result.append(ast)
      else:
        if result[-1] * ast > 0:
          result.append(ast)
        else:
          if abs(result[-1]) == abs(ast):
            result.pop(-1)
          elif abs(result[-1]) < abs(ast):
            result.pop(-1)
            result.append(ast)
            while len(result) > 1 and result[-1] < 0 and max(result) > 0:
              if abs(result[-2]) == abs(result[-1]):
                result.pop(-1)
                result.pop(-1)
              elif abs(result[-2]) > abs(result[-1]):
                result.pop(-1)
              else:
                result.pop(-2)
          else:
            while len(result) > 1 and result[-1] < 0:
              if abs(result[-2]) == abs(result[-1]):
                result.pop(-1)
                result.pop(-1)
              elif abs(result[-2]) > abs(result[-1]):
                result.pop(-1)
              else:
                result.pop(-2)

  return result
nums = [-2,1,1,-2]
print(asteroidCollision(nums))
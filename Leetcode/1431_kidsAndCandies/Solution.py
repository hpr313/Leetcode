
def getResult(candies, extraCandies):
    result = []
    maximum = max(candies)
    for i in range(len(candies)):
        if maximum - candies[i] <= extraCandies:
            result.append(True)
        else:
            result.append(False)
    return result
candies = [2,3,5,1,3]
extraCandies = 3

print(getResult(candies, extraCandies))
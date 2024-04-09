def getIndex(flowerbed):
    indecies = []
    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            indecies.append(i)
    return indecies

def getResult(flowerbed, n, indecies):
    for i in range(len(indecies)):
        if indecies[i] == 0:
            flowerbed[1] = 1
        elif indecies[i] == len(flowerbed) - 1:
            flowerbed[len(flowerbed) - 2] = 1
        else:
            flowerbed[i-1] = 1
            flowerbed[i+1] = 1
    print(flowerbed)
    if flowerbed.count(0) > n:
        return True
    elif flowerbed.count(0) == 1 & n == 1:
        return True
    else:
        return False

flowerbed = [1,0,0,0,1]
n = 1
print(getIndex(flowerbed))
print(getResult(flowerbed,n,getIndex(flowerbed)))
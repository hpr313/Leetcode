def searchMatrix(matrix, target):
    if target > matrix[-1][-1] or target < matrix[0][0]:
        return False
    else:
        i = 0
        while i < len(matrix):
            if target > matrix[i][-1]:
                i += 1
            else:
                if target in matrix[i]:
                    return True
                else:
                    i += 1
        return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 29
print(searchMatrix(matrix, target))
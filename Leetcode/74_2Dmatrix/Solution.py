def searchRow(matrix, target):
    row = 0
    while row < len(matrix):
        if matrix[row][len(matrix[row])-1] >= target:
            break
        row += 1
    return row

def check(matrix, target, index):
    if index >= len(matrix):
        return False
    else:
        if target in matrix[index]:
            return True
        else:
            return False

mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

print(searchRow(mat, 70))

print(check(mat, 3, searchRow(mat, 34)))

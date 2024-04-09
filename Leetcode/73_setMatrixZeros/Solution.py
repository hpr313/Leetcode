

def getIndex(matrix):
    row = []
    column = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0:
                row.append(i)
                column.append(j)

    return list(set(row)), list(set(column))
def setZero(matrix, index):
    row = index[0]
    column = index[1]
    for i in range(0, len(row)):
        matrix[row[i]] = [0] * len(matrix[i])
    for j in range(0, len(column)):
        for i in range(0, len(matrix)):
            matrix[i][column[j]] = 0

    return matrix

mat = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

print(setZero(mat, getIndex(mat)))



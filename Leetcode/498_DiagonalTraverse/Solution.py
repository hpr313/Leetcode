def findDiagonalOrder(mat):
    ans = [mat[0][0]]
    i = 1
    while i < len(mat)+len(mat[0])-1:
        if i % 2 == 0:
            if i < len(mat):
                p = i
                q = 0
                while q < len(mat[0]) and p >= 0:
                    ans.append(mat[p][q])
                    p -= 1
                    q += 1
            else:
                p = len(mat) - 1
                q = i - len(mat) + 1
                while q < len(mat[0]):
                    ans.append(mat[p][q])
                    p -= 1
                    q += 1
        else:
            if i < len(mat):
                j = i
                k = 0
                while k < len(mat[0]) and j >= 0:
                    ans.append(mat[k][j])
                    j -= 1
                    k += 1
            else:
                j = len(mat)
                k = i - len(mat)
                while k < len(mat):
                    ans.append(mat[k][j])
                    j -= 1
                    k += 1
        i += 1
    return ans

mat = [[1,2,3,2,3],[4,5,6,2,3],[7,8,9,2,3]]

print(findDiagonalOrder(mat))
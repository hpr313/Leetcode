def equalPairs(grid):
    row = getRow(grid)
    column = getColumn(grid)
    ans = 0
    for i in range(len(row)):
        ans += column.count(row[i])
    return ans

def getRow(grid):
    row = []
    for i in range(len(grid)):
        row.append(' '.join(str(num) for num in grid[i]))
    return row

def getColumn(grid):
    column = []
    for i in range(len(grid)):
        j = 0
        text = ''
        while j < len(grid):
            text += str(grid[j][i]) + ' '
            j += 1
        column.append(text.strip())
    return column
def findCircleNum(isConnected):
    connections = len(isConnected)
    for i in range(len(isConnected)):
        if sum(isConnected) > 1:
            pass

    if connections == 0:
        return len(isConnected)
    else:
        return connections

isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(findCircleNum(isConnected))
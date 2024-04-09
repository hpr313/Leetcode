def getStringArr(s):
    strArray = s.strip().split(' ')
    # n = strArray.count('')
    # for i in range(n):
    #     strArray.remove('')
    return strArray

def getResult(strArray):
    result = ''
    for i in range(len(strArray)-1, 0, -1):
        if strArray[i] == '':
            pass
        else:
            result += strArray[i] + ' '
    result += strArray[0]
    return result

s = "the sky   is blue"

print(getResult(getStringArr(s)))
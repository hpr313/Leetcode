
checkList = ['-', '+', ' ']
for i in range(0,10):
    checkList.append(str(i))
def getStringArray(str):
    return str.strip().split(' ')

def getNumber(str, stringArray):
    if str[0] not in checkList:
        return 0
    elif s[0:2] == '+-':
        return 0
    elif s[0:2] == '-+':
        return 0
    else:
        index = 0
        while index < len(stringArray):
            try:
                num = float(stringArray[index])
                return num
            except:
                index += 1

def getResult(num):
    if num > 2 ** 31 -1:
        return 2 ** 31
    elif num < -2 ** 31:
        return -2 ** 31
    else:
        return int(num)

s = ""
print(s[0:2])
# print(checkList)
# print(s[0])
# print(getStringArray(s))
# print(getInteger(s, getStringArray(s)))
# print(eval(s))
print(getResult(getNumber(s, getStringArray(s))))
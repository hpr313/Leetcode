
def getResult(word1, word2):
    result = ''
    if len(word1) == len(word2):
        for i in range(len(word1)):
            result += word1[i]
            result += word2[i]

    elif len(word1) < len(word2):
        for i in range(len(word1)):
            result += word1[i]
            result += word2[i]
        for i in range(len(word1), len(word2)):
            result += word2[i]
    else:
        for i in range(len(word2)):
            result += word1[i]
            result += word2[i]
        for i in range(len(word2), len(word1)):
            result += word1[i]
    return result
word1 = "abcd"
word2 = "pq"

print(getResult(word1, word2))

def maxVowels(s, k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s[0:k]:
        if char in vowels:
            count += 1
    if count == k:
        return k
    else:
        ans = count
        i = 1
        j = len(s)-k+1
        while i < j and ans < k:
            if s[i-1] in vowels:
                count -= 1
            if s[i+k-1] in vowels:
                count += 1
            ans = max(ans, count)
            i += 1
        return ans
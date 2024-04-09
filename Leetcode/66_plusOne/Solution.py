def plusOne(digits):
    if digits.count(9) == len(digits):
        digits = [1] + [0] * len(digits)
    else:
        digits[-1] += 1
        for i in range(-1,-len(digits)-1,-1):
            if digits[i] < 10:
                break
            else:
                digits[i] = 0
                digits[i-1] += 1
    return digits


digits = [9,9]
print(plusOne(digits))
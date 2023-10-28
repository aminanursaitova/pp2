def sumDigit(n):
    if n >= 10:
        s = sumDigit(n//10) + n % 10
    else:
        s = n
    return s

n = 36538742849
print(sumDigit(n))
n = 5
print(sumDigit(n))
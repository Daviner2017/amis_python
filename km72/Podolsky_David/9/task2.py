def power(a, n):
    if a == 0 and n <= 0:
        print('Undefined')
    elif n == 0:
        return 1
    elif n>0:
        return a*power(a, n-1)
    else:
        return round((1/a*power(a, n+1)), 6)
print(power(3, 4))
print(power(0, 0))
print(power(0, -5))
print(power(3, -2))

def power(a, n):
    if a == 0 and n == 0:
        print('Undefined')
    elif n == 0:
        return 1
    else:
        return a*power(a, n-1)
print(power(float(input('a=')),float(input('n='))))

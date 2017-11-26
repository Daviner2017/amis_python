def inputCheck1():
    n = input('Enter positive integer n=')
    if not(n.isdigit()) or int(n)==0 or len(n)==0:
        print('It has to be a positive integer')
        return inputCheck1()
    else:
        return int(n)

def inputCheck2():
    x = input('Enter a float number (except x=1) x=')
    if x == 1:
        print('x has to be a float number (except x=1)')
        return inputCheck2()
    try:
        float(x)
        return float(x)
    except ValueError:
        print('x has to be a float number (except x=1)')
        return inputCheck2()

def equationSum(x, n, sum=0):
    if n > 0:
        sum=(((x+2)**(n))/(x-1)) + equationSum(x, (n-1))
        return sum
    else:
        return sum

print(equationSum(inputCheck2(), inputCheck1()))

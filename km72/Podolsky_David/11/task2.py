def minOfTheList(l, i):
    global min
    if i < len(l) - 1:
        if min > l[i + 1]:
            min = l[i+1]
            return minOfTheList(l, i+ 1)
    else:
        return minOfTheList(l, i + 1)
    return min

i=int(0)
l=input('Enter the list of numbers ').split()
min=l[i]
print(minOfTheList(l, i))

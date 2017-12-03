def listConvertion(listC, iter = 0):
	
    """
    This function converts all elements of list into int type
    Args:
        listC: list to be converted
        iter: integer iterator
    Returns:
        listC: converted list
    Raises:
        OverflowError
        ValueError
    Examples:
        print(listConvertion(["1", "2", "3"]))
        [1, 2, 3]
        print(listConvertion(["a", "2", "3"]))
        Traceback (most recent call last):
            ...
        ValueError
    """
    
    if iter < len(listC):
        listC[iter] = int(listC[iter])
        return listConvertion(listC, iter + 1)
    return listC



n = 0
compareList = []
def groupMeasure(listC, iter = 0):
    
    """
    This function counts the same elements and returns the max of such counting
    Args:
        listC: list, where elements are compared to each another
        iter: integer iterator
    Returns:
        max(compareList): integer that show the biggest amount of repeated elements
    Raises:
        OverflowError
        ValueError
    Examples:
        print(groupMeasure([1, 1, 1, 2, 2, 3]))
        3
        print(groupMeasure([1, 1, "a", 2, 2, 3]))
        Traceback (most recent call last):
            ...
        ValueError
    """	
    
    global n
    global compareList
    if iter < len(listC) - 1:
        if listC[iter] == listC[iter+1]:
            n += 1
            return groupMeasure(listC, iter + 1)
        elif not(listC[iter] == listC[iter+1]):
            n += 1
            compareList.append(n)
            n = 0
            return groupMeasure(listC, iter + 1)
    elif iter == len(listC) - 1:
        n += 1
        compareList.append(n)
        return max(compareList)



def maxCountDet(listC, m, iter = 0):
	
    """
    This function returns the numbers that mostly repeat
    Args:
        listC: list, where elements are compared to each another
        m: integer, which is returned from groupMeasure(listC) and shows the max amount of repeated elements
        iter: integer iterator
    Returns:
        ' '.join(str(e) for e in [listC[iter]]*m): a string with repeated integers
    Raises:
        OverflowError
        ValueError
    Examples:
        print(maxCountDet([1, 1, 1, 2, 2, 3], 3))
        1 1 1
        print(maxCountDet([1, 1, "a", 2, 2, 3], 3))
        Traceback (most recent call last):
            ...
        ValueError
    """	
    
    if iter < len(listC) -1:
        if listC.count(listC[iter]) == m:
            return ' '.join(str(e) for e in [listC[iter]]*m)
        else:
            return maxCountDet(listC, m, iter + 1)



listC = input("Enter the row of positive integers: ").split()

m=groupMeasure(listConvertion(listC))
print("The biggest amount of same numbers is", m)
print("These numbers are: ", maxCountDet(listConvertion(listC), m))

posIntList = input("Enter list of positive integers: ").split()

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


posIntListC = listConvertion(posIntList)
listMax = posIntListC[0]


def findMaxEl(inputList, iter = 0):
	
    """
    This function calculates the max element
    Args:
        inputList: list where max element is being searched
        iter: integer iterator
    Returns:
        listMax: max integer
    Raises:
        OverflowError
        ValueError
    Examples:
        print(findMaxEl([1,2,3,4]))
        "4"
        print(findMaxEl([1,2,"a",3]))
        Traceback (most recent call last):
            ...
        ValueError
    """
    
    global listMax
    if iter < len(inputList) - 1:
        if listMax < inputList[iter+1]:
            listMax = inputList[iter + 1]
            return findMaxEl(inputList, iter + 1)
        else:
            return findMaxEl(inputList, iter + 1)
    return listMax

theMaxEl = findMaxEl(posIntList)
n = 0

def maxCount(listC, iter = 0):
    """
     This function counts the amount of repeteable elements equal to max(listC)
     Args:
         listC: list, where max is counting
         iter: integer iterator
     Returns:
         n: integer, number of max elements
     Raises:
         OverflowError
         ValueError
     Examples:
         print(max_f([1,2,3,4]))
         "1"
         print(max_f([1,2,"a",3]))
         Traceback (most recent call last):
             ...
         ValueError
     """
    global n
    global theMaxEl
    if iter < len(listC) - 1:
        if listC[iter] == theMaxEl:
            n += 1
            return maxCount(listC, iter + 1)
        else:
            return maxCount(listC, iter + 1)
    elif iter == len(listC) - 1:
        if listC[iter] == theMaxEl:
            n += 1
            return maxCount(listC, iter + 1)
        else:
            return maxCount(listC, iter + 1)
    return n


print("Amount of elements equal to the max element:", maxCount(posIntListC))

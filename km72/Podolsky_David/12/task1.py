
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
        listMax: integer
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
test = []


def eraseMaxEls(listC, maxElement, iter = 0):
	
    """
    This function deletes all elements equal to the max element
    Args:
        listC: list where max element is being searched
        iter: integer iterator
        maxElement: max element of the listC
    Returns:
        test: listC without max element(s)
    Raises:
        OverflowError
        ValueError
    Examples:
        print(eraseMaxEls([1, 2, 3, 4], 4))
        [1, 2, 3]
        print(eraseMaxEls([1, "a", 3, 4], 4))
        Traceback (most recent call last):
            ...
        ValueError
    """
    
    global test
    if iter < len(listC) - 1:
        if listC[iter] != maxElement:
            test.append(listC[iter])
            return eraseMaxEls(listC, maxElement, iter + 1)
        else:
            return eraseMaxEls(listC, maxElement, iter + 1)
    elif iter == len(listC)-1:
        if listC[iter] != maxElement:
            test.append(listC[iter])
    return test


eraseMaxEls(posIntListC, theMaxEl)



def find2MaxEl(listC, iter = 0):
	
    """
    This function searches for second max element in the listC
    Args:
        listC: list, where second max is searching
        iter: integer iterator
    Returns:
        maxEl2: 2nd max integer
    Raises:
        OverflowError
        ValueError
    Examples:
        print(find2MaxEl([1, 2, 3]))
        "2"
        print(sec_max_f([1, 2, "b"]))
        Traceback (most recent call last):
            ...
        ValueError
    """
    
    global maxEl2
    if iter < len(listC) - 1:
        if maxEl2 < listC[iter+1]:
            maxEl2 = listC[iter + 1]
            return find2MaxEl(listC, iter + 1)
        else:
            return find2MaxEl(listC, iter + 1)
    return maxEl2

if len(test) > 0:
    maxEl2 = test[0]
    print("2nd max element from the input is", find2MaxEl(test))
else:
    print("The following list does not have second max element.")

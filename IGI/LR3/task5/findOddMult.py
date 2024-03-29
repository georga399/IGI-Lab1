def findOddMult(lst: list):
    """Find multiplication of elements on
    the odd postitions.
    
    """
    counter = 1
    res:float = 1
    for el in lst:
        if counter % 2 == 0:
            res*=el
        counter+=1 
    return res
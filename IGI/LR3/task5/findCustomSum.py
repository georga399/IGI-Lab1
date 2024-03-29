def findCustomSum(lst: list) -> float:
    """Find sum of elements between first elements and 
    last element equal 0.    

    """
    res: float = 0
    preres: float = 0
    for el in lst:
        if abs(el) < 1e-6:
            res += preres
            preres = 0
        preres += el
    return res
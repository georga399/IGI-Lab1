from .gener import gener
import math
import numpy as np
import statistics

def taylor(x:float, maxN) -> tuple:
    """Counting value of taylor."""
    FMath: float = math.asin(x)
    F:float = x
    n: int = 0
    prev: float = x
    arr = []
    for i in gener(prev, x) :
        n+=1
        arr.append(i)
        F+=i
        if (n > maxN):
            break
    mean = statistics.mean(arr)
    median = statistics.median(arr)
    mode = statistics.mode(arr)
    dispersion = statistics.variance(arr)
    std = statistics.stdev(arr)
    eps = abs(FMath - F) 

    return F, eps, FMath, mean, median, mode, dispersion, std

        


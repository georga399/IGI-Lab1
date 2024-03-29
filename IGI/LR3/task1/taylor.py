from .gener import gener
import math

def taylor(x:float, eps:float) -> tuple:
    """Counting value of taylor."""
    mathF = math.asin(x)
    F:float = x
    maxN: int = 500
    n: int = 0
    prev: float = x
    for i in gener(prev, x) :
        n+=1
        F+=i
        if (abs(F - mathF) < eps) or (n > maxN):
            break
    return n, F, mathF
        


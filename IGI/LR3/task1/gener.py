def gener(prev:float, x:float):
    """Generate i-th elements of taylor."""
    for n in range(1, 500):
        prev*=x*x*(2*n - 1)*2*n
        prev/=4
        prev/=n*n
        prev/=(2*n+1)
        prev*=(2*n-1)
        yield prev
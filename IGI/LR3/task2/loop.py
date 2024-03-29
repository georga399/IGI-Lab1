def loop() -> int:
    """Calcultate number of negative elements in the sequence."""
    stringNums = input()
    counter: int = 0
    parts = stringNums.split(' ')
    for p in parts:
        a: int   
        try:
            a = int(p)
            if(a < 0):
                counter+=1
            elif a > 100:
                break
        except:
            print(f"Wrong format!!! {p}")
            break

    return counter
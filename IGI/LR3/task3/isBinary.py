def isBinary() -> bool:
    """Determine that string is binary number or not"""
    notEmpty = False
    inputString = input()
    parts = inputString.split(' ')
    for p in parts:
        for c in inputString:
            if c != '1' and c!='0':
                return False
            notEmpty = True
    return True and notEmpty
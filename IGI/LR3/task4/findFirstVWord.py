def findFirstVWord(text:str) -> tuple:
    """Find first word that contains V."""
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    counter: int = 0
    for w in words:
        counter+=1
        if 'v' in w:
            return counter, w 
    return -1, str('')
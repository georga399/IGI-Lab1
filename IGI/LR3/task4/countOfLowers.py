def countOfLowers(string:str) -> int:
    """Calculate number of lower symbols in the string."""
    return sum(1 for c in string if c.islower())
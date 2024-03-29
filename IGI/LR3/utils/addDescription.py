def addDescription(string:str):
    """Decorator that allow print description with running task."""
    def wrapper(fn):
        def fnc(*args, **kw):
            print("------------")
            print(string)
            fn(*args, **kw)
            print("------------")
        return fnc
    return wrapper
 
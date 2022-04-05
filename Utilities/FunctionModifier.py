def addToFunction(function, new_function):
    def newFunctionWrapper(*args, **kwargs):
        function(*args, **kwargs)
        new_function(*args, **kwargs)

    return newFunctionWrapper



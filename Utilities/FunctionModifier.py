def addToFunction(function, new_function):
    """
    Adds a new function to the end of a function.
    :param function: The function to add to.
    :param new_function: The function to add.
    :return: The new function.
    """
    def newFunctionWrapper(*args, **kwargs):
        function(*args, **kwargs)
        new_function(*args, **kwargs)

    return newFunctionWrapper



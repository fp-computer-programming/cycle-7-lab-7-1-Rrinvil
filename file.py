#Author-Ryan Rinvil
def greeting():
    """
    This function prints 'Hello World' on one line.
    """
    print("Hello World!")
    return greeting.__doc__

greeting()
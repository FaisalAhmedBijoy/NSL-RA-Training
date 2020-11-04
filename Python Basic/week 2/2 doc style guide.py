# style guide is used to write good documentation
def square_function(n):
    """
    Args:
        n: input of the number
    Return:
        the square of the number
    Raises:
        TypeError: if n is not a number
        ValueError: if n is negative
    """
    return n*n
print(square_function(10))
""" 
The square(number) function calculates the number of grains in the specific square number.
The total() function calculates the total number of grains in the chessboard.
"""

def square(number: int) -> int:
    """
    This function calculates the number of grain in the given number from 1 to 64.
    
    :param number: int - number in the chessboard from 1 to 64
    :return: int - the number of grain in the given number
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 1 << (number-1)

def total() -> int:
    """
    This function calculates the total number of grains in the chessboard.

    :return: int - returns the total number of grains in the chessboard.
    """
    return (1 << 64)-1
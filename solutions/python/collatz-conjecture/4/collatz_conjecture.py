"""Function for calculating the steps it will take for any positive integer to reach 1"""

def steps(number):
    """
    This function takes in a positive integer, return the number of steps it takes to          reach 1 according to the rules of the Collatz Conjecture.

    :param number: int - a positive integer.
    :return: int - number of steps it took to reach 1.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
        
    count = 0
    while number != 1:
        number = number / 2 if number % 2 ==0 else (number * 3) + 1
        count += 1
    return count

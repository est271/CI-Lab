"""Prints prime numbers from 2 up to the number 'num' """

# prime numbers are divisible only by 1 and itself.


def find_prime(num):
    """This function will print all the prime numbers up to the input 'num' """

    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError("number input must be an integer")

    if num <= 1:
        raise ValueError("number must be greater than 1")

    # The code below will test if every iteration of 'var' is a prime number
    for var in range(0, num + 1):
        for var2 in range(2, var + 1):
            if var == var2:
                print(var2)
            elif var % var2:
                continue
            else:
                break
    return 0

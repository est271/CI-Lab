"""Prints prime numbers from 2 up to the number 'num' """

# Number 1 is not a prime number. prime number has to be divisible only by 1 and itself.

def find_prime(num):
    """This function will print all the prime numbers up to the input 'num' """

    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError("number input must be an integer")

    if num <= 1:
        raise ValueError("number must be greater than 1")

    # The code below will test if every iteration of 'var' is a prime number
    for var in range(0, num+1):
        for var2 in range(2, var+1): # All 'integers' are divisible by 1 so start testing with divisors at 2
            if var == var2:         # All options exhausted, the number stored in var is a prime number. print the number
                print(var2)
            elif (var % var2):      # ex. (5/2= 2 remainder 1 or 2.5) might be a prime number. continue testing
                continue
            else:                   # ex. (4/2= 2 no remainder) Not a prime number, break from loop & test next number
                break

"""Prints prime numbers from 2 up to the number 'num' """

# prime numbers are divisible only by 1 and itself.
# implement Sieve of Eratosthenes algorithm (divide only by prime numbers)


def find_prime(num):
    """This function will print all the prime numbers up to the input 'num' """

    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError("number input must be an integer")

    if num <= 1:
        raise ValueError("number must be greater than 1")

    pri_num = [2]

    # The code below will test if every iteration of 'var' is a prime number
    for var in range(2, num + 1):
        res = 0
        for var2 in pri_num:
            if var == 2:
                break
            elif (var % var2) == 0:
                break
            elif (var2 == pri_num[-1]):
                res = var
        if res:
            pri_num.append(res)
    print(pri_num)

    return 0

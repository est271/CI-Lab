"""Prints prime numbers from 2 up to the number 'num' """

# Remember that the number 1 is not a prime number. prime number has to be divisible only by 1 and itself.

num = 100

"""The code below will test if the number stored in 'var' is a prime number """
for var in range(0,num+1): 
    forr var2 in range(2,var+1): # All 'integers' are divisible by 1 so start testing with divisors at 2
        if var == var2:         # All options exhausted, the number stored in var is a prime number. print the number
            print(var2)
            continue
        elif (var % var2):      # ex. (5/2= 2 remainder 1 or 2.5) might be a prime number. continue testing
            continue
        elif (var % var2) == 0: # ex. (4/2= 2 no remainder) Not a prime number, break from loop & test next number
            break

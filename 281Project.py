import math
import random
import sys

#  system to display large integers without scientific notation
sys.set_int_max_str_digits(0)

def gcd(a, b):
    """
    Calculate the greatest common divisor of two numbers using Euclid's algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def isPrime(n):
    """
    Returns False if n is divisible by any number
    from 2 to the square root of n, True otherwise.
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def nextValue(x, n, c):
    """
    Generate the next number in the sequence for the factorization process.
    Function f(x) = x^2  + c  mod n .
    """
    return        ((x*x) + c)  %  n

def spellCheck(x):
    """
    Validate the input to ensure it is a positive number or -1 to exit.
    Re-prompts the user if the input is not valid.
    """
    while x <= 0:
        if x == -1:
            return -1
        else:
            x = int(input("Enter a positive number (or -1 to exit):"))
    return x

# application Start
n = 0
while n != -1:
    n = int(input("Enter a number (or -1 to exit):"))
    n = spellCheck(n)
    
    if n == -1:
        break
    
    # Set the initial conditions 
    c = 1
    x0 = 2
    y0 = 2
    
    #todo [4,8,16] does not work.
    if not isPrime(n):
        while True:
            x0 = nextValue(x0, n, c)
            y0 = nextValue(nextValue(y0, n, c), n, c)

            d = gcd(abs(x0 - y0), n)
            
            # Check if a non-trivial divisor has been found
            if d != 1 and d != n:
                fac1 = d
                break
            # Reset the sequence if it starts repeating
            elif y0 == x0:
                x0 = 2
                y0 = 2
                c  = 2

        # Calculate the second factor
        # [//] floor division   
        fac2 = n // fac1
        print(f"Factors of {n} are = {fac1} * {fac2}\n")
    else:
        print(f"The number {n} is prime.\n")

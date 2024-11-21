import math
import random
import sys
sys.set_int_max_str_digits(0)





def gcd(a, b):
   
    while b != 0:
        a, b = b, a % b
    return a

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def rdSequence(x , n , c):
    return ((x*x)+ c) % n

#checks for if x is not integer 
def spellCheck(x):
    while x <= 0 :
        if x == -1:
            return -1
        else:
            x = int(input("Enter a positive number (or -1 to exit):"))
    return x
            
        
    

n = 0
while n != -1:
    
    n = int(input("Enter a number (or -1 to exit):"))
    n = spellCheck(n)
    
    if n == -1:
        break
    
    c = 1
    x0 = 2
    y0 = 2
    
    if not isPrime(n):
        while True:
            
            x0 = rdSequence(x0, n, c)
            y0 = rdSequence(rdSequence(y0, n, c), n, c)

            d = gcd(abs(x0 - y0), n)
            

            if d != 1 and d != n:
                fac1 = d
                break
            elif y0 == x0 :
                c = 2
        fac2 = n // fac1
        print(f"factors for {n} are = {(fac1)} * {(fac2)}\n")
    else:
        print(f"factors for {n} are = {n}\n")

    
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isPrime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
import math

def isPrimeAuxiliar(n):
    if (n == 1): return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True

def isPrime(n):
    if isPrimeAuxiliar(n):
        return 1
    else:
        i = 1
        prod = 1
        factors = []

        while prod <= n and i <= n:
            if prod == n:
                break

            if n % i == 0 and i != 1:
                prod = prod * i
                factors.append(i)                
            i = i + 1
            
        return factors[0]
    

if __name__ == '__main__':

    n = int(input().strip())

    result = isPrime(n)

    print(str(result) + '\n')
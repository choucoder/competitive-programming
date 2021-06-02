#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    # Write your code here
    candies = [1 for _ in range(n)]
        
    for i in range(n - 1):
        c1, c2 = arr[i: i + 1 + 1]
        if c1 > c2:
            lr, hr = i + 1, i
        elif c2 > c1:
            lr, hr = i, i + 1
        
        # if c1 != c2:
        while candies[hr] <= candies[lr]:
            candies[hr] += 1
    #     else:
    #         if candies[i] == 1:
    #             candies[i + 1] = candies[i] + 1
    #         else:
    #             candies[i + 1] = candies[i] - 1
            
    #         if i != 0:
    #             if candies[i - 1] > candies[i + 1] and candies[i + 1] > candies[i]:
    #                 candies[i], candies[i + 1] = candies[i + 1], candies[i]
    # print(f"Candies: {candies}")
    return sum(candies)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    print(str(result) + '\n')
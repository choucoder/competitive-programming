def howSum(targetSum, numbers):
    if (targetSum == 0): return []
    if (targetSum < 0): return None

    for n in numbers:
        result = howSum(targetSum - n, numbers)
        if result != None:
            return result + [n]
    
    return None

def howSum(targetSum, numbers, dp={}):
    if (targetSum in dp): return dp[targetSum]
    if (targetSum == 0): return []
    if (targetSum < 0): return None

    for n in numbers:
        result = howSum(targetSum - n, numbers, dp)
        if result != None:
            dp[targetSum] = result + [n]
            return dp[targetSum]
    
    dp[targetSum] = None
    return dp[targetSum]

if __name__ == '__main__':
    print(howSum(7, [2, 3]))
    print(howSum(300, [7, 14]))